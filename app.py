import streamlit as st


st.title(' Aula 7 - Meu primeiro deploy')

# Cria uma barra de seleção
slider = st.slider("Selecione o ano: ", min_value=1995, max_value=2024)
st.write(f'O ano selecionado foi: {slider}')

# Cria uma barra de seleção podendo seleciona os anos que vão aparecer
st.select_slider("Selecione o ano", options=[1995, 2015, 2023, 2024, 2025])

# git add . (sempre que for adicionar)
#git commit -m

#$ pip freeze > requiriments.txt: Qual são as bibliotecas instaladaas