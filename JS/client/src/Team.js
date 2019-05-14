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
    console.log(this.state.file)
    return (
      <div className="App">
        <header className="App-header">
          <Nav current='team'/>
          <video src='/wave.mov' autoPlay loop className="App-logo" alt="logo"/>
          <div className='title'>
            <span className='titleBlue'>&lt;</span>
            &nbsp;team&nbsp;
            <span className='titleBlue'> &#47;&gt;</span>
          </div>

          <div className='cardContainer'>
            <div className='container'>
              <div className='colorbg'>
                <img className='profimg' src='/sarah.png' alt='' />
              </div>
              <div className='name'>Sarah O'Brien</div>
              <div className='description'>
                she does math good and also plays the music #jinglebells
                <br/>
                <a href="mailto:sarahobrien2020@u.northwestern.edu">
                  Email Sarah
                </a>
              </div>
            </div>
            <div className='container'>
              <div className='colorbg'>
                <img className='profimg' src='/ryan.jpg' alt='' />
              </div>
              <div className='name'>Ryan McHenry</div>
              <div className='description'>
                he makes things pretty and colorful and writes the no fun code!
                <br/>
                <a href="mailto:ryanmchenry2019@u.northwestern.edu">
                  Email Ryan
                </a>
              </div>
            </div>
          </div>
        </header>
      </div>
    );
  }
}

export default Team;
