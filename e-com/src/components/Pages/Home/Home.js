import React from 'react'
import Nav from '../Nav'
import JewelleryBoxes from './JewelleryBoxes';
import JewelleryPouches from './JewelleryPouches';
import JewelleryTools from './JewelleryMakingTools';
import FeaturedProducts from './FeaturedProducts';
import AboutUs from './AboutUs';
import Gallery from './Gallery';
import Contact from './Contact';
import Footer from '../Footer';
import Banner from './Banner';

const Home=()=>{
    return(
      <>
<Nav></Nav>
<Banner></Banner>
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