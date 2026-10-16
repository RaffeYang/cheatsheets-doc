import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import update_references as updater


class UpdateTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.previous = os.getcwd()
        os.chdir(self.directory.name)

    def tearDown(self):
        os.chdir(self.previous)
        self.directory.cleanup()

    def test_download_error_does_not_replace_any_output(self):
        Path('docs').mkdir()
        Path('docs/A.md').write_text('old')
        config = {'repositories': [{'owner': 'o', 'repo': 'r', 'files': [
            {'path': 'a', 'destination': 'docs/A.md'},
            {'path': 'b', 'destination': 'docs/B.md'}]}]}
        with patch.object(updater, 'download_file', side_effect=['# A\n', RuntimeError('network')]):
            with self.assertRaisesRegex(ValueError, 'no documents replaced'):
                updater.update_references(config)
        self.assertEqual(Path('docs/A.md').read_text(), 'old')
        self.assertFalse(Path('docs/B.md').exists())

    def test_custom_wins_and_skips_upstream(self):
        Path('custom/tools').mkdir(parents=True)
        Path('custom/tools/UV.md').write_text('# UV\n\nLocal.\n')
        config = {'repositories': [{'owner': 'o', 'repo': 'r', 'files': [
            {'path': 'uv', 'destination': 'docs/tools/UV.md'}]}]}
        with patch.object(updater, 'download_file') as download:
            updater.update_references(config)
            download.assert_not_called()
        self.assertIn('Local.', Path('docs/tools/UV.md').read_text())

    def test_invalid_content_retains_previous_file(self):
        Path('A.md').write_text('old')
        with self.assertRaises(ValueError):
            updater.save_file('```rust\nlet x = 1;', 'A.md')
        self.assertEqual(Path('A.md').read_text(), 'old')

    def test_replace_failure_cleans_temporary_file(self):
        Path('A.md').write_text('old')
        with patch.object(updater.os, 'replace', side_effect=OSError('disk')):
            with self.assertRaises(OSError):
                updater.save_file('# A\n', 'A.md')
        self.assertEqual(list(Path('.').iterdir()), [Path('A.md')])
        self.assertEqual(Path('A.md').read_text(), 'old')

    def test_duplicates_rejected(self):
        config = {'repositories': [{'owner': 'o', 'repo': 'r', 'files': [
            {'path': 'a', 'destination': 'docs/A.md'},
            {'path': 'b', 'destination': 'docs/a.md'}]}]}
        with patch.object(updater, 'download_file', return_value='# A\n'):
            with self.assertRaisesRegex(ValueError, 'Duplicate'):
                updater.update_references(config)
        self.assertFalse(Path('docs').exists())

    def test_existing_custom_filename_is_preserved(self):
        Path('custom/tools').mkdir(parents=True)
        Path('docs/tools').mkdir(parents=True)
        Path('custom/tools/PowerPoint.md').write_text('# PowerPoint\n')
        Path('docs/tools/PowerPoint.md').write_text('# Old\n')
        updater.process_custom_files()
        self.assertEqual([p.name for p in Path('docs/tools').glob('*.md')], ['PowerPoint.md'])
