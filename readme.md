# Previsão de Preço de Pizzas

Este projeto é uma aplicação de previsão de preços de pizzas baseada no diâmetro da pizza. A aplicação é desenvolvida usando Streamlit e utiliza um modelo de regressão linear para prever o preço da pizza com base em seu diâmetro.

## Funcionalidades

- **Entrada do Usuário:** Permite que o usuário insira o diâmetro da pizza.
- **Previsão:** Calcula o preço estimado da pizza usando um modelo de regressão linear treinado com dados históricos.
- **Exibição dos Resultados:** Mostra o preço estimado em uma área expansível ou modal para uma melhor visualização.

## Instalação

   ```bash
   pip install -r requirements.txt
   ```

   Certifique-se de que o arquivo `diametro_por_preco_pizzas.csv` esteja presente no diretório do projeto. Este arquivo deve conter os dados históricos em duas colunas, uma de diâmetro e outra de preço, das pizzas usados para treinar o modelo.

## Execução

Para iniciar a aplicação Streamlit, execute o seguinte comando:

```bash
streamlit run ./app.py
```

Isso iniciará o servidor Streamlit e abrirá a aplicação no navegador padrão, geralmente acessível em `http://localhost:8501` (ou na porta especificada).

## Uso

Na página da aplicação, insira o diâmetro da pizza no campo de entrada e pressione enter.
