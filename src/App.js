import React, { Component } from "react";
import Header from "./Components/Header";
import Login from "./Components/Login";
import DashBoard from "./Components/Dashboard";

export default class App extends Component {
  state = {
    loggedIn: false
  };

  handleLogin = bool => {
    this.setState({ loggedIn: bool });
  };
  render() {
    const { loggedIn } = this.state;
    return (
      <div className="App">
        <Header />
        {!loggedIn && <Login handleLogin={this.handleLogin} />}
        {loggedIn && <DashBoard handleLogin={this.handleLogin} />}
      </div>
    );
  }
}
