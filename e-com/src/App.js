import React, { useEffect } from "react";
import {
  Switch,
  Route
} from 'react-router-dom'
import Home from "./components/Pages/Home/Home";
import 'font-awesome/css/font-awesome.min.css';
import Login from "./components/Pages/Login/Login";
import Signup from "./components/Pages/SignUp/Signup";
import { ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css'
import RegisterComplete from "./components/Pages/RegisterComplete/RegisterComplete";
import { auth } from "./firebase";
import { useDispatch } from "react-redux";
import { useHistory } from 'react-router-dom'
function App() {
  const dispatch =useDispatch()
  const history= useHistory()
  useEffect(()=>{
    const unsubscribe= auth.onAuthStateChanged(async(user)=>{
      if(user){
        const authtoken = await user.getIdTokenResult()
        dispatch({
          type:"LOGGED_IN_USER",
          payload:{
            email: user.email,
            token: authtoken.token
          }
        })
      }
    })
  },[])
  return (
    <>
    <ToastContainer/>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/login" component={Login} />
      <Route exact path="/signup" component={Signup} />
      <Route exact path="/register-complete" component={RegisterComplete} />
    </Switch>
    </>
  );
}

export default App;
