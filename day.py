import streamlit as st
import sqlite3

menu = st.sidebar.selectbox("MENU", ['로그인', '회원가입', '회원정보수정', '회원탈퇴'])

if menu == '로그인':
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    
    st.title("로그인")
    id = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    btn = st.button("로그인")
    
    if btn:
        cursor.execute(f"SELECT * FROM user WHERE username='{id}'")
        row = cursor.fetchone()
        
        if row:    
            db_pw = row[2]
            db_id = row[1]
            db_nickname = row[3]  # 닉네임을 가져옵니다
        else:
            db_id = ''
            db_pw = ''
            db_nickname = ''
        
        if db_pw == pw:
            st.write("로그인 성공")
            st.sidebar.write(f"{db_nickname}님 환영합니다.")  # 닉네임으로 환영합니다
        else:
            st.error("로그인 실패!!")

elif menu == '회원가입':
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    
    st.title("회원가입")
    id = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    pw_check = st.text_input("비밀번호 확인", type="password")
    email = st.text_input("이메일")
    nickname = st.text_input("닉네임")
    btn = st.button("회원가입")
    
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

elif menu == '회원정보수정':
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    
    st.title("회원정보 수정")
    id = st.text_input("아이디")
    pw = st.text_input("비밀번호", type='password')
    email = st.text_input("이메일")
    nickname = st.text_input("닉네임")
    btn = st.button("수정")
    
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

elif menu == '회원탈퇴':
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    
    st.title("회원탈퇴")
    id = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    btn = st.button("회원탈퇴")
    
    if btn:
        cursor.execute(f"DELETE FROM user WHERE username = '{id}'")
        conn.commit()
        st.success("회원탈퇴가 완료되었습니다.")
    conn.close()