import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as firebase from 'firebase';

const firebaseConfig = {
  apiKey: "AIzaSyDBz3R9SfCsKclNUshAVUd4ew_VOuPxVb4",
  authDomain: "cart-adf35.firebaseapp.com",
  databaseURL: "https://cart-adf35.firebaseio.com",
  projectId: "cart-adf35",
  storageBucket: "cart-adf35.appspot.com",
  messagingSenderId: "543265478563",
  appId: "1:543265478563:web:e5795efe744c842752ec16"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

