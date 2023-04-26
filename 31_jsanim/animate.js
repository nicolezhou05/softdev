var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");
ctx.fillStyle = "blue";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, 500, 500);
};

var radius = 0;
var growing = true;

var drawDot = () =>{
    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
    clear();
    if (radius == 250) {
        growing = false;
    }
    else if (radius == 0 && !growing) {
        growing = true;
    }
    if (growing == true) {
        radius = radius + 1;
    }
    else {
        radius = radius - 1;
    }
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, Math.PI * 2, true);
    ctx.fill();
    ctx.stroke();
};

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
