import streamlit as st
import sqlite3

st.title("회원가입")
id = st.text_input("아이디")
pw = st.text_input("비밀번호", type="password")
pw_check = st.text_input("비밀번호 확인", type="password")
email = st.text_input("이메일")
nickname = st.text_input("닉네임")
btn = st.button("회원가입")

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
    
if btn:
    if pw != pw_check:
        st.error("비밀번호가 일치하지 않습니다.")
    else:
        sql = f"""INSERT INTO user(username, password, email, nickname)
                    VALUES('{id}', '{pw}', '{email}', '{nickname}')"""
        cursor.execute(sql)
        conn.commit()
        st.success("회원가입이 완료되었습니다.")
conn.close()