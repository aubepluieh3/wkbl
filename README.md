# wkbl

### About Project
평소 취미 중 하나가 농구 경기 관람이라 어떤 프로젝트를 진행할 지 고민하던 중 직접 농구 사이트를 만들어 보면 어떨까 라는 생각이 들어 이 프로젝트를 진행하게 됨
이 프로젝트를 통해서 농구 정보를 전달하고 농구 관련 이야기를 할 수 있는 커뮤니티를 구현해보고 싶었음


### Project Goals
회원가입, 로그인 및 로그아웃   
정보 게시판   
농구 게시판   

### Project Detail
+ 회원가입 : 사용자 이름, 비밀번호, 이메일, 전화번호, 생년월일 입력받음    


![image](https://user-images.githubusercontent.com/66086544/174559724-e0c9dd9b-10bb-45d5-a422-04646b7043bb.png)


+ 로그인 : 사용자 이름과 비밀번호로 로그인 


![image](https://user-images.githubusercontent.com/66086544/174560002-4c017087-03c0-4c75-8820-eceb0501b2e8.png)


+ 로그아웃 : Navar를 사용하여 로그인을 하게 되면 사용자이름(로그아웃) 마이페이지로 변경되고 로그아웃을 클릭하면 로그아웃이 됨


+ 마이페이지 : 마이페이지를 클릭하면 회원가입 했을 당시 작성한 정보가 뜨고, 이메일과 생년월일은 readonly로 설정하여 수정이 불가하게 함   
회원 정보 수정시, DB가 수정됨을 확인할 수 있음


+ 첫 화면 : 웹 페이지의 첫 화면으로, WKBL를 누르면 이 화면으로 돌아옴
Carousel을 이용하여 이미지 슬라이드 형식으로 지정하였고, 버튼을 누르면 해당하는 곳으로 이동


![image](https://user-images.githubusercontent.com/66086544/174560778-bdf3cdeb-307d-44f8-8d61-39c6eadc7cbc.png)


+  WKBL 

![image](https://user-images.githubusercontent.com/66086544/174560931-4db300b2-d0d8-4aa8-9b21-e44ffa0645a8.png)
![image](https://user-images.githubusercontent.com/66086544/174560968-2b33f065-89d3-4b64-8c4e-e9baa4f35aaa.png)


Dropdowns를 이용하여 항목을 보여주고 클릭하면 해당 페이지로 이동
Breadcrumb를 사용하여 CSS로 구분자를 자동으로 추가해 내비게이션 계층 내에서 현재 페이지의 위치를 표시함
Home을 클릭하면 첫 화면 페이지로 이동


+ NEWS

![image](https://user-images.githubusercontent.com/66086544/174561337-251116db-fce0-4b14-a3ba-2831a941ae44.png)

사용자가 WKBL일 때만 기사 작성하기 버튼이 보이도록 설정

![image](https://user-images.githubusercontent.com/66086544/174561538-de1f8186-111e-48da-9677-09998187a399.png)
![image](https://user-images.githubusercontent.com/66086544/174561566-127897fc-1e63-4811-9c4c-bf7649ed5dc2.png)

본인이 작성한 글은 추천할 수 없고, 글쓴이와 현재 사용자가 같은 경우에만 글을 수정할 수 있도록 설정   
페이징 처리를 해주었고, 해당 게시판 내에서의 검색기능을 만들었음

+ TEAM


![image](https://user-images.githubusercontent.com/66086544/174561889-f6809277-70f8-4550-83bf-c51efacac676.png)
![image](https://user-images.githubusercontent.com/66086544/174561919-a68c9718-c738-4be1-aa6f-b003115de6c8.png)

WKBL과 마찬가지로 TEAM 역시 Dropdowns를 이용하여 항목을 보여주고, BreadCrumb를 사용   
해당 아이콘을 클릭하면 각각 구단 홈페이지, 인스타그램, 페이스북과 연결되어 현재 페이지가 아닌 새로운 페이지에서 열림   

![image](https://user-images.githubusercontent.com/66086544/174562551-8a541f04-0d3f-4e90-9c2e-ff66f64f510e.png)

선수 정보는 Accordion을 이용하여 아코디언의 내용을 접기/펼치기 가능


+ BOARD


![image](https://user-images.githubusercontent.com/66086544/174562818-b430267b-f206-4092-bc26-a01c5fcc2f3c.png)
![image](https://user-images.githubusercontent.com/66086544/174562851-57744a36-6f9a-4d00-8c3a-cd8d703c786d.png)
![image](https://user-images.githubusercontent.com/66086544/174562880-66237ec5-a435-4cbd-b3ac-df07d6dbc294.png)


BOARD도 Dropdowns를 이용하여 Q&A와 자유 게시판으로 이뤄져 있고, 똑같이 검색 기능과 페이징 처리를 함   
로그인을 해야 작성할 수 있고, NEWS와 다른 점은 사용자가 누구든 작성할 수 있음   


Q&A 게시판

![image](https://user-images.githubusercontent.com/66086544/174563013-8f15767a-a1d5-44f2-8f4a-b10bb34469a6.png)
![image](https://user-images.githubusercontent.com/66086544/174563060-55651413-a89f-4bf8-9ab8-b8b1e062e385.png)

자유 게시판

![image](https://user-images.githubusercontent.com/66086544/174563242-971376f2-52a0-41e9-b7d3-3859170acafc.png)

두 게시판의 다른 점은 Q&A는 질문과 답변 형식, 자유게시판은 게시글과 댓글 형식으로 구현함


### Expected Effect
회원정보 관리, 기본 정보 전달 가능, 게시판을 통해서 의사소통과 소식 전달 가능 









