import React from "react";
import Camera from "./Camera";
import Webcamera from "./Webcamera"

function Dashboard() {
  return (
    <div id="Dashboard">
      <h1>Today you are: happy</h1>
      {/* <Camera /> */}
      <Webcamera />
    </div>
  );
}

export default Dashboard;
