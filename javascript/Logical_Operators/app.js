// const password = prompt('enter your password');

// if (password.length >= 6 && password.indexOf(' ') === -1) {
//     console.log('valid password')
// } else {
//     console.log('incorrect format4 for password')
// }

// 0-5 free
// 5-10 $10
// 10-65 $20
// 65+ free

// 포인트는 &&은 and 조건, ||는 or조건이며
// 연결되는 조건에 대해서는 하나의 괄호 ()안에 들어와야 된다는 속성을 띈다.
// const age = 100;
// if (age >= 0 && age < 5 || age >= 65) {
//     console.log('free');
// } else if (age >= 5 && age < 10) {
//     console.log('$10');
// } else if (age >= 10 && age < 65) {
//     console.log('$20');
// } else {
//     console.log('invalid age!');
// }


// const firstName = prompt('enter your first name');
// // !는 '아니면'이라는 뜻이다. != 로 보통 비교 불리언으로 사용되지만 !firstName으로도 사용된다.
// if (!firstName) {
//     firstName = prompt('try agein')
// }

const age = 45;
if (!(age >= 0 && age < 5 || age >= 65)) {
    console.log('you are not a baby or senior');
}