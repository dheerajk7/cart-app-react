import React from 'react';

class CartItem extends React.Component      //creating react component
{

    tesingSetStateWithPromise()
    {
        let promise = new Promise((resolve,reject) =>
        {
            setTimeout(()=>
            {
                resolve();
                console.log('resolved');
            },500);
        });

        promise.then(() =>
        {
            //in these case call are synchronous and each case will add one to quantity
            //cart is also rendered 3 times here
            this.setState({qty:this.state.qty + 1});
            this.setState({qty:this.state.qty + 1});
            this.setState({qty:this.state.qty + 1});
            console.log(this.state.qty);
        });
    }

    increaseQuantity()
    {
        //to increase quantity we need to call set state function 
        //there are two ways to call function one using object another using call back function
        //list is rendered once in these case
        //using object
        // this.setState({
        //     qty : this.state.qty + 1,       //these way 
        // });

        // //if we do it two three times then only last changes will be applied because of shallow mergin happens and only one attribute applied which is last one
        // this.setState(
        //     {
        //         qty : this.state.qty + 2,
        //     }
        // );

        //another way is by using call back fuction in call back we received previous state
        //list is rendered only once in these case
        // this.setState((prevState) => {
        //     return ({
        //         qty : prevState.qty + 1,
        //     });
        // });
        // //if we use this thing two three then everytime changes apply because these call back are passed to job queue and each got executed
        // this.setState((prevState) =>
        // {
        //     return ({
        //         qty:prevState.qty + 2,
        //     });
        // })

        // //if we print state here then old one is printed because these function are in job queue and executed later on so for that we will pass one more call back in this state
        // console.log(this.state.qty);
        //now these function are in job queue one after other
        this.setState((prevState) =>
        {
            return ({
                qty:prevState.qty + 1,
            });
        },() => {
            console.log(this.state.qty);
        })

        // this.tesingSetStateWithPromise()
    }

    decreaseQuantity()
    {
        if(this.state.qty === 0)
        {
            return;
        }
        this.setState((prevState) =>
        {
            return ({
                qty:prevState.qty - 1,
            });
        },() => {
            console.log(this.state.qty);
        })
    }

    deleteItem = () =>
    {
        console.log('Delete');
    }
    render()
    {
        const {title,price,qty,img} = this.props.product;
        return(
            <div className="cart-item">
                <div className="left-block">
                    <img className='cart-item-image' src={img} alt = "not found"/>
                </div>
                <div className="right-block">
                    <div style={style.title}>{title}</div>
                    <div style={style.price}>RS {price}</div>
                    <div style={style.price}>Quantity : {qty}</div>
                    <div className="cart-item-actions">
                        <img 
                            alt="increase" 
                            className="action-icons" 
                            src="https://image.flaticon.com/icons/svg/1828/1828817.svg"
                            onClick={()=>{this.props.increaseQuantity(this.props.product);}}/>
                        <img 
                            alt="decrease" 
                            className="action-icons" 
                            src="https://image.flaticon.com/icons/svg/929/929430.svg"
                            onClick={()=>{this.props.decreaseQuantity(this.props.product);}}/>
                        <img 
                            alt="delete" 
                            className="action-icons" 
                            src="https://image.flaticon.com/icons/svg/833/833520.svg"
                            onClick={()=>{this.props.deleteItem(this.props.product);}}/>
                    </div>
                </div>
            </div>
        );
    }
}

// we can apply styles these way as well using style object inside js
const style = 
{
    title:{
        color:'navy',
        fontSize:25,
        padding:5,
    },
    price:{
        color:'grey',
        fontSize:15,
        padding:5,
    }
}

export default CartItem;