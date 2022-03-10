import React from "react";
import about_us from '../../../images/about_us.webp'
const AboutUs=() =>{
    return(
        <section id="about-us" style={{
            backgroundColor:"#26122e",
            marginRight:"100px",
            marginLeft:"100px" ,
            paddingBottom:"20px"
          }}>
  
  
    <h1 class="text-center" style={{
       color: "pink",
       padding:"30px",
       fontSize:"32px",
       fontStyle: "Large"
    }}>About Us</h1>

  
    
    <div class="row">
      <div class="col-lg-7 col-md-6 mb-lg-0 mb-4">
        <p style={{fontSize:"16.5px", color:"white", fontFamily:"sans-serif", textAlign:"center"}}>We Sanyam Enterprise, situated at Dhamawala Bazar, Dehradun, Uttarakhand, are one of the prominent dealer of an engineered range of Jewelry Making Machine and Equipments, Jewelry Bags , Pouches and Jewelry Boxes. We provide printing over Boxes, Purses and Bags as per the client’s specification following industrial standards.Our products are widely renowned for their excellent performance, good quality, less maintenance and many more. We also have a wide range of Jewellery Boxes and Pouches of various sizes and pattern at a reasonable price. We have team of expert & professional quality analyst, who are dedicated towards supplying qualitative range of Jewelry rendering productsto our esteemed clients. </p>
      </div>  

      <div class="col-lg-5 col-md-6" style={{marginTop:"20px"}}>
        <div class="card card-cascade narrower card-ecommerce">
          <div class="view view-cascade overlay">
            <img src={about_us} class="card-img-top"
              alt="sample photo"/>
          </div>
        </div>
      </div>
    </div>
  
  
  </section>
    )

}

export default AboutUs;