import React from 'react';

const Navbar = (props)=>
{
    return(
        <div className="navbar">
            <div className="cart-icon-container">
                <img src="https://image.flaticon.com/icons/svg/833/833339.svg" alt="cart-icon" className="cart-icon"/>
            <div className="item-count">{props.count}</div>
            </div>
        </div>
    );
}

export default Navbar;