import streamlit as st
import time
import threading

# Set page config
def set_page_config():
    st.set_page_config(page_title="Vipul Singh Portfolio", page_icon="🧊")

# Add custom CSS styles
def add_custom_styles():
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #FFD700 !important; /* Yellow color */
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Display welcome toast message
def display_welcome_message():
    st.toast('Welcome to My Portfolio', icon='👋')

# Display header and image
def display_header_and_image():
    col1, col2 = st.columns([1, 1])
    col1.title("I am :blue[Vipul Singh]")
    col1.header("An Aspiring Analyst")
    col2.image('vipulimage.jpg', width=200)

# Display about me section
def display_about_me():
    st.subheader("About Me", divider=True)
    st.markdown("""
    I am a highly motivated and analytical professional with a Bachelor's of Technology from the Modern Institute of Technology & Research Center, specializing in Artificial Intelligence and Data Science. With a strong foundation in SQL, MySQL Server, Database Admin, Excel, Python, Power BI, I possess a passion for extracting insights from data. My hands-on experience includes analyzing datasets, developing end-to-end data analysis report dashboards, and creating educational content to simplify complex analytical concepts.
    """)

# Display resume section
def display_resume():
    st.subheader("Resume", divider=True)
    col1, col2 = st.columns([0.4, 1])
    with col1:
        st.text("Profile:")
        st.text("Domain:")
        st.text("Education:")
        st.text("Tools:")
        st.text("Other Skills:")
    with col2:
        st.text("Data Science & Analytics")
        st.text("Analysis, Dashboards & Trend Forecasting")
        st.text("Bachelor of Engineering")
        st.text("Microsoft Power BI, Excel, MYSQL Server, Git, Jupyter")
        st.text("VS Code, Machine Learning, Python, C")

# Display connect section
def display_connect():
    st.subheader("Connect with me On", divider=True)
    col1, col2, col3 = st.columns([0.4, 0.4, 0.4])
    col1.link_button("LinkedIn", "https://vipulsingh.com")
    col2.link_button("GitHub", url='https://github.com', icon="🛜")
    col3.link_button("Resume", url='https://example.com/resume')

# Display sidebar
def display_sidebar():
    st.sidebar.empty()
    st.sidebar.image('vipulimage.jpg', width=250)
    st.sidebar.text("Name: Vipul Singh")
    st.sidebar.text("Job Role: Aspiring Data Analyst")
    st.sidebar.text("Experience: 1 Month")
    st.sidebar.text("Address: Rajasthan, India")
    st.sidebar.write("Skills")
    st.sidebar.progress(80, text="SQL 80%")
    st.sidebar.progress(75, text="Python 75%")
    st.sidebar.progress(80, text="Data Visualization 80%")
    st.sidebar.progress(85, text="Excel & Spreadsheet 85%")
    st.sidebar.progress(80, text="Statistical Analysis 75%")

# Display contact form
def display_contact_form():
    st.subheader("How can I Contact You")
    with st.form(key='contact_form'):
        name = st.text_input("Name", placeholder="ABC DEF")
        email = st.text_input("Email", placeholder="simba@email.com")
        mob_no = st.text_input("Mobile no.", placeholder="80030.....")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            if name and email and mob_no:
                st.success("Submitted successfully!")
            else:
                st.error("Please fill in all fields.")

# Display main content
def display_main_content():
    col1, col2 = st.columns([3, 4])
    with col1:
        st.header("Name:")
        st.text("Job Role:")
        st.text("Experience:")
    with col2:
        st.text("Vipul Singh")
        st.text("Data Analyst")
        st.text("1 Month")
        st.image('vipulimage.jpg')

    st.container().write("This will show first")
    st.container().write("This will show second")
    st.write("This will show last")

# Display tabs
def display_tabs():
    tab1, tab2 = st.tabs(["EXCEL", "SQL"])
    tab1.header("Below are the projects made using excel")

# Main function to run the app
def main():
    set_page_config()
    add_custom_styles()
    display_welcome_message()
    display_header_and_image()
    display_about_me()
    display_resume()
    display_connect()
    display_sidebar()
    display_main_content()
    display_tabs()
    display_contact_form()

    if st.button("Rerun"):
        st.experimental_rerun()

    with open("vipulimage.jpg", "rb") as file:
        st.download_button("Download file", data=file, file_name="vipulimage.jpg", mime="image/jpg")

    st.metric(label="Temperature", value="70°F", delta="1.2°F")
    st.feedback("stars")

# Run the app
if __name__ == "__main__":
    main()
