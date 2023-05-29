import streamlit as st
import webbrowser

# Custom CSS
pink_style = """
<style>
body {
    background-color: white;
}

.sidebar .sidebar-content {
    background-color: #FF69B4 !important;
    color: white;
}

.sidebar .sidebar-content .sidebar-collapse-control {
    color: white;
    font-weight: bold;
    font-size: 24px;
}

.sidebar .sidebar-content a {
    color: white;
    font-weight: bold;
    font-size: 18px;
}

.sidebar .sidebar-content a:hover {
    color: #FF69B4;
    background-color: white;
}
</style>
"""

# Login Page
def login():
    st.title("ศูนย์การแพทย์กาญจนาภิเษก")
    st.header("งานสารบรรณ")
    st.markdown(pink_style, unsafe_allow_html=True)

    password = st.text_input("Password", type="password")
    if password == "Nongwin":
        st.success("Login successful!")
        return True
    else:
        st.error("Incorrect password.")
        return False

# Transcribe Page
def home():
    st.title("")
    st.write("โปรแกรมถอดไฟล์บันทึกจากซูมเป็นไฟล์อักษร ผ่านไฟล์เสียง")
# Main App
def main():
    if not login():
        return

    # Sidebar menu
    st.sidebar.title("โปรดเลือกเมนู")
    menu_item = st.sidebar.selectbox("", ["Home","Transcribe", "Convert", "Split"])

    if menu_item == "Home":
        home()
    elif menu_item == "Transcribe":
        webbrowser.open_new_tab("https://drkamthorn-whisperai.streamlit.app/")
    elif menu_item == "Convert":
        webbrowser.open_new_tab("https://drkamthorn-docconvert-app-kjr9mv.streamlit.app/") 
    elif menu_item == "Split":
        webbrowser.open_new_tab("https://drkamthorn-splitok-app-jbowxz.streamlit.app/")
    #elif menu_item == "Tempo":
        #tempo()

# Run the app
if __name__ == "__main__":
    main()