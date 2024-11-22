import streamlit as st
import sqlite3

if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False
if 'nickname' not in st.session_state:
    st.session_state['nickname'] = None

pages = {
    "회원정보" : [
        st.Page("page/login.py",title="로그인"),
        st.Page("page/signup.py",title="회원가입"),
        st.Page("page/modify.py",title="회원정보수정"),
        st.Page("page/delete.py",title="회원탈퇴")
    ],
    "오늘의 하루" : [
        st.Page("page/today.py", title="오늘의 하루 쓰기")
    ],
    "오늘의 하루 모아보기" : [
        st.Page("page/all.py", title="전체"),
        st.Page("page/daily.py", title="일상"),
        st.Page("page/travel.py", title="여행"),
        st.Page("page/food.py", title="음식")
    ]
}


pg = st.navigation(pages)
pg.run()