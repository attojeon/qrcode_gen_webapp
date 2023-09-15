# QR Code 자동 생성 앱
# pip install qrcode pillow streamlit
#
# 1. 사용자로부터 QR Code 메시지를 입력받음
# 2. 입력받은 메시지를 QR Code 이미지로 변환
# 3. QR Code 이미지를 화면에 표시
# 4. QR Code 이미지를 다운로드할 수 있는 링크 생성
# 5. QR Code 이미지를 다운로드할 수 있는 버튼 생성
# 6. QR Code 이미지를 다운로드할 수 있는 버튼을 클릭하면 QR Code 이미지를 다운로드함

import streamlit as st 
import qrcode 
import time 

st.title("QR Code Generator")
st.image("static/assets/cover.png", width=300)
msg = st.text_input("QR Code에 담을 메시지를 입력하시오.")
st.write("QR Code 메시지>>> ", msg)

if len(msg) > 0:
    print(f"msg: {msg}")
    filename = f'{time.time()}.png'
    filepath = f"./upload/{filename}"
    img = qrcode.make(msg)
    img.save(filepath)

    st.subheader("QR Code 이미지파일 사용하기")
    st.image(filepath, width=300, caption="QR Code") 
    st.divider()

    # QR Code 이미지파일을 다운로드할 수 있는 버튼 생성
    st.subheader("QR Code 이미지파일 다운로드 버튼")
    st.download_button(
        label="Download QR Code",
        data=open(filepath, "rb").read(),
        file_name=filename,
        mime="image/png"
    )
    st.divider()

