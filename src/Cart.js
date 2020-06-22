import React from 'react';
import CartItem from './CartItem';

class Cart extends React.Component      //creating react component
{
    constructor()
    {
        super();
        this.state= {
            products:
            [   
                {
                    title:'Mobile Phone',
                    price:999,
                    qty:1,
                    id:1,
                },
                {
                    title:'Watch',
                    price:121,
                    qty:1,
                    id:2,
                },
                {
                    title:'Laptop',
                    price:10999,
                    qty:1,
                    id:3,
                },
            ]
        }
    }

    handleIncreaseQuantity = (product)=>
    {
        console.log(product);
        let {products} = this.state;
        let index = -1;
        for(let i=0;i<products.length;i++)
        {
            if(product.id === products[i].id)
            {
                index = i;
            }
        }
        products[index].qty = products[index].qty + 1;
        this.setState({
            products : products,
        });
    }

    handleDecreaseQuantity = (product) =>
    {
        if(product.qty === 0)
        {
            return;
        }
        let {products} = this.state;  //way of just getting product in another variable products
        let index = -1;
        for(let i=0;i<products.length;i++)
        {
            if(product.id === products[i].id)
            {
                index = i;
            }
        }
        products[index].qty = products[index].qty - 1;
        this.setState({
            products : products,
        });
    }

    delete = (product) =>
    {
        let products = this.state.products;
        let index = products.indexOf(product);
        products.splice(index,1);
        this.setState({
            products:products
        });
    }

    render()
    {
        const {products} = this.state;
        return(
            <div className="cart-container">
                <h1>Cart</h1>
                {products.map((product) =>  //we can pass any number of argument like product and key
                {
                    return <CartItem 
                    product={product} 
                    key={product.id}
                    increaseQuantity = {this.handleIncreaseQuantity}
                    decreaseQuantity = {this.handleDecreaseQuantity}
                    deleteItem = {this.delete}
                    /> 
                })}
                
            </div>
        );
    }
}

export default Cart;