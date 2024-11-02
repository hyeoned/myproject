import streamlit as st
import pandas as pd
from PIL import Image
from io import StringIO

st.title("TODAY'S DIARY")
st.markdown("오늘 내 기분은?")

# 표정 이미지와 레이블 정의
expressions = [
    ('간지.png', '간지'),
    ('무표정.png', '무표정'),
    ('미소.png', '미소'),
    ('삐질.png', '삐질'),
    ('슬픔.png', '슬픔'),
    ('재미.png', '재미'),
    ('쿨쿨.png', '쿨쿨'),
    ('헐.png', '헐'),
    ('화남.png', '화남')
]

# 세션 상태에 일기 데이터 저장 공간 초기화
if 'diaries' not in st.session_state:
    st.session_state.diaries = {
        "전체": [],
        "일상": [],
        "여행": [],
        "음식": []
    }

# 세션 상태에 카테고리 저장 공간 초기화
if "categories" not in st.session_state:
    st.session_state.categories = ["일상", "여행", "음식"]

# 사이드바에서 카테고리 추가 기능
st.sidebar.header("카테고리 관리")
new_category = st.sidebar.text_input("새 카테고리 이름")
if st.sidebar.button("카테고리 추가"):
    if new_category and new_category not in st.session_state.categories:
        st.session_state.categories.append(new_category)
        st.session_state.diaries[new_category] = []  # 새 카테고리의 일기 목록 초기화
        st.success(f"{new_category} 카테고리가 추가되었습니다!")
    elif new_category in st.session_state.categories:
        st.warning("이미 존재하는 카테고리입니다.")
    else:
        st.error("카테고리 이름을 입력하세요.")

# 선택된 감정을 저장할 변수
selected_feeling = st.session_state.get('selected_feeling', None)

# 각 표정 이미지 표시
cols = st.columns(9)
for i, (image, label) in enumerate(expressions):
    with cols[i]:
        if st.button("", key=f"btn_{i}"):  # 빈 버튼 생성
            selected_feeling = label
            st.session_state['selected_feeling'] = selected_feeling  # 상태 저장
        st.image(image)

# 카테고리 선택 및 일기 작성
category = st.selectbox("카테고리를 선택하세요", st.session_state.categories, key="write_category")
tt = st.text_input("제목")
today = st.text_area("오늘 하루 있었던 일", height=200)

# 이미지 업로드
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if st.button("확인"):
    if today:
        if st.session_state.selected_feeling:
            # 일기를 저장
            diary_entry = {
                'title': tt,
                'content': today,
                'feeling': st.session_state.selected_feeling,
                'category': category,
                'image': uploaded_file  # 이미지 파일 추가
            }
            # 선택된 카테고리와 전체 카테고리에 일기를 추가
            st.session_state.diaries[category].append(diary_entry)
            st.session_state.diaries["전체"].append(diary_entry)
            st.success(f"{category} 카테고리에 일기가 저장되었습니다!")
        else:
            st.error("하나의 감정을 선택해주세요.")
    else:
        st.error("일기를 작성해주세요.")