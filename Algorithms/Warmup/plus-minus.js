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
  var n = parseInt(readLine());
  arr = readLine().split(' ');
  arr = arr.map(Number);

  var positive = 0, negative = 0, zeros = 0, total = 0;

  arr.map((number) => {
    total++;
    if (number > 0) {
      positive++;
    } else if (number < 0) {
      negative++;
    } else {
      zeros++;
    }
  });

  console.log(`${positive / total}\n${negative / total}\n${zeros / total}`);
}