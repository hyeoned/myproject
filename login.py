import streamlit as st
import sqlite3

st.title("로그인")

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

id = st.text_input("아이디")
pw = st.text_input("비밀번호", type="password")
btn = st.button("로그인")

if btn:
        cursor.execute(f"SELECT * FROM user WHERE username='{id}'")
        row = cursor.fetchone()
        
        if row:    
            db_pw = row[2]
            db_id = row[1]
            db_nickname = row[3]
        else:
            db_id = ''
            db_pw = ''
            db_nickname = ''
        
        if db_pw == pw:
            st.write("로그인 성공")
            st.sidebar.write(f"{db_nickname}님 환영합니다.")
        else:
            st.error("로그인 실패!!")