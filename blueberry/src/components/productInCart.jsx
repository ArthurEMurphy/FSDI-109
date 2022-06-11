
import "./productInCart.css";
import { useContext } from 'react';
import StoreContext from "../context/storeContext";

const ProductInCart = (props) => {
    const removeProdFromCart = useContext(StoreContext).removeProdFromCart;

    const getTotal = () => {
        let total = props.data.price * props.data.quantity;
        return total.toFixed(2);
    };

    const deleteProd = () => {
        removeProdFromCart(props.data._id);
    };

    return (
        <div className="product-cart">
            <img className="productImg" src={"/img/" + props.data.image} alt="product" />

            <div className="description">
                <h4>{props.data.title}</h4>
                <p>{props.data.category}</p>
            </div>

            <label>${props.data.price}</label>
            <label>{props.data.quantity}</label>
            <label>${getTotal()}</label>

            <button onClick={deleteProd} className="btn btn-sm btn-danger">Remove</button>
        </div>
    );
};

export default ProductInCart;