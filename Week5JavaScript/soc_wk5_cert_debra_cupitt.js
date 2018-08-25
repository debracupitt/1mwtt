// =================== WEEK 1 HOMEWORK ====================
$(document).ready(function(){

  // =========================  DAY 1 ==========================

  var timeCalc = {
    hrInYr: function () {
      var hrInYr = 24 * 365
      return hrInYr
    },
    minInDec: function () {
      var minInDec = this.hrInYr() * 60 * 10 + (2 * 24)
      return minInDec
    },
    secInDay: function () {
      var secsInDay = 24 * 60 * 60
      return secsInDay
    },
    myAgeSecs: function () {
      var myAgeDays = (27 * 365) + 35 + Math.round(27 / 4)
      var myAgeSecs = myAgeDays * this.secInDay()
      return myAgeSecs
    },
    CristinaTarantinoAgeMillisecs: function () {
      var millisecInDay = this.secInDay() * 1000
      var CristinaTarantinoAgeMillisecs = (32 * (365 + (32/4))) * millisecInDay
      return CristinaTarantinoAgeMillisecs
    }
  }

  // Print homework day 1 to page
  var $day1 = $( "#day1" )
  var htmlHw1 =
          '<div>' + '<h4>Hours in a Year: ' + timeCalc.hrInYr() +'</h4></div>' +
          '<div>' + '<h4>Minutes in a Decade: ' + timeCalc.minInDec() +'</h4></div>' +
          '<div>' + '<h4>My Age in Seconds: ' + timeCalc.myAgeSecs() +'</h4></div>' +
          '<div>' + '<h4>Cristina Tarantino\'s Age in Milliseconds: ' + timeCalc.CristinaTarantinoAgeMillisecs() +'</h4></div>';
  $day1.append(htmlHw1);

  // ==============================  DAY 2 =================================

  // Calculate and console.log the frequency each of the 12 notes between A and A'
  // Expected results: [A = 440, A# = 466.16, B = 493.88, C = 523.25, C# = 554.37, D = 587.33, D# = 622.25, E = 659.26, F = 698.46, F# = 739.99, G = 783.99, G# = 830.61, A = 880;]

  var musicScaleNotes = [" A", " A#", " B", " C", " C#", " D", " D#", " E", " F", " F#", " G", " G#", " A"];

  // Create as an array
  function scaleHz (array) {
    var newArray = [];
    for (var i = 0; i < array.length - 1; i++) {
      newArray.push(array[i] + " : " + (440 * (2 ** ((i)/12))).toFixed(2));
    };
    console.log(newArray);
    return newArray;
  }

  scaleHz(musicScaleNotes);

  // Create as an object
  function scaleHzObject (array) {
    var newArray = [];
    for (var i = 0; i < array.length - 1; i++) {
      var element = array[i];
      newArray.push({[element]: (440 * (2 ** ((i)/12))).toFixed(2)});
    };
    console.log(newArray);
    return newArray;
  }

  scaleHzObject(musicScaleNotes);

  // Calculate and console log how many 'minutes' the Moon travels in a day.
  function moonMinsCalc () {
    var minsInDay = 24 * 60; // 1440
    var minsPerDegree = minsInDay/360;
    var moonMins = 13 * minsPerDegree;
    console.log("The number of 'minutes' the moon travels in a day is: ", moonMins)
    return moonMins
  }

  moonMinsCalc()

  // print hw day 2
  document.getElementById('day2').innerHTML = '<h3>Music notes frequency</h3>' + '<p>The frequency each of the 12 notes between A and A\':</br></br>' +
  scaleHz(musicScaleNotes) + '</p>' +
  '<h3>Moon minutes</h3><p>' +
  "The number of 'minutes' the moon travels in a day is: " + moonMinsCalc() + '</p>'

  // ==============================  DAY 3 =================================

  // Full name greeting

  function greeting () {
    var firstName = prompt("What is your first name?", "e.g. Harriet")
    var middleName = prompt("What is your middle name?", "e.g. Josephine")
    var lastName = prompt("What is your last name?", "e.g. Clarke")
    var favGame = prompt("What is your favourite game?", "e.g. Cluedo")
    var favAnimal = prompt("What is your favourite animal?", "e.g. Giraffe")
    alert('Hello ' + firstName + ' ' + middleName + ' ' + lastName + '!')
    var $day3 = $( "#day3" )
    var htmlHw3 =
            '<div>' + '<p> The person on this page is ' + firstName + " " +
            middleName + " " + lastName + '</p></div>' +
            '<div>' + '<p>Their favourie game is ' + favGame + '</p></div>' +
            '<div>' + '<p>Their favourie animal is a ' + favAnimal + '</p></div>';

    $day3.append(htmlHw3);
  }

  // greeting()

  // Bigger, better favorite number

  function favNum () {
    var favNum = parseInt(prompt("What is your favourite number?"));
    function checkInt (input) {
      while (Number.isInteger(input) === false) {
        input = parseInt(prompt("What is your favourite number?"));
      }
      return input;
    }
    favNum = checkInt(favNum);
    var betterNum = favNum + 1;
    console.log("Perhaps a better number would be: ", betterNum);
  }

  // favNum()

  // Angry boss
  function angryBoss () {
    var bossSays = prompt('Boss says: What do you want?')
    while (bossSays !== 'I want a raise') {
      bossSays = prompt('Boss says: What do you WANT?')
    }
    console.log('Boss says: WHADDAYA MEAN "I WANT A RAISE"?!? YOU\'RE FIRED!!')
  }

  // angryBoss()

  // Table of contents.
  var scrumContents = [
  ["Chapter 1: The Way the World Works Is Broken", "p. 1"],
  ["Chapter 2 The Origins of Scrum", "p. 23"],
  ["Chapter 3 Teams", "p. 41"],
  ["Chapter 4 Time", "p. 71"],
  ["Chapter 5 Waste Is a Crime", "p. 85"],
  ["Chapter 6 Plan Reality, Not Fantasy", "p. 111"],
  ["Chapter 7 Happiness", "p. 145"],
  ["Chapter 8 Priorities", "p. 171"],
  ["Chapter 9 Change the World", "p. 203"],
  ["Acknowledgments", "p. 232"],
  ["Appendix: Implementing Scrum-How to Begin", "p. 234"],
  ["Notes", "p. 239"],
  ["Index", "p. 242"]
  ]

  function printCotents (contentsArray) {
    var htmlHw2 = '<h3>Table of Contents</h3><table>'
    for (var i = 0; i < scrumContents.length - 1; i++) {
      htmlHw2 += '<tr>'
      htmlHw2 += '<td>' + scrumContents[i][0] + '</td>'
      htmlHw2 += '<td>' + scrumContents[i][1] + '</td>'
      htmlHw2 += '</tr>'
    }
    htmlHw2 += '</table>'
    document.getElementById('day3').innerHTML = htmlHw2
  }

  printCotents(scrumContents)

  // Generate a random number
  function generateRandom (min, max) {
    var randNum = Math.floor(Math.random() * (max - min) + min)
    console.log('Random number between ' + min + ' and ' + max + ' is: ' + randNum)
    return randNum
  }

  // between 1 and 10
  generateRandom(1, 10)

  // between 1 and 100
  generateRandom(1, 100)

  // between 1930 and 1950
  generateRandom(1930, 1950)

  // Practice: ** pow(base, power) 365%7 abs(-7)
  // **
  function power (a, b) {
    var p = a ** b
    console.log("a: " + a + " to the power of b: " + b + " = " + p)
    return p
  };

  power(3, 3);

  // pow(base, power)
  function powerMath (a, b) {
    var pM = Math.pow(a, b)
    console.log("a: " + a + " to the power of b: " + b + " = " + pM);
    return pM
  }

  powerMath(2, 2)

  // remainder
  var remainder = 365%7;
  console.log("365%7: ", remainder);

  // abs()
  var absolute = Math.abs(-7);
  console.log("absolute '-7': ", absolute);

  // ==============================  DAY 4 =================================
  // “99 Bottles of Beer on the Wall.”
  function bottlesBeer () {
    var htmlHw4 = '<h3>Bottles of Beer of the Wall</h3><ul>' +
    '<li>1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, 1 bottle of beer on the wall.</li>'
    for (var i = 2; i < 100; i++) {
      htmlHw4 += '<li>' + i + ' bottles of beer on the wall, ' + i + ' bottles of beer. Take one down and pass it around, ' + i + ' bottles of beer on the wall.</li>'
    }
    htmlHw4 += '<li>No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.</li></ul>'
    document.getElementById('beer').innerHTML = htmlHw4
  }

  // bottlesBeer()

  // Deaf grandma.

  var deafGrandma = {
    grandma_convo: function (num) {
      var year = Math.floor(Math.random() * (1950 - 1930) + 1930)
      var words_to_grandma = prompt("What would you like to say to Grandma?")
      var count = num
      var htmlConvo = '<p>What would you like to say to Grandma?</p>'

      if (words_to_grandma === "BYE" && count === 2) {
        this.buildConvo('You said: ' + words_to_grandma)
        this.buildConvo('Grandma says: OK BYE DEAR!')
        console.log("Grandma says: OK BYE DEAR!")
      }
      else if (words_to_grandma === "BYE") {
        this.buildConvo('You said: ' + words_to_grandma)
        this.buildConvo('Grandma says: HOW\'S THE WEATHER?')
        console.log("Grandma says: HOW\'S THE WEATHER?")
        count = count + 1
        this.grandma_convo(count)
      }
      else if (words_to_grandma === words_to_grandma.toUpperCase()) {
        this.buildConvo('You said: ' + words_to_grandma)
        this.buildConvo('Grandma says: NO, NOT SINCE ' + year + '!')
        console.log("Grandma says: 'NO, NOT SINCE " + year + "!'")
        this.grandma_convo(0)
      }
      else {
        this.buildConvo('You said: ' + words_to_grandma)
        this.buildConvo('Grandma says: HUH?! SPEAK UP, GIRL!')
        console.log("Grandma says: 'HUH?! SPEAK UP, GIRL!'")
        this.grandma_convo(0)
      }
    },

    buildConvo: function (textToAppend) {
      var li = document.createElement("li");
      var text = document.createTextNode(textToAppend);
      li.appendChild(text);
      document.getElementById("deafGrandma").appendChild(li);
    }
  }

  // deafGrandma.grandma_convo(0)

  // Leap years
  // var leapYears = {
  //   startYr: parseInt(prompt("What year would you like to start counting from?  ")),
  //
  //   endYr: parseInt(prompt("What year would you like to stop counting?  ")),
  //
  //   leap_year_calc: function leap_year_calc (startYr, endYr) {
  //     for (var i = startYr; i <= endYr; i++) {
  //       if (i % 100 === 0 && i % 400 === 0) {
  //         console.log(i)
  //         this.printYrs(i)
  //       }
  //       if (i % 4 === 0 && i % 100 !== 0) {
  //         console.log(i)
  //         this.printYrs(i)
  //       }
  //     }
  //   },
  //
  //   printYrs: function (year) {
  //     var li = document.createElement("li");
  //     var text = document.createTextNode(year);
  //     li.appendChild(text);
  //     document.getElementById("leapYr").appendChild(li);
  //   }
  // }

// leapYears.leap_year_calc(leapYears.startYr, leapYears.endYr)

// Life calculation - productivity
function productivityScore (sleepHrs, coffees) {
  var productiveness;
  if (6 <= sleepHrs && sleepHrs <= 8 && 1 < coffees && coffees < 4) {
    productiveness = sleepHrs * coffees;
    return productiveness
  }
  else if (sleepHrs < 6 && 1 < coffees && coffees < 4) {
    var productiveness = sleepHrs * coffees - 2;
    return productiveness
  }
  else {
    var productiveness = 0;
    return productiveness
  }
}

// var sleepHrs = parseInt(prompt('How many hours of sleep did you get last night?'))
// var coffees = parseInt(prompt('How many coffees will you drink today?'))
//
// console.log('Your estimated productivity today will be: ' + productivityScore(sleepHrs, coffees) + ' out of 25')

// Building and sorting an array.

function getWords (newWordsList) {
  var wordList = newWordsList
  var wordInput = prompt("Please enter one word to add to your list, or press Enter to finalise your list:  ")
  if (wordInput === "") {
    var sortedList = wordList.sort()
    var html = '<h3>Sorted Words List</h3>'
    for (var i = 0; i < sortedList.length; i++) {
      html += '<p>' + sortedList[i] + '</p>'
    }
    document.getElementById('wordList').innerHTML = html
  }
  else {
    wordList.push(wordInput)
    getWords(wordList)
  }
}

// getWords([])

// Write a function that prints out "moo" n times
function printMoo (n) {
  for (var i = 1; i <= n; i++) {
    console.log('moo')
  }
}

printMoo(3)

// Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any of this new-fangled subtraction “IX” nonsense.
// Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. Make sure to test your method on a bunch of different numbers.



// “Modern” Roman numerals. Eventually, someone thought it would be terribly clever if putting a smaller number before a larger one meant you had to subtract the smaller one. As a result of this development, you must now suffer. Rewrite your previous method to return the new-style Roman numerals so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.



});
