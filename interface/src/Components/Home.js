import React from 'react';
import fire from '../config';

const Home = () => {
  const logout = () => {
    fire.auth().signOut();
  };

  return (
    <div>
      <h1>You are home!</h1>
      <button onClick={logout}>Log Out</button>
    </div>
  );
};

export default Home;
