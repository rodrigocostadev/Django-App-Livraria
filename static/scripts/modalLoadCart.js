



////////////////////////////////////////////////////////////////////////////
////////////////////////        REMOVE URL         ////////////////////////
document.addEventListener('DOMContentLoaded', function () {

    // let modal = new bootstrap.Modal(document.getElementById('myModal'))
    let modalElement = document.getElementById('myModal')

    // Remove o caminho "myModal" da url quando o modal é aberto
    modalElement.addEventListener('hidden.bs.modal', function(){
        history.pushState('', document.title, window.location.pathname)
    })  
});


////////////////////////////////////////////////////////////////////////////
////////////////////////    QUANTIDADE DE LIVROS    ////////////////////////
// let spanQuantityBook = document.getElementById('quantityBookCartModal')
// let fieldValueBook = document.getElementById('valueCartModal')
// let quantityBook = 1

// function plus(){
//     quantityBook += 1
//     spanQuantityBook.textContent = quantityBook
//     let btnIconCarts = document.querySelector(".btnIconCarts")
//     const bookValue = btnIconCarts.getAttribute('data-book-value')
//     updateQuantBook(bookValue)
// }
// function minus(){
//     if(quantityBook > 1){
//         quantityBook -= 1
//         spanQuantityBook.textContent = quantityBook
//         let btnIconCarts = document.querySelector(".btnIconCarts")
//         const bookValue = btnIconCarts.getAttribute('data-book-value')
//         updateQuantBook(bookValue)
//     }
    
// }
// function updateQuantBook(bookValue){
//     result = parseFloat(bookValue) * parseInt(spanQuantityBook.textContent)
//     fieldValueBook.textContent = result
//     // return result
// }



////////////////////////////////////////////////////////////////////////////
////////////////////////    RENDERIZA O CARRINHO    ////////////////////////
let fieldTitle = document.getElementById("titleCartModal")
let fieldImg = document.getElementById("imgCartModal") 
let fieldValue = document.getElementById("valueCartModal") 

let fieldQuantityBook = document.getElementById('quantityBookCartModal')
let fieldValueBook = document.getElementById('valueCartModal')
let quantityBook = 1
let currentBookValue = 0


function renderCart(element){

    console.log("Ok")

    let fieldQuantityBook = document.getElementById('quantityBookCartModal')

    quantityBook = 1
    fieldQuantityBook.textContent = quantityBook

    const bookTitle = element.getAttribute('data-book-title')
    const bookImage = element.getAttribute('data-book-image')
    const bookValue = element.getAttribute('data-book-value')
    // console.log(bookValue)

    currentBookValue = parseFloat(bookValue.replace(',','.'))

    fieldImg.src = bookImage
    fieldTitle.textContent = bookTitle    
    fieldValue.textContent = `R$ ${bookValue}` // Valor inicial

    updateQuantBook(bookValue)

    let add = document.getElementById('add')
    add.addEventListener('click', function(){        
        quantityBook += 1
        fieldQuantityBook.textContent = quantityBook
        console.log(quantityBook)
        updateQuantBook(bookValue)
    })

    let decrease = document.getElementById('decrease')
    decrease.addEventListener('click', function(){
        if(quantityBook > 1){
            quantityBook -= 1
            fieldQuantityBook.textContent = quantityBook
            updateQuantBook(bookValue)

            console.log(quantityBook)
        }        
    })

    // function add(){
    //     quantityBook += 1
    //     fieldQuantityBook.textContent = quantityBook
    //     console.log(quantityBook)
    //     updateQuantBook(bookValue)
    // }

    // function decrease(){
    //     if(quantityBook > 1){
    //         quantityBook -= 1
    //         fieldQuantityBook.textContent = quantityBook
    //         updateQuantBook(bookValue)

    //         console.log(quantityBook)
    // }

    function updateQuantBook(bookValue){
        let bookValueValid = parseFloat(bookValue.replace(',','.'))
        // let result = bookValueValid * parseInt(fieldQuantityBook.textContent)
        let result = bookValueValid * quantityBook
        fieldValueBook.textContent = `R$ ${result.toFixed(2).replace('.',',')}`
    }

}

function closeModal(){
    quantityBook = 1
    fieldQuantityBook.textContent = quantityBook
    updateQuantBook(bookValue)
}




// function updateValueBook(bookValue){

// }















// function clearLocalStorage(){
//     localStorage.removeItem('titleBook')
//     localStorage.removeItem('imageBook')
//     localStorage.removeItem('valueBook')

// }






























