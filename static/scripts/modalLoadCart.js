






document.addEventListener('DOMContentLoaded', function () {

    let loadTitleBookLS = localStorage.getItem('titleBook')
    // let titleBook = JSON.parse(loadTitleBookLS)
    let titleBook = loadTitleBookLS

    let loadImageBookLS = localStorage.getItem('imageBook')
    // let imageBook = JSON.parse(loadImageBookLS)
    let imageBook = loadImageBookLS

    let loadValueBookLS = localStorage.getItem('valueBook')
    // let valueBook = JSON.parse(loadValueBookLS)
    // let valueBookValid = parse(valueBook)
    // let valueBook = loadValueBookLS
    let valueBook = parseFloat(loadValueBookLS.replace(",","."))
    console.log(valueBook)

    let fieldTitle = document.getElementById("titleCartModal")
    let fieldImg = document.getElementById("imgCartModal") 
    let fieldValue = document.getElementById("valueCartModal") 

    console.log(imageBook)
    console.log(titleBook)

    function calculateCart(imageBook,titleBook){
        fieldImg.src = imageBook
        fieldTitle.textContent = titleBook
        fieldValue.textContent = `R$ ${valueBook}`

        console.log(imageBook)
        console.log(titleBook)
        // console.log(55)
        // console.log("55")
        // console.log(parseFloat(valueBook))
    }

     // Chama a função ao abrir o modal
    const modal = document.getElementById('myModal');
    modal.addEventListener('show.bs.modal', function () {
        calculateCart();
    });

    calculateCart(imageBook, titleBook)

});

 


function clearLocalStorage(){
    localStorage.removeItem('titleBook')
    localStorage.removeItem('imageBook')
    localStorage.removeItem('valueBook')

}






























// let loadTitleBookLS = localStorage.getItem('titleBook')
// // let titleBook = JSON.parse(loadTitleBookLS)
// let titleBook = loadTitleBookLS

// let loadImageBookLS = localStorage.getItem('imageBook')
// // let imageBook = JSON.parse(loadImageBookLS)
// let imageBook = loadImageBookLS

// let loadValueBookLS = localStorage.getItem('valueBook')
// // let valueBook = JSON.parse(loadValueBookLS)
// // let valueBookValid = parse(valueBook)
// let valueBook = parseFloat(loadValueBookLS)
// // console.log(valueBook)

// let fieldTitle = document.getElementById("titleCartModal")
// let fieldImg = document.getElementById("imgCartModal") 
// // let fieldValue = document.getElementById("") 

// console.log(imageBook)
//     console.log(titleBook)

// function calculateCart(imageBook,titleBook){
//     fieldImg.src = imageBook
//     fieldTitle.textContent = titleBook

//     console.log(imageBook)
//     console.log(titleBook)
//     // console.log(55)
//     // console.log("55")
//     // console.log(parseFloat(valueBook))
// }



// calculateCart()