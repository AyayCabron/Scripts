import pandas as pd
import matplotlib.pyplot as plt

# variavel que irá armazenar o dataframe
data = pd.read_excel("call_data.xlsx")

#calcular média da duração das chamadas (data['duration'] acessa a coluna duration do DataFrame, que supostamente contém a duração de cada chamada.)
#.mean() calcula a média dos valores nessa coluna. 2 O resultado é armazenado em average_duration, representando a duração média em segundos de todas as chamadas.

average_duration = data["duration"].mean()

#converte para minutos
average_duration_minutes = average_duration/ 60

# Calcular a taxa de sucesso (chamadas atendidas) - len(data) conta o número total de linhas no DataFrame, ou seja, o total de chamadas.
# Enquanto total_calls vai armazenar esse valor.
total_calls = len(data)

#data[data['status'] == 'answered'] cria um DataFrame filtrado com apenas as linhas onde o valor na coluna status é 'answered', indicando chamadas atendidas.
#len(...) conta o número de linhas nesse DataFrame filtrado, que corresponde ao total de chamadas atendidas.
#answered_calls armazena esse valor.

answered_calls = len(data[data["status"]== "answered"])

#answered_calls / total_calls calcula a proporção de chamadas atendidas em relação ao total.
#Multiplicar por 100 converte essa proporção para uma porcentagem.
#success_rate guarda essa taxa de sucesso como uma porcentagem.

sucess_rate = (answered_calls / total_calls) * 100

print(f"Média de duração das chamadas: {average_duration / 60:.2f} minutos")
print(f"Taxa de sucesso: {sucess_rate: .2f} %")

#configurar o gráfico

metrics = ["Média de Duração (min)" , "Taxa de Sucesso (%)"]
values = [average_duration_minutes, sucess_rate]
plt.figure(figsize=(8, 5))
plt.bar(metrics, values, color=["skyblue", "lightgreen"])
plt.ylabel("Valores")
plt.title("Métricas de Chamadas")
plt.ylim(0, max(values) + 10) #ajusta o limite do eixo y

#exibir os valores em cima das barras

for index, value in enumerate(values):
    plt.text(index, value + 1, f"{value:.2f}", ha="center")


#mostrar o gráfico
plt.show()