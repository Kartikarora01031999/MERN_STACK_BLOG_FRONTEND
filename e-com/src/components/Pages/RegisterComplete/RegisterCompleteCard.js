import React,{useEffect, useState} from "react";
import { toast } from "react-toastify";
import { auth } from "../../../firebase";
import { useHistory } from "react-router-dom";
const RegisterCompleteCart=({history}) =>{

    history=useHistory()
    const [email,setEmail]=useState("");
    const [password, setPassword]=useState("")

    useEffect(()=>{
        setEmail(window.localStorage.getItem('emailForRegistration'));
    },
    [])
    const handleSubmit=async(e)=>{
        e.preventDefault();
        if (!email || !password){
          toast.error("Email & Password cannot be empty")
          return
        }
        if(password.length < 6){
          toast.error("Password Length should be greater than 5")
          return
        }
        try{
          const result = await auth.signInWithEmailLink(
            email,
            window.location.href
          )
          console.log(result)
          if(result.user.emailVerified){
            //remove from local storage
            window.localStorage.removeItem('emailForRegistration')
            //update password 
            let user= auth.currentUser
            await user.updatePassword(password)
            //get auth token
            const authtoken = await user.getIdTokenResult()
            // redux 
            console.log(authtoken.token)
            // redirect
            history.push('/')
          }
        }catch(error){
          console.log(error);
          toast.warning(error.message);

        }
    }
    return(
        <div class="container login col d-flex justify-content-center">
            <div class="card login-card w-8" style={{
                backgroundColor:"#26122e"
            }}>
                <div class="card">
  <div class="card-header justify-content-center login-header text-center">
        Create a new password
  </div>
  
  <div class="card-body login-body">
  <label class="card-text" style={{
      paddingBottom: "10px"
  }}>Welcome to Sanyam Enterprise, Please create password for your account</label>
  <form onSubmit={handleSubmit}>
  <div class="form-group">
    <label>Email address</label>
    <input type="email" class="form-control disabled" aria-describedby="emailHelp" placeholder="Enter email" value={email} />
    <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
  </div>
  <div class="form-group">
    <label>Password</label>
    <input type="password" class="form-control" placeholder="Password" value={password} onChange={e=> setPassword(e.target.value)}/>
  </div>
  <div class="form-check">
    <input type="checkbox" class="form-check-input"/>
    <label class="form-check-label">Check me out</label>
  </div>
  <div class="text-center">
  <button type="submit" class="btn btn-primary ">Create Password</button>
  </div>
</form>
  </div>
  
</div>
            </div>
            
        </div>
    );
}

export default RegisterCompleteCart;