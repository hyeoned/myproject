import streamlit as st
from PIL import Image

emotion_images = {
    '간지': '간지.png',
    '무표정': '무표정.png',
    '미소': '미소.png',
    '삐질': '삐질.png',
    '슬픔': '슬픔.png',
    '재미': '재미.png',
    '쿨쿨': '쿨쿨.png',
    '헐': '헐.png',
    '화남': '화남.png'
}

st.title("음식 카테고리")

if 'diaries' in st.session_state and st.session_state.diaries['음식']:
    for entry in reversed(st.session_state.diaries['음식']):
        st.write(f"카테고리: {entry['category']}")  # 카테고리 표시
        st.subheader(entry['title'])  # 일기 제목 표시
        st.write(entry['content'])      # 일기 내용 표시
        
        emotion = entry['feeling']
        if emotion in emotion_images:
            st.image(emotion_images[emotion], caption=f"감정: {emotion}", width=50)

        # 이미지가 있는 경우 표시
        if entry.get('image') is not None:
            # 이미지 파일 열기
            image = Image.open(entry['image'])  # PIL로 열기
            st.image(image, caption="Uploaded Image", use_column_width=True)  # 이미지 표시
        st.write("---")  # 구분선
else:
    st.write("저장된 일기가 없습니다.")