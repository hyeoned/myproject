import streamlit as st

st.title("TODAY'S DIARY")

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

# 선택된 감정을 저장할 변수
selected_feeling = None

# 각 표정 이미지 표시
cols = st.columns(9)
for i, (image, label) in enumerate(expressions):
    with cols[i]:
        if st.button("", key=f"btn_{i}"):  # 빈 버튼 생성
            selected_feeling = label
        st.image(image)

tt = st.text_input("제목")
today = st.text_area("오늘 하루 있었던 일", height=200)

if st.button("확인"):
    if today:
        if selected_feeling:
            st.success("일기가 저장되었습니다!")
            st.write(f"오늘의 감정: {selected_feeling}")
        else:
            st.error("하나의 감정을 선택해주세요.")
    else:
        st.error("일기를 작성해주세요.")