// demo 1
// JS event propagation

var tds = document.getElementsByTagName('td');

var clicky = function(e) {
  alert( this.innerHTML );
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}


// What might be rendered: a table
// Behavior predictions: a pop up cotaining components from the table

// What is observed:
// * Whatever text is clicked produces a pop up of that text
// * Clicking on what is not text does not produce a pop up