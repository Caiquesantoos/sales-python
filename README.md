# Sales Python — análise de vendas por CSV
CLI em Python 3.10+ que calcula receita e unidades, rejeita linhas inválidas e exporta JSON. Sem dependências externas. Amostra fictícia.
```sh
python sales.py sample.csv
python sales.py sample.csv --output report.json
python -m unittest -v
```
## Contrato de entrada
CSV UTF-8 com cabeçalhos product,quantity,price. Quantidade inteira positiva, preço decimal não negativo com até duas casas e ponto decimal. Linhas inválidas são listadas pelo número físico para CSVs sem campos multilinha; cabeçalhos ausentes encerram com código 2.

## Decisões
Decimal preserva precisão monetária; leitura sequencial não carrega o CSV inteiro. Não mistura moedas: a origem deve fornecer uma única moeda. Sem deduplicação, impostos, estornos ou conversão cambial. Próximos passos: validação de moeda, identificador de venda e relatório por produto.
