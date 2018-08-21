// =================== WEEK 1 HOMEWORK ====================
$(document).ready(function(){
  // ===================  DAY 1 ====================

  // Hours in a year. How many hours are in a year?
  var hrInYr = 24 * 365;
  var hrInYrString = "Hours in a Year: " + hrInYr;
  console.log(hrInYrString);


  // Minutes in a decade. How many minutes are in a decade?
  var minInDec = hrInYr * 60 * 10 + (2 * 24);
  var minInDecString = "Minutes in a Decade: " + minInDec;
  console.log(minInDecString);


  // Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
  var secInDay = 24 * 60 * 60;
  var myAgeDays = (27 * 365) + 35 + Math.round(27 / 4);
  var myAgeSecs = myAgeDays * secInDay;
  var myAgeSecsString = "My Age in Seconds: " + myAgeSecs;
  console.log(myAgeSecsString);


  // Cristina Tarantino: 32 yesterday! How many milliseconds old is she hahaha? Calculate @Cristina Tarantino's age in milliseconds.
  var millisecInDay = secInDay * 1000;
  var CristinaTarantinoAgeMillisecs = (32 * (365 + (32/4))) * millisecInDay;
  CristinaTarantinoAgeMillisecsString = "Cristina Tarantino's Age in Milliseconds: " + CristinaTarantinoAgeMillisecs;
  console.log(CristinaTarantinoAgeMillisecsString);


  // Print homework day 1 to page

  var $day1 = $( "#day1" )
  var htmlHw =
          '<div>' + '<h1>' + hrInYrString +'</h1></div>' +
          '<div>' + '<h1>' + minInDecString +'</h1></div>' +
          '<div>' + '<h1>' + myAgeSecsString +'</h1></div>' +
          '<div>' + '<h1>' + CristinaTarantinoAgeMillisecsString +'</h1></div>';
  $day1.append(htmlHw);

  // ============================================================================
  // ===================  DAY 2 ====================

  // Music note A 440 Hz 1 octave is double the frequency tempered piano A' 880 Hz Calculate and console.log the frequency each of the 12 notes between A and A' Hint: the notes are NOT in a linear scale, but in a geometric scale
  // Expected results:
  // var A = 440
  // A# = 466.16
  // B = 493.88
  // C = 523.25
  // C# = 554.37
  // D = 587.33
  // D# = 622.25
  // E = 659.26
  // F = 698.46
  // F# = 739.99
  // G = 783.99
  // G# = 830.61
  // A = 880;
  var musicScale = [440, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.26, 698.46, 739.99, 783.99, 830.61, 880];

  function scaleDif (array) {
    var difArray = [];
    for (i = 0; i < musicScale.length - 1; i++) {
      var dif = array[i + 1] - array[i];
      difArray.push(dif);
    };
    console.log(difArray)
  }

  scaleDif(musicScale);

  // A * (2 ^ i/12)

  var musicScaleNotes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"];

  function scaleHz (array) {
    var newArray = [];
    for (var i = 0; i < array.length - 1; i++) {
      newArray.push(array[i] + " : " + (440 * (2 ** ((i)/12))).toFixed(2));
    };
    console.log(newArray);
    return newArray;
  }

  scaleHz(musicScaleNotes);

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


  // Planets
  // Calculate and console log how many 'minutes' the Moon travels in a day. Hint: first calculate how many degrees the Moons travels in the sky when the Earth returns to the same position during its daily rotation.

  // Earth travels 360 degrees = minsInDay minutes > 360d = 1440m
  var minsInDay = 24 * 60; // 1440
  // Moon orbit in 24 hours: 13 degrees
  var minsPerDegree = minsInDay/360;
  var moonMins = 13 * minsPerDegree;

  console.log("The number of 'minutes' the moon travels in a day is: ", moonMins)

  // Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.

  // var firstName = prompt("What is your first name?", "e.g. Harriet")
  // var middleName = prompt("What is your middle name?", "e.g. Josephine")
  // var lastName = prompt("What is your last name?", "e.g. Clarke")
  // var favGame = prompt("What is your favourite game?", "e.g. Cluedo")
  // var favAnimal = prompt("What is your favourite animal?", "e.g. Giraffe")

  // var $day3 = $( "#day3" )
  // var htmlHw3 =
  //         '<div>' + '<h2> The person on this page is: ' + firstName + " " +
  //         middleName + " " + lastName + '.</h2></div>' +
  //         '<div>' + '<h2>Their favourie game is ' + favGame + '.</h2></div>' +
  //         '<div>' + '<h2>Their favourie animal is a ' + favAnimal + '.</h2></div>';
  //
  // $day3.append(htmlHw3);


  // Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)
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


  // Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:
  // WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!





  // Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
  // Table of Contents
  //
  // Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13




  // Optional: in JS we may prefer to 'print' these to the HTML file itself rather than the console.


  // Generate a random number
  // between 1 and 10
  // between 1 and 100
  // between 1930 and 1950


  // ** pow(base, power) 365%7 abs(-7)

  function power (a, b) {
    var p = a ** b
    console.log("a: " + a + " to the power of b: " + b + " = " + p)
    return p
  };

  power(3, 3); // returns 9

  function powerMath (a, b) {
    var pM = Math.pow(a, b)
    console.log("a: " + a + " to the power of b: " + b + " = " + pM);
    return pM
  }

  powerMath(2, 2) // returns 4

  var remainder = 365%7;
  console.log("365%7: ", remainder);

  var absolute = Math.abs(-7);
  console.log("absolute '-7': ", absolute);


});
