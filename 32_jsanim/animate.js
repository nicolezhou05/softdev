var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var dvdButton = document.getElementById("dvd");

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var radius = 0;
var growing = true;

var drawDot = () =>{
    window.cancelAnimationFrame(requestID);
    clear();
    if (radius == 250) {
        growing = !growing;
    } else if (radius == 0 && !growing) {
        growing = !growing;
    }
    if (growing == true) {
        radius++;
    } else {
        radius--;
    }
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, Math.PI * 2, true);
    ctx.fill();
    ctx.stroke();
    requestID = window.requestAnimationFrame(drawDot);
};

var clear = function(e) {
    // e.preventDefault();
    ctx.clearRect(0, 0, 500, 500);
};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);

    var rectWidth = 60;
    var rectHeight = 40;

    var rectX = Math.floor(Math.random() * (500-rectWidth));
    var rectY = Math.floor(Math.random() * (500-rectHeight));

    var xVel = 2;
    var yVel = 2;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if (((c.width - rectWidth) - rectX) < 5 || rectX < 5) {
            xVel = -1 * xVel;
        } 
        if (((c.height - rectHeight) - rectY) < 5 || rectY < 5) {
            yVel = -1 * yVel;
        }
        rectX = rectX + xVel;
        rectY = rectY + yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    };
    dvdLogo();
}

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
dvdButton.addEventListener("click", dvdLogoSetup);