import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error, r2_score

# Carregar os dados da planilha
file_path = 'loja_roupas_dados.xlsx'
data = pd.read_excel(file_path)

# Limpar os dados da coluna 'Total' para que seja possível trabalhar com valores numéricos
data['Total'] = data['Total'].replace({'R\$ ': '', ' ': '', ',': '.'}, regex=True).astype(float)

# Criar uma nova coluna para mapear os meses
meses_map = {
    "Janeiro": 1,
    "Fevereiro": 2,
    "Março": 3,
    "Abril": 4,
    "Maio": 5,
    "Junho": 6,
    "Julho": 7,
    "Agosto": 8,
    "Setembro": 9,
    "Outubro": 10,
    "Novembro": 11,
    "Dezembro": 12
}

data['Mês'] = data['Mês'].map(meses_map)

# Agrupar dados por mês e produto, somando as quantidades vendidas
vendas_por_produto = data.groupby(['Mês', 'Produto'])['Quantidade Vendida'].sum().reset_index()

# Visualizar as vendas totais por produto por mês
plt.figure(figsize=(12, 6))
sns.barplot(x='Mês', y='Quantidade Vendida', hue='Produto', data=vendas_por_produto, palette='deep')
plt.title('Vendas Totais por Mês e Produto')
plt.xlabel('Mês')
plt.ylabel('Quantidade Vendida')
plt.xticks(ticks=range(1, 13), labels=list(meses_map.keys()), rotation=45)
plt.legend(title='Produto')
plt.grid()
plt.show()

# Análise de regressão para todos os produtos
produtos_unicos = data['Produto'].unique()

for produto in produtos_unicos:
    produto_data = data[data['Produto'] == produto]
    X = produto_data[['Mês']]
    y = produto_data['Quantidade Vendida']

    # Dividir os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Regressão Linear para cada produto
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    y_pred_linear = lin_reg.predict(X_test)

    # Avaliar o modelo de Regressão Linear
    print(f"\nRegressão Linear para {produto}:")
    print(f"MSE: {mean_squared_error(y_test, y_pred_linear)}")
    print(f"R²: {r2_score(y_test, y_pred_linear)}")

    # Comparação de Vendas: Gráficos para cada produto
    plt.figure(figsize=(10, 5))
    plt.plot(X_test['Mês'], y_test, marker='o', label='Dados reais', color='blue', linestyle='-')
    plt.plot(X_test['Mês'], y_pred_linear, marker='o', label='Previsão (Regressão Linear)', color='red', linestyle='--')
    plt.title(f'Comparação de Vendas de {produto}: Modelo de Regressão Linear')
    plt.xlabel('Mês')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(X_test['Mês'])
    plt.legend()
    plt.grid()
    plt.show()

# Criar uma árvore de decisão para prever a quantidade vendida baseada nas vendas de todos os produtos
X_all = data[['Mês']]  # Usando apenas o mês como variável preditora para simplificação
y_all = data['Quantidade Vendida']

# Dividir os dados em conjuntos de treino e teste
X_train_all, X_test_all, y_train_all, y_test_all = train_test_split(X_all, y_all, test_size=0.2, random_state=42)

# Treinar a árvore de decisão
tree_reg = DecisionTreeRegressor(random_state=42)
tree_reg.fit(X_train_all, y_train_all)

# Prever usando a árvore de decisão
y_pred_tree = tree_reg.predict(X_test_all)

# Avaliar o modelo de Árvore de Decisão
print("\nÁrvore de Decisão:")
print(f"MSE: {mean_squared_error(y_test_all, y_pred_tree)}")
print(f"R²: {r2_score(y_test_all, y_pred_tree)}")

# Visualizar a árvore de decisão com tamanhos de fonte maiores
plt.figure(figsize=(16, 12))  # Aumentar o tamanho da figura
plot_tree(tree_reg, filled=True, feature_names=X_all.columns, rounded=True, impurity=False, fontsize=12)  # Aumentar o tamanho da fonte
plt.title('Árvore de Decisão para Previsão de Vendas')
plt.show()

# Opcional: Salvar a árvore como uma imagem
plt.figure(figsize=(16, 12))
plot_tree(tree_reg, filled=True, feature_names=X_all.columns, rounded=True, impurity=False, fontsize=12)
plt.title('Árvore de Decisão para Previsão de Vendas')
plt.savefig('arvore_decisao_vendas.png', bbox_inches='tight')  # Salvar a árvore como um arquivo PNG
plt.close()  # Fechar a figura para não exibi-la novamente
