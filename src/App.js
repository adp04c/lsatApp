import React, { Component } from 'react';
import logo from './datasciencewrangle.png';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <body>
          <font face="arial" color="FF33E0">
            <img src={logo} className="App-logo" alt="logo" />
            <h2>Rory's and A2s sick app for law students who want to perform well and learn to do other things</h2>
            <h3>We have a lot to learn to get this to work</h3>
          </font>
          </body>
        </div>
        <p className="App-intro">
          <body>
          <font face="arial" color="FF33E0">
            <h1>Good job guys!</h1>
            To get started, edit <code>src/App.js</code> and save to reload.
          </font>
          </body>
        </p>
      </div>
    );
  }
}

export default App;

