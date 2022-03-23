// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import firebase from "firebase/compat/app";
import "firebase/compat/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC_RapvUwgBau5tcy9jwg7sToWMOFD_mS4",
  authDomain: "sanyamenterprise-7734e.firebaseapp.com",
  databaseURL: "https://sanyamenterprise-7734e-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "sanyamenterprise-7734e",
  storageBucket: "sanyamenterprise-7734e.appspot.com",
  messagingSenderId: "426784483806",
  appId: "1:426784483806:web:eea8cf65a99e9e9b98554f",
  measurementId: "G-71N0N6XZR3"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
export const auth = firebase.auth();
export const googleAuthProvider = new firebase.auth.GoogleAuthProvider()