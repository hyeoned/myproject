import streamlit as st
import sqlite3

st.title("회원정보 수정")
id = st.text_input("아이디")
pw = st.text_input("비밀번호", type='password')
email = st.text_input("이메일")
nickname = st.text_input("닉네임")
btn = st.button("수정")

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
    
if btn:
    sql = f"""
    UPDATE user SET password = "{pw}",
    email = "{email}",
    nickname = "{nickname}"
    WHERE username = "{id}"
    """
    cursor.execute(sql)
    conn.commit()
    st.success("회원정보가 수정되었습니다.")
conn.close()