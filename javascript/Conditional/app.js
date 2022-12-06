// console.log('before conditiopn!')
// let random = Math.random();
// if (random < 0.5) {
//     console.log('your number is less than 0.5');
// } else {
//     console.log('your number is greater than 0.5');
// }
// console.log(random);

// 입력 알럿을 띄워줌과 동시에, 입력받은 값이 대문자로 되더라도 반드시 소문자로 전환하여 비교하게끔 해준다.
// const dayOfWeek = prompt('ENTER A DAY').toLocaleLowerCase();

// if (dayOfWeek === 'monday') {
//     console.log('i love monday too!');
// } else if (dayOfWeek === 'saturday') {
//     console.log('i love saturday too!!');
// } else if (dayOfWeek === 'friday') {
//     console.log('i love Friday too!!');
// } else if (dayOfWeek === 'wednesday') {
//     console.log('Thursday also good');
// }

// const age = 8;

// if (age < 5) {
//     console.log('you are a baby. you get in for free!');
//     // 이것의 의미는 이미 5세 미만은 걸러냈으니, 5세이상, 10세 미만을 의미한다.
// } else if (age < 10) {
//     console.log('you are a child. you need pay $10');
// } else if (age < 65) {
//     console.log('you are an adult. you pay $20');
// }

const password = prompt('please enter a new password!');

// password must be 6+ characters
if (password.length >= 6) {
    console.log('long enough password!');
} else {
    console.log('password too short must be 6+ characters');
}

if (password.indexOf(' ') === -1) {
    console.log('good job no space!');
} else {
    console.log('password cannot contain spaces');
}