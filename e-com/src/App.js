import React from "react";
import {
  Switch,
  Route
} from 'react-router-dom'
import Home from "./components/Pages/Home/Home";
import 'font-awesome/css/font-awesome.min.css';
import Login from "./components/Pages/Login/Login";

function App() {
  return (
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/login" component={Login} />
    </Switch>
  );
}

export default App;
