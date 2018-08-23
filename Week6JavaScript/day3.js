// In ecmascript 6 syntax instead of function() {} shorter is () => {} sometimes you can even skip () and {} if function is short, it is called arrow function

function foo (b) {
  var a = 10
  return a + b + 11
}

function bar (x) {
  var y = 3
  return foo(x * y)
}

console.log(bar(17))

// setTimeout

// const s = new Date().getSeconds()
//
// setTimeout()
//
// while (true) {
//   if (new Date().getSeconds() - s >= 2) {
//     console.log('Good, 2 seconds have passed, we were happily looping.')
//   }
// }

var promise1 = new Promise(function (resolve, reject) {
  setTimeout(resolve, 100, 'Good morning ladies!')
})

console.log(promise1)
