import React from "react";
import axios from "axios";

export const createUpdateUser= async(authtoken)=>{
    console.log("Api hit", authtoken)
    return await axios.post('http://127.0.0.1:5000/api/create-update-user',{},{
        headers:{
            authorization:authtoken,
        },
    });

};