import React from 'react';
import logo from './logo.svg';
import './App.css';
import Header from "./Components/Header"
import Camera from "./Components/Camera"

function App() {
  return (
    <div className="App">
      <Header/>
      <Camera />
    </div>
  );
}

export default App;
