import streamlit as st

# 定义一个简单的用户验证函数
def validate_login(username, password):
    # NEVER store passwords like this in real code.
    # Always use secure methods and hashing for production applications.
    if username == "admin" and password == "password":
        return True
    return False

# 创建一个侧边栏，用于输入用户名和密码
st.sidebar.title("登录")
username = st.sidebar.text_input("用户名", value="", max_chars=50)
password = st.sidebar.text_input("密码", value="", max_chars=50, type="password")

# 登录按钮
login_button = st.sidebar.button("登录")

# 当用户点击登录按钮时
if login_button:
    if validate_login(username, password):
        st.success("登录成功！")
        # 登录成功后，你可以在这里加入你应用的主要功能部分
        # 比如：st.write("Welcome to the main application.")
    else:
        st.error("用户名或密码错误，请重新输入。")

