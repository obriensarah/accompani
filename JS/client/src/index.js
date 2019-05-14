import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Team from './Team';
import About from './About';
import { BrowserRouter, Route } from 'react-router-dom'

class Routes extends React.Component {
  render() {
    return (
      <div>
        <Route exact path="/" component={App} />
        <Route exact path="/team" component={Team} />
        <Route exact path="/about" component={About} />
      </div>
    );
  }
}

ReactDOM.render(
  <BrowserRouter>
    <Routes />
  </BrowserRouter>,
  document.getElementById("root")
);
