import streamlit as st


if 'userName' not in st.session_state:
    st.session_state.userName = ""

st.title('사용자 정보 입력')


st.session_state.userName = st.text_input(
    '이름', 
    value=st.session_state.userName, 
    placeholder='ex.홍길동'  
)

button_clicked = st.button('저장')
if button_clicked:
    if st.session_state.userName:
        st.success(f'저장되었습니다: {st.session_state.userName}')
    else:
        st.warning('이름을 입력해 주세요!')