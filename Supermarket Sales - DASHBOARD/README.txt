*Supermarket Sales Dashboard*

Este projeto é um dashboard interativo de vendas de supermercado, criado com Streamlit e Plotly. Ele fornece uma visão detalhada dos dados de vendas, permitindo explorar o faturamento, os produtos mais vendidos, a contribuição das filiais, o desempenho dos métodos de pagamento e a avaliação média das lojas.

Funcionalidades
Visão mensal das vendas: Filtre as vendas por mês e analise o desempenho em tempo real.
Faturamento por dia: Visualize o faturamento diário, organizado por cidade.
Faturamento por tipo de produto: Acompanhe os tipos de produto mais vendidos.
Contribuição das filiais: Explore o faturamento total por filial.
Desempenho dos métodos de pagamento: Analise a distribuição dos pagamentos por tipo.
Avaliação das filiais: Visualize as avaliações médias de cada filial.

Instalação
Clone o repositório para o seu ambiente local:



git clone https://github.com/seu-usuario/seu-repositorio.git
Navegue até o diretório do projeto:


cd nome-do-diretorio
Instale as dependências necessárias:


pip install -r requirements.txt
Ou instale individualmente:


pip install streamlit pandas plotly
Executando o Dashboard
Para executar o dashboard, utilize o seguinte comando:


streamlit run dashboards.py
Estrutura de Arquivo Esperada
Este código espera o arquivo supermarket_sales.csv na mesma pasta que o script dashboards.py. Certifique-se de que o arquivo supermarket_sales.csv esteja no diretório correto para evitar erros.

Visualizações
Faturamento por Dia: Exibe o faturamento por dia de acordo com a cidade.
Faturamento por Tipo de Produto: Exibe o faturamento dividido por tipo de produto, facilitando a identificação dos mais vendidos.
Faturamento por Filial: Mostra o faturamento de cada filial.
Desempenho dos Métodos de Pagamento: Gráfico de pizza para comparar os diferentes tipos de pagamento.
Avaliação Média das Filiais: Exibe a média das avaliações de cada filial.
Observações
Este dashboard foi projetado para facilitar a análise de dados de vendas e dar suporte a decisões de negócios.
Certifique-se de configurar o layout com wide para uma exibição ideal.
Tecnologias Utilizadas
Python: Linguagem principal.
Pandas: Para manipulação de dados.
Plotly: Para criação de visualizações interativas.
Streamlit: Para desenvolvimento e exibição do dashboard interativo.