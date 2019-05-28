import React, { Component } from 'react';
import './App.css';
import Upload from './upload/Upload';
import Nav from './Nav'
import Loading from './Loading'
import { Link } from 'react-router-dom'

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      upload:false,
      loading:false,
      complete:false,
      complete_with_error:false
    }
  }

  closeUpload(closebutton){
    if (closebutton === true){
      this.setState({upload:false})
    }
    else{
      this.setState({upload:false, loading:true})
    }
  }

  renderUploadBox(){
    if (this.state.upload){
      return(
        <div style={{position:'absolute', zIndex:999, height: '100vh', width: '100vw', top:'20vh',margin:'auto'}}>
          <div className='Card' style={{margin:'auto'}}>
            <Upload closeUpload={(e)=>this.closeUpload(e)}/>
          </div>
        </div>
      )
    }
  }

  waitForComplete(){
    window.setTimeout(()=>{
      if (this.fileExists()){
        this.setState({complete:true,loading:false})
      }
      else{
       this.setState({complete_with_error:true,loading:false})
      }
    },4000)
  }

  renderSampleMidiBox(){
    return(
      <a href='http://35.174.137.122:8000/sampledownload'>
      {/* // <a href='http://localhost:8000/sampledownload'> */}
        <div className='lightbox'>
          Download a Sample MusicXML File for Testing!
        </div>
      </a>
    )
  }

  fileExists(){

    var http = new XMLHttpRequest();

    http.open('HEAD', 'http://35.174.137.122:8000/download', false);
    http.send();

    return http.status != 404;

}

  render() {
    console.log("SOLUTION READY: ", this.fileExists())
    if (!this.state.loading && !this.state.complete){
      return (
        <div className="App">
          <header className="App-header">
            <Nav current='home'/>
            <video src='/wave.mov' autoPlay muted loop className="App-logo" alt="logo"/>
            {this.renderSampleMidiBox()}
            <div className='title'>
              <span className='titleBlue'>&lt;</span>
              &nbsp;accompani&nbsp;
              <span className='titleBlue'> &#47;&gt;</span>
            </div>

            <div className='title' style={{fontSize:'.8em', fontWeight:'100', color:'#bbb', letterSpacing:'1px'}}>an automated lead sheet generator<br/>powered by live input, real artists, and machine learning.</div>

            <div className='cardContainer'>
              
              <div className='card' onClick={()=>this.setState({upload:true})}>
                <div className='cardHeader'>YOU GIVE US:</div>
                <div className='cardBody'>
                  Input MusicXML file<br/>
                  Key Signature<br/>
                  Stylistic Preferences
                </div>
              </div>
              <Link to='/about'>
                <div className='card'>
                  <div className='cardHeader'>WE GIVE YOU:</div>
                  <div className='cardBody'>
                    Output MusicXML file<br/>
                    Chord Progression<br/>
                    Lead Sheet
                  </div>
                </div>
              </Link>
              <br/>

              <br/>
              <button className='buttonPrimary' onClick={()=>this.setState({upload:true})}>BUILD ACCOMPANIMENT</button>
            </div>

          </header>
          {this.renderUploadBox()}
        </div>
      );
    }


    if (this.state.loading){
      this.waitForComplete()
      return (
        <div className="App">
          <header className="App-header">
            <Nav current='home'/>
            <video src='/wave.mov' autoPlay loop className="App-logo" alt="logo"/>

            <div className='cardContainer'>
              <Loading/>
            </div>

          </header>
        </div>
      );
    }

    if (this.state.complete){
      return (
        <div className="App">
          <header className="App-header">
            <Nav current='home'/>
            <video src='/wave.mov' autoPlay loop className="App-logo" alt="logo"/>
            <div className='title'>
              <span className='titleBlue'>&lt;</span>
              &nbsp;complete&nbsp;
              <span className='titleBlue'> &#47;&gt;</span>
            </div>

            <div className='cardContainer'>
              <a href='http://35.174.137.122:8000/download'>
              {/* <a href='http://localhost:8000/download'> */}
                <button className='buttonPrimary'>DOWNLOAD XML FILE</button>
              </a>
              <br/>
              <button className='buttonSecondary' onClick={()=>this.setState({loading:false,complete:false})}>START OVER</button>
            </div>

          </header>
        </div>
      );
    }

    if (this.state.complete_with_error){
      return (
        <div className="App">
          <header className="App-header">
            <Nav current='home'/>
            <video src='/wave.mov' autoPlay loop className="App-logo" alt="logo"/>
            <div className='title'>
              <span className='titleBlue'>&lt;</span>
              &nbsp;error&nbsp;
              <span className='titleBlue'> &#47;&gt;</span>
            </div>
            <div className='title' style={{fontSize:'.8em', fontWeight:'100', color:'#bbb', letterSpacing:'1px'}}>This is often caused by a bad XML file, or perhaps a melody that contains notes outside its key signature. Check your input file and try again.</div>

            <div className='cardContainer'>
              <button className='buttonSecondary' onClick={()=>this.setState({loading:false,complete:false})}>TRY AGAIN</button>
            </div>

          </header>
        </div>
      );
    }

  }
}

export default App;
