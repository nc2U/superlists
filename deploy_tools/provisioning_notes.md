#### 신규 사이트 프로비저닝
=======================

##### 필요 패키지

- nginx
- git
- python3
- pip
- virtualenv

##### 우분투에서 실행 방법 예:

```bash
sudo apt install nginx git python3 python3-pip
sudo pip install virtualenv
```

##### Nginx 가상 호스트 설정

- nginx.template.conf 참고
- SITENAME 부분을 실제 도메인 또는 퍼블릭 IP로 변경

##### Upstart Job

- gunicorn-dev 파일의 SITENAME 부분을 실제 도메인 또는 퍼블릭 IP로 변경
- /etc/systemd/system/gunicorn-dev.service 로 링크 또는 복사
- sudo chmod 755 /etc/systemd/system/gunicorn-dev.service
- sudo systemctl start gunicorn-dev.service
- sudo systemctl status gunicorn-dev.service

##### 폴더 구조

/home/ubuntu  
└── dev  
............├── database  
............├── source  
............├── static  
............└── virtualenv  
