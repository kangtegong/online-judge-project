# ide 

API를 받아오는 BASE url은 다음과 같이 지정한다.

```
var BASE_URL = localStorageGetItem("baseUrl") || "https://api.judge0.com";
var PB_URL = "https://pb.judge0.com";
```
# url create

ide/templates/ftz.html
```
<button class="btn btn-default" id="saveBtn" data-toggle="tooltip"title="create URL">
  <i class="fa fa-plus-circle"></i> (Ctrl+S)
</button>

```
`id="saveBtn"`에 의해 ide/static/ide.js의 `save()` 함수 동작


사용자가 입력한 입력값을 바탕으로 JSON.stringify 적용
```
function save() {
  // username(pk), encoding된 source code와 input, language_id를 문자열화된 JSON으로 변환
  // 해당 내용을 content 변수에 담음

  var content = JSON.stringify({
    username: username,
    source_code: encode(sourceEditor.getValue()),
    stdin: encode(inputEditor.getValue()),
    language_id: $selectLanguageBtn.val()
  });

  var filename = "judge0-ide.json";     // 넘겨줄 json 파일 이름
  // data에 전송받을 파일 이름 `judge0-ide.json`과 content를 다시 담아주고 해당 부분을 보냄
  var data = {
    content: content,
    filename: filename
  };

  $saveBtn.button("loading");       // 세이브 버튼 로딩 화면 
  
  // 이제 최종적으로 data만 보내주고 결과를 success / error에 따라 처리
  $.ajax({
    url: PB_URL,
    type: "POST",
    async: true,
    headers: {
      "Accept": "application/json"
    },
    data: data,
    
    // 전송이 성공적이었을 경우
    success: function(data, textStatus, jqXHR) {
      // URL Create 버튼 로딩화면 -> 리셋
      $saveBtn.button("reset");
      // URL Prefix를 더하는 부분
      // data["long"] = prefix
      if (getIdFromURI() != data["long"]) {
        window.history.replaceState(null, null, location.origin + location.pathname + "?" + data["long"]);
      }
    },
    
    // 전송이 실패했을 경우
    error: function(jqXHR, textStatus, errorThrown) {
      handleError(jqXHR, textStatus, errorThrown);
      // URL Create 버튼 로딩화면 -> 리셋
      $saveBtn.button("reset");
    }
  });
}
```

참고로 여기서 getIdFromURI()는 다음과 같이 정의된 함수

```
function getIdFromURI() {
  return location.search.substr(1).trim();
}
```
