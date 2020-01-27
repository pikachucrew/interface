import React from "react";
import { Link } from "@reach/router";
import DashBoard from "./Dashboard";

function Login() {
  return (
    <form className="login">
      <label>
        {" "}
        Username: <input type="text"></input>
      </label>
      <label>
        {" "}
        Password: <input type="password"></input>
      </label>
      <Link to="/home">
        <button onClick={<DashBoard />}>Login</button>
      </Link>
    </form>
  );
}

export default Login;
