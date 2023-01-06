const fruits = [
    { number: 1, title: '레드향' },
    { number: 2, title: '샤인머스켓' },
    { number: 3, title: '산청딸기' },
    { number: 4, title: '한라봉' },
    { number: 5, title: '사과' },
    { number: 6, title: '애플망고' },
    { number: 7, title: '딸기' },
    { number: 8, title: '천혜향' },
    { number: 9, title: '과일선물세트' },
    { number: 10, title: '귤' }
];
// undefined
let laila = fruits[0].number
// undefined
laila
// 1
laila.push(fruits[0].title
// VM4503:1 Uncaught SyntaxError: missing ) after argument list
fruits[0].number + ' ' + fruits[0].title
// '1 레드향'