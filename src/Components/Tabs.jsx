import React from "react";
import { Link } from "@reach/router";

function Tabs() {
  return (
    <div className="Tabs">
      <a href="/pages/settings.html">
        <div id="postButton">
          <h2>Settings</h2>
        </div>
      </a>
      <a href="/pages/dashboard.html">
        <div id="postButton">
          <h2>DashBoard</h2>
        </div>
      </a>
      <a href="/pages/viewCam.html">
        <div id="postButton">
          <h2>View Camera</h2>
        </div>
      </a>
    </div>
  );
}

export default Tabs;
