import streamlit as st
import sqlite3

st.title("회원탈퇴")

# 로그인 상태 체크
if not st.session_state.get('is_logged_in', False):
    st.warning("로그인 후 접근 가능합니다.")
    # 로그인하지 않은 경우 입력 필드와 버튼 비활성화
    st.text_input("아이디", disabled=True, key="id_disabled")
    st.text_input("비밀번호", type="password", disabled=True, key="pw_disabled")
    st.button("회원탈퇴", disabled=True, key="btn_disabled")
else:
    # 로그인한 경우 입력 필드 활성화
    id = st.text_input("아이디", key="id_input")
    pw = st.text_input("비밀번호", type="password", key="pw_input")
    btn = st.button("회원탈퇴", key="btn_input")

    if btn:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()

        # 아이디와 비밀번호 일치 여부 확인 후 탈퇴
        cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", (id, pw))
        row = cursor.fetchone()

        if row:
            cursor.execute("DELETE FROM user WHERE username = ?", (id,))
            conn.commit()
            st.success("회원탈퇴가 완료되었습니다.")
        else:
            st.error("아이디 또는 비밀번호가 일치하지 않습니다.")
        conn.close()