import streamlit as st
from pathlib import Path 

#-------PATH SETTINGS-------

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "resume.pdf"

#-------LOAD FILE---------

with open(resume_file, "rb") as pdf_file: 
    PDFbyte = pdf_file.read()

st.set_page_config(
    page_title="NURA RAMADHANI CV",
    page_icon=":brain:",
    )

#---------------SIDEBAR--------------------------

st.sidebar.image("nura.png", width=200)
st.sidebar.write("###")

st.sidebar.write("###")
st.sidebar.header("**SOFT SKILLS**")
st.sidebar.markdown('''
    - Communication Skills
    - Team work and collaboration
    - Problem solving skills
    - Adaptability
    - Microsoft office packages ''')

st.sidebar.write("###")
st.sidebar.header("**LANGUAGE**")
st.sidebar.write('''
    - Swahili 
    - English ''')

st.sidebar.subheader("CONTACT ME")
st.sidebar.markdown(":telephone_receiver:(+255) 625 922 967")
st.sidebar.write((":envelope: nuramahmoud@aiesec.net "))
st.sidebar.markdown(":round_pushpin: Dar es Salaam, Tanzania")


#------------------PAGE SETUP---------------

st.title(" :violet[NURA RAMADHANI] ")
st.download_button(
    label="Download CV",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
)
st.write(":envelope: [nuramahmoud@aiesec.net]")



st.write("###")
st.write("---")

st.subheader(" :violet[SUMMARY] ")
st.markdown(''' 
    > Passionate and driven individual with thirst for knowledge and personal growth. I thrive in challenging environments and enjoy pushing myself
      outside of my comfort zone. I have a strong desire to continously learn and develop new skills. i value creativity, adaptability and taking initiatives.
      I am always eager to take new opportunities and make positive impact''')


st.write("###")

st.subheader(" :red[EXPERIENCE] ")
st.write(" :red[AIESEC IN UDSM],  *Dar es Salaam — Team Leader (PD and EwA)*")
st.markdown("July 2023 - Present")
st.markdown('''
    - Coordinated team activities and ensured efficient completion of assigned tasks 
    ''')

st.write("###")    

st.write(" :red[OCVP Sales in World Environment Day Project],  *AIESEC IN UDSM, Dar es salaam*")
st.markdown("April 2023 - June 2023")
st.markdown('''
    - Collaborated with team members for effective communications and efficient workflow of the event preparations.
    - Report day-to-day progress.
    ''')

st.write("###")

st.subheader(":green[EDUCATION AND TRAINING]")
st.write(" :green[University of Dar es Salaam], *Dar es Salaam, Tanzania*")
st.markdown("Bachelor of Arts in Economics and Statistics")
st.markdown("Expected in 10/2024")
st.markdown('''
    - Team work skills
    - Leadership skills
    ''')

st.write(" :green[Ifunda Girls High School], *Iringa, Tanzania*")
st.markdown("Advanced Certificate")
st.markdown("5/2021")
st.markdown('''
    - Team work skills
    - Communication skills
    ''')

st.write("###")
st.write("---")

#----------------FOOTER----------------------------------
st.header("**REFERENCES**")

cols1, cols2 = st.columns(2)

cols1.subheader("COLLINS WILLY")
cols1.caption("*AIESEC IN UDSM / LOCAL CHAPTER PRESIDENT* ")
cols1.markdown(":telephone_receiver: (+255) 625 511 297")
cols1.write(":envelope: collins.kibona@aiesec.net")
