import streamlit as st
import google.generativeai as genai

def profile():
  
    api_key = st.secrets["API_KEY"] #your gemini api key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash') 
    
    col1, col2 = st.columns(2) 
    
    with col1: 
        st.subheader("Hi :wave:")    
        st.title("I am Abhinav Varshney") 
    
    with col2:
        st.image("D:/PROGRAMMING LANGUAGES/1.png",width=250)  
    
    persona = """
            You are Abhinav's AI bot 😊.The user is here to interact with you and you help people
            answer questions about Abhinav.
            If something about Abhinav that you don't know then simply reply That's a secret.
            You can tell the user that you know several things about Abhinav and feel free to use emojis.
            Don't answer in second or third person.If someone is asking you about anything else then
            you will answer accordingly.

            Here is more info about Abhinav: 

            Abhinav Varshney is 21 years old from Chandausi, Uttar Pradesh, India from where he had completed his schooling.
            From class 12th he found his interest in coding when first interact with turtle module of the Python
            programming language.

            He is an Computer Science undergraduate from Jaypee College of Engineering, Guna.
            Currently he is in the third year of the course with 8+ GPA score and ofcourse with no backlogs 😎.
            He has keen interest in Data Science and Artificial Intelligence specially in Computer Vision.His
            several projects are hosted on GitHub and essential information are available on LinkedIn.

            Abhinav's Email: varshneyabhinav66@gmail.com 
            Abhinav's Instagram: https://www.instagram.com/abhinavvarshney17
            Abhinav's Linkdin: https://www.linkedin.com/in/abhinav-varshney-bb9bb7204/
            Abhinav's Github :https://github.com/imabhnv
            """

    st.title("Abhinav's AI Bot")
    
    user_question = st.text_input("Ask anything about me")
    if st.button("ASK", use_container_width=400):
        prompt = persona +"Here is the question that the user asked: " +  user_question
        response = model.generate_content(prompt)
        st.write(response.text)
    
    st.title(" ") 
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("My Profile")
        st.write("- CSE Undergrad")
        st.write("- Tech Enthusiast ")
        st.write("- SSoC'23 Contributor")
        st.write("- Computer Vision")

    with col2:
        st.write(" ")
        st.write("Email: varshneyabhinav66@gmail.com ")
        st.write("Linkdin: https://www.linkedin.com/in/abhinav-varshney-bb9bb7204/")
        st.write("Github :https://github.com/imabhnv")
        st.write("Instagram: https://www.instagram.com/abhinavvarshney17")

    st.subheader(" ")
    st.write("CONTACT ME")
    st.title("For any inquiries, email at:")
    st.subheader("varshneyabhinav66@gmail.com")

profile()
