import './cart.css';
import { useContext } from 'react';
import StoreContext from "../context/storeContext";


const Cart = () => {
    let cart = useContext(StoreContext).cart;

    return (
       <div className="cart">
           <h6>These {cart.length} items are in your cart</h6>
           <h3>Are you ready to place your order?</h3>
           <hr />

           <ul>
               {cart.map(prod => <li key={prod._id}>{prod.title} - ${prod.price}</li>)}
           </ul>
       </div>
    );
};


export default Cart