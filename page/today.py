import streamlit as st

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
if 'diaries' not in st.session_state:
    st.session_state.diaries = {
        "전체": [],
        "일상": [],
        "여행": [],
        "음식": []
    }
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


category = st.selectbox("카테고리를 선택하세요", ["전체", "일상", "여행", "음식"])

tt = st.text_input("제목")
today = st.text_area("오늘 하루 있었던 일", height=200)

if st.button("확인"):
    if today:
        if st.session_state.selected_feeling:
            # 일기를 저장
            diary_entry = {
                'title': tt,
                'content': today,
                'feeling': st.session_state.selected_feeling
            }
            st.session_state.diaries[category].append(diary_entry)  # 선택된 카테고리에 일기 추가
            st.session_state.diaries["전체"].append(diary_entry)  # 전체 카테고리에 일기 추가
            st.success("일기가 저장되었습니다!")
        else:
            st.error("하나의 감정을 선택해주세요.")
    else:
        st.error("일기를 작성해주세요.")

bb=st.button("이미지 업로드")

