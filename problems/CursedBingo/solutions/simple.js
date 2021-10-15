"use strict";

function processData(input) {
    const rows = input.split('\n');
    rows.shift(); //Discard L, we don't care.
    rows.map(N => Number(N)).forEach(N => {
        console.log(Math.floor((N - 1) * N));
    });
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
let _input = "";
process.stdin.on("data", function (input) {
  _input += input;
});
process.stdin.on("end", function () {
 processData(_input);
});