import streamlit as st
import sqlite3

# 로그아웃 처리 함수
def logout():
    st.session_state['is_logged_in'] = False
    st.session_state.pop('nickname', None)  # 세션에서 사용자 닉네임 삭제
    st.success("로그아웃 되었습니다.")
    st.session_state['logout'] = True  # 로그아웃 후 상태를 세션에 저장

st.title("로그인")

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# 이미 로그인한 상태라면 로그인 화면을 건너뛰고 환영 메시지
if 'is_logged_in' in st.session_state and st.session_state['is_logged_in']:
    st.success(f"이미 로그인된 상태입니다. {st.session_state['nickname']}님 환영합니다!")
    
    # 로그아웃 버튼
    if st.button("로그아웃"):
        logout()  # 로그아웃 처리
else:
    # 로그인하지 않은 상태에서 로그인 폼
    id = st.text_input("아이디")
    pw = st.text_input("비밀번호", type="password")
    btn = st.button("로그인")

    if btn:
        cursor.execute("SELECT * FROM user WHERE username = ?", (id,))
        row = cursor.fetchone()

        if row:
            db_pw = row[2]
            db_nickname = row[3]
        else:
            db_pw = None
            db_nickname = None

        # 비밀번호 확인
        if db_pw == pw:
            st.session_state['is_logged_in'] = True
            st.session_state['nickname'] = db_nickname
            st.success(f"로그인 성공! {db_nickname}님 환영합니다.")
        else:
            st.error("아이디 또는 비밀번호가 일치하지 않습니다.")
    
    conn.close()