

// let btnIconCart = document.getElementById("btnIconCart")






document.addEventListener('DOMContentLoaded', function () {

    let btnIconCarts = document.querySelectorAll(".btnIconCarts")

    btnIconCarts.forEach((btn) => {
        btn.addEventListener('click', function(){
            renderCart(this)
        })
    })



    function renderCart(btnIconCarts){
        const bookTitle = btnIconCarts.getAttribute('data-book-title')
        const bookImage = btnIconCarts.getAttribute('data-book-image')
        const bookValue = btnIconCarts.getAttribute('data-book-value')

        // let titleBook = JSON.stringify(bookTitle)
        // localStorage.setItem('titleBook',titleBook)
        localStorage.setItem('titleBook',bookTitle)


        // let imageBook = JSON.stringify(bookImage)
        // localStorage.setItem('imageBook',imageBook)
        localStorage.setItem('imageBook',bookImage)
        

        // let valueBook = JSON.stringify(bookValue)
        // localStorage.setItem('valueBook',valueBook)
        localStorage.setItem('valueBook',bookValue)

        console.log("OK") 
        console.log(bookTitle)   
        console.log(bookImage)     
        console.log(bookValue)   
    }


    // let btnIconCarts = document.querySelectorAll(".btnIconCarts");

    // btnIconCarts.forEach((btn) => {
    //     btn.addEventListener('click', function() {
    //         renderCart(this);
    //     });
    // });

    // function renderCart(btnIconCarts) {
    //     const bookTitle = btnIconCarts.getAttribute('data-book-title');
    //     const bookImage = btnIconCarts.getAttribute('data-book-image');
    //     const bookValue = btnIconCarts.getAttribute('data-book-value');

    //     // Armazenando as informações no localStorage
    //     localStorage.setItem('titleBook', bookTitle);
    //     localStorage.setItem('imageBook', bookImage);
    //     localStorage.setItem('valueBook', bookValue);

    //     console.log("OK");
    //     console.log(bookTitle);
    //     console.log(bookImage);
    //     console.log(bookValue);
    // }
});

















// let btnIconCarts = document.querySelectorAll(".btnIconCarts")

// btnIconCarts.forEach((btn) => {
//     btn.addEventListener('click', function(){
//         renderCart(this)
//     })
// })



// function renderCart(btnIconCarts){
//     const bookTitle = btnIconCarts.getAttribute('data-book-title')
//     const bookImage = btnIconCarts.getAttribute('data-book-image')
//     const bookValue = btnIconCarts.getAttribute('data-book-value')

//     // let titleBook = JSON.stringify(bookTitle)
//     // localStorage.setItem('titleBook',titleBook)
//     localStorage.setItem('titleBook',bookTitle)


//     // let imageBook = JSON.stringify(bookImage)
//     // localStorage.setItem('imageBook',imageBook)
//     localStorage.setItem('imageBook',bookImage)
    

//     // let valueBook = JSON.stringify(bookValue)
//     // localStorage.setItem('valueBook',valueBook)
//     localStorage.setItem('valueBook',bookValue)

//     console.log("OK") 
//     console.log(bookTitle)   
//     console.log(bookImage)     
//     console.log(bookValue)   
// }











// btnIconCarts.forEach((btn) => {
//     btn.addEventListener('click', function(event){
//         renderCart(event.target)
//     })
// })

// btnIconCarts.forEach((btn) => {
//     btn.addEventListener('click', function(){
//         renderCart(this)
//     })
// })