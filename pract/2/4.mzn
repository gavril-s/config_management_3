% Use this editor as a MiniZinc scratch book
include "alldifferent.mzn";

var [1,2]: A;
var 1..9: B;
var 1..9: C;
var 1..9: D;
var 1..9: E;
var 1..9: F;

constraint A + B + C == D + E + F;

solve satisfy;

