import unittest
from url_extractor import extract_urls_from_html

class TestURLExtractor(unittest.TestCase):
    def test_extract_urls(self):
        test_file = "example.html"
        expected_urls = [
            "https://example.com",
            "https://github.com",
            "https://www.python.org"
        ]
        self.assertEqual(extract_urls_from_html(test_file), expected_urls)

if __name__ == '__main__':
    unittest.main()
