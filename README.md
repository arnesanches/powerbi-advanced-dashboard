### English

# Power BI Advanced Dashboard

## Description

This project features an interactive dashboard built in Power BI to present financial data in a clear and visually appealing way. One of the most impressive aspects of this project is the advanced interactivity of the dashboard. By hovering over or selecting a bank's logo, all the data in the dashboard is automatically updated to reflect the specific results for that bank.

## Video Demonstration

To view the interactivity and dynamism of this dashboard, watch the demonstration video, which is located in the same directory as the project. In this brief video, you can see how the data is automatically updated when selecting different banks, highlighting the interactive features and dynamic changes in the dashboard.

## Key Features:

- **Dynamic Charts**: All charts, including the waterfall chart and indicators, change according to the selection, facilitating decision-making based on financial data.  
- **Updated Values**: Key values such as revenue, costs, taxes, and profit, located at the top of the dashboard, are also dynamically adjusted.  
- **Custom Comments**: Even the brief comment on the dashboard, which includes numerical variables, changes according to the selected bank.  
- **Intuitive Design**: Focused on delivering a user-friendly experience, even for non-technical users.  

These features provide a highly interactive user experience, making financial analysis more practical and engaging.

## How It Works

The input data is loaded from an Excel file, which contains information about financial transactions, such as transaction type (revenue or payment) and payment method. This data is then used to calculate the following indicators:

- **Total revenue**: The sum of all revenue transactions.
- **Total costs**: The sum of all payment transactions (negative values).
- **Taxes**: Calculated as 15% of total revenue.
- **Total profit**: Total revenue - Total costs - Taxes.
- **Profit margin**: Calculated as the ratio of profit to total revenue.
- **Cash flow**: The difference between total revenue and total payments.
- **Percentage of transactions via Pix**: The percentage of transactions made via Pix.
- **Target deviation**: Comparison between the profit margin of different cities and the target of 30%.

## How Power BI Was Used

**Power BI** was the main tool used to:

1. **Load financial data** from an Excel file.
2. **Create interactive visualizations** to represent the calculations and metrics clearly and visually.
3. **Set up logos** for the banks, ensuring a professional design for the dashboard.

## How Python Was Used

Although Power BI was the main tool for generating the calculations and the dashboard, Python code was used to calculate the variables and ensure the consistency of the values presented. The Python code performs the following calculations:

- **Total revenue**
- **Total costs**
- **Taxes (15% of revenue)**
- **Total profit**
- **Profit margin**
- **Cash flow**
- **Percentage of transactions via Pix**
- **Target deviation**

The Python code is present in this repository as an extra confirmation of the values calculated in Power BI, providing "proof" that the results are consistent and accurate.

## Repository Structure

The repository contains the following files:

- **python_code**: Python scripts that perform the financial calculations and ensure the consistency of the results.
- **powerbi_advanced_dashboard**: Power BI dashboard file (.pbix).
- **excel_data**: Excel file with the financial transaction data.
- **Dashboard Demonstration**: A brief video that demonstrates the interactivity and dynamism of the dashboard, showing how the data is automatically updated when selecting different banks.
- **README.md**: This file, which explains the project, how it works, and how the code is structured.

## How to Run the Project

1. **Power BI**:
    - Open the `powerbi_advanced_dashboard.pbix` file in Power BI Desktop.
    - The dashboard will automatically load the financial data and display the interactive visualizations.
  
2. **Python**:
    - If you want to verify the calculations, you can run the `python_code.py` or `python_code.ipynb` files in a Python environment.
    - The calculations made in Python are an extra confirmation of the values in Power BI.

## Conclusion

This project was developed to demonstrate skills in using **Power BI** for financial data analysis and creating interactive visualizations. Additionally, the use of **Python** as a tool for verifying the calculations shows the accuracy and consistency of the data presented. The combination of these two tools is a powerful way to present financial insights clearly and effectively.

## Technologies Used

- **Power BI**: For visualization and creating interactive dashboards.
- **Python**: For financial calculations and verification of results.
- **Pandas**: For financial data manipulation in Python.

## License

This project is licensed under the [MIT License](LICENSE).

---

### Português

# Power BI Advanced Dashboard

## Descrição

Este projeto consiste em um dashboard interativo no Power BI para apresentar dados financeiros de maneira clara e visualmente atraente. Uma das características mais impressionantes deste projeto é a interatividade avançada do dashboard. Ao passar o mouse ou selecionar a logomarca de um banco, todos os dados no dashboard são atualizados automaticamente para refletir os resultados específicos daquele banco.  

## Demonstração em Vídeo

Para visualizar a interatividade e o dinamismo deste dashboard, assista ao vídeo de demonstração, que se encontra no mesmo diretório do projeto. Nesse breve vídeo, é possível ver como os dados são atualizados automaticamente ao selecionar diferentes bancos, destacando as funcionalidades interativas e as mudanças dinâmicas no dashboard.

## Principais Características:

- **Gráficos Dinâmicos**: Todos os gráficos, incluindo o gráfico de cascata e os indicadores, mudam de acordo com a seleção, facilitando a tomada de decisões com base em dados financeiros.  
- **Valores Atualizados**: Os valores principais, como receita, custos, impostos e lucro, localizados na parte superior do dashboard, também são ajustados dinamicamente.  
- **Comentários Personalizados**: Até mesmo o breve comentário no dashboard, que contém variáveis numéricas, é alterado conforme o banco selecionado.
- **Design Intuitivo**: Focado em entregar uma experiência amigável, mesmo para usuários não técnicos.  

Essas funcionalidades proporcionam uma experiência de usuário altamente interativa, tornando a análise financeira mais prática e envolvente.  

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
3. **Configurar logotipos** para os bancos, garantindo um design profissional no dashboard.

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

O repositório contém os seguintes arquivos:

- **python_code**: Scripts Python que realizam os cálculos financeiros e garantem a consistência dos resultados.
- **powerbi_advanced_dashboard**: Arquivo do dashboard criado no Power BI (.pbix).
- **excel_data**: Arquivo Excel com os dados de transações financeiras.
- **Dashboard Demonstration**: Vídeo breve que demonstra a interatividade e o dinamismo do dashboard, mostrando como os dados são atualizados automaticamente ao selecionar diferentes bancos.
- **README.md**: Este arquivo, que explica o projeto, como ele funciona e como o código foi estruturado.

## Como Executar o Projeto

1. **Power BI**:
    - Abra o arquivo `powerbi_advanced_dashboard.pbix` no Power BI Desktop.
    - O dashboard irá carregar automaticamente os dados financeiros e exibir as visualizações interativas.
  
2. **Python**:
    - Se quiser conferir os cálculos realizados, você pode executar os arquivos `python_code.py` ou `python_code.ipynb` no ambiente Python.
    - Os cálculos feitos no Python são uma confirmação extra dos valores que estão no Power BI.

## Conclusão

Este projeto foi desenvolvido para demonstrar habilidades no uso do **Power BI** para análise de dados financeiros e na criação de visualizações interativas. Além disso, o uso do **Python** como ferramenta de conferência dos cálculos mostra a precisão e consistência dos dados apresentados. A combinação dessas duas ferramentas é uma maneira poderosa de apresentar insights financeiros de maneira clara e eficaz.

## Tecnologias Utilizadas

- **Power BI**: Para visualização e criação de dashboards interativos.
- **Python**: Para cálculos financeiros e confirmação dos resultados.
- **Pandas**: Para manipulação de dados financeiros no Python.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

