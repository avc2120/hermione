// alert('js attached');
$(document).ready(function(e) {
    $(".add-position").click(function() {
        // console.log('button clicked');
        $(".positions-list").append('<div class="form-group"><label>Add Diversity Program/Partnership</label><input type="text" class="form-control" class="partnership" placeholder="" required></div>');
    });

    $("#fileToLoad").click(function () {
     var fileToLoad = document.getElementById("fileToLoad").files[0];

      var fileReader = new FileReader();
      fileReader.onload = function(fileLoadedEvent){
          var textFromFileLoaded = fileLoadedEvent.target.result;
          document.getElementById("inputTextToSave").value = textFromFileLoaded;
          var fileUpload = document.getElementById("fileUpload");
  var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;
  if (regex.test(fileUpload.value.toLowerCase())) {
    if (typeof(FileReader) != "undefined") {
      var reader = new FileReader();
      reader.onload = function(e) {
        var table = document.createElement("table");
        var rows = e.target.result.split("\n");
        for (var i = 0; i < rows.length; i++) {
          var row = table.insertRow(-1);
          var cells = rows[i].split(",");
          for (var j = 0; j < cells.length; j++) {
            var cell = row.insertCell(-1);
            cell.innerHTML = cells[j];
          }
        }
        var dvCSV = document.getElementById("dvCSV");
        dvCSV.innerHTML = "";
        dvCSV.appendChild(table);
      }
      reader.readAsText(fileUpload.files[0]);
    } else {
      alert("This browser does not support HTML5.");
    }
  } else {
    alert("Please upload a valid CSV file.");
  }
      };
      fileReader.addEventListener("loadend", function() {
       // reader.result contains the contents of blob as a typed array
       // we insert content of file in DOM here
       console.log("HERE")
           console.log(fileReader.result);
        });
    });
});

