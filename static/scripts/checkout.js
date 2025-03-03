

////////////////////////////////////////////////////////////////////////////
////////////////////////    REMOVE URL e CARREGA LOCALSTORAGE    ////////////////////////

// document.addEventListener('DOMContentLoaded', function () {
    
//     let loadSaveCart = JSON.parse(localStorage.getItem("saveCart"));

//     if (loadSaveCart ) {
//         renderCheckoutCart();
//         console.log("ONLOAD LOADSAVECART checkout")
//     }

// });


// function renderCheckoutCart(){   

//     console.log("checkout")


//     let modalNavTitleh6 = document.getElementById("quantityBookCartModalNavTitle")
//     // let statusModalContent = document.getElementById("status-modal-content")
//     let totalValueStatusCart = document.getElementById("totalValueStatusCart")

//     let totalItemsCart = 0
//     let totalValueCart = 0
//     let loadSaveCart = JSON.parse(localStorage.getItem("saveCart"))

//     let checkout = document.getElementById("checkout-content")

//     // iconCart.classList.remove("d-none")     
//     // iconCart.classList.add("d-flex")  
//     // iconCart.style = ""




//     // Se tem dados salvos no LocalStorage
//     if (loadSaveCart){

//         // statusModalContent.innerHTML = ""
//         checkout.innerHTML = ""

//         for( item of loadSaveCart.reverse()){
//             totalItemsCart += item.quantity
//             totalValueCart += item.totalValue
    
//             // console.log("esse é o VALOR TOTAL:", totalValueCart.toFixed(2).replace('.',','))    
//             totalValueStatusCart.textContent = " R$ "+ totalValueCart.toFixed(2).replace('.',',')
                                            

//             checkout.innerHTML += `<div class="d-flex align-items-center" style="height:120px;">
//                                             <img src="${item.img}" class="w-25 img-fluid" style="object-fit:contain; height:100%; width:auto;" >
//                                             <div class="text-center" style="width:100%;">
//                                                 <h6 id="title-book-status" class="mb-4" >${item.title}</h6>
//                                                 <div class="d-flex align-items-center justify-content-center gap-4">
//                                                     <button onclick="removeItem('${item.title}')" class="btn btn-danger small-btn" >Excluir</button>
//                                                     <a class="p-2" onclick="decreaseStatus('${item.title}')" href="#">
//                                                         <i   class="fa-solid fa-minus"></i>
//                                                     </a>                            
//                                                     <span id="quantityStatusCart" >${item.quantity}</span>
//                                                     <a class="p-2" onclick="addStatus('${item.title}')" style="margin-left:5px;" href="#">
//                                                         <i class="fa-solid fa-plus"></i>
//                                                     </a>
//                                                     <span style="margin-left:30px;">R$ ${item.totalValue.toFixed(2).replace('.',',')}</span>
//                                                 </div>                        
//                                             </div>                  
//                                         </div>
//                                         <hr>`


//         }


//         numberCart.textContent = totalItemsCart  // Numero de itens no icone da navbar
//         modalNavTitleh6.textContent = totalItemsCart        

//         numberCart.classList.remove("d-none")
//         numberCart.classList.add("d-flex")        
//         iconCart.style = ""

//         // console.log("esse é o totalValue: ", totalValueCart)
//     }

// }





















    // if(itemShoppingCart.length === 0){
    //     totalValueStatusCart.textContent = "R$ 0,00"
    //     // numberCart.classList.add("d-none")
    //     // numberCart.classList.remove("d-flex")
    //     iconCart.style = "margin-right:10px"   
    //     console.log("TESTE itemShoppingCart")
    //     // statusModalContent.innerHTML = "Você não possui itens adicionados ao carrinho"
    //     // iconCart.classList.add("d-none")
    // }