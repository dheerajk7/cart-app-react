import React from 'react';
import CartItem from './CartItem';

class Cart extends React.Component      //creating react component
{
    render()
    {
        return(
            <div className="cart-container">
                <h1>Cart</h1>
                <CartItem/>
                <CartItem/>
                <CartItem/>
                <CartItem/>
            </div>
        );
    }
}

export default Cart;