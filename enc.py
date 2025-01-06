import ast
import base64
import python_minifier
import random
import zlib
import os
import sys

class Obfuscator:
    def __init__(self):
        self._map = {}
        self._counter = 0

    def fake_name(self, style: int = 1) -> str:
        """Generate a fake obfuscated name based on the style."""
        self._counter += 1
        if style == 1:
            return f'{"O0" * (self._counter % 5)}' + ''.join(random.choice(['O0', 'O']) for _ in range(10)).replace('O', 'O0')
        elif style == 2:
            return f'{"O0" * (self._counter % 10)}' + ''.join(random.choice(['O0', 'O']) for _ in range(100)).replace('O', 'O0')
        else:
            raise ValueError("Invalid style selected.")

    @staticmethod
    def str_compress(s: str) -> str:
        """Compress a string and encode it for obfuscation."""
        compressed = zlib.compress(s.encode())
        ba64_enc = base64.b64encode(compressed).decode()
        return f"(lambda s: zlib.decompress(base64.b64decode(s)).decode())('{ba64_enc}')"

    def obfuscate(self, tree: ast.AST) -> None:
        """Obfuscate function names, argument names, and variable names."""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                new_name = self.fake_name(1)
                self._map[node.name] = new_name
                node.name = new_name

        for node in ast.walk(tree):
            if isinstance(node, ast.arg):
                new_name = self.fake_name(2)
                self._map[node.arg] = new_name
                node.arg = new_name

        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id in self._map:
                node.id = self._map[node.id]

    def replace_str(self, code: str) -> str:
        """Replace strings in the code with compressed versions."""
        tree = ast.parse(code)
        new_code = code
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                compressed_string = self.str_compress(node.value)
                new_code = new_code.replace(repr(node.value), compressed_string)
        return new_code

    @staticmethod
    def ensure_imports(code: str) -> str:
        """Ensure the necessary imports exist in the code."""
        required_imports = ["import zlib", "import base64"]
        existing_imports = set(line.strip() for line in code.splitlines() if line.startswith("import"))
        missing_imports = [imp for imp in required_imports if imp not in existing_imports]
        return "\n".join(missing_imports) + "\n" + code if missing_imports else code

    def execute(self, code: str) -> str:
        """Process and obfuscate the input code."""
        tree = ast.parse(code)
        self.obfuscate(tree)
        code = ast.unparse(tree)
        code = self.replace_str(code)
        code = self.ensure_imports(code)
        return code


class NgoccoderObfuscator:
    def __init__(self):
        self.obfuscator = Obfuscator()

    def run(self):
        """Run the obfuscator with user-provided inputs."""
        input_file = input('Your file: ').strip()
        rename_identifiers = input('Rename global? yes/no: ').strip().lower() == 'yes'
        output_file = input_file.rsplit('.', 1)[0] + '-obf.py'

        if not os.path.isfile(input_file):
            print(f"Error: The file '{input_file}' does not exist.")
            return

        try:
            with open(input_file, 'r', encoding='utf-8') as file:
                code = file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return

        try:
            processed_code = self.obfuscator.execute(code)
            obfuscated_code = python_minifier.minify(
                processed_code,
                rename_globals=rename_identifiers,
                convert_posargs_to_args=True,
                remove_annotations=True
            )
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(obfuscated_code)
            print(f'Obfuscated code saved to: {output_file}')
        except Exception as e:
            print(f"Error during obfuscation: {e}")
            return


if __name__ == "__main__":
    app = NgoccoderObfuscator()
    app.run()