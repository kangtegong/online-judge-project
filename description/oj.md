# ide 

```
var BASE_URL = localStorageGetItem("baseUrl") || "https://api.judge0.com";
var PB_URL = "https://pb.judge0.com";
var SUBMISSION_CHECK_TIMEOUT = 10; // in ms
var WAIT = localStorageGetItem("wait") == "true";

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

function save() {
  var content = JSON.stringify({
    source_code: encode(sourceEditor.getValue()),
    stdin: encode(inputEditor.getValue()),
    language_id: $selectLanguageBtn.val()
  });
  var filename = "judge0-ide.json";
  var data = {
    content: content,
    filename: filename
  };

  $saveBtn.button("loading");
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

