// =================== WEEK 1 HOMEWORK ====================
$(document).ready(function(){
  
  // ===================  DAY 1 ====================
  // HW: celebrity id function - how do we fix this loop bug in closures?

  function celebrityIDCreator (theCelebrities) {
    var i
    for (i = 0; i < theCelebrities.length; i++) {
      theCelebrities[i]["id"] = function () {
        var uniqueID = 100
        return uniqueID + i
      }()
    }
    return theCelebrities
  }

  var celebrities = [{name: "Reese Witherspoon", id: 0}, {name: "Sarah Jessica Parker", id: 0}, {name: "Angelina Joile", id: 0}, {name: "Marie Curie", id: 0}, {name: "Priyanka Chopra", id: 0}, {name: "Kate McKinnon", id: 0},
  {name: "Julia Roberts", id: 0}, {name: "Jenniger Aniston", id: 0}, {name: "Malala Yousafzai", id: 0}]

  var createIdsForCelebs = celebrityIDCreator(celebrities)
  console.log(createIdsForCelebs)


  // Build a very simple kitchen timer: modify the countdown() function in countdown.js to take a number of seconds, then print each second counting down to zero.

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

  // ===================  DAY 2 ====================

});
