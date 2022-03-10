import React from "react";
import gal_1 from "../../../images/gal_1.webp"
import gal_2 from "../../../images/gal_2.webp"
import gal_3 from "../../../images/gal_3.webp"

const Gallery=() =>{
    return(
        <section class="text-center " id="featured-products" style={{
            backgroundColor:"#0d0115",
            marginRight:"100px",
            marginLeft:"100px" ,
            paddingBottom:"50px"
              
          }}>
  
  
    <h1 class="text-center" style={{
       color: "pink",
       padding:"30px",
       fontSize:"32px",
       fontStyle: "Large"
    }}>Gallery</h1>

  
    
    <div class="row">
      <div class="col-lg-4 col-md-6 mb-lg-0 mb-4">
        <div class="card card-cascade narrower card-ecommerce">
        <img src={gal_1} class="card-img-top"
              alt="sample photo"/>
       
        </div>
      </div>  
      <div class="col-lg-4 col-md-6 mb-lg-0 mb-4">
        <div class="card card-cascade narrower card-ecommerce">
          <div class="view view-cascade overlay">
            <img src={gal_2} class="card-img-top"
              alt="sample photo"/>
          </div>
        </div>
      </div>
      <div class="col-lg-4 col-md-6 mb-md-0 mb-4">
        <div class="card card-cascade narrower card-ecommerce">
          <div class="view view-cascade overlay">
            <img src={gal_3} class="card-img-top"
              alt="sample photo"/>
          </div>     
        </div> 
      </div>
    </div>
    <div class="row" style={{marginTop:"50px"}}> 
      <div class="col-lg-4 col-md-6">
        <div class="card card-cascade narrower card-ecommerce">
          <div class="view view-cascade overlay">
            <img src={gal_1} class="card-img-top"
              alt="sample photo"/>
          </div>
        </div>
      </div>
    </div>
  
  
  </section>
    )

}

export default Gallery;