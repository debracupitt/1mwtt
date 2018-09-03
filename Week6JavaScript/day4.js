// Promises
'use strict';

var p1 = new Promise(function (resolve, reject) {
  var newMessage = 'Good morning ladies! \u{1F64B}';
  // newMessage = false;
  if (newMessage) {
    setTimeout(resolve, 3000, newMessage);
  }
  else {
    reject(new Error("Sorry, couldn\'t print your message. \u{1F61E}"))
  }
})

console.log(promise1)

p1.then((message) => {
  console.log(message)
})
.catch((error) => {
  console.log(error)
})

var p2 = new Promise((resolve, reject) => {
  setTimeout(function() {
    resolve('Success! \u{1F939}\u{200D}\u{2640}\u{FE0F}')
  }, 1000)
})

console.log(p2)

p2.then((successMessage) => {
  console.log("Yay! " + successMessage)
})

var promise1 = Promise.resolve(3);
var promise2 = 42;
var promise3 = new Promise(function(resolve, reject) {
  setTimeout(resolve, 100, 'foo');
});

Promise.all([promise1, promise2, promise3]).then(function(values) {
  console.log(values);
});

function myAsyncFunction (url) {
  return new Promise ((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.onload = () => resolve(xhr.resposeText);
    xhr.onerror = () => reject(xhr.statusText);
  });
}

myAsyncFunction('http://treasures-tech.business.site/')

var promiseCount = 0;

function testPromise () {
  let thisPromiseCount = ++promiseCount;

  let log = document.getElementById('log');
  log.insertAdjacentHTML('beforeend', 'Started (<small>Sync code has started</small>)</br>');

  let p1 = new Promise ((resolve, reject) => {
    if (thisPromiseCount === NaN) {
      reject();
    }
    while (thisPromiseCount <= 3) {
      resolve(log.insertAdjacentHTML('beforeend', thisPromiseCount + ' Started (<small>Async code has started</small>)</br>'));
      thisPromiseCount++
    }
  });
  p1.then(console.log('All promises counted!'))
  .then(log.insertAdjacentHTML('beforeend', 'Async code has completed'))
  .catch ()
}

document.getElementById('pinky').addEventListener('click', testPromise)

var promiseCount2 = 0;

function testPromise2 () {
  let thisPromiseCount = ++promiseCount2;

  let log2 = document.getElementById('log2');
  log2.insertAdjacentHTML('beforeend', thisPromiseCount + ' Started (<small>Sync code has started</small>)</br>');

  let p2 = new Promise ((resolve, reject) => {
    log2.insertAdjacentHTML('beforeend', thisPromiseCount + ' Promise started (<small>Async code has started</small>)</br>');
    window.setTimeout(function () {
      resolve(thisPromiseCount);
    }, (Math.random() * 2000 + 1000));
  });

  p2.then(val => log2.insertAdjacentHTML('beforeend', val + ' Promise fulfilled. (<small>Async code terminated</small>)</br></br>'))
  .catch (reason => console.log('Handle rejected promise ('+reason+')'))

  log2.insertAdjacentHTML('beforeend', thisPromiseCount + ' Promise made (<small>Sync code terminated</small>)</br></br>')
}

document.getElementById('btn').addEventListener('click', testPromise2)


// Go through Advanced JS examples on Promises
// You don't know JS github - read

const myPromise = amount => {
  return new Promise((resolve, reject) => {
    if (amount > 0) {
      resolve(amount + " = Success!")
    }

    reject(amount + " = Failure!")
  })
}

let handleSuccess = (x) => {
  console.log(x + " it worked!")
}

let handleError = (x) => {
  console.log(x + " oh no, it failed!")
}

console.log(myPromise(1).then(handleSuccess, handleError))
console.log(myPromise('Hello'))
console.log(myPromise(0))
console.log(myPromise(-1).then(handleSuccess, handleError))
console.log(myPromise([]))
console.log(myPromise({}))
console.log(myPromise(3))

const anotherProm = amount => {
  return new Promise ((resolve, reject) => {
    if (amount > 0) {
      resolve(amount + " = Success!")
    }
    reject(amount + " = Failure!")
  })
}

anotherProm(0).then(res => {
  console.log(res + " success!")
}).catch(err => {
  console.log(err + " Oh no, it failed!")
})

anotherProm(5).then(res => {
  console.log(res + " Success!")
}).catch(err => {
  console.log(err + " oh no it failed!")
})
