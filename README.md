# ajax_crawler
ajax 통신 기반의 html을 크롤링하는 토이 프로젝트

### OBJECTIVE 초등학교의 가정통신문과 공지사항, 급식 메뉴를 크롤링 해보자!

- Condition
  * 세션 진입과 로그인 과정이 필요하다
  * URL을 지정하여 GET 방식으로 데이터를 끌어올 수 없다

- Soultion one 
  * 링크가 바뀌지 않는 Ajax 기반 html 페이지이다
  * GET이 아닌 POST 방식으로 데이터를 끌어오자

- Challenge
  * POST 요청에 키를 전달하는 방식에서 ifNttid가 필수값이었는데, 해당 파라미터는 해쉬값으로 암호화가 되어있어
  암호화 방식을 재현하지 않는 이상 크롤링 할 수 없었다

  ![image](https://github.com/zzakjista/ajax_crawler/assets/102800414/d362e67a-98da-4bbb-b1d7-731b37127a4f)


  * Response를 보니 Nttid를 ifNttid로 인코딩하는 코드가 내부에서 동작하고 있었다
  ![image](https://github.com/zzakjista/ajax_crawler/assets/102800414/a0a18c23-160a-478c-a31c-aa6dc186de83)


- Solution two
  * Selenium으로 모든 페이지를 동적으로 방문하여 데이터를 수집하자

- Result
  * 수집 데이터가 정상적으로 수집되었다
  * OOP 패턴을 적용하기 위해 코드 리뷰를 거쳤다
  * 모듈 단위로 분절 및 option과 template 모듈을 생성해 파라미터 정의를 손 쉽게 하도록했다

- 수집 데이터
  * 가정통신문 및 공지사항 : 작성자, 작성일, 제목, 본문, 첨부파일
  * 급식 : 급식분류, 날짜, 제목, 메뉴, 칼로리
