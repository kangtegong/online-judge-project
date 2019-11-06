# ide 

API를 받아오는 BASE url은 다음과 같이 지정한다.

```
var BASE_URL = localStorageGetItem("baseUrl") || "https://api.judge0.com";
var PB_URL = "https://pb.judge0.com";
```

# source download

```
function download(data, strFileName, strMimeType) {
	
	var self = window, // this script is only for browsers anyway...
		u = "application/octet-stream", // this default mime also triggers iframe downloads
		m = strMimeType || u, 
		x = data,
		D = document,
		a = D.createElement("a"),
		z = function(a){return String(a);},
		
		
		B = self.Blob || self.MozBlob || self.WebKitBlob || z,
		BB = self.MSBlobBuilder || self.WebKitBlobBuilder || self.BlobBuilder,
		fn = strFileName || "download",
		blob, 
		b,
		ua,
		fr;
```

# url create

사용자가 입력한 입력값을 바탕으로 JSON.stringify 적용
```
function save() {
  var content = JSON.stringify({
    source_code: encode(sourceEditor.getValue()),
    stdin: encode(inputEditor.getValue()),
    language_id: $selectLanguageBtn.val()
  });
  var filename = "judge0-ide.json";     // 넘겨줄 json 파일 이름
  var data = {
    content: content,
    filename: filename
  };

  $saveBtn.button("loading");       // 세이브 버튼 로딩 화면 
  $.ajax({
    url: PB_URL,
    type: "POST",
    async: true,
    headers: {
      "Accept": "application/json"
    },
    data: data,
    success: function(data, textStatus, jqXHR) {
      $saveBtn.button("reset");
      if (getIdFromURI() != data["long"]) {
        window.history.replaceState(null, null, location.origin + location.pathname + "?" + data["long"]);
      }
    },
    error: function(jqXHR, textStatus, errorThrown) {
      handleError(jqXHR, textStatus, errorThrown);
      $saveBtn.button("reset");
    }
  });
}
```
