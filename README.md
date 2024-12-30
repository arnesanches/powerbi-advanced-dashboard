#### English

# Power BI Advanced Dashboard

This project features an interactive dashboard built in Power BI to present financial data in a clear and visually appealing way. One of the most impressive aspects of this project is the advanced interactivity of the dashboard. By hovering over or selecting a bank's logo, all the data in the dashboard is automatically updated to reflect the specific results for that bank. The Excel data is integrated into the Power BI .pbix file, eliminating the need to load external files to view the dashboard.

## Demonstration Video

To experience the interactivity and dynamism of the dashboard, download the "Dashboard Demonstration" video located in the project directory. GitHub does not support direct video playback, so you will need to download the file to watch it.

## Key Features:

- **Dynamic Charts**: All charts, including the waterfall chart and indicators, change according to the selection, facilitating decision-making based on financial data.  
- **Updated Values**: Key values such as revenue, costs, taxes, and profit, located at the top of the dashboard, are also dynamically adjusted.  
- **Custom Comments**: Even the brief comment on the dashboard, which includes numerical variables, changes according to the selected bank.  
- **Intuitive Design**: Focused on delivering a user-friendly experience, even for non-technical users.  

These features provide a highly interactive user experience, making financial analysis more practical and engaging.

## How It Works and Tools Used

The input data, derived from an Excel spreadsheet, contains financial information such as transaction type (revenue or payment) and payment method. From this data, key indicators were calculated, including total revenue, total costs, profit, profit margin, cash flow, and the percentage of transactions via Pix.

### Use of Power BI

**Power BI** was used to create the interactive dashboard, presenting results in a clear and visual manner. The tool enables:

- Loading financial data directly integrated into the Power BI (.pbix) file.  
- Presenting metrics and insights dynamically and interactively.  
- Customizing the design, including bank logos, for a professional visual experience.

### Use of Python

**Python** was employed as an additional step to validate the financial calculations, ensuring consistency and accuracy. The calculations include indicators such as revenue, costs, taxes, profit, and profit margin.

## Repository Structure

The repository contains the following files:

- **python_code**: Python script that performs the financial calculations and ensure the consistency of the results.
- **powerbi_advanced_dashboard**: Power BI dashboard file (.pbix).
- **Dashboard Demonstration**: A brief video that demonstrates the interactivity and dynamism of the dashboard, showing how the data is automatically updated when selecting different banks.
- **README.md**: This file, which explains the project, how it works, and how the code is structured.

## How to Run the Project

1. **Power BI**:
    - Open the `powerbi_advanced_dashboard.pbix` file in Power BI Desktop. You can download the latest version of Power BI Desktop [here](https://www.microsoft.com/pt-br/download/details.aspx?id=58494).
    - The dashboard will automatically load the financial data and display the interactive visualizations.
  
2. **Python**:
    - If you want to verify the calculations, you can run the `python_code.py` file in a Python environment.
    - The calculations made in Python are an extra confirmation of the values in Power BI.

## Conclusion

This project was developed to demonstrate skills in using **Power BI** for financial data analysis and creating interactive visualizations. Additionally, the use of **Python** as a tool for verifying the calculations shows the accuracy and consistency of the data presented. The combination of these two tools is a powerful way to present financial insights clearly and effectively.

## Technologies Used

- **Power BI**: For visualization and creating interactive dashboards.
- **Python**: For financial calculations and verification of results.
- **Pandas**: For financial data manipulation in Python.

## License

This project is licensed under the MIT License.

---

#### Português

# Power BI Advanced Dashboard

Este projeto consiste em um dashboard interativo no Power BI, desenvolvido para apresentar dados financeiros de forma clara e visualmente atraente. Um dos destaques mais impressionantes é a interatividade avançada do dashboard, que permite aos usuários filtrar os dados ao passar o mouse sobre a logomarca de um banco ou ao clicar nela, atualizando instantaneamente todos os elementos visuais. Isso possibilita comparações rápidas e eficientes. Além disso, os dados da planilha Excel estão incorporados no arquivo .pbix, eliminando a necessidade de arquivos externos e facilitando tanto a distribuição quanto o uso do dashboard.

## Vídeo de Demonstração

Para visualizar a interatividade e o dinamismo do dashboard, faça o download do vídeo "Dashboard Demonstration" que está no mesmo diretório do projeto. O GitHub não suporta a reprodução de vídeos diretamente, então é necessário baixar o arquivo para assisti-lo.

## Principais Características:

- **Gráficos Dinâmicos**: Todos os gráficos, incluindo o gráfico de cascata e os indicadores, mudam de acordo com a seleção, facilitando a tomada de decisões com base em dados financeiros.  
- **Valores Atualizados**: Os valores principais, como receita, custos, impostos e lucro, localizados na parte superior do dashboard, também são ajustados dinamicamente.  
- **Comentários Personalizados**: Até mesmo o breve comentário no dashboard, que contém variáveis numéricas, é alterado conforme o banco selecionado.
- **Design Intuitivo**: Focado em entregar uma experiência amigável, mesmo para usuários não técnicos.  

Essas funcionalidades proporcionam uma experiência de usuário altamente interativa, tornando a análise financeira mais prática e envolvente.  

## Como Funciona e Ferramentas Utilizadas

Os dados de entrada, provenientes de uma planilha Excel, contêm informações financeiras, como tipo de movimentação (recebimento ou pagamento) e forma de pagamento. A partir desses dados, foram calculados indicadores essenciais, como receita total, custos totais, lucro, margem de lucro, fluxo de caixa e percentual de transações via Pix.

### Uso do Power BI

O **Power BI** foi utilizado para criar o dashboard interativo, apresentando os resultados de maneira clara e visual. A ferramenta permite:

- Carregar os dados financeiros integrados diretamente no arquivo Power BI (.pbix).  
- Apresentar métricas e insights de forma dinâmica e interativa.  
- Personalizar o design, incluindo logotipos de bancos, para uma experiência visual profissional.

### Uso do Python

O **Python** foi empregado como uma etapa adicional para validar os cálculos financeiros, garantindo consistência e precisão. Os cálculos incluem indicadores como receita, custos, impostos, lucro e margem de lucro.

## Estrutura do Repositório

O repositório contém os seguintes arquivos:

- **python_code**: Script Python que realiza os cálculos financeiros e garantem a consistência dos resultados.
- **powerbi_advanced_dashboard**: Arquivo do dashboard criado no Power BI (.pbix).
- **Dashboard Demonstration**: Vídeo breve que demonstra a interatividade e o dinamismo do dashboard, mostrando como os dados são atualizados automaticamente ao selecionar diferentes bancos.
- **README.md**: Este arquivo, que explica o projeto, como ele funciona e como o código foi estruturado.

## Como Executar o Projeto

1. **Power BI**:
    - Abra o arquivo `powerbi_advanced_dashboard.pbix` no Power BI Desktop. Você pode baixar a versão mais recente do Power BI [aqui](https://www.microsoft.com/pt-br/download/details.aspx?id=58494).
    - O dashboard irá carregar automaticamente os dados financeiros e exibir as visualizações interativas.
  
2. **Python**:
    - Se quiser conferir os cálculos realizados, você pode executar o arquivo `python_code.py` no ambiente Python.
    - Os cálculos feitos no Python são uma confirmação extra dos valores que estão no Power BI.

## Conclusão

Este projeto foi desenvolvido para demonstrar habilidades no uso do **Power BI** para análise de dados financeiros e na criação de visualizações interativas. Além disso, o uso do **Python** como ferramenta de conferência dos cálculos mostra a precisão e consistência dos dados apresentados. A combinação dessas duas ferramentas é uma maneira poderosa de apresentar insights financeiros de maneira clara e eficaz.

## Tecnologias Utilizadas

- **Power BI**: Para visualização e criação de dashboards interativos.
- **Python**: Para cálculos financeiros e confirmação dos resultados.
- **Pandas**: Para manipulação de dados financeiros no Python.

## Licença

Este projeto está licenciado sob a MIT License.
