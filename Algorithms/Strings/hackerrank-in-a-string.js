process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
  input_stdin += data;
});

process.stdin.on('end', function () {
  input_stdin_array = input_stdin.split("\n");
  main();
});

function readLine() {
  return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
  var q = parseInt(readLine());
  var searchString = "hackerrank";
  for (var a0 = 0; a0 < q; a0++) {
    var s = readLine();
    var current = 0;
    var result = true;
    for (var i = 0; i < searchString.length; i++) {
      var found = false;

      for (var j = current; j < s.length; j++) {
        if (searchString[i] === s[j]) {
          found = true;
          current = j + 1;
          break;
        }
      }

      if (!found) {
        result = false;
        break;
      }
    }

    if (result) {
      console.log("YES");
    } else {
      console.log("NO");
    }
  }

}
