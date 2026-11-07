import tempfile
import unittest
from pathlib import Path
from sales import summarize

class SalesTest(unittest.TestCase):
    def report(self, data):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'sales.csv'
            path.write_text(data,encoding='utf-8')
            return summarize(path)
    def test_decimal_and_invalid_rows(self):
        result=self.report('product,quantity,price\na,3,0.10\nb,0,5\nc,1,NaN\nd,1,1.001\n')
        self.assertEqual(result,{'revenue':'0.30','units':3,'rejected_lines':[3,4,5]})
    def test_missing_headers(self):
        with self.assertRaises(ValueError): self.report('name\na\n')
    def test_empty(self):
        self.assertEqual(self.report('product,quantity,price\n')['revenue'],'0.00')

if __name__=='__main__': unittest.main()
