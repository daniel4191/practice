const messageContainer = document.querySelector('#d-day-message');
const container = document.querySelector('#d-day-container')
const intervalIdArr = [];

// 객체
// const obj = {
//     name: 'Jason',
//     age: 25
// };
// // if 로직 1 - else if 조건
// if (obj.name === 'Jason') {
//     console.log('안녕,' + obj.name);
// } else if (obj.name === 'Peter') {
//     console.log('안녕,' + obj.name);
// } else {
//     console.log('넌 우리 멤버가 아니구나.');
// };

// // if 로직 2 - or조건 ||
// if (obj.name === 'Jason' || obj.name == 'Peter') {
//     console.log('안녕,' + obj.name);
// } else {
//     console.log('넌 우리 멤버가 아니구나');
// }

// // if 로직 3 - and 조건 &&
// if (obj.name === 'Jason' && obj.age >= 25) {
//     // console.log('안녕,'+obj.name + '너의 나이는'+obj.age + '이구나')
//     console.log(`안녕, ${obj.name}, 너의 나이는 ${obj.age}살 이구나`)
// } else {
//     console.log('넌 우리 멤버가 아니구나.')
// }



// 조건문
// 조건식이 성립해야 {}안의 값들이 실행된다.
// let name = 'Peter';
// if (name === 'Jason') {
//     console.log('조건문 통과');
// };

// 참조 타입 케이스
// const arr = [1, 2, 3]
// console.log('arr === [1,2,3]', arr === [1, 2, 3])

// dataFormMaker과 counterMake 변수는 각각의 "지역변수"가 된다.
const dateFormMaker = function () {
    const inputYear = document.querySelector('#target-year-input').value;
    const inputMonth = document.querySelector('#target-month-input').value;
    const inputDate = document.querySelector('#target-date-input').value;

    // const dateFormat = inputYear + '-' + inputMonth + '-' + inputDate;
    // document는 해당 페이지의 html값 전체를 스크래핑하는 기능이다.
    // querySelector를 사용하면 그 안에 입력한 태그의 값을 가져오는것이 가능하다.
    // target-year-input라는 이름의 id값을 가져올것이고
    // .value를 통해서 그 안에 있는 "값"을 가져올 것이다.
    // console.log(document.querySelector('#target-year-input').value);
    // console.log(document.querySelector('#target-month-input').value);
    // console.log(document.querySelector('#target-date-input').value);
    // console.log(inputYear, inputMonth, inputDate);

    // `${}`처리는 파이썬으로 따지면 f-string으로 format해주는 것 같다.
    // 바로 문자열로 만들어 주는 것이다. str로 감싸듯이.
    // 이것을 "템플릿 리터럴"이라고 부른다고 한다.
    const dateFormat = `${inputYear}-${inputMonth}-${inputDate}`
    return dateFormat;
};

const counterMaker = function () {    
    // 테스트용 콘솔 출력
    // console.log('반복 실행중');
    // console.log(dateFormMaker())
    const targetDateInput = dateFormMaker()

    // console.log(targetDateInput);
    // 현재의 연월일을 영어식 표기법으로. 시간도 현재시각으로 24시간기준으로 출력
    const nowDate = new Date();

    // 특정 일자의 연월일을 영어식 표기법으로 출력. 시간은 오전 9시표준
    // 하지만 .setHours(0,0,0,0)을 통해서 "자정"을 기준하는 것으로 리셋해줬다.
    const targetDate = new Date(targetDateInput).setHours(0, 0, 0, 0);

    // console.log(nowDate);
    // 이것을 해주는 이유는 대상이되는 시각 - 현재 시각을 구해주는 것인데
    // 1000을 곱해주는 이유는 0.001초 단위까지 계산이 되기때문에 해당 부분을 배제해주기 위해서 하는 것이다.
    const remaining = (targetDate - nowDate) / 1000;    

    if (remaining <= 0) {
        container.style.display = 'none';
        // 만약, remaining이 0 이하라면, 타이머가 종료 되었습니다. 출력
        messageContainer.innerHTML = '<h3>타이머가 종료되었습니다.</h3>';
        messageContainer.style.display = 'flex';
        // 타이머가 종료되어야 하는 상황에 종료시켜주는 함수
        setClearInterval()
        return;
        

        // javascript에서는 === NaN으로 판별이 안된다.
        // isNaN()을 써줘야한다.
    } else if (isNaN(remaining)) {
        container.style.display = 'none';
        messageContainer.innerHTML = '<h3>유효한 시간대가 아닙니다.</h3>';
        messageContainer.style.display = 'flex';
        // return은 함수가 종료가 됨을 의미한다.
        // 지금의 경우에는 최상위 함수인 const counterMaker = function ()의 종료다.

        setClearInterval()
        return;
    }

    // text
    // console.log('함수 종료 안됨')

    const remainingObj = {
        // 1시간은 3600초로 이루어져있다. 하루는 24시간으로 이루어져있다.
        // "몇일"인지를 계산하기 위해서 이렇게 하는 것이다.
        // Math.floor는 소수점 아래의 숫자를 "버림"해주는 기능이다.            
        remainingDate: Math.floor(remaining / 3600 / 24),

        // 이 방식은 이미 계산된 날자에서 시간이 얼마나 되는지,
        // 그리고 그 시간중에서도 날자를 빼주기 위해서 만들었는데
        // ex. 10일 12시간일 경우에는 252시간이다. (10일 *24시간 = 240시간 + 12시간 = 252시간)
        // 하지만 이렇게 해주니 결과값으로 0이 나왔다.
        // 생각해보니깐 당연했다. 10일일 경우 24를 곱해주면 240. 거기에 24를 나눠주고
        // 나머지를 구하라면 몫은 10이되고 나머지는 0이되니깐
        // const remainingHours = ((remainingDate * 24) % 24);
        // 그래서 다시 정의해주었다.
        remainingHours: Math.floor(remaining / 3600) % 24,

        // 이것도 마찬가지로 계산이 안된다;
        // const remainingMins = (remainingHours * 60) % 60;
        remainingMin: Math.floor(remaining / 60) % 60,

        remainingSec: Math.floor(remaining) % 60
    };
    

    

    // days.textContent = remainingDate
    // hours.textContent = remainingHours
    // min.textContent = remainingMin
    // sec.textContent = remainingSec

    
    // for 문의 형태 2
    // for (let i = 0; i < timeKeys.length; i += 1) {
    //     // console.log(documentObj[docKeys[i]]);
    //     // documentObj[docKeys[i]].textContent = '변경';
    //     documentObj[docKeys[i]].textContent = remainingObj[timeKeys[i]]
    // };

    // for 문의 형태 3
    // for (let key in documentObj) {
    //     console.log(key);
    // };

    // const documentObj = {
    //     days: document.getElementById('days'),
    //     hours: document.getElementById('hours'),
    //     min: document.getElementById('min'),
    //     sec: document.getElementById('sec')
    // }
    
    // for 문의 형태 4

    // let i = 0;
    // for (let key in documentObj) {
    //     // console.log(documentObj[key], key);
    //     documentObj[key].textContent = remainingObj[timeKeys[i]]
    //     i ++
    // };
    

    // documentObj['days'].textContent = remainingObj['remainingDate'];
    // documentObj['hours'].textContent = remainingObj['remainingHours'];
    // documentObj['min'].textContent = remainingObj['remainingMin'];
    // documentObj['sec'].textContent = remainingObj['remainingSec'];

    const documentArr = ['days', 'hours', 'min', 'sec']
    const timeKeys = Object.keys(remainingObj);
    // const docKeys = Object.keys(documentObj);
    // console.log(timeKeys, docKeys);

    // for 문의 형태 1
    // for of 문은 배열에 많이 사용해줌

    let i = 0;
    for (let tag of documentArr) {
        document.getElementById(tag).textContent = remainingObj[timeKeys[i]];
        i ++;
    }
};

const starter = function () {
    // 지역함수(함수 내부의 함수)는 어떤 '임시'의 데이터값과 같다.
    // 때문에 결과값을 원한다면 밖으로 빼주어야한다.
    // const intervalIdArr = []
    container.style.display = 'flex';
    messageContainer.style.display = 'none';
    counterMaker();
    // 이 setInterval함수 하나로 밑의 3줄에 걸친 for문을 대체 가능
    // setInterval(counterMaker, 1000)
    // for (let i = 0; i < 100; 1++) {
    //     setTimeout(counterMaker, 1000 * i);
    // }

    const intervalId = setInterval(counterMaker, 1000);
    // console.log(intervalId);
    
    intervalIdArr.push(intervalId)
    // console.log(intervalIdArr);
};

const setClearInterval = function () {
    // 이것은 container를 보이지 않게 해주는 것이다.
    container.style.display = 'none';
    // style로 접근해줌으로써 css를 직접적으로 javascript에 적용한다.
    // messageContainer.style.color = 'red';

    // innerHTML을 통해서 javascript에서 html식의 작성도 가능하다.
    messageContainer.innerHTML = '<h3>D-day를 입력해 주세요.</h3>'
    // 바로 위의 함수인 starter에서 none값으로 주어졌기 때문에, flex로 변형해주어야한다.
    messageContainer.style.display = 'flex';
    for(let i = 0; i < intervalIdArr.length; i++) {
        clearInterval(intervalIdArr[i]);
    }
}