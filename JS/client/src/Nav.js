import React, { Component } from 'react';
import './Nav.css';
import { Link } from 'react-router-dom'

class Nav extends Component {

  selectClass(word){
    if (word === this.props.current){
      return 'linkselected'
    }
    return 'linkunselected'
  }

  render() {
    return (
      <div className='containter'>
        <Link to='/'><div className={this.selectClass('home')}>home</div></Link>
        <Link to='/team'><div className={this.selectClass('team')}>team</div></Link>
        <Link to='/about'><div className={this.selectClass('about')}>about</div></Link>
      </div>
    );
  }
}

export default Nav;
