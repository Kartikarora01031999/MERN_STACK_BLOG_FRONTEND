import React from "react";

const Contact=() =>{
    return(
        <section id="contact" style={{
            marginRight:"100px",
            marginLeft:"100px" ,
            paddingBottom:"20px"
          }}>
        <h1 class="text-center" style={{
       color: "pink",
       padding:"30px",
       fontSize:"32px",
       fontStyle: "Large"
    }}>Contact Us</h1>
    <div class="row px-5">
        <div class="col-sm-6">
            <div>
                <h2 class="text-white">Get a quote</h2>
            </div>
            <div class="links" id="bordering"> 
            <a href="#" class="btn rounded text-white p-3">
            <i className="fa fa-phone"></i> +91 9557 304 483</a>
            <br/>
             <a href="#" class="btn rounded text-white p-3">
            <i className="fa fa-envelope"></i> sanyamenterprise@gmail.com</a> 
            <br/>
            <a href="#" class="btn rounded text-white p-3">
                <i className="fa fa-map-marker"></i>  46/2, Dhamwala Bazar, Dehradun,<br/> Uttarakhand, India</a> </div>
        </div>
        <div class="col-sm-6 pad">
            <form class="rounded msg-form">
                <div class="form-group"> <label for="name" class="h6">Your Name</label>
                    <div class="input-group border rounded">
                     <input type="text" class="form-control"/>
                    </div>
                </div>
                <div class="form-group"> <label for="name" class="h6">Email</label>
                    <div class="input-group border rounded">
                        <input type="text" class="form-control border-0"/>
                    </div>
                </div>
                <div class="form-group"> <label for="msg" class="h6">Message</label> <textarea name="message" id="msgus" cols="10" rows="5" class="form-control bg-light" placeholder="Message"></textarea> </div>
                <div class="form-group d-flex justify-content-end"> <input type="submit" class="btn btn-primary text-white" value="Send Message"/> </div>
            </form>
        </div>
    </div>
         </section>
    )

}

export default Contact;