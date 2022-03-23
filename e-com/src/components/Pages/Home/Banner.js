import React from "react";
import Banner1 from  '../../../images/banner_image_1.webp'
import Banner2 from  '../../../images/banner_image_2.webp'
const Banner= () =>{
    return(
    <div class="banner-home-page">
      <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active banner">
      <img class="d-block w-100" src={Banner1} alt="First slide"/>
    </div>
    <div class="carousel-item banner">
      <img class="d-block w-100" src={Banner2}  alt="Second slide"/>
    </div>
  </div>

</div>
</div>
    );
}

export default Banner;