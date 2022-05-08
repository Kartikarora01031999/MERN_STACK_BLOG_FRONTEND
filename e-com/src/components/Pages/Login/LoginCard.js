import React,{useState,useEffect} from "react";
import { useDispatch,useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { toast } from "react-toastify";
import { auth } from "../../../firebase";
import { createUpdateUser } from "../../../Functions/Auth";
const LoginCart=() =>{
    let dispatch= useDispatch()
    let history=useHistory()
    const [email,setEmail]=useState("");
    const [password, setPassword]=useState("")
    let {user}=useSelector((state)=>((state)))
    useEffect(() => {
      if (user && user.token){history.push("/");}
    }, [user, history])
    const handleSubmit= async(e)=>{
      e.preventDefault();
        try{
        console.log(email, password)
        const result= await  auth.signInWithEmailAndPassword(email,password);
        console.log(result)
        const {user} =result
        const authtoken= await user.getIdTokenResult()
        console.log(authtoken.token)
        createUpdateUser(authtoken.token).then((res)=> {
          console.log(res.data)
          dispatch({
            type:"LOGGED_IN_USER",
            payload:{
              email: res.data.email,
              token: authtoken.token,
              _id: res.data._id,
              role: res.data.role
            }
          })
          history.push('/')}
        ).catch((err) =>{console.log(err)
          toast.warning(err.message)});
        }
        catch(error){
          console.log(error)
          toast.warning(error.message)
        }
        
        
    }
    return(
        <div class="container login col d-flex justify-content-center">
            <div class="card login-card w-8" style={{
                backgroundColor:"#26122e"
            }}>
                <div class="card">
  <div class="card-header justify-content-center login-header text-center">
        Log In
  </div>
  
  <div class="card-body login-body">
  <label class="card-text" style={{
      paddingBottom: "10px"
  }}>Welcome to Sanyam Enterprise, Please login to your account</label>
  <form onSubmit={handleSubmit}>
  <div class="form-group">
    <label>Email address</label>
    <input type="email" class="form-control" aria-describedby="emailHelp" placeholder="Enter email" value={email} onChange={e=> setEmail(e.target.value)}/>
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
  <button type="submit" class="btn btn-primary ">Sign In</button>
  </div>
  <div class="row">
      <div class=" text-center  col-sm-12 p-10" style={{
      paddingBottom: "10px"
  }}>
            <a href="/signup"> Create a New Account</a>
      </div>
      <div class="text-center col-sm-12 p-10" style={{
      paddingBottom: "10px"
  }}>
            <a href="/">Forgot Password</a>
      </div>

  </div>
</form>
  </div>
  
</div>
            </div>
            
        </div>
    );
}

export default LoginCart;