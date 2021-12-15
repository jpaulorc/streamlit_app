from cProfile import label
import pandas as pd
import streamlit as st
from register_person import draw_person_info

def display_introduction():
    """Mostrando como usar o streamlit"""
    st.title("Introdução ao Streamlit")
    st.text("""O Streamlit permite escrever aplicações simplesmente chamando funções.""")
    st
    

def display_text():
    """Formas de mostrar texto"""
    st.header("1.) Como mostrar texto.")
    st.subheader("1.1 Este é o subcabeçalho.")
    st.markdown("_Markdown_")
    st.latex(r"e^{i\pi} + 1 = 0 ")
    st.write("O wrtite aceita qualquer coisa que vc jogar aqui")
    st.write([1,2,3,4,5])
    st.write({1:2,2:3})
    cod = """
    for i in range(10):
        print(i)
    """
    st.code(body=cod, language="python")
    

def display_magic_functions():
    """Mostra textos de forma mágica"""    
    a = "Este texto será exibido de forma mágica pelo streamlit."
    a
    
    """O Streamlit consegue interpretar strings formatadas"""
    b = pd.DataFrame({
        "colA": [3,2,1],
        "colB": [4,5,6]
    })
    b
    
    """---"""
    st.title("Formas de titulos")
    "# Titulo de nivel 1"
    "## Titulo de nivel 2"
    "### Titulo de nivel 3"
    "#### Titulo de nivel 4"
    "##### Titulo de nivel 5"
    "###### Titulo de nivel 6"
    

def display_data():
    """Formas de mostrar dados pelo Streamlit"""    
    b = pd.DataFrame({
        "colA": [3,2,1],
        "colB": [4,5,6]
    })
    "### Usando DataFrame"
    st.dataframe(b)
    
    "### Usando Tables"
    st.table(b)
    
    "### Usando Dicionario"
    st.json(b.to_dict())
    
    "### Usando Json"
    st.json(b.to_json())
    
    "### Usando Metricas"
    st.metric(
        label="Temperatura",
        value="30C°",
        delta="3C°",
        delta_color="normal"
    )
    
    st.metric(
        label="Umidade",
        value="40%°",
        delta="5%",
        delta_color="inverse"
    )
    

def display_midia():
    """Formas de mostrar midia."""
    
    """#### Mostrando audio"""
    st.audio(
        "https://ssl.gstatic.com/dictionary/static/sounds/oxford/morning--_us_1.mp3"
    )
    
    """#### Mostrando imagens"""
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/1200px-African_Bush_Elephant.jpg"
    )
    
    """#### Mostrando videos"""
    st.video(
        "https://www.youtube.com/watch?v=BinwuzZVjnE"
    )
    

def display_columns():
    """Mostrando valores em colunas"""
    
    "#### Mostrando Objetos em colunas"
    col1, col2, col3 = st.columns([3,2,1])        
    col1.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/1200px-African_Bush_Elephant.jpg")
    col2.audio("https://ssl.gstatic.com/dictionary/static/sounds/oxford/morning--_us_1.mp3")
    col3.video("https://www.youtube.com/watch?v=BinwuzZVjnE")
    
    with col1:
        st.write("Esta senença estará na coluna 1")
    

def display_status():
    """Mostra as formas de status"""
    
    st.error("Sua operação gerou erro")
    st.warning("Fique esperto, algo pode estar errado.")
    st.info("Isso é uma informação.")
    st.success("Esta é uma mensagem de sucesso")
    try:
        st.write(10/0)
    except ZeroDivisionError as error:
        st.exception(error)
        
        
def display_widgets():
    """Formas de widgets do streamlit"""
    
    "#### Botoes clicaveis"
    button = st.button("Clique aqui.")
    button
    
    "#### Checkbox"
    checkbox = st.checkbox("Eu concordo, clique aqui")
    checkbox
    
    "#### Radio Button"
    radio = st.radio(
        "Selecione a opção:",
        ["Gatos", "Cachorros", "Vacas"]
    )
    radio
    
    selectbox = st.selectbox(
        "Selecione a opção:",
        ["Gatos", "Cachorros", "Vacas"]
    )
    selectbox      
    
    selectslider = st.select_slider("Selecione uma opção", [1,2,3,4,5,6])
    selectslider
    
    number = st.number_input("Selecione um numero", 1, 10)
    number
    
    area = st.text_area("Entre com o texto:")
    area
    
    date = st.date_input("Qual é a data:")
    date
    
    time = st.time_input("Qual é o horário:")
    time
    
    upload = st.file_uploader("Entre com arquivo")
    upload
    
    df = pd.DataFrame({
        "colA": [3,2,1],
        "colB": [4,5,6]
    })
    csv = df.to_csv(index=False)
    st.download_button("Download CSV File", csv)
    
    picker = st.color_picker("Selecione a cor")
    picker
    


def display_sidebar():
    """Mostra uma barra lateral"""
    with st.sidebar:
        st.title("Navegação de tutorial")
        
        options = {
            "Introdução": display_introduction,
            "Formas de mostrar texto": display_text,
            "Forma mágica": display_magic_functions,
            "Mostrando dados": display_data,
            "Mostrando Midia": display_midia,
            "Mostrando colunas": display_columns,
            "Mostrando status": display_status,
            "Widgets são estes": display_widgets,
            "Formulario Pessoa": draw_person_info
        }
        
        opt = st.radio("Selecione a opção de navegação", options)
    
    options[opt]()
        

display_sidebar()
