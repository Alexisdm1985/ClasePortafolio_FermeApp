// const fragment = document.createDocumentFragment();

// document.addEventListener("click", e => {

//     if (e.target.matches('.card .card-btn') || e.target.matches('.addBtn')){
//         console.log('Add new item to cart')
//         addItemCart(e);
//     } else if (e.target.matches('.removeBtn')){
//         delItemCart(e);
//     };
// });

// const addItemCart = (e) => {
    
//     const item = {
//         name: e.target.dataset.id,
//         price: parseInt(e.target.dataset.price),
//         amount: 1,
//     }

//     const exist = cart.findIndex( (fItem) => fItem.name === item.name)
    
//     if(exist === -1) {
//             cart.push(item);
//     }else {
//             cart[exist].amount++;
//         }
    
//     printCart();
// };  

// const delItemCart = (e) => {
//     const index = cart.findIndex( (item) => item.name === e.target.dataset.id)
    
//     cart[index].amount--;
    
//     if (cart[index].amount === 0){
//         cart.splice(index, 1);
//     }
//     printCart();
// };

// const printCart = () => {
    
//     list.textContent = " "; 

//     cart.forEach( (item) => {
//         const cloneTemp = template.content.cloneNode(true);
        
//         cloneTemp.querySelector('.itemAmount').textContent = item.amount;
//         cloneTemp.querySelector('.itemName').textContent = item.name;
//         cloneTemp.querySelector('.totalSection .totalPrice span').textContent= 
//                     item.amount * item.price

//         //Add id and price to add/remove bttns
//         cloneTemp.querySelector('.addBtn').dataset.id = item.name;
//         cloneTemp.querySelector('.addBtn').dataset.price = item.price
//         cloneTemp.querySelector('.removeBtn').dataset.id = item.name;
//         cloneTemp.querySelector('.removeBtn').dataset.price = item.price;

//         // suma += total;
//         fragment.appendChild(cloneTemp);
//     } );
    
//     const total = cart.reduce( (acc, current) => acc + current.amount * current.price, 0)
    
//     if (total !== 0) {
//         const cloneTempF = templateFooter.content.cloneNode(true);
//         cloneTempF.querySelector('.total span').textContent = total;
//         fragment.appendChild(cloneTempF);
//     }
//     list.appendChild(fragment);
//     // console.log(cart)
// };

