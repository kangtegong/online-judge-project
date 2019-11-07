
# URL Snapshot based Online IDE

![uos oj](accounts/static/css/logo.png)


## 요약

Source Code를 입력 및 실행할 수 있고, 10개 이상의 언어와 소스 다운로드 기능이 제공되는 Online IDE입니다. 타 Online IDE와 차별화되는 점은, 코드의 저장 및 제출에 있어 소스파일이 아닌, 
** 코드를 담은 IDE의 URL** 을 저장한다는 점입니다. 
 
입력한 코드를 임시저장하게 되면, URL prefix에 고유 문자열 값이 생성되어 고유한 URL이 생성됩니다. 서버 측에서는 해당 URL만 저장/관리하면 되므로, 더욱 적은(정형화된) 용량의 데이터만 다루면 된다는 효용이 있습니다. 또한 해당 아이디어로 구현된 IDE는 없(거나 찾기 어려울 정도로 적)으므로 구현의 가치는 충분하다고 판단했습니다.  
 
이 밖에도 질문답변/공지사항 게시판, 대외활동 및 개발자 대회 크롤링, 서울시립대 컴퓨터과학부  수업계획서/수업목록 API 등을 끌어와 완성도와 상품가치를 높였습니다.

[시연영상](https://github.com/kangtegong/online-judge-project/blob/master/demo/demo.md#%EC%8B%9C%EC%97%B0-%EC%98%81%EC%83%81
)
