let arr = [1,2,3]

let anonFunc = (x) => x + 2


let mappedArr = arr.map((x) => x + 2)


console.log(mappedArr)


// anonFunc(3)
function something(num){
    let newNum = num + 5
    return function thisThing(a){
        return a + num
    }
}



// let returnVal = anonFunc(3) // print 5
// console.log("In JS Land", returnVal)
