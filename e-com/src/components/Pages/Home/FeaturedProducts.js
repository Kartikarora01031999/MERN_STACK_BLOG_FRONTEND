import React from "react";

const FeaturedProducts=() =>{
    return(
        <section class="text-center " id="faetured-products"style={{
            backgroundColor:"#0d0115",
            marginRight:"100px",
            marginLeft:"100px" ,
              
          }}>
  
  
    <h1 class="text-center" style={{
       color: "pink",
       padding:"30px",
       fontSize:"32px",
       fontStyle: "Large"
    }}>Featured Products</h1>

  
    
    <div class="row">
      <div class="col-lg-3 col-md-6 mb-lg-0 mb-4">
        <div class="card card-cascade narrower card-ecommerce">
        <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/2.webp" class="card-img-top"
              alt="sample photo"/>
       
        </div>
        <p style={{fontSize:"20px"}}> Jewellery Bags</p>
      </div>  
      <div class="col-lg-3 col-md-6 mb-lg-0 mb-4">
        <div class="card card-cascade narrower card-ecommerce">
          <div class="view view-cascade overlay">
            <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/2.webp" class="card-img-top"
              alt="sample photo"/>
          </div>
        </div>
        <p style={{fontSize:"20px"}}>Jewellery Purses</p>
      </div>
      <div class="col-lg-3 col-md-6 mb-md-0 mb-4">
        <div class="card card-cascade narrower card-ecommerce">
          <div class="view view-cascade overlay">
            <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/4.webp" class="card-img-top"
              alt="sample photo"/>
          </div>     
        </div> 
        <p style={{fontSize:"20px"}}> Jewellery Boxes </p> 
      </div>
      <div class="col-lg-3 col-md-6">
        <div class="card card-cascade narrower card-ecommerce">
          <div class="view view-cascade overlay">
            <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/3.webp" class="card-img-top"
              alt="sample photo"/>
          </div>
        </div>
        <p style={{fontSize:"20px"}}> Jewellery Tools</p> 
      </div>
    </div>
  
  
  </section>
    )

}

export default FeaturedProducts;