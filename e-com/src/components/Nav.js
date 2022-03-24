import React, { useState } from 'react'
import './Pages/Home/home.css'

import { useDispatch,useSelector } from 'react-redux'
import { useHistory } from 'react-router-dom'
import firebase from "firebase/compat/app";
const Nav=()=>{
  let dispatch =useDispatch();
  let history=useHistory();
  let {user}=useSelector((state)=>((state)))
  const [search,setSearch]= useState("");
  const handleSubmit=(e)=>{
    e.preventDefault();
    console.log(search)
  }

  const logout=()=>{

    firebase.auth().signOut();
    dispatch({
      type:"LOGOUT",
      payload:null,
    })
    history.push('/login')
  }
    return(

        <nav class="navbar navbar-expand-lg navbar-dark sticky" style={{
          backgroundColor:"#26122e"

        }}>
    <a class="navbar-brand header" href="/">
      <span style={{backgroundColor:'pink', color: "#26122e", padding:"12px", fontFamily:"Aladin" , borderRadius:"10px", fontSize: "30px"}}>SE</span>
    </a>
    <a class="navbar-brand header" href="/">
    <h1>Sanyam Enterprise</h1></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon">
      </span>
  </button>
  <div class="container">
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link header" href="/">HOME <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link header" href="#">JEWELLERY BOXES</a>
      </li>
      <li class="nav-item">
        <a class="nav-link header" href="#">JEWELLERY POUCHES</a>
      </li>
      <li class="nav-item">
        <a class="nav-link header" href="#">JEWELLERY MAKING TOOLS</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle header" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-expanded="false">
          MORE
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown" style={{fontFamily:"Aladin", fontSize:"16px"}}>
          <a class="dropdown-item" href="#">About Us {search}</a>
          <a class="dropdown-item" href="#">Gallery</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Featured Products</a>
          <a class="dropdown-item" href="#">Contact us</a>
        </div>
      </li>
    </ul>
    </div>
    { !user && 
    (<div class="row mt-2">
    <div class="form-inline my-2 my-lg-0 col-4">
    <a href="/login" class="btn rounded text-white p-3">
        Login/SignUp</a>
    </div>
    <form class="form-inline my-2 my-lg-0 col-8" onSubmit={handleSubmit}>
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" value={search} onChange={e=> setSearch(e.target.value)}/>
      <button class="btn-primary">
      <i class="fa fa-search text-white" type="submit"></i>
      </button>

    </form>
    </div>)
}
{user &&
  (<div class="row mt-2">
    <div class="form-inline my-2 my-lg-0 col-2">
    <span class="nav-item dropdown">
    <a href="#" class="nav-link dropdown-toggle text-white p-3" id="navbarDropdown" role="button" data-toggle="dropdown" aria-expanded="false">
        <i class="fa fa-user"></i></a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown" style={{fontFamily:"Aladin", fontSize:"16px"}}>
          <a class="dropdown-item" href="#">Profile</a>
          <a class="dropdown-item" href="#">My Orders</a>
          <div class="dropdown-divider"></div>
          <span class="dropdown-item" onClick={logout}>logout</span>
        </div>
    </span>
    </div>
    <div class="form-inline my-2 my-lg-0 col-2">
    <a href="#" class="btn rounded text-white p-3">
        <i class="fa fa-shopping-cart"></i></a>
    </div>
    <form class="form-inline my-2 my-lg-0 col-8" onSubmit={handleSubmit}>
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" value={search} onChange={e=> setSearch(e.target.value)}/>
      <button class="btn-primary">
      <i class="fa fa-search text-white" type="submit"></i>
      </button>

    </form>
    </div>
  )

}

  </div>

</nav>
    );
}
export default Nav;