import React, { Component } from 'react';
import fire from './config';
import Login from './Components/Login';
import Home from './Components/Home';

class App extends Component {
  state = {
    user: {}
  };

  componentDidMount() {
    this.authListener();
  }

  authListener = () => {
    fire.auth().onAuthStateChanged(user => {
      if (user) {
        this.setState({ user });
      } else {
        this.setState({ user: null });
      }
    });
  };

  render() {
    const { user } = this.state;
    return <div>{user ? <Home /> : <Login />}</div>;
  }
}

export default App;
