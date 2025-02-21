



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

let quantityBook = 1
let currentValue = 0
// console.log("teste",currentValue)

// function teste(){
//     console.log("Esse é o teste ",currentValue)
// }


function add(){
    let spanQuantityBook = document.getElementById('quantityBookCartModal')
    quantityBook += 1
    spanQuantityBook.textContent = quantityBook
    // let btnIconCarts = document.querySelector(".btnIconCarts")
    // const bookValue = btnIconCarts.getAttribute('data-book-value')
    updateQuantBook(currentValue)
}

function decrease(){
    let spanQuantityBook = document.getElementById('quantityBookCartModal')
    if(quantityBook > 1){
        quantityBook -= 1
        spanQuantityBook.textContent = quantityBook
        // let btnIconCarts = document.querySelector(".btnIconCarts")
        // const bookValue = btnIconCarts.getAttribute('data-book-value')
        updateQuantBook(currentValue)
    }
}



// let quantityBook = 1

// function add(){
//     let spanQuantityBook = document.getElementById('quantityBookCartModal')
//     quantityBook += 1
//     spanQuantityBook.textContent = quantityBook
//     let btnIconCarts = document.querySelector(".btnIconCarts")
//     const bookValue = btnIconCarts.getAttribute('data-book-value')
//     updateQuantBook(bookValue)
// }

// function decrease(){
//     let spanQuantityBook = document.getElementById('quantityBookCartModal')
//     if(quantityBook > 1){
//         quantityBook -= 1
//         spanQuantityBook.textContent = quantityBook
//         let btnIconCarts = document.querySelector(".btnIconCarts")
//         const bookValue = btnIconCarts.getAttribute('data-book-value')
//         updateQuantBook(bookValue)
//     }
// }

function updateQuantBook(bookValue){
    let bookValueValid = parseFloat(bookValue.replace(',','.'))

    console.log(bookValueValid)

    // let result = bookValueValid * parseInt(fieldQuantityBook.textContent)
    let result = bookValueValid * quantityBook
    fieldValueBook.textContent = `R$ ${result.toFixed(2).replace('.',',')}`
    console.log(result)

}




////////////////////////////////////////////////////////////////////////////
////////////////////////    RENDERIZA O CARRINHO    ////////////////////////

let fieldTitle = document.getElementById("titleCartModal")
let fieldImg = document.getElementById("imgCartModal") 
let fieldValue = document.getElementById("valueCartModal") 

let fieldQuantityBook = document.getElementById('quantityBookCartModal')
let fieldValueBook = document.getElementById('valueCartModal')



function renderCart(element){

    console.log("Ok rendercart")

    let fieldQuantityBook = document.getElementById('quantityBookCartModal')

    // Atribuindo valor ao campo de quantidade ( que sempre inicia vazio )
    if (fieldQuantityBook.textContent == ""){
        fieldQuantityBook.textContent = 1
    }

    let quantityBook = fieldQuantityBook.textContent
    console.log(quantityBook)    

    const bookTitle = element.getAttribute('data-book-title')
    const bookImage = element.getAttribute('data-book-image')
    const bookValue = element.getAttribute('data-book-value')

    currentValue = bookValue

    console.log(bookValue)

    fieldImg.src = bookImage
    fieldTitle.textContent = bookTitle    
    fieldValue.textContent = `R$ ${bookValue}` // Valor inicial

    // TESTE
    // updateQuantBook(currentValue)
    updateQuantBook(bookValue)    

    let modal = document.getElementById('myModal')

    // Zera o contador ao abrir o modal
    if( !modal.classList.contains('show') ){     
        // console.log("teste close if")
        closeModal()
    }
}






////////////////////////////////////////////////////////////////////////////
////////////////////////    FECHA O CARRINHO    ////////////////////////

function closeModal(){
    quantityBook = 1
    fieldQuantityBook.textContent = quantityBook
    updateQuantBook(bookValue)
    // console.log("teste F close modal")
}



































    // let add = document.getElementById('add')
    // add.addEventListener('click', function(){        
    //     quantityBook += 1
    //     fieldQuantityBook.textContent = quantityBook
    //     console.log(quantityBook)
    //     updateQuantBook(bookValue)
    // })

    // let decrease = document.getElementById('decrease')
    // decrease.addEventListener('click', function(){
    //     if(quantityBook > 1){
    //         quantityBook -= 1
    //         fieldQuantityBook.textContent = quantityBook
    //         updateQuantBook(bookValue)

    //         console.log(quantityBook)
    //     }        
    // })




// function clearLocalStorage(){
//     localStorage.removeItem('titleBook')
//     localStorage.removeItem('imageBook')
//     localStorage.removeItem('valueBook')

// }






























