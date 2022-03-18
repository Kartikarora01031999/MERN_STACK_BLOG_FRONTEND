import React from "react";

const Footer=() =>{
    return(
        <footer class="text-white" style={{
            backgroundColor:"#26122e"
  
          }}>
            <div class="container p-4">
                    <div class="row">
                        <div class="col-lg-4 col-md-12 mb-4 mb-md-0">
                            <a class="navbar-brand header" href="#">
                            <span style={{backgroundColor:'white', color: "#26122e", padding:"12px", fontFamily:"Aladin" , borderRadius:"10px", fontSize: "30px"}}>SE</span>
                            </a>
                            <a class="navbar-brand header" href="#">
                            <h1>Sanyam Enterprise</h1></a>
                            <br></br>
                        </div>
                        <div class="col-lg-8 col-md-6 mb-4 mb-md-0">
                        <div class="text-right p-5">
                           © Copyrights 2022 - 2023.Sanyam Enterprise.All Rights Reserved.
                        </div>
                        
                        </div>


                    </div>
                    <div class="row ">
                    <div class="col-lg-3 col-md-4 mb-4 mb-md-0">
                    <a href="#" class="btn rounded text-white ">
                                    <i className="fa fa-phone"></i> +91 9557 304 483</a>
                    </div>
                    <div class="col-lg-4 col-md-4 mb-4 mb-md-0">
                    <a href="#" class="btn rounded text-white">
                    <i className="fa fa-envelope"></i> sanyamenterprise@gmail.com</a> 
                    </div>
                    <div class="col-lg-5 col-md-4 mb-4 mb-md-0">
                    <a href="#" class="btn rounded text-white">
                        <i className="fa fa-map-marker"></i>  46/2,Dhamwala Bazar, Dehradun, Uttarakhand,India</a>
                    </div>
                    </div>

            </div>
        </footer>
    
    );

}

export default Footer;