import React from 'react';
import Cart from './Cart';
import Navbar from './Navbar';
import * as firebase from 'firebase';

class App extends React.Component {

  constructor()
    {
        super();
        this.state= {
            products:
            [   
            //     {
            //         title:'Mobile Phone',
            //         price:100,
            //         qty:1,
            //         id:1,
            //         img:'https://images.unsplash.com/photo-1580910051074-3eb694886505?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=701&q=80',
            //     },
            //     {
            //         title:'Watch',
            //         price:200,
            //         qty:1,
            //         id:2,
            //         img:'https://images.unsplash.com/photo-1524805444758-089113d48a6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80'
            //     },
            //     {
            //         title:'Laptop',
            //         price:300,
            //         qty:1,
            //         id:3,
            //         img:'https://images.unsplash.com/photo-1548611635-b6e7827d7d4a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80'
            //     },
            ],
            loading:true,
        }
    }

    componentDidMount()
    {
    //      if we use these way using get method we values are not updated in real time as we updated in db because we have not added any listener so for getting that real time update we will onSnapshot method instead of get
    //     firebase
    //     .firestore()
    //     .collection('products')         //mention collection
    //     .get()                          //to get document
    //     .then((snapshot) =>
    //     {
    //         // snapshot.docs.map((doc) =>
    //         // {
    //         //     console.log(doc.data());            //printing docs
    //         // });

    //         //setting product with these docs
    //         const products = snapshot.docs.map((doc) =>
    //         {
    //             let data = doc.data();
    //             data['id'] = doc.id;
    //             return data;
    //         });

    //         this.setState({
    //             products,
    //             loading:false,
    //         });
    //     })

        firebase
        .firestore()
        .collection('products')
        .onSnapshot((snapshot) =>
        {
            snapshot.docs.map((doc) =>
            {
                console.log(doc.data());
                return '';
            });

            const products = snapshot.docs.map((doc) => 
            {
                let data = doc.data();
                data['id'] = doc.id;
                return data;
            });

            this.setState(
                {
                    products:products,
                    loading:false,
                }
            );
        });

    }

    handleIncreaseQuantity = (product)=>
    {
        console.log(product);
        //using when incresing product count in products array not in db
        // let {products} = this.state;
        // let index = -1;
        // for(let i=0;i<products.length;i++)
        // {
        //     if(product.id === products[i].id)
        //     {
        //         index = i;
        //     }
        // }
        // products[index].qty = products[index].qty + 1;
        // this.setState({
        //     products : products,
        // });

        //finding doc reference using product id
        const docRef = firebase
        .firestore()
        .collection('products')
        .doc(product.id);
        
        //updating in db
        docRef.update(
            {
                qty:product.qty + 1,
            }
        ).then( () => {
            console.log('Product Quantity Increased Successfully');
        }).catch((error) => 
        {
            console.log('Error ',error);
        });
    }

    handleDecreaseQuantity = (product) =>
    {
        if(product.qty === 0)
        {
            return;
        }
        //using when using product array not db
        // let {products} = this.state;  //way of just getting product in another variable products
        // let index = -1;
        // for(let i=0;i<products.length;i++)
        // {
        //     if(product.id === products[i].id)
        //     {
        //         index = i;
        //     }
        // }
        // products[index].qty = products[index].qty - 1;
        // this.setState({
        //     products : products,
        // });

        //updating in db
        const docRef = firebase
        .firestore()
        .collection('products')
        .doc(product.id);

        docRef.update({
            qty : product.qty - 1,
        })
        .then(() => {
            console.log('Product Quantity Decreased Successfully');
        });
    }

    delete = (product) =>
    {
        //deleting when using product array not db
        // let products = this.state.products;
        // let index = products.indexOf(product);
        // products.splice(index,1);
        // this.setState({
        //     products:products,
        // });

        //deleting when usnig db
        const docRef = firebase
        .firestore()
        .collection('products')
        .doc(product.id);

        docRef.delete()
        .then(() => 
        {
            console.log('Product deleted successfully')
        })
        .catch((error) => {
            console.log('Error in deleting product',error);
        });
    }

    getProductCount = () => 
    {
      const {products} = this.state;
      let count = 0;
      products.forEach((product) =>
      {
        count += product.qty;
      });

      return count;
    }

    getTotalPrice = () =>
    {
      const {products} = this.state;
      let totalPrice = 0;
      products.forEach((product) =>
      {
        totalPrice += product.price * product.qty;
      });
      return totalPrice;
    }

    addProduct = () =>
    {
        firebase
        .firestore()
        .collection('products')
        .add({
            title:"Washing Machine",
            price:100,
            qty:1,
            img:'https://images.unsplash.com/photo-1551761429-8232f9f5955c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=909&q=80'
        })
        .then((docRef) =>
        {
            console.log('New Product Added Succesfully',docRef);
        })
    }

  render()
  {
    const {products,loading} = this.state;
    return (
      <div className="App">
          <Navbar count = {this.getProductCount()}/>
          <button onClick={this.addProduct} style= {{fontSize:20, padding:20, background:'cyan',margin:10}}>Add Product</button>
          {loading && <h1>Product Loading...</h1>}
          <Cart products={products}
          onIncreaseQuantity = {this.handleIncreaseQuantity}
          onDecreaseQuantity = {this.handleDecreaseQuantity}
          onDelete = {this.delete}
          total = {this.getTotalPrice()}
          />
      </div>
    );
  }
}

export default App;
