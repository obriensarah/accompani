import React, { Component } from 'react';
import './App.css';
import './Team.css';
import Upload from './upload/Upload';
import Nav from './Nav'

class Team extends Component {

  constructor(props){
    super(props);
    this.state = {
      file:[],
      upload:false
    }
  }

  closeUpload(finished){
    // if (finished){
    //   <Redirect to=''
    // }
    this.setState({upload:false})
  }

  renderUploadBox(){
    if (this.state.upload){
      return(
        <div style={{position:'absolute', zIndex:999, height: '100vh', width: '100vw', top:'20vh',margin:'auto'}}>
          <div className='Card' style={{margin:'auto'}}>
            <Upload closeUpload={()=>this.closeUpload()}/>
          </div>
        </div>
      )
    }
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <Nav current='team'/>
          <video src='/wave.mov' autoPlay loop className="App-logo" alt="logo"/>
          <div className='title'>
            <span className='titleBlue'>&lt;</span>
            &nbsp;developers&nbsp;
            <span className='titleBlue'> &#47;&gt;</span>
          </div>
          
          <div className='cardContainer'>

            <div className='container'>
              <div className='colorbg'>
                <a href='https://www.linkedin.com/in/sarah-bridget-obrien/' target='_blank' rel="noopener noreferrer">
                  <img className='profimg' src='/sarah.png' alt='' />
                </a>
              </div>
              <div className='name'>Sarah O'Brien</div>
              <div className='description'>
                Northwestern University <br/>
                Weinberg College of Arts and Sciences <br/>
                Computer Science<br/>Class of 2020
                <br/>
                <a href="mailto:sarahobrien2020@u.northwestern.edu">
                  Email Sarah
                </a>
              </div>
            </div>
            <div className='container'>
              <div className='colorbg'>
                <a href='https://www.linkedin.com/in/ryanmchenry2/' target='_blank' rel="noopener noreferrer">
                  <img className='profimg' src='/ryan.jpg' alt='' />
                </a>
              </div>
              <div className='name'>Ryan McHenry</div>
              <div className='description'>
                Northwestern University <br/>
                Bienen School of Music <br/>
                Computer Science and Music Engineering <br/>
                Class of 2019
                <br/>
                <a href="mailto:ryanmchenry2019@u.northwestern.edu">
                  Email Ryan
                </a>
              </div>
            </div>
          </div>
          <br/><br/>
          <div className='title' style={{fontSize:'.6em', fontWeight:'100', opacity:'.5', letterSpacing:'1px'}}>designed @ Northwestern University's Interactive Audio Lab<br/>under the guidance of <a style={{color:'lightblue'}} href='http://users.cs.northwestern.edu/~pardo/'  target='_blank' rel="noopener noreferrer">Prof. Bryan Pardo</a></div>
        </header>
      </div>
    );
  }
}

export default Team;
