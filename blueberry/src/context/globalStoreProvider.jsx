import StoreContext from "./storeContext";
import { useState } from "react";

const GlobalStoreProvider = (props) => {
const [cart, setCart] = useState([]);
const [user, setUser] = useState({ name: 'admin", id: 43'});

const addProdToCart = (prod) => {
    console.log("Global add prod", prod);

    let copy = [...cart];
    copy.push(prod);
    setCart(copy);
};

const removeProdFromCart = () => {
    console.log("Global remove prod");
};

  return ( 
    <StoreContext.Provider value={{
        cart: cart,
        user: user,
        addProdToCart: addProdToCart,
        removeProdFromCart: removeProdFromCart,
    }}>
      {props.children}
    </StoreContext.Provider>
  )
};

export default GlobalStoreProvider;
