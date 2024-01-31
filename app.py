import streamlit as st
#import llm 
from modals import llm
st.title('AI based question generator')

with st.sidebar:
    st.header('Inputs')
    st.subheader('Language')
    language = st.selectbox('Select language', ['English'])
    st.subheader('Model')
    model = st.selectbox('Select model', ['flan-T5-base'])
    # st.subheader('Number of questions')
    # num_questions = st.slider('Select number of questions', 1,1)
    # st.subheader('Question type')
    # question_type = st.selectbox('Select question type', ['Objective', 'Subjective'])
    # st.subheader('Difficulty')
    # difficulty = st.selectbox('Select difficulty', ['Easy', 'Medium', 'Hard'])
    st.subheader('Class')
    classs = st.selectbox('Select class', ['8','9', '10', '11', '12'])
    st.subheader('Subject')
    subject = st.selectbox('Select subject', ['Science', 'English', 'Social Science'])
    st.subheader('Topic')
    topic = st.text_input("Enter the main topic")


if st.sidebar.button('Generate'):
    # st.write('Generating questions...')
    # st.write('Language: ', language)
    # st.write('Model: ', model)
    # st.write('Number of questions: ', num_questions)
    # st.write('Question type: ', question_type)
    # st.write('Difficulty: ', difficulty)
    # st.write('Class: ', classs)
    # st.write('Subject: ', subject)
    # st.write('Topic: ', topic)
    # st.write('Questions: ')
    # for i in range(num_questions):
    #     st.write(i+1, '. ', 'Question', i+1)
    # st.write('Done')
    que = llm.gen_ques(classs , subject , topic)
    que = ">" + que
    st.write("   ")
    st.write(que)
