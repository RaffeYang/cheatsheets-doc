import unittest
from markdown_format import format_markdown

class FormattingTests(unittest.TestCase):
    def test_rules_and_headings(self):
        source = 'Title\n===\n\nIntro\n----\n\n### Body\n\n----\ntext\n\n---\n'
        result = format_markdown(source)
        self.assertIn('# Title', result)
        self.assertIn('## Intro', result)
        self.assertNotRegex(result, r'(?m)^-{3,}$')

    def test_code_examples_are_preserved(self):
        code = '```html\n---\n<p>example</p>\n<!-- comment -->\n```'
        source = code + '\n\n`<pur>literal</pur>` and `<ENVNAME>`\n'
        result = format_markdown(source)
        self.assertIn(code, result)
        self.assertIn('`<pur>literal</pur>` and `<ENVNAME>`', result)

    def test_markup_and_tables(self):
        source = '### 选择\n<!--rehype:layout-->\n快捷方式 | 说明\n:- | -\n`v`<pur>i</pur><yel>"</yel> | 选择 {.underline}\n'
        result = format_markdown(source)
        self.assertIn('| 快捷方式 | 说明 |', result)
        self.assertIn('| `v`i" | 选择 |', result)
        self.assertNotIn('<pur>', result)
        self.assertNotIn('rehype', result)
        self.assertNotIn('{.underline}', result)
        self.assertEqual(format_markdown(result), result)

    def test_links_and_symbols(self):
        source = '<a href="https://example.com">site</a> <a href="javascript:alert(1)">value</a>\n\n[\\<table>](https://example.com) <ENVNAME>\n'
        result = format_markdown(source)
        self.assertIn('[site](https://example.com)', result)
        self.assertNotIn('javascript:', result)
        self.assertIn('[\\<table>]', result)
        self.assertIn('<ENVNAME>', result)

    def test_attribution_and_relative_links(self):
        source = '<!--\nSource: https://github.com/jaywcjlove/reference/blob/main/docs/vim.md\nRetrieved on: 2026-10-15\n-->\n\nSee [regex](./regex.md).\n'
        result = format_markdown(source)
        self.assertIn('https://github.com/jaywcjlove/reference/blob/main/docs/regex.md', result)
        self.assertIn('来源', result)
        self.assertIn('2026-10-15', result)
        self.assertEqual(format_markdown(result), result)

    def test_table_escape_and_list(self):
        source = 'A | B\n- | -\nx | `a` \\| `b`\n\n- item\n  - child\n1. ordered\n'
        result = format_markdown(source)
        self.assertIn('| x | `a` \\| `b` |', result)
        self.assertIn('- item\n  - child\n1. ordered', result)

    def test_html_table(self):
        result = format_markdown('<table><tr><th>A</th><th>B</th></tr><tr><td>x</td><td>y</td></tr></table>')
        self.assertIn('| A | B |\n| --- | --- |\n| x | y |', result)


class IntegrationTests(unittest.TestCase):
    def test_html_code_with_backticks(self):
        source = '<code>\\`a</code> | mark\n\n`<code>literal</code>`\n'
        result = format_markdown(source)
        self.assertIn('`` `a ``', result)
        self.assertIn('`<code>literal</code>`', result)
        self.assertEqual(format_markdown(result), result)

    def test_input_does_not_swallow_following_text(self):
        result = format_markdown('<input type="text">\n\nkeep this\n\n<progress value="2">2</progress>\n')
        self.assertIn('keep this', result)

    def test_saving_normalizes_and_preserves_existing_name(self):
        import tempfile
        import os
        from pathlib import Path
        from update_references import save_file
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'npm.md'
            path.write_text('old')
            save_file('### Title\n\n----\n\n<p>content</p>', str(path))
            self.assertEqual([entry.name for entry in Path(directory).iterdir()], ['npm.md'])
            self.assertIn('content', path.read_text())
            self.assertNotIn('<p>', path.read_text())
            self.assertNotIn('----', path.read_text())

class AdditionalRegressionTests(unittest.TestCase):
    def test_color_swatches_retain_values(self):
        result = format_markdown('<table><tr><td style="background-color: rgb(255, 204, 204);"></td></tr></table>')
        self.assertIn('rgb(255, 204, 204)', result)

    def test_escaped_backticks_and_backslashes_in_wrappers(self):
        result = format_markdown(r'<pur>\\</pur> / <pur>\`</pur>')
        self.assertNotIn('pur>', result)
        self.assertIn(r'\\', result)
        self.assertIn(r'\`', result)

if __name__ == '__main__':
    unittest.main()
