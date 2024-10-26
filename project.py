import streamlit as st

pages = {
    "회원정보" : [
        st.Page("page/login.py",title="로그인"),
        st.Page("page/signup.py",title="회원가입"),
        st.Page("page/modify.py",title="회원정보수정")
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