import React from "react";

function Login(props) {
  const { handleLogin } = props;

  const handleClick = (e) => {
    e.preventDefault()
    handleLogin(true);
  };

  return (
    <form onSubmit={handleClick}>
      <label>
        Username <input type="text" id="username" required></input>
      </label>
      <label>
        Password <input type="password" id="password" required></input>
      </label>
      <button type="submit">Enter</button>
    </form>
  );
}

export default Login;
