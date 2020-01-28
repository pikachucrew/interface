import React from 'react';
import './App.css';
import Header from "./Components/Header"
import Camera from "./Components/Camera"
import Tabs from "./Components/Tabs"
import {Link} from "@reach/router"


function App() {
  return (
    <div className="App">
      <Header/>
      <a href = "settings.html">
         <div id = "postButton">
           <h2>Settings</h2>
         </div>
         </a>
      <Camera />
    </div>
  );
}

export default App;
