



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
let result


function add(){
    let spanQuantityBook = document.getElementById('quantityBookCartModal')
    quantityBook += 1
    spanQuantityBook.textContent = quantityBook
    updateQuantBook(currentValue)

    if( !modal.classList.contains('show') ){     
        console.log("teste close if")
        closeModal()
        // teste()
    }
}

function decrease(){
    let spanQuantityBook = document.getElementById('quantityBookCartModal')
    if(quantityBook > 1){
        quantityBook -= 1
        spanQuantityBook.textContent = quantityBook
        updateQuantBook(currentValue)
    }

    if( !modal.classList.contains('show') ){     
        console.log("teste close if")
        closeModal()
    }
}



function updateQuantBook(bookValue){
    let bookValueValid = parseFloat(bookValue.replace(',','.'))

    console.log("valor livro: ",bookValueValid)
    console.log("quantidade livro: ",quantityBook)

    // let result = bookValueValid * parseInt(fieldQuantityBook.textContent)
    result = bookValueValid * quantityBook
    // result = bookValueValid * quantityBook
    fieldValueBook.textContent = `R$ ${result.toFixed(2).replace('.',',')}`
    console.log("result: ",result)

}




////////////////////////////////////////////////////////////////////////////
////////////////////////    RENDERIZA O CARRINHO    ////////////////////////

let fieldTitle = document.getElementById("titleCartModal")
let fieldImg = document.getElementById("imgCartModal") 
let fieldValue = document.getElementById("valueCartModal") 

let fieldQuantityBook = document.getElementById('quantityBookCartModal')
let fieldValueBook = document.getElementById('valueCartModal')



function renderCart(element){

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

    fieldImg.src = bookImage
    fieldTitle.textContent = bookTitle    
    fieldValue.textContent = `R$ ${bookValue}` // Valor inicial

    // TESTE
    // updateQuantBook(currentValue)
    updateQuantBook(bookValue)    

    let modal = document.getElementById('myModal')

    // Zera o contador ao abrir o modal quando não tem a classe show
    if( !modal.classList.contains('show') ){     
        console.log("teste close if")
        closeModal()
    }
}



////////////////////////////////////////////////////////////////////////////
////////////////////////    ADICIONA AO CARRINHO    ////////////////////////

let itemShoppingCart = []
let numberCart = document.getElementById("numberCart")
let iconCart = document.getElementById("iconCart")

function addBookCart(){
    console.log(fieldTitle.textContent)
    console.log(fieldImg.src)
    console.log(fieldValue.textContent)

    // valor unitario em string
    console.log(currentValue)

    // valor unitario em numero
    console.log(parseFloat(currentValue.replace(',','.')))

    // valor total em numero
    console.log(result)

    let totalItems = Math.round(result / parseFloat(currentValue.replace(',','.')))
    console.log(totalItems)

    itemShoppingCart.push({
        title: fieldTitle.textContent,
        img: fieldImg.src,
        quantity: totalItems,
        valueString: fieldValue.textContent,
        valueUnitBook: parseFloat(currentValue),
        totalValue: result,
    })

    console.log(itemShoppingCart)

    numberCart.classList.remove("d-none")
    numberCart.classList.add("d-flex")
    // numberCart.textContent = totalItems
    renderIconCart()
    
    iconCart.style = ""
}


function renderIconCart(){
    let totalItems = 0
    for( item of itemShoppingCart){
        totalItems += item.quantity
    }
    numberCart.textContent = totalItems
}


function clearCart(){
    itemShoppingCart = []
    renderIconCart()
    numberCart.classList.remove("d-flex")
    numberCart.classList.add("d-none")
    iconCart.style = "margin-right:10px"    
}




////////////////////////////////////////////////////////////////////////////
////////////////////////    FECHA O CARRINHO    ////////////////////////


// Verifica se a classe show foi removida para voltar ao valor inicial do livro
let modal = document.getElementById('myModal')

const observer = new MutationObserver((mutationList) => {
    for( let mutation of mutationList){
        if(mutation.type === 'attributes' && mutation.attributeName === 'class'){
            if( !modal.classList.contains('show') ){     
                console.log("teste close if MUTATION OBSERVER ")
                closeModal()
            }
        }
    }
})

observer.observe(modal, {
    attributes: true
})


// Reseta configurações ao fechar o carrinho
function closeModal(){
    quantityBook = 1
    fieldQuantityBook.textContent = quantityBook
    updateQuantBook(quantityBook)
    console.log("Teste Função close modal")
}
































// function btnExcluir(){
//     modal.classList.remove("show")
//     modal.attributes.removeNamedItem("role")    
//     modal.attributes.removeNamedItem("aria-modal") 
//     modal.setAttribute('aria-hidden', 'true');  
//     modal.style.display = "none"

//     document.body.classList.remove('modal-open')

//     // remove tela escura e opaca
//     let backdrop = document.querySelector('.modal-backdrop')
//     if (backdrop){
//         backdrop.remove()
//     }

//     document.querySelector("nav").style.removeProperty("padding-right")
//     document.querySelector("nav").style.removeProperty("margin-right")

//     document.body.style.removeProperty("overflow")
//     document.body.style.removeProperty("padding-right")

//     modal.addEventListener('hidden.bs.modal', function(){
//         history.pushState('', document.title, window.location.pathname)
//     })  
    
// }



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






























