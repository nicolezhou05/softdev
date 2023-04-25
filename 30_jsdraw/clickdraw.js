// Team Joyful Jalapenos :: Julia Lee, Nicole Zhou
// SoftDev pd7
// K30 -- canvas based JS drawing
// 2023-04-24

// retrieve node in DOM via ID
var c = document.getElementById("slate");

// instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

ctx.fillStyle = "red";

// init global state var
var mode = "rect";

// var toggleMode = function(e) {
var toggleMode = (e) => {
  console.log("toggling...");
  if (mode == "rect") {
    mode = "circle";
    buttonToggle.innerHTML = "circle";
  }
  else {
    mode == "rect";
    buttonToggle.innerHTML = "rect";
  }
}

var drawRect = function(e) {
  var mouseX = e.offsetX;
  var mouseY = e.offsetY;
  console.log("mouseclick registered at ", mouseX, mouseY);
  ctx.fillRect(mouseX, mouseY, 50, 120);
}

// var drawCircle = function(e) {
var drawCircle = (e) => {
  var mouseX = e.offsetX;
  var mouseY = e.offsetY;
  console.log("mouseclick registered at ", mouseX, mouseY);
  ctx.beginPath();
  ctx.arc(mouseX, mouseY, 30, 0, Math.PI * 2, true);
  ctx.fill();
}

// var draw = function(e) {
var draw = (e) => {
  if (mode == "rect") {
    drawRect(e);
  }
  if (mode == "circle") {
    drawCircle(e);
  }
}

// var wipeCanvas = function() {
var wipeCanvas = () => {
  ctx.clearRect(0, 0, 600, 600);
}

c.addEventListener("click", draw);

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);

var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);