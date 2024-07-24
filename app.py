import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carregar os dados
df = pd.read_csv('diametro_por_preco_pizzas.csv')

# Treinar o modelo
modelo = LinearRegression()
x = df[['diametro']]
y = df[['preco']]
modelo.fit(x, y)

# Aplicativo Streamlit
st.title('Previsão de Preço de Pizzas')
st.write(
    '''
    Este aplicativo prevê o preço de uma pizza com base no seu diâmetro. 
    Insira o diâmetro da pizza em centímetros para obter uma estimativa do preço.
    '''
)
st.divider()

diametro = st.number_input('Digite o diâmetro da pizza (cm)', min_value=0, max_value=100, step=1)

if diametro:
    try:
        preco_previsto = modelo.predict([[diametro]])[0][0]
        st.write(f'O preço estimado para uma pizza de {diametro} cm é R$ {preco_previsto:.2f}')
    except Exception as e:
        st.error(f'Ocorreu um erro ao fazer a previsão: {e}')
