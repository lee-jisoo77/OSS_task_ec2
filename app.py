import streamlit as st
from datetime import datetime

if 'userName' not in st.session_state:
    st.session_state.userName = ""

print(f"[{datetime.now()}] 페이지 로드됨", flush=True)

st.title('사용자 정보 입력')

st.session_state.userName = st.text_input(
    '이름', 
    value=st.session_state.userName, 
    placeholder='ex.홍길동'  
)

button_clicked = st.button('저장')
if button_clicked:
    print(f"[{datetime.now()}] 저장 버튼 클릭됨 - 입력: {st.session_state.userName}", flush=True)
    if st.session_state.userName:
        st.success(f' {st.session_state.userName}님 반갑습니다.')
    else:
        st.warning('이름을 입력해 주세요!')