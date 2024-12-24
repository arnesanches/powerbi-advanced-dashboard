# Projeto de Dashboard Financeiro no Power BI

Este projeto consiste em um **dashboard financeiro** criado no Power BI, com cálculos e visualizações detalhadas sobre receita, custos, lucros, impostos, margem de lucro e fluxo de caixa. Os resultados são extraídos diretamente de um conjunto de dados financeiros, e o dashboard é projetado para fornecer insights sobre a performance financeira de uma organização.

## Objetivo

O principal objetivo deste projeto foi criar um dashboard interativo no Power BI para apresentar dados financeiros de maneira clara e visualmente atraente, utilizando os seguintes cálculos:

- **Receita total**
- **Custos totais**
- **Impostos (15% da receita)**
- **Lucro total**
- **Margem de lucro**
- **Fluxo de caixa**
- **Percentual de transações via Pix**
- **Desvio de meta de margem de lucro por cidade**

## Como Funciona

Os dados de entrada são carregados a partir de um arquivo Excel, que contém informações sobre transações financeiras, como tipo de movimentação (recebimento ou pagamento) e forma de pagamento. Esses dados são então usados para calcular os seguintes indicadores:

- **Receita total**: A soma de todos os recebimentos.
- **Custos totais**: A soma de todos os pagamentos (valores negativos).
- **Impostos**: Calculado como 15% da receita total.
- **Lucro total**: Receita total - Custos totais - Impostos.
- **Margem de lucro**: Calculada como a razão entre o lucro e a receita total.
- **Fluxo de caixa**: A diferença entre recebimentos totais e pagamentos totais.
- **Percentual de transações via Pix**: A porcentagem de transações realizadas via Pix.
- **Desvio de meta**: Comparação entre a margem de lucro de diferentes cidades e a meta de 30%.

## Como o Power BI foi usado

O **Power BI** foi a principal ferramenta usada para:

1. **Carregar os dados financeiros** a partir de um arquivo Excel.
2. **Criar visualizações interativas** para representar os cálculos e as métricas de maneira clara e visual.
3. **Configurar imagens e logotipos** para os bancos, garantindo um design profissional no dashboard.

## Como o Python foi usado

Embora o Power BI tenha sido a ferramenta principal para gerar os cálculos e o dashboard, o código Python foi utilizado para calcular as variáveis e garantir a consistência dos valores apresentados. O código Python realiza os seguintes cálculos:

- **Receita total**
- **Custos totais**
- **Impostos (15% da receita)**
- **Lucro total**
- **Margem de lucro**
- **Fluxo de caixa**
- **Percentual de transações via Pix**
- **Desvio de meta**

O código Python está presente neste repositório como uma confirmação extra dos valores calculados no Power BI, fornecendo uma "prova" de que os resultados são consistentes e precisos.

## Estrutura do Repositório

O repositório contém as seguintes pastas e arquivos:

- **/python_code**: Contém os scripts Python que realizam os cálculos financeiros e garantem a consistência dos resultados.
- **/powerbi_dashboard**: Contém o arquivo do dashboard criado no Power BI (.pbix).
- **README.md**: Este arquivo, que explica o projeto, como ele funciona e como o código foi estruturado.

## Como Executar o Projeto

1. **Power BI**:
    - Abra o arquivo `dashboard.pbix` no Power BI Desktop.
    - O dashboard irá carregar automaticamente os dados financeiros e exibir as visualizações interativas.
  
2. **Python**:
    - Se quiser conferir os cálculos realizados, você pode executar os arquivos `script.py` ou `script.ipynb` no ambiente Python.
    - Os cálculos feitos no Python são uma confirmação extra dos valores que estão no Power BI.

## Conclusão

Este projeto foi desenvolvido para demonstrar habilidades no uso do **Power BI** para análise de dados financeiros e na criação de visualizações interativas. Além disso, o uso do **Python** como ferramenta de conferência dos cálculos mostra a precisão e consistência dos dados apresentados. A combinação dessas duas ferramentas é uma maneira poderosa de apresentar insights financeiros de maneira clara e eficaz.

## Tecnologias Utilizadas

- **Power BI**: Para visualização e criação de dashboards interativos.
- **Python**: Para cálculos financeiros e confirmação dos resultados.
- **Pandas**: Para manipulação de dados financeiros no Python.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

