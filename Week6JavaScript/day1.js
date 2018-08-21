// Modify echo.js to print out each argument to the echo() function on a new line. It should work for an arbitrary number of arguments.

function print () {
  console.log(arguments);
};

function echo () {
  for(var i = 0; i < arguments.length; i++) {
	console.log(arguments[i]);
  }
};

echo();
// should print nothing

echo('bla');
// should print
//
// 'bla'

echo('foo', 'bar', 'baz');
// should print
//
// 'foo'
// 'bar'
// 'baz'



// Build a very simple kitchen timer: modify the countdown() function in countdown.js to take a number of seconds, then print each second counting down to zero.

// countdown(3);
// should print
// 3...
// 2...
// 1...
// 0

function countdown (timeSet) {
  var timeleft = timeSet;
  var countdownTimer = setInterval(function(){
    console.log(timeleft);
    timeleft--;
    if (timeleft <= 0) {
      clearInterval(countdownTimer);
    }
  },1000);

	var kitchenTimer = window.setTimeout(
		function(timeSet){
			console.log("Time's up! " + timeSet + " seconds have passed.")
		}, (timeSet*1000), timeSet);
}
