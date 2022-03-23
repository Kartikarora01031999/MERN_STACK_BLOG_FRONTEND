
import React,{useState} from "react";
import { toast} from "react-toastify";
import { auth } from "../../../firebase";

const SignupCart=() =>{
    const [email,setEmail]=useState("");
    const handleSubmit=async(e)=>{
        e.preventDefault();
        const config={
            url:"http://localhost:3000/register-complete",
            handleCodeInApp: true
        }
        await auth.sendSignInLinkToEmail(email,config)
        toast.success('Email Sent to complete registration please verify ')
        window.localStorage.setItem('emailForRegistration', email)
        setEmail("")
    }
    return (
        
        <div class="container login col d-flex justify-content-center">
            <div class="card login-card w-8" style={{
                backgroundColor:"#26122e"
            }}>
                <div class="card">
  <div class="card-header justify-content-center login-header text-center">
      Create a New Account
  </div>
  
  <div class="card-body login-body">
  <label class="card-text" style={{
      paddingBottom: "10px"
  }}>Welcome to Sanyam Enterprise, Please create a new account</label>
  <form onSubmit={handleSubmit}>
  <div class="form-group">
    <label>Email address</label>
    <input type="email" class="form-control" aria-describedby="emailHelp" placeholder="Enter email" value={email} onChange={e=> setEmail(e.target.value)}/>
    <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
  </div>
  <div class="text-center">
        <button type="submit" class="btn btn-primary ">Sign Up with Email</button>
  </div>
  <br></br>
  <div class="row">
      <div class=" text-center  col-sm-12 p-10" style={{
      paddingBottom: "10px"
  }}>
           <button type="button" class="btn btn-primary ">Sign Up with Google</button>
      </div>

  </div>
</form>
  </div>
  
</div>
            </div>
            
        </div>);

}

export default SignupCart;