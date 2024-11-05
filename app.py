import streamlit as st

# Set page config
def set_page_config():
    st.set_page_config(page_title="Vipul Singh Portfolio", page_icon="🧊", layout='wide')

# Add custom CSS styles
def add_custom_styles():
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #FFD700 !important; /* Yellow color */
            color: black !important;
        }
        .stHeader {
            background-color: #f0f2f6;
            padding: 1em;
            border-radius: 10px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
        }
        .stSidebar {
            background-color: #f8f9fa;
            padding: 1em;
            border-radius: 10px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
        }
        .stColumn {
            padding: 1em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Display header and image
def display_header_and_image():
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div class='stHeader'>", unsafe_allow_html=True)
        st.title("I am :blue[Vipul Singh]")
        st.header("Aspiring Data Analyst")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.image('vipulimage.jpg', width=200)

# Display about me section
def display_about_me():
    st.subheader("Contact Information")
    st.markdown("""
    - **Phone:** +91-8769521995
    - **Email:** vipulsingh592005@gmail.com
    - **Location:** Alwar, Rajasthan
    """)
    
    st.subheader("Education")
    st.markdown("""
    - **B.Tech in Artificial Intelligence and Data Science**  
      Modern Institute of Technology & Research Centre  
      Graduation Year: 2024  
      CGPA: 8.23
    - **Class XII**  
      Engineer’s Point Sr. Secondary School, Alwar, Rajasthan  
      April 2020, 62.50%
    """)

# Display skills section
def display_skills():
    st.subheader("Technical Skills")
    st.markdown("""
    - **Languages:** Python, SQL, C
    - **Developer Tools:** Visual Studio Code
    - **Data Analysis Tools:** Excel, Power BI, MySQL, Pandas, NumPy
    - **Data Visualization:** Power BI, Matplotlib, Streamlit
    - **Machine Learning:** Machine Learning
    - **Other Tools:** Git, Jupyter Notebook, PyCharm
    """)

# Display experience section
def display_experience():
    st.subheader("Internship Experience")
    st.markdown("""
    - **Accenture North America**  
      June 2023 - August 2023  
      - Gained experience analyzing large datasets to uncover insights and support data-driven decisions.
      - Developed data visualizations and dashboards to effectively communicate findings to stakeholders.
    - **Prolific Systems And Technologies Pvt. Ltd.**  
      - Participated in multiple projects related to data science, machine learning, and data visualization.
      - Developed a WhatsApp Chat Sentiment Analysis application, a Hospital Management System, and analyzed e-commerce sales data in Power BI.
    """)

# Display certifications section
def display_certifications():
    st.subheader("Certifications")
    st.markdown("""
    - Data Analysis Virtual Internship - Forage
    - SMART India Hackathon (SIH-2023)
    - Deep Learning Training
    - Python for Data Science
    """)

# Display projects section
def display_projects():
    st.subheader("Projects")
    st.markdown("""
    - **WhatsApp Chat Sentiment Analysis (Python, Machine Learning)**  
      Developed a Python application to analyze sentiment in WhatsApp chat data using machine learning techniques. Utilized libraries such as Pandas, Scikit-learn, and NLTK for data preprocessing, feature extraction, and sentiment classification.
    - **Analyzing E-commerce Sales Data (Power BI)**  
      Conducted a comprehensive analysis of e-commerce sales data using Power BI to identify trends, patterns, and actionable insights. Created interactive dashboards and reports to visualize key metrics such as sales performance, customer behavior, and product popularity.
    """)

# Display positions of responsibility section
def display_responsibility():
    st.subheader("Positions of Responsibility")
    st.markdown("""
    - SIH Mentor, MITRC
    """)

# Display interests section
def display_interests():
    st.subheader("Interests")
    st.markdown("""
    - Programming Problems
    - Counting combinations or permutations and finding unique characters in strings
    """)

# Main function to run the app
def main():
    set_page_config()
    add_custom_styles()
    display_header_and_image()
    display_about_me()
    display_skills()
    display_experience()
    display_certifications()
    display_projects()
    display_responsibility()
    display_interests()

# Run the app
if __name__ == "__main__":
    main()
