



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
    let h6QuantityBookTitle = document.getElementById('quantityBookCartModalTitle')
    let spanQuantityBook = document.getElementById('quantityBookCartModal')
    quantityBook += 1
    spanQuantityBook.textContent = quantityBook
    h6QuantityBookTitle.textContent = quantityBook
    updateQuantBook(currentValue)

    if( !modal.classList.contains('show') ){     
        console.log("teste close if")
        closeModal()
        // teste()
    }
}

function decrease(){
    let h6QuantityBookTitle = document.getElementById('quantityBookCartModalTitle')
    let spanQuantityBook = document.getElementById('quantityBookCartModal')
    if(quantityBook > 1){
        quantityBook -= 1
        spanQuantityBook.textContent = quantityBook
        h6QuantityBookTitle.textContent = quantityBook
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

let h6QuantityBookTitle = document.getElementById('quantityBookCartModalTitle')
let fieldQuantityBook = document.getElementById('quantityBookCartModal')
let fieldValueBook = document.getElementById('valueCartModal')


function renderCart(element){

    let fieldQuantityBook = document.getElementById('quantityBookCartModal')
    let h6QuantityBookTitle = document.getElementById('quantityBookCartModalTitle')

    // Atribuindo valor ao campo de quantidade ( que sempre inicia vazio )
    if (fieldQuantityBook.textContent == ""){
        fieldQuantityBook.textContent = 1
        h6QuantityBookTitle.textContent = 1
        console.log("teste AAA")
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
    // console.log(fieldTitle.textContent)
    // console.log(fieldImg.src)
    // console.log(fieldValue.textContent)    
    // console.log(currentValue) // valor unitario em string    
    // console.log(parseFloat(currentValue.replace(',','.'))) // valor unitario em numero    
    // console.log(result) // valor total em numero

    // Numero de itens do carrinho
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
    // console.log(itemShoppingCart)

    numberCart.classList.remove("d-none")
    numberCart.classList.add("d-flex")
    renderStatusCart()
    
    iconCart.style = ""
}



//////////////////////////////////////////////////////////////////////////////////////
////////////////////////    RENDERIZA O STATUS DO CARRINHO    ////////////////////////

function renderStatusCart(){   

    console.log(itemShoppingCart)

    let modalNavTitleh6 = document.getElementById("quantityBookCartModalNavTitle")
    let statusModalContent = document.getElementById("status-modal-content")
    let totalValueStatusCart = document.getElementById("totalValueStatusCart")

    let totalItemsCart = 0
    let totalValueCart = 0
    statusModalContent.innerHTML = ""

    let reversedItems = itemShoppingCart.reverse()

    // Se não tiver itens o valor é 0
    if(itemShoppingCart.length === 0){
        totalValueStatusCart.textContent = "R$ 0,00"
        numberCart.classList.add("d-none")
        numberCart.classList.remove("d-flex")
        iconCart.style = "margin-right:10px"    
    }

    for( item of reversedItems){
        totalItemsCart += item.quantity
        totalValueCart += item.totalValue

        console.log("esse é o VALOR TOTAL:", totalValueCart.toFixed(2).replace('.',','))


        totalValueStatusCart.textContent = " R$ "+ totalValueCart.toFixed(2).replace('.',',')
        statusModalContent.innerHTML += `<div class="d-flex align-items-center" style="height:140px;">
                                            <img src="${item.img}" class="w-25 img-fluid" style="object-fit:contain; height:100%; width:auto;" >
                                            <div class="text-center" style="width:100%;">
                                                <h6 id="title-book-status" class="mb-4" >${item.title}</h6>
                                                <div class="d-flex align-items-center justify-content-center gap-4">
                                                    <button onclick="removeItem('${item.title}')" class="btn btn-danger small-btn" >Excluir</button>
                                                    <a class="p-2" onclick="decreaseStatus('${item.title}')" href="#">
                                                        <i   class="fa-solid fa-minus"></i>
                                                    </a>                            
                                                    <span id="quantityStatusCart" >${item.quantity}</span>
                                                    <a class="p-2" onclick="addStatus('${item.title}')" style="margin-left:5px;" href="#">
                                                        <i class="fa-solid fa-plus"></i>
                                                    </a>
                                                    <span style="margin-left:30px;">R$ ${item.totalValue.toFixed(2).replace('.',',')}</span>
                                                </div>                        
                                            </div>                  
                                        </div>
                                        <hr>`
    }
    numberCart.textContent = totalItemsCart  // Numero de itens no icone da navbar

    modalNavTitleh6.textContent = totalItemsCart
    console.log("esse é o totalValue: ", totalValueCart)
}


function addStatus(title){
    let reversedItems = itemShoppingCart.reverse()
    for (item of reversedItems){
        if(item.title == title){
            item.quantity += 1
            item.totalValue = item.quantity * item.valueUnitBook
            break
        }
    }
    renderStatusCart()
}

function decreaseStatus(title){
    let reversedItems = itemShoppingCart.reverse()
    for (item of reversedItems){
        if(item.title == title){
            if(item.quantity > 1){
                item.quantity -= 1
                item.totalValue = item.quantity * item.valueUnitBook
            }            
            break
        }
    }
    renderStatusCart()
}


function removeItem(title){
    let reversedItems = itemShoppingCart.reverse()

    // Retorna o item encontrado com o título igual ao valor da variável title. Nesse caso, o findIndex() retorna o índice do item encontrado no array.
    let indexToRemove = reversedItems.findIndex(item => item.title === title) 

    if(indexToRemove !== -1){ // Se o item for encontrado (ou seja, se indexToRemove for diferente de -1)
        reversedItems.splice(indexToRemove,1)
    }

    renderStatusCart()
}



////////////////////////////////////////////////////////////////////////
////////////////////////    LIMPA O CARRINHO    ////////////////////////

function clearCart(){
    itemShoppingCart = []
    renderStatusCart()
    numberCart.classList.remove("d-flex")
    numberCart.classList.add("d-none")
    iconCart.style = "margin-right:10px"    
    totalValueStatusCart.textContent = "R$ 0,00"
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
    h6QuantityBookTitle.textContent = quantityBook
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






























