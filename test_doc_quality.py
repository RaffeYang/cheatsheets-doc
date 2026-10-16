import unittest
from pathlib import Path
from doc_quality import check_document, fenced_blocks
from markdown_format import format_markdown


class QualityTests(unittest.TestCase):
    def test_code_preserved(self):
        text = '# A\n\n```rust\nlet x = "<red>{: hi}</red>";\n```\n'
        self.assertEqual(fenced_blocks(text), fenced_blocks(format_markdown(text)))

    def test_missing_local_link(self):
        self.assertTrue(check_document('[file](missing.md)', Path('README.md')))

    def test_remote_links_are_offline(self):
        self.assertEqual(check_document('[file](https://example.invalid/a)', Path('README.md')), [])

    def test_code_links_are_ignored(self):
        self.assertEqual(check_document('```md\n[file](missing.md)\n```\n', Path('README.md')), [])

    def test_unclosed_fence(self):
        self.assertTrue(check_document('```rust\nfn main() {}', Path('a.md')))


class RustSmokeTests(unittest.TestCase):
    def test_selected_complete_examples_compile(self):
        import shutil
        import subprocess
        import tempfile
        compiler = shutil.which('rustc')
        if not compiler:
            self.skipTest('rustc is not installed')
        blocks = fenced_blocks(Path('docs/languages/Rust.md').read_text(encoding='utf-8'))
        selections = ['println!("Hello, World!");', 'let mut slices:',
                      'let S_string =', 'let res = loop', "assert!(matches!('x',",
                      'let sum = add((1, 2));']
        with tempfile.TemporaryDirectory() as directory:
            for selector in selections:
                block = next(block for block in blocks if selector in block)
                code = '\n'.join(block.splitlines()[1:-1])
                if 'fn main' not in code:
                    code = 'fn main() {\n' + code + '\n}'
                source = Path(directory) / 'sample.rs'
                source.write_text(code, encoding='utf-8')
                result = subprocess.run([compiler, '--edition=2021', '--emit=metadata',
                                         '-o', str(Path(directory) / 'sample.rmeta'), str(source)],
                                        capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, selector + '\n' + result.stderr)
