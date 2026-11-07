"""Relatório de vendas CSV com validação e aritmética decimal."""
import argparse
import csv
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

def summarize(path):
    revenue = Decimal('0')
    units = 0
    rejected = []
    with Path(path).open(encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        if not {'product', 'quantity', 'price'} <= set(reader.fieldnames or []):
            raise ValueError('CSV exige product, quantity e price')
        for line, row in enumerate(reader, 2):
            try:
                quantity = int(row['quantity'])
                price = Decimal(row['price'])
                if not row['product'].strip() or quantity <= 0 or not price.is_finite() or price < 0 or price != price.quantize(Decimal('.01')):
                    raise ValueError('Valores inválidos')
            except (ValueError, InvalidOperation, AttributeError):
                rejected.append(line)
                continue
            units += quantity
            revenue += quantity * price
    return {'revenue': str(revenue.quantize(Decimal('.01'))), 'units': units, 'rejected_lines': rejected}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        report = json.dumps(summarize(args.csv), ensure_ascii=False, indent=2)
    except (OSError, ValueError) as error:
        parser.exit(2, f'Erro: {error}\n')
    if args.output:
        args.output.write_text(report + '\n', encoding='utf-8')
    else:
        print(report)

if __name__ == '__main__':
    main()
