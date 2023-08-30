import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importando dataset
dataset = pd.read_csv("netflix1.csv")

#retirando dados duplicados
dataset.duplicated(["type","title","release_year"]).sum()
duplicate_rows = dataset[dataset.duplicated(["type","title","release_year"], keep = False)]
rows = duplicate_rows[["type","title","release_year"]].duplicated(keep='first')
indexes_to_drop = duplicate_rows[~rows].index
dataset['date_added'] = pd.to_datetime(dataset['date_added'], format='%m/%d/%Y')
dataset['release_year'] = pd.to_datetime(dataset['release_year'], format='%Y')
dataset['release_year'] = dataset['release_year'].dt.year

#opções do dashboard
st.title('Projeto SAD')
st.sidebar.title('Selecione os módulos')
show_dataset = st.sidebar.checkbox('Mostrar Dataset')
show_movies = st.sidebar.checkbox('Informações sobre os Filmes')
show_tvshow = st.sidebar.checkbox('Informações sobre os Programas de Tv')

#execução
if show_dataset:
    st.dataframe(dataset)
    
if show_movies:
    st.subheader('Selecione como ver os dados')
    op1_movie = st.checkbox('Ver infomações por filme')
    op2_movie = st.checkbox('Ver todas as informações')
    op3_movie = st.checkbox('Informações da quantidade de lançamentos dos filmes por ano')
    op4_movie = st.checkbox('Filmes por cada País')
    op5_movie = st.checkbox('Gêneros mais assistidos')
    
    #funcionalidades
    if op1_movie:
        st.subheader('Selecione o Ano')
        maks_years = dataset[dataset['type'] == 'Movie']['release_year'].value_counts().sort_index()
        movie_counts = st.selectbox(' ',options=maks_years.index)
        st.subheader('Selecione um Filme')
        mask_movies = dataset[dataset['release_year']==movie_counts]
        movie = st.selectbox(' ',options=mask_movies['title'])
        mask_movie = mask_movies[mask_movies["title"]==movie]
        st.dataframe(mask_movie)
    
    if op2_movie:
        st.subheader('Informações Gerais dos Filmes')
        maks_years = dataset[dataset['type'] == 'Movie']['release_year'].value_counts().sort_index()
        movie_counts = st.selectbox('Selecione o ano',options=maks_years.index)
        mask_movies = dataset[dataset['release_year']==movie_counts]
        st.dataframe(mask_movies)
    
    if op3_movie:
        st.subheader('Selecionar quantidade de filmes')
        qtd_movie = st.slider('Quantidade de anos',1,73)
        st.subheader('Selecionar quantidade de filmes por periodos')
        movies_1 = st.checkbox('Filmes de 1942 - 1961')
        movies_2 = st.checkbox('Filmes dos 1962 - 1974')
        movies_3 = st.checkbox('Filmes dos 1975 - 1987')
        movies_4 = st.checkbox('Filmes dos 1988 - 2000')
        movies_5 = st.checkbox('Filmes dos 2000 - 2013')
        movies_6 = st.checkbox('Filmes dos 2013 - 2021')
        
        if qtd_movie:
            count_movies = dataset[dataset['type'] == 'Movie']['release_year'].value_counts().sort_index().head(qtd_movie)

        if movies_1:    
            count_movies = dataset[dataset['type'] == 'Movie']['release_year'].value_counts().sort_index().head(13)

        if movies_2:
            count_movies = dataset[dataset['type'] == 'Movie']['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[14:26]
        
        if movies_3:
            count_movies = dataset[dataset['type'] == 'Movie']['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[26:39]
        
        if movies_4:
            count_movies = dataset[dataset['type'] == 'Movie']['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[39:52]

        if movies_5:
            count_movies = dataset[dataset['type'] == 'Movie']['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[52:65]

        if movies_6:
            count_movies = dataset[dataset['type'] == 'Movie']['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[65:73]
        
        #plotando grafico
        st.bar_chart(count_movies,color='#2b9efc')
    
    if op4_movie:
        st.subheader('Selecione um País')
        mask_country = dataset['country'][dataset['type']=='Movie'].value_counts().sort_index()
        country_counts = st.selectbox('Países',options=mask_country.index)
        mask_movie_country = dataset[dataset['country']==country_counts][dataset['type']=='Movie']
        st.dataframe(mask_movie_country)
        graph_movie_country = st.checkbox('Mostrar quantidade de filmes por cada país')

        if graph_movie_country:
            st.subheader('Selecione a quantidade de Páises')
            qtd_country = st.slider(' ',1,86)
            mask_country = dataset['country'][dataset['type']=='Movie'].value_counts().sort_index().head(qtd_country)
            st.line_chart(mask_country,color='#eb4034',width=900,height=500)

    if op5_movie:
        st.subheader('Selecione uma das opções')
        mask_category = dataset['listed_in'].value_counts()
        graph_qtd_category = st.checkbox('Mostrar gráfico dos gêneros')
        table_qtd_category = st.checkbox('Mostrar tabela dos gêneros')
        graph_genre_country = st.checkbox('Mostrar gêneros por cada país')

        if graph_qtd_category:
            st.subheader('Selecione e quantidade de gêneros')
            qtd_category = st.slider(' ',1,513)
            st.line_chart(mask_category.head(qtd_category),color='#1ff084',height=500,width=700)
        
        if table_qtd_category:
            st.subheader('Selecione e quantidade de gêneros')
            qtd_category = st.slider(' ',1,513)
            st.dataframe(mask_category.head(qtd_category),width=600)
        
        if graph_genre_country:
            st.subheader('Selecione um país')
            mask_country = dataset['country'][dataset['type']=='Movie'].value_counts().sort_index()
            country_counts = st.selectbox('Países',options=mask_country.index)
            mask_movie_country_genre = dataset[dataset['country']==country_counts][dataset['type']=='Movie']['listed_in'].value_counts().sort_index()
            st.bar_chart(mask_movie_country_genre,height=400,color='#a22bfc')

