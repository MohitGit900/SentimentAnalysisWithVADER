import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Sidebar contents
with st.sidebar:
    st.title('Sentiment Analysis App')
    st.markdown('''
    This app is built using:            
    - [Streamlit](https://streamlit.io/)
    - [VADER](https://github.com/cjhutto/vaderSentiment)            
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ in Streamlit')

st.header('Sentiment Analysis')
with st.container():
    def analyze(x):
        if x >= 0.05:
            st.toast('Its a Positive sentiment!', icon='😎')
            return 'Positive'
        elif x <= -0.05:
            st.toast('Its a Negative sentiment!', icon='😢')
            return 'Negative'
        else:
            st.toast('Its a Neutral sentiment!', icon='😐')
            return 'Neutral'
        
    def clear_text():
        st.session_state["text"] = ""    
    text = st.text_input('Please enter text here: ', key="text")

    if text:
        sid_obj= SentimentIntensityAnalyzer()
        sid_obj_var = sid_obj.polarity_scores(text)
        st.write('Sentiment: ',analyze(sid_obj_var['compound']))
        with st.expander('Details'):
            st.write('Sentence was rated: ')
            st.write(round(sid_obj_var['pos']*100,2),' % Positive')
            st.write(round(sid_obj_var['neu']*100,2),' % Neutral')
            st.write(round(sid_obj_var['neg']*100,2),' % Negative')
        
        st.button('Clear', on_click=clear_text)
    


