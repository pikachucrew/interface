import React from "react";
import { Link } from "@reach/router";
import Stats from "./Stats";
import FriendlyTips from "./FriendlyTips";

function Dashboard(props) {
  const { handleLogin } = props;

  const trigger = e => {
  console.log(e.target.id)
  };

  const handleClick = e => {
    e.preventDefault();
    handleLogin(false);
  };
  return (
    <div>
      <button id = "button" onClick={trigger}>Who's your Daddy?</button>
      <Stats />
      <FriendlyTips />
      <p>pee</p>
      <button onClick={handleClick}>Log out</button>
    </div>
  );
}

export default Dashboard;
