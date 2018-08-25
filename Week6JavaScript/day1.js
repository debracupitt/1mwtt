

function celebrityID () {
  var uniqueID = 999
  return {
    getID: function () {
      return uniqueID
    },
    setID: function (newID) {
      uniqueID = newID
      return uniqueID
    }
  }
}

var mjID = celebrityID()
console.log(mjID)
console.log(mjID.getID())
console.log(mjID.setID(543))
mjID.setID(2940)
console.log(mjID.getID())

// Hoisting is JavaScript's default behavior of moving declarations to the top.
// Before the code execution happens, the interpreter goes through the whole
// program and takes the declarations but NOT the assignments and hoists them
// to the top so they are always available.
// let and const are not hoisted.
// initializations are not hoisted either.
// e.g.

x = 5

var elem = document.getElementById('kasia')
elem.innerHTML = x

var x

// HW: celebrity id function - how do we fix this loop bug in closures?

function celebrityIDCreator (theCelebrities) {
  var i
  for (i = 0; i < theCelebrities.length; i++) {
    theCelebrities[i]['id'] = (function () {
      var uniqueID = 100
      return uniqueID + i
    }())
  }
  return theCelebrities
}

var celebrities = [{name: 'Reese Witherspoon', id: 0}, {name: 'Sarah Jessica Parker', id: 0}, {name: 'Angelina Joile', id: 0}, {name: 'Marie Curie', id: 0}, {name: 'Priyanka Chopra', id: 0}, {name: 'Kate McKinnon', id: 0},
  {name: 'Julia Roberts', id: 0}, {name: 'Jenniger Aniston', id: 0}, {name: 'Malala Yousafzai', id: 0}]

var createIdsForCelebs = celebrityIDCreator(celebrities)
console.log(createIdsForCelebs)

// Modify echo.js to print out each argument to the echo() function on a new line. It should work for an arbitrary number of arguments.

function print () {
  console.log(arguments)
};

function echo () {
  for (var i = 0; i < arguments.length; i++) {
    console.log(arguments[i])
  }
};

echo()
// should print nothing

echo('bla')
// should print
//
// 'bla'

echo('foo', 'bar', 'baz')
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
  var timeleft = timeSet
  var countdownTimer = setInterval(function () {
    console.log(timeleft)
    timeleft--
    if (timeleft <= 0) {
      clearInterval(countdownTimer)
    }
  }, 1000)

  var kitchenTimer = window.setTimeout(
    function (timeSet) {
      console.log('Time\'s up! ' + timeSet + ' seconds have passed.')
    }, (timeSet * 1000), timeSet)
}

// jQuery plugin - blink
(function blink ($) {
  $.fn.greenify = function () {
    this.css('color', 'green')
    return this
  }
}(jQuery))
