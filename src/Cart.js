import React from 'react';
import CartItem from './CartItem';

const Cart  = (props) => {

    const {products} = props;
    return(
        <div className="cart-container">
            <h1>Cart</h1>
            {products.map((product) =>  //we can pass any number of argument like product and key
            {
                return <CartItem 
                product={product} 
                key={product.id}
                increaseQuantity = {props.onIncreaseQuantity}
                decreaseQuantity = {props.onDecreaseQuantity}
                deleteItem = {props.onDelete}
                /> 
            })}
           <div className='total-price'>RS {props.total}</div>
        </div>
    );
}

export default Cart;