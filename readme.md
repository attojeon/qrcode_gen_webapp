# QR코드 생성하는 웹앱

## docker 실행의 권한 문제
docker-compose.yml에서 다음의 코드가 있음.
```
volumes:
      - ./app:/app # 현재 디렉토리를 컨테이너의 /app 디렉토리에 바인딩
```
  - /app/upload 폴더에 파일이 업로드될 때 권한 문제가 발생함. 
  - chmod 777 /upload 등의 명령어를 사용하여 권한 문제를 해결해야 함. 

## 실행 
```sh
docker-compose up -d --build
```
