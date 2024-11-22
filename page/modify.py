import streamlit as st
import sqlite3

st.title("회원정보 수정")

# 로그인 상태 체크
if not st.session_state.get('is_logged_in', False):
    st.warning("로그인 후 접근 가능합니다.")
    # 로그인하지 않은 경우 입력 필드와 버튼 비활성화
    st.text_input("아이디", disabled=True, key="id_disabled")
    st.text_input("새 비밀번호", type="password", disabled=True, key="pw_disabled")
    st.text_input("새 이메일", disabled=True, key="email_disabled")
    st.text_input("새 닉네임", disabled=True, key="nickname_disabled")
    st.button("수정", disabled=True, key="btn_disabled")
else:
    # 로그인한 경우 입력 필드 활성화
    id = st.text_input("아이디", key="id_input")
    pw = st.text_input("새 비밀번호", type="password", key="pw_input")
    email = st.text_input("새 이메일", key="email_input")
    nickname = st.text_input("새 닉네임", key="nickname_input")
    btn = st.button("수정", key="btn_input")

    if btn:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()

        # 사용자 정보 수정 SQL 실행
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