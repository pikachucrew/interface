import React from "react";
import { Link } from "@reach/router";

function Tabs() {
  return (
    <div className="Tabs">
     <Link to = "Settings">Settings</Link>
      <Link to="Stats">Stats</Link>
      <Link to="View Camera">View Camera</Link>
    </div>
  );
}

export default Tabs;
