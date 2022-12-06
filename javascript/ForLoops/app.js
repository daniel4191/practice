// console.log(1)
// console.log(2)
// console.log(3)
// console.log(4)
// console.log(5)
// console.log(6)
// console.log(7)
// console.log(8)
// console.log(9)
// console.log(10)

// 1부터 10까지 1씩 증가
// for (let i = 1; i <= 10; i++) {
//     console.log(i);
// }

// 0부터 20까지 2씩 증가
// for (let i = 0; i < 21; i += 2) {
//     console.log(i)
// };

// 100부터 0까지 10씩 감소
// for (let i = 100; i >= 0; i -= 10) {
//     console.log(i);
// };

// 무한루프
// for(let i = 20; i >= 0; i++) {
//     console.log(i);
// }

// 목록 출력
// length에 -1을 해주는 이유는 인덱스의 슬라이싱 구조상 0부터 시작해서 가장 마지막 숫자의 -1까지 긁기 때문
// for (let i = 목록.length - 1; i >= 0; i--) {
//     console.log(목록[i]);
// }

// const people = ["Scooby", "Velma", "Daphne", "Shaggy", "Fred"]; //DONT TOUCH THIS LINE!

// // WRITE YOUR LOOP BELOW THIS LINE:

// for (let i = 0; i <= people.length - 1; i++) {
//     console.log(people[i].toUpperCase())
// }

// 반복문 1
// for (let i = 1; i <= 10; i++) {
//     console.log(`i is: ${i}`)
//     for (let j = 1; j <= 3; j++) {
//         console.log(`    j is: ${j}`)
//     }
// }

// 반복문 2
const seathingChart = [
    ['Kristen', 'Erik', 'Namita'],
    ['Geoffrey', 'Juanita', 'Antonio', 'Kevin'],
    ['Yuma', 'Sakura', 'Jack', 'Erika']
]

// 내가 풀이한 코드
// for (let i = 0; i < seathingChart.length; i++) {
//     console.log(seathingChart[i])
//     for (let j = 0; j < seathingChart[i].length; j++) {
//         console.log(seathingChart[i][j])
//     }
// }

// 강사님 코드
for (let i = 0; i < seathingChart.length; i++) {
    const row = seathingChart[i];
    console.log(`Phase: #${i + 1}`)
    for (let j = 0; j < row.length; j++) {
        console.log(row[j])
    }
}