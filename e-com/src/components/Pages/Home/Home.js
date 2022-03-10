import React from 'react'
import Nav from '../Nav'
import Banner1 from  '../../../images/banner_image_1.webp'
import Banner2 from  '../../../images/banner_image_2.webp'
import JewelleryBoxes from './JewelleryBoxes';
import JewelleryPouches from './JewelleryPouches';
import JewelleryTools from './JewelleryMakingTools';
import FeaturedProducts from './FeaturedProducts';
import AboutUs from './AboutUs';
import Gallery from './Gallery';
import Contact from './Contact';
import Footer from '../Footer';

const Home=()=>{
    return(
      <>
      <Nav/>,
    <section class="banner-home-page">
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
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</section>
<JewelleryBoxes></JewelleryBoxes>
<JewelleryPouches></JewelleryPouches>
<JewelleryTools></JewelleryTools>
<FeaturedProducts></FeaturedProducts>
<AboutUs></AboutUs>
<Gallery></Gallery>
<Contact></Contact>
<Footer></Footer>
      </>
    );
}
export default Home;