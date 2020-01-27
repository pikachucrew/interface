import React from "react";
import Camera from "./Camera";
import PictureBooth from "./Picturebooth"

function Dashboard() {
  return (
    <div id="Dashboard">
      <h1>Today you are: happy</h1>
      {/* <Camera /> */}
      <WebCamera />
    </div>
  );
}

export default Dashboard;
