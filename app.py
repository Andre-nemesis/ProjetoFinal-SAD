import streamlit as st
import pandas as pd

#importando dataset
dataset = pd.read_csv("netflix1.csv")

#Nome da equipe
equipe="""
<p class="css-cio0dv ea3mdgi1">
Developed by André Casimiro, Carlos Jeronimo, Fábio Souza, Miqueias, Rian
</p>
"""
st.markdown(equipe,unsafe_allow_html=True)

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

titulos_abas = ['Mostrar Dataset', 'Informações sobre os Filmes', 'Informações sobre os Programas de Tv', 'Informações gerais sobre Programas e Filmes']
abas = st.tabs(titulos_abas)

with abas[0]:
    st.header('Dados do Dataset')
    st.dataframe(dataset)
 
with abas[1]:
    st.subheader('Selecione como ver os dados')
    op1_movie = st.checkbox('Ver infomações por filme')
    op2_movie = st.checkbox('Ver todas as informações dos Filmes')
    op3_movie = st.checkbox('Informações da quantidade de lançamentos dos filmes por ano')
    op4_movie = st.checkbox('Filmes por cada País')
    op5_movie = st.checkbox('Gêneros de Filmes mais assistidos')
    op6_movie = st.checkbox('Classificação dos Filmes')
    
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
        mask_movies = dataset[dataset['release_year']==movie_counts][dataset['type']=='Movie']
        st.dataframe(mask_movies)
        show_duration_movie = st.checkbox('Mostrar informações sobre o tempo de duração dos filmes')
        show_director_movie = st.checkbox('Quantidade de Filmes por cada diretor')
        show_top_genre_movie = st.checkbox('Mostrar Gêneros mais assistidos (Filmes)')
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_movie = st.checkbox('Gráfico de Barras')
        graph_line_movie = st.checkbox('Gráfico de Linhas')

        if show_duration_movie:
            st.subheader('Tempo de duração dos Filmes')
            mask_movie_duration = dataset[dataset['type'] == 'Movie'][dataset['release_year']==movie_counts]['duration'].value_counts().sort_index()
    
        if show_director_movie:
            st.subheader('Qunatidade de Filmes por cada Diretor')
            st.text('Not Given = Desconhecido')
            geral_director = st.checkbox('Ver estástica Geral dos diretores')

            if geral_director:
                st.subheader('Estastisca geral dos Diretores que Produziram filmes')
                qtd_director = st.slider('Quantidade de Diretores',1,4355)
                mask_director_geral = dataset[dataset['type'] == 'Movie']['director'].value_counts().sort_values(ascending=False).head(qtd_director)
            st.subheader(f'Quantidade de filmes por cada diretor no ano: {movie_counts}')
            mask_director = dataset[dataset['type'] == 'Movie'][dataset['release_year']==movie_counts]['director'].value_counts().sort_index()

        if show_top_genre_movie:
            mask_genre_geral_movie = dataset['listed_in'][dataset['type'] == 'Movie'].value_counts().sort_values(ascending=False)
            st.subheader('Gêneros de Programas mais assistidos')
            qtd_geral_genre_tv = st.slider('Selecione quantos gêneros de Filmes deseja ver',1,278)

        if graph_bar_movie:
            if show_duration_movie:
                st.bar_chart(mask_movie_duration,height=500,color='#1129ad')
            if show_director_movie:
                if geral_director:
                    st.bar_chart(mask_director_geral,color='#ad4d11',height=400,width=700)
                st.bar_chart(mask_director,color='#ad4d11',height=400)
            if show_top_genre_movie:
                st.bar_chart(mask_genre_geral_movie.head(qtd_geral_genre_tv),height=400,color='#03fc49')
        
        if graph_line_movie:
            if show_duration_movie:
                st.line_chart(mask_movie_duration,height=500,color='#1129ad')
            if show_director_movie:
                if geral_director:
                    st.line_chart(mask_director_geral,color='#ad4d11',height=400,width=700)
                st.line_chart(mask_director,color='#ad4d11',height=400)
            if show_top_genre_movie:
                st.line_chart(mask_genre_geral_movie.head(qtd_geral_genre_tv),height=400,color='#03fc49')

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
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_movie_2 = st.checkbox('Gráfico de Barras')
        graph_line_movie_2 = st.checkbox('Gráfico de Linhas')
        
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
        if graph_bar_movie_2:
            st.bar_chart(count_movies,color='#2b9efc')
        
        if graph_line_movie_2:
            st.line_chart(count_movies,color='#2b9efc')
        
    
    if op4_movie:
        st.subheader('Selecione um País')
        mask_country = dataset['country'][dataset['type']=='Movie'].value_counts().sort_index()
        country_counts = st.selectbox('Países',options=mask_country.index)
        mask_movie_country = dataset[dataset['country']==country_counts][dataset['type']=='Movie']
        st.dataframe(mask_movie_country)
        graph_movie_country = st.checkbox('Mostrar quantidade de filmes por cada país')
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_movie_3 = st.checkbox('Gráfico de Barras')
        graph_line_movie_3 = st.checkbox('Gráfico de Linhas')

        if graph_movie_country:
            st.subheader('Selecione a quantidade de Páises')
            qtd_country = st.slider(' ',1,86)
            st.text('Not Given = Desconhecido')
            mask_country = dataset['country'][dataset['type']=='Movie'].value_counts().sort_values(ascending=False).head(qtd_country)
        
        if graph_bar_movie_3:
            if graph_movie_country:
                st.bar_chart(mask_country,color='#eb4034',width=900,height=500)
        if graph_line_movie_3:
            if graph_movie_country:
                st.line_chart(mask_country,color='#eb4034',width=900,height=500)

    if op5_movie:
        st.subheader('Selecione uma das opções')
        mask_category = dataset['listed_in'][dataset['type']=='Movie'].value_counts()
        graph_qtd_category = st.checkbox('Mostrar gráfico dos gêneros')
        table_qtd_category = st.checkbox('Mostrar tabela dos gêneros')
        graph_genre_country = st.checkbox('Mostrar gêneros por cada país')
        graph_country_genre = st.checkbox('Ver informações sobre cada gênero')
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_movie_4 = st.checkbox('Gráfico de Barras')
        graph_line_movie_4 = st.checkbox('Gráfico de Linhas')

        if graph_qtd_category:
            st.subheader('Selecione e quantidade de gêneros')
            qtd_category = st.slider(' ',1,278)
        
        if table_qtd_category:
            st.subheader('Selecione e quantidade de gêneros')
            qtd_category = st.slider(' ',1,278)
            st.dataframe(mask_category.head(qtd_category),width=600)
        
        if graph_genre_country:
            st.subheader('Selecione um país')
            mask_country = dataset['country'][dataset['type']=='Movie'].value_counts().sort_index()
            country_counts = st.selectbox('Países',options=mask_country.index)
            mask_movie_country_genre = dataset[dataset['country']==country_counts][dataset['type']=='Movie']['listed_in'].value_counts().sort_index()

        if graph_country_genre:
            st.subheader('Selecione o gênero')
            mask_genre = dataset['listed_in'][dataset['type']=='Movie'].value_counts().sort_index()
            select_genre = st.selectbox('Gêneros',options=mask_genre.index)
            st.subheader('Países que mais viram o gênero')
            genre_counts = dataset[dataset['listed_in']==select_genre][dataset['type']=='Movie']['country'].value_counts().sort_index()
        
        if graph_bar_movie_4:
            if graph_qtd_category:
                st.bar_chart(mask_category.head(qtd_category),color='#1ff084',height=500,width=700)
            if graph_genre_country:
                st.bar_chart(mask_movie_country_genre,height=400,color='#a22bfc')
            if graph_country_genre:
                st.bar_chart(genre_counts)
        
        if graph_line_movie_4:
            if graph_qtd_category:
                st.line_chart(mask_category.head(qtd_category),color='#1ff084',height=500,width=700)
            if graph_genre_country:
                st.line_chart(mask_movie_country_genre,height=400,color='#a22bfc')
            if graph_country_genre:
                st.line_chart(genre_counts)

    if op6_movie:
        st.subheader('Selecione a classificação')
        mask_class = dataset["rating"][dataset['type']=='Movie'].value_counts().sort_index()
        select_class = st.selectbox('Classificações',options=mask_class.index)
        show_movie_rating = st.checkbox('Mostrar dados da classificação')
        show_movie_rating_date = st.checkbox('Mostrar quantidade de filmes por cada categoria')
        #tipo de plotagem
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_movie_5 = st.checkbox('Gráfico de Barras')
        graph_line_movie_5 = st.checkbox('Gráfico de Linhas')
        mask_select_class = dataset[dataset['rating']==select_class][dataset['type']=='Movie']['country'].value_counts().sort_index()
        
        if show_movie_rating:
            st.subheader('Países que veem filmes dessa classificação')
            st.text('Not Given = Desconhecido')

        if show_movie_rating_date:
            st.subheader('Quantidade de Filmes por Gênero')
            maks_movie_rating_geral = dataset['rating'][dataset['type']=='Movie'].value_counts().sort_index()
        
        if graph_bar_movie_5:
            if show_movie_rating:
                st.bar_chart(mask_select_class,color='#f542aa',height=500)
            if show_movie_rating_date:
                st.bar_chart(maks_movie_rating_geral,color='#f542aa',height=500)

        if graph_line_movie_5:
            if show_movie_rating:
                st.bar_chart(mask_select_class,color='#f542aa',height=500)
            if show_movie_rating_date:
                st.line_chart(maks_movie_rating_geral,color='#f542aa',height=500)
 
with abas[2]:
    st.subheader('Selecione como ver os dados')
    op1_tvshow = st.checkbox('Ver infomações por Programa')
    op2_tvshow = st.checkbox('Ver todas as informações dos Programas')
    op3_tvshow = st.checkbox('Informações da quantidade de lançamentos dos programas por ano')
    op4_tvshow = st.checkbox('Programas por cada País')
    op5_tvshow = st.checkbox('Gêneros de Programas mais assistidos')
    op6_tvshow = st.checkbox('Classificação por Programas')
    
    #funcionalidades
    if op1_tvshow:
        st.subheader('Selecione o Ano')
        maks_years_tv = dataset[dataset['type'] == 'TV Show']['release_year'].value_counts().sort_index()
        select_tvshow = st.selectbox(' ',options=maks_years_tv.index)
        st.subheader('Selecione um Programa')
        mask_tvshow = dataset[dataset['release_year']==select_tvshow]
        tv = st.selectbox(' ',options=mask_tvshow['title'][mask_tvshow['type']=='TV Show'])
        mask_tvshow = mask_tvshow[mask_tvshow["title"]==tv]
        st.dataframe(mask_tvshow)
    
    if op2_tvshow:
        st.subheader('Informações Gerais dos Programas')
        maks_years_tv = dataset[dataset['type'] == 'TV Show']['release_year'].value_counts().sort_index()
        select_tvyear = st.selectbox('Selecione o ano',options=maks_years_tv.index)
        mask_tvshow = dataset[dataset['release_year']==select_tvyear][dataset['type']=='TV Show']
        st.dataframe(mask_tvshow)
        show_duration_tvshow = st.checkbox('Mostrar informações sobre o tempo de duração dos Programas')
        show_director_tvshow = st.checkbox('Quantidade de Programas por cada diretor')
        show_top_genre_tv = st.checkbox('Mostrar Gêneros mais assistidos (Programas de TV)')
        #tipo de Gráfico para plotagem
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_tv = st.checkbox('Gráfico de Barras')
        graph_line_tv = st.checkbox('Gráfico de Linhas')

        if show_duration_tvshow:
            st.subheader('Tempo de duração dos Programas')
            mask_tv_duration = dataset[dataset['type'] == 'TV Show'][dataset['release_year']==select_tvyear]['duration'].value_counts().sort_index()
    
        if show_director_tvshow:
            st.subheader('Qunatidade de Programas por cada Diretor')
            st.text('Not Given = Desconhecido')
            geral_director = st.checkbox('Ver estástica Geral dos diretores')

            if geral_director:
                st.subheader('Quantidade de Programas por cada diretor')
                qtd_director = st.slider('Quantidade de Diretores',1,226)
                mask_director_geral = dataset[dataset['type'] == 'TV Show']['director'].value_counts().sort_values(ascending=False).head(qtd_director)
            
            mask_director = dataset[dataset['type'] == 'TV Show'][dataset['release_year']==select_tvyear]['director'].value_counts().sort_index()
        
        if show_top_genre_tv:
            mask_genre_geral_tv = dataset['listed_in'][dataset['type']=='TV Show'].value_counts()
            st.subheader('Gêneros de Filmes mais assistidos')
            qtd_geral_genre_tv = st.slider('Selecione quantos gêneros de programas deseja ver',1,235)

        if graph_bar_tv:
            if show_duration_tvshow:
                st.bar_chart(mask_tv_duration,height=500,color='#1129ad')
            if show_director_tvshow:
                if geral_director:
                    st.bar_chart(mask_director_geral,color='#ad4d11',height=400,width=700)
                st.bar_chart(mask_director,color='#ad4d11',height=400)
            if show_top_genre_tv:
                st.bar_chart(mask_genre_geral_tv.head(qtd_geral_genre_tv),height=400,color='#6c0be3')
        
        if graph_line_tv:
            if show_duration_tvshow:
                st.line_chart(mask_tv_duration,height=500,color='#1129ad')
            if show_director_tvshow:
                if geral_director:
                    st.line_chart(mask_director_geral,color='#ad4d11',height=400,width=700)
                st.line_chart(mask_director,color='#ad4d11',height=400)
            if show_top_genre_tv:
                st.line_chart(mask_genre_geral_tv.head(qtd_geral_genre_tv),height=400,color='#6c0be3')

    if op3_tvshow:
        st.subheader('Selecionar quantidade de Programas')
        qtd_tvshow = st.slider('Quantidade de anos',1,46)
        st.subheader('Selecionar quantidade de Programas por periodos')
        tv_1 = st.checkbox('Programas de 1925 - 1988')
        tv_2 = st.checkbox('Programas dos 1988 - 2002')
        tv_3 = st.checkbox('Programas dos 2002 - 2015')
        tv_4 = st.checkbox('Programas dos 2016 - 2021')
        #tipo de Gráfico para plotagem
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_tv_2 = st.checkbox('Gráfico de Barras')
        graph_line_tv_2 = st.checkbox('Gráfico de Linhas')

        
        if qtd_tvshow:
            count_movies = dataset[dataset['type'] == 'TV Show']['release_year'].value_counts().sort_index().head(qtd_tvshow)

        if tv_1:    
            count_movies = dataset[dataset['type'] == 'TV Show']['release_year'].value_counts().sort_index().head(13)

        if tv_2:
            count_movies = dataset[dataset['type'] == 'TV Show']['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[14:27]
        
        if tv_3:
            count_movies = dataset[dataset['type'] == 'TV Show']['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[27:40]
        
        if tv_4:
            count_movies = dataset[dataset['type'] == 'TV Show']['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[40:46]
        
        #plotando grafico
        if graph_bar_tv_2:
            st.bar_chart(count_movies,color='#2b9efc')
        if graph_line_tv_2:
            st.line_chart(count_movies,color='#2b9efc')
    
    if op4_tvshow:
        st.subheader('Selecione um País')
        mask_country_tv = dataset['country'][dataset['type']=='TV Show'].value_counts().sort_index()
        select_country = st.selectbox('Países',options=mask_country_tv.index)
        mask_tv_country = dataset[dataset['country']==select_country][dataset['type']=='TV Show']
        st.dataframe(mask_tv_country)
        graph_tvshow_country = st.checkbox('Mostrar quantidade de Programa por cada país')
        
        #tipo de gráfico
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_tv_3 = st.checkbox('Gráfico de Barras')
        graph_line_tv_3 = st.checkbox('Gráfico de Linhas')

        if graph_tvshow_country:
            st.subheader('Selecione a quantidade de Páises')
            qtd_country = st.slider(' ',1,59)
            st.text('Not Given = Desconhecido')
            mask_country = dataset['country'][dataset['type']=='TV Show'].value_counts().sort_index().head(qtd_country)
            
        if graph_bar_tv_3:
            if graph_tvshow_country:
                st.bar_chart(mask_country,color='#eb4034',width=900,height=500)
        if graph_line_tv_3:
            if graph_tvshow_country:
                st.line_chart(mask_country,color='#eb4034',width=900,height=500)

    if op5_tvshow:
        st.subheader('Selecione uma das opções')
        mask_category = dataset['listed_in'][dataset['type']=='TV Show'].value_counts()
        graph_qtd_category = st.checkbox('Mostrar gráfico dos gêneros')
        table_qtd_category = st.checkbox('Mostrar tabela dos gêneros')
        graph_genre_country = st.checkbox('Mostrar gêneros por cada país')
        graph_country_genre = st.checkbox('Ver informações sobre cada gênero')
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_tv_4 = st.checkbox('Gráfico de Barras')
        graph_line_tv_4 = st.checkbox('Gráfico de Linhas')

        if graph_qtd_category:
            st.subheader('Selecione e quantidade de gêneros')
            qtd_category_graph = st.slider(' ',1,235)
        
        if table_qtd_category:
            st.subheader('Selecione e quantidade de gêneros')
            qtd_category_table = st.slider('    ',1,235)
            st.dataframe(mask_category.head(qtd_category_table),width=600)
        
        if graph_genre_country:
            st.subheader('Selecione um país')
            mask_country = dataset['country'][dataset['type']=='TV Show'].value_counts().sort_index()
            country_counts = st.selectbox('Países',options=mask_country.index)
            mask_movie_country_genre = dataset[dataset['country']==country_counts][dataset['type']=='TV Show']['listed_in'].value_counts().sort_index()

        if graph_country_genre:
            st.subheader('Selecione o gênero')
            mask_genre = dataset['listed_in'][dataset['type']=='TV Show'].value_counts().sort_index()
            select_genre = st.selectbox('Gêneros',options=mask_genre.index)
            st.subheader('Países que mais viram o gênero')
            genre_counts = dataset[dataset['listed_in']==select_genre][dataset['type']=='TV Show']['country'].value_counts().sort_index()
        
        if graph_bar_tv_4:
            if graph_qtd_category:
                st.bar_chart(mask_category.head(qtd_category_graph),color='#1ff084',height=500,width=700)
            if graph_genre_country:
                st.bar_chart(mask_movie_country_genre,height=400,color='#a22bfc')
            if graph_country_genre:
                st.bar_chart(genre_counts)

        if graph_line_tv_4:
            if graph_qtd_category:
                st.line_chart(mask_category.head(qtd_category_graph),color='#1ff084',height=500,width=700)
            if graph_genre_country:
                st.line_chart(mask_movie_country_genre,height=400,color='#a22bfc')
            if graph_country_genre:
                st.line_chart(genre_counts)

    if op6_tvshow:
        st.subheader('Selecione a classificação')
        mask_class = dataset["rating"][dataset['type']=='TV Show'].value_counts().sort_index()
        select_class = st.selectbox('Classificações',options=mask_class.index)
        show_tv_rating = st.checkbox('Mostrar dados da classificação')
        show_tv_rating_date = st.checkbox('Mostrar quantidade de Programa por cada categoria')
        #tipo de gráfico
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_tv_5 = st.checkbox('Gráfico de Barras')
        graph_line_tv_5 = st.checkbox('Gráfico de Linhas')
        mask_select_class = dataset[dataset['rating']==select_class][dataset['type']=='TV Show']['country'].value_counts().sort_index()
        
        if show_tv_rating:
            st.subheader('Países que veem programas dessa classificação')
            st.text('Not Given = Desconhecido')

        if show_tv_rating_date:
            st.subheader('Quantidade de Programa por Gênero')
            maks_tv_rating_geral = dataset['rating'][dataset['type']=='TV Show'].value_counts().sort_index()
        
        if graph_bar_tv_5:
            if show_tv_rating:
                st.bar_chart(mask_select_class,color='#f542aa',height=500)
            if show_tv_rating_date:
                st.bar_chart(maks_tv_rating_geral,color='#f542aa',height=500)

        if graph_line_tv_5:
            if show_tv_rating:
                st.bar_chart(mask_select_class,color='#f542aa',height=500)
            if show_tv_rating_date:
                st.line_chart(maks_tv_rating_geral,color='#f542aa',height=500)

with abas[3]:
    st.subheader('Selecione como ver os dados')
    op1_movie_tv = st.checkbox('Ver todas as informações sobre Filmes e Programas')
    op2_movie_tv = st.checkbox('Informações da quantidade de lançamentos dos filmes e programas por ano')
    op3_movie_tv = st.checkbox('Filmes e Programas por cada País')
    op4_movie_tv = st.checkbox('Gêneros de Filmes e Programas mais assistidos')
    op5_movie_tv = st.checkbox('Classificação dos Filmes e Programas')
    
    #funcionalidades
    
    if op1_movie_tv:
        st.subheader('Informações Gerais dos Filmes e Programas')
        maks_years_movie_show = dataset['release_year'].value_counts().sort_index()
        movie_show_select = st.selectbox('Selecione o ano',options=maks_years_movie_show.index)
        mask_movies_shows = dataset[dataset['release_year']==movie_show_select]
        st.dataframe(mask_movies_shows)
        show_duration_movie_show = st.checkbox('Mostrar informações sobre o tempo de duração')
        show_director_movie_show = st.checkbox('Quantidade de Filmes e Programas por cada diretor')
        show_top_genre_movie_show = st.checkbox('Mostrar Gêneros mais assistidos')
        #tipo de gráfico
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_tvmovie = st.checkbox('Gráfico de Barras')
        graph_line_tvmovie = st.checkbox('Gráfico de Linhas')

        if show_duration_movie_show:
            st.subheader('Tempo de duração dos Filmes e programas')
            st.text('Season = Programas de Tv\nMinutos = Filmes')
            mask_movie_duration = dataset[dataset['release_year']==movie_show_select]['duration'].value_counts()
    
        if show_director_movie_show:
            st.subheader('Qunatidade de Filmes e programas por cada Diretor')
            st.text('Not Given = Desconhecido')
            geral_director_show_movie = st.checkbox('Ver estástica Geral dos diretores')

            if geral_director_show_movie:
                qtd_director_movie_show = st.slider('Quantidade de Diretores',1,4581)
                mask_director_geral_movie_show = dataset['director'].value_counts().sort_values(ascending=False).head(qtd_director_movie_show)
            
            mask_director = dataset[dataset['release_year']==movie_show_select]['director'].value_counts().sort_index()

        if show_top_genre_movie_show:
            mask_genre_geral_movie = dataset['listed_in'].value_counts().sort_values(ascending=False)
            st.subheader('Gêneros de Programas e Filmes mais assistidos')
            qtd_geral_genre_tv = st.slider('Selecione quantos gêneros de Programas deseja ver',1,513)
        
        if graph_bar_tvmovie:
            if show_duration_movie_show:
                st.bar_chart(mask_movie_duration,height=500,color='#1129ad')
            if show_director_movie_show:
                if geral_director_show_movie:
                    st.bar_chart(mask_director_geral_movie_show,color='#1c25d6',height=400)
                st.bar_chart(mask_director,color='#ad4d11',height=400)
            if show_top_genre_movie_show:
                st.bar_chart(mask_genre_geral_movie.head(qtd_geral_genre_tv),height=400,color='#03fc49')
            
        if graph_line_tvmovie:
            if show_duration_movie_show:
                st.line_chart(mask_movie_duration,height=500,color='#1129ad')
            if show_director_movie_show:
                if geral_director_show_movie:
                    st.line_chart(mask_director_geral_movie_show,color='#1c25d6',height=400)
                st.line_chart(mask_director,color='#ad4d11',height=400)
            if show_top_genre_movie_show:
                st.line_chart(mask_genre_geral_movie.head(qtd_geral_genre_tv),height=400,color='#03fc49')

    if op2_movie_tv:
        st.subheader('Selecionar quantidade de filmes/programas')
        qtd_movie_show = st.slider('Quantidade de anos',1,74)
        st.subheader('Selecione por periodos')
        movies_shows_1 = st.checkbox('Filmes e Programas de 1925 - 1960')
        movies_shows_2 = st.checkbox('Filmes e Programas 1961 - 1973')
        movies_shows_3 = st.checkbox('Filmes e Programas 1974 - 1986')
        movies_shows_4 = st.checkbox('Filmes e Programas 1987 - 1999')
        movies_shows_5 = st.checkbox('Filmes e Programas 2000 - 2012')
        movies_shows_6 = st.checkbox('Filmes e Programas 2013 - 2021')
        #tipo de gráfico
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_tvmovie_2 = st.checkbox('Gráfico de Barras')
        graph_line_tvmovie_2 = st.checkbox('Gráfico de Linhas')
        
        if qtd_movie_show:
            count_movies = dataset['release_year'].value_counts().sort_index().head(qtd_movie_show)

        if movies_shows_1:    
            count_movies = dataset['release_year'].value_counts().sort_index().head(13)

        if movies_shows_2:
            count_movies = dataset['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[13:26]
        
        if movies_shows_3:
            count_movies = dataset['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[26:39]
        
        if movies_shows_4:
            count_movies = dataset['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[39:52]

        if movies_shows_5:
            count_movies = dataset['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[52:65]

        if movies_shows_6:
            count_movies = dataset['release_year'].value_counts().sort_index()
            count_movies = count_movies.iloc[65:73]
        
        #plotando grafico
        if graph_bar_tvmovie_2:
            st.bar_chart(count_movies,color='#2b9efc')
        if graph_line_tvmovie_2:
            st.line_chart(count_movies,color='#2b9efc')

    if op3_movie_tv:
        st.subheader('Selecione um País')
        mask_country = dataset['country'].value_counts().sort_index()
        country_counts = st.selectbox('Países',options=mask_country.index)
        mask_movie_country = dataset[dataset['country']==country_counts]
        st.dataframe(mask_movie_country)
        graph_movie_tv_country = st.checkbox('Mostrar quantidade de filmes e programas por cada país')
        graph_movie_tv_qtd = st.checkbox('Mostrar quantidade filmes e programas lançados')
        #tipo de gráfico
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_tvmovie_3 = st.checkbox('Gráfico de Barras')
        graph_line_tvmovie_3 = st.checkbox('Gráfico de Linhas')

        if graph_movie_tv_country:
            st.subheader('Selecione a quantidade de Páises')
            qtd_country = st.slider(' ',1,86)
            mask_country = dataset['country'].value_counts().sort_index().head(qtd_country)
        
        if graph_movie_tv_qtd:
            st.subheader('Quantidade de Lançamentos de Programas e Filmes')
            maks_qtd_movie_tv = dataset['type'].value_counts()

        if graph_bar_tvmovie_3:
            if graph_movie_tv_country:
                st.bar_chart(mask_country,color='#eb4034',width=900,height=500)
            if graph_movie_tv_qtd:
                st.bar_chart(maks_qtd_movie_tv,color='#f59b42',width=900,height=500)

        if graph_line_tvmovie_3:
            if graph_movie_tv_country:
                st.line_chart(mask_country,color='#eb4034',width=900,height=500)
            if graph_movie_tv_qtd:
                st.line_chart(maks_qtd_movie_tv,color='#f59b42',width=900,height=500)

    if op4_movie_tv:
        st.subheader('Selecione uma das opções')
        mask_category = dataset['listed_in'].value_counts()
        graph_qtd_category = st.checkbox('Mostrar gráfico dos gêneros')
        table_qtd_category = st.checkbox('Mostrar tabela dos gêneros')
        graph_genre_country = st.checkbox('Mostrar gêneros por cada país')
        graph_country_genre = st.checkbox('Ver informações sobre cada gênero')
        #tipo de gráfico
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_tvmovie_4 = st.checkbox('Gráfico de Barras')
        graph_line_tvmovie_4 = st.checkbox('Gráfico de Linhas')

        if graph_qtd_category:
            st.subheader('Selecione e quantidade de gêneros')
            qtd_category_graph = st.slider(' ',1,513)
        
        if table_qtd_category:
            st.subheader('Selecione e quantidade de gêneros')
            qtd_category_table = st.slider('    ',1,513)
            st.dataframe(mask_category.head(qtd_category_table),width=600)
        
        if graph_genre_country:
            st.subheader('Selecione um país')
            mask_country = dataset['country'].value_counts().sort_index()
            country_counts = st.selectbox('Países',options=mask_country.index)
            mask_movie_country_genre = dataset[dataset['country']==country_counts]['listed_in'].value_counts().sort_index()

        if graph_country_genre:
            st.subheader('Selecione o gênero')
            mask_genre = dataset['listed_in'].value_counts().sort_index()
            select_genre = st.selectbox('Gêneros',options=mask_genre.index)
            st.subheader('Países que mais viram o gênero')
            genre_counts = dataset[dataset['listed_in']==select_genre]['country'].value_counts().sort_index()
        
        if graph_bar_tvmovie_4:
            if graph_qtd_category:
                st.bar_chart(mask_category.head(qtd_category_graph),color='#1ff084',height=500,width=700)
            if graph_genre_country:
                st.bar_chart(mask_movie_country_genre,height=400,color='#a22bfc')
            if graph_country_genre:
                st.bar_chart(genre_counts)

        if graph_line_tvmovie_4:
            if graph_qtd_category:
                st.line_chart(mask_category.head(qtd_category_graph),color='#1ff084',height=500,width=700)
            if graph_genre_country:
                st.line_chart(mask_movie_country_genre,height=400,color='#a22bfc')
            if graph_country_genre:
                st.line_chart(genre_counts)

    if op5_movie_tv:
        st.subheader('Selecione a classificação')
        mask_class = dataset["rating"].value_counts().sort_index()
        select_class = st.selectbox('Classificações',options=mask_class.index)
        show_tv_movie_rating = st.checkbox('Mostrar dados da classificação')
        show_tv_movie_rating_date = st.checkbox('Mostrar quantidade de Programa e Filmes por cada categoria')
        #tipo de gráfico
        st.subheader('Selecione o tipo de gráfico')
        graph_bar_tv_5 = st.checkbox('Gráfico de Barras')
        graph_line_tv_5 = st.checkbox('Gráfico de Linhas')
        mask_select_class = dataset[dataset['rating']==select_class]['country'].value_counts().sort_index()

        if show_tv_movie_rating:
            st.subheader('Países que veem filmes dessa classificação')
            st.text('Not Guiven = Desconhecido')
        
        if show_tv_movie_rating_date:
            st.subheader('Quantidade de Programa e Filmes por Gênero')
            maks_tv_movie_rating_geral = dataset['rating'].value_counts().sort_index()
        
        if graph_bar_tv_5:
            if show_tv_movie_rating:
                st.bar_chart(mask_select_class,color='#f542aa',height=500)
            if show_tv_movie_rating_date:
                st.bar_chart(maks_tv_movie_rating_geral,color='#f542aa',height=500)

        if graph_line_tv_5:
            if show_tv_movie_rating:
                st.line_chart(mask_select_class,color='#f542aa',height=500)
            if show_tv_movie_rating_date:
                st.line_chart(maks_tv_movie_rating_geral,color='#f542aa',height=500)
