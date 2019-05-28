import React, { Component } from "react";
import Dropzone from "../dropzone/Dropzone";
import "./Upload.css";
import Progress from "../progress/Progress";

class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
      uploading: false,
      uploadProgress: {},
      successfullUploaded: false,
      tonality:'',
      genre:'Rock',
      rhythm:'',
      renderStyleInfo: false
    };

    this.onFilesAdded = this.onFilesAdded.bind(this);
    this.uploadFiles = this.uploadFiles.bind(this);
    this.sendRequest = this.sendRequest.bind(this);
    this.renderActions = this.renderActions.bind(this);
  }

  onFilesAdded(files) {
    this.setState(prevState => ({
      files: prevState.files.concat(files)
    }));
  }

  async uploadFiles() {
    if (!this.state.key || !this.state.tonality){
      alert('Whoops! Make sure to select a key!')
      return
    }
    this.setState({ uploadProgress: {}, uploading: true });
    const promises = [];
    this.state.files.forEach(file => {
      promises.push(this.sendRequest(file));
    });
    try {
      await Promise.all(promises);

      this.setState({ successfullUploaded: true, uploading: false });
      window.setTimeout(()=>{this.props.closeUpload()},500)
    } catch (e) {
      // Not Production ready! Do some error handling here instead...
      this.setState({ successfullUploaded: true, uploading: false });
    }
  }

  sendRequest(file) {
    return new Promise(async (resolve, reject) => {
      const req = new XMLHttpRequest();

      req.upload.addEventListener("progress", event => {
        if (event.lengthComputable) {
          const copy = { ...this.state.uploadProgress };
          copy[file.name] = {
            state: "pending",
            percentage: (event.loaded / event.total) * 100
          };
          this.setState({ uploadProgress: copy });
        }
      });

      req.upload.addEventListener("load", event => {
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "done", percentage: 100 };
        this.setState({ uploadProgress: copy });
        resolve(req.response);
      });

      req.upload.addEventListener("error", event => {
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "error", percentage: 0 };
        this.setState({ uploadProgress: copy });
        reject(req.response);
      });

      const formData = new FormData();
      let filename = this.state.key + '-' + this.state.tonality + '-' + this.state.genre + '-' + this.state.rhythm
      formData.append("file", file, filename);

      req.open("POST", "http://35.174.137.122:8000/upload");
      // req.open("POST", "http://localhost:8000/upload");
      req.send(formData);

    });
  }

  renderProgress(file) {
    const uploadProgress = this.state.uploadProgress[file.name];
    if (this.state.uploading || this.state.successfullUploaded) {
      return (
        <div className="ProgressWrapper">
          <Progress progress={uploadProgress ? uploadProgress.percentage : 0} />
          <img
            className="CheckIcon"
            alt="done"
            src="baseline-check_circle_outline-24px.svg"
            style={{
              opacity:
                uploadProgress && uploadProgress.state === "done" ? 0.5 : 0
            }}
          />
        </div>
      );
    }
  }

  componentDidMount(){
    this.setState({genre:'Rock', rhythm:'Note'})
  }

  renderActions() {
    if (this.state.successfullUploaded) {
      return (
        <button
          onClick={() =>
            this.setState({ files: [], successfullUploaded: false })
          }
        >
          Clear
        </button>
      );
    } else {
      return (
        <button
          disabled={this.state.files.length < 0 || this.state.uploading}
          onClick={this.uploadFiles}
        >
          Upload
        </button>
      );
    }
  }

  async selectKey(key){
    await this.setState({key:key})
  }

  keyStyle(key){
    if (key.length === 1){
      return this.state.key === key ? 'whiteKey selectedKey' : 'whiteKey'
    }
    return this.state.key === key ? 'blackKey selectedKey' : 'blackKey'
  }

  tonalityButtonStyle(tonality){
    if (this.state.tonality === tonality.toLowerCase()){
      return 'button buttonSmall buttonSelected'
    }
    return 'button buttonSmall buttonUnselected'
  }

  rhythmButtonStyle(rhythm){
    if (this.state.rhythm === rhythm.toLowerCase()){
      return 'button buttonSmall buttonSelected'
    }
    return 'button buttonSmall buttonUnselected'
  }

  renderStyleInfo(){
    if (this.state.renderStyleInfo){
      return(
      <div>
        <div style={{fontSize:'.6em', color: '#999',width: '110%', margin:'5px 0px'}}>
          Accompani uses a machine learning model to automatically build chord progressions. By selecting a genre, you decide what music trains the model, and what musicians content is considered in building each progression.
        </div>
      </div>
      )
    }
    return null
  }

  renderRhythmInfo(){
    if (this.state.renderRhythmInfo){
      return(
      <div>
        <div style={{fontSize:'.6em', color: '#999',width: '110%', margin:'5px 0px'}}>
          Accompani analyzes individual notes and measures to determine a chord progression. By choosing your rhythm preference, you decide how often accompani chooses to change chords - on each new measure, or each new note.
        </div>
      </div>
      )
    }
    return null
  }

  renderPiano(){
    if (this.state.files.length > 0){
      return(
        <div style={{textAlign:'center'}}>
          <div>Select a key signature...&nbsp;<b style={{color: '#B80F42', fontSize:'1.2em', background:'transparent'}}>{this.state.key}</b></div>
          <div className='pianoContainer'>
            <div className={this.keyStyle('C')} onClick={()=>this.selectKey('C')}>C</div>
            <div className={this.keyStyle('D')} onClick={()=>this.selectKey('D')}>D</div>
            <div className={this.keyStyle('E')} onClick={()=>this.selectKey('E')}>E</div>
            <div className={this.keyStyle('F')} onClick={()=>this.selectKey('F')}>F</div>
            <div className={this.keyStyle('G')} onClick={()=>this.selectKey('G')}>G</div>
            <div className={this.keyStyle('A')} onClick={()=>this.selectKey('A')}>A</div>
            <div className={this.keyStyle('B')} id='B' onClick={()=>this.selectKey('B')}>B</div>

            <div className={this.keyStyle('Db')} id='Db' onClick={()=>this.selectKey('Db')}>Db</div>
            <div className={this.keyStyle('Eb')} id='Eb' onClick={()=>this.selectKey('Eb')}>Eb</div>
            <div className={this.keyStyle('Gb')} id='Gb' onClick={()=>this.selectKey('Gb')}>Gb</div>
            <div className={this.keyStyle('Ab')} id='Ab' onClick={()=>this.selectKey('Ab')}>Ab</div>
            <div className={this.keyStyle('Bb')} id='Bb' onClick={()=>this.selectKey('Bb')}>Bb</div>
          </div>
          <br/>
          <button className={this.tonalityButtonStyle('Major')} onClick={()=>this.setState({tonality:'major'})}>Major</button>
          <button className={this.tonalityButtonStyle('Minor')} onClick={()=>this.setState({tonality:'minor'})}>Minor</button>
          <br/>
          <div style={{display:'inline-block', verticalAlign:'top', margin:'20px',width: '40%'}}>Select musical style...&nbsp;
            <img style={{height:'15px', opacity:'.4', cursor:'pointer', display:'inline-block'}} src='/info.png' alt='info' onClick={()=>this.setState({renderStyleInfo:!this.state.renderStyleInfo})} />
            <br/>
            {this.renderStyleInfo()}
            <select value={this.state.genre} onChange={(e)=>this.setState({genre:e.target.value})}>
              <option value="Rock">Rock</option>
              <option value="Pop">Pop</option>
              <option value="Folk">Folk</option>
            </select>
          </div>
          <div style={{display:'inline-block', verticalAlign:'top', margin:'20px',width: '40%'}}>Select harmonic rhythm...&nbsp;
            <img style={{height:'15px', opacity:'.4', cursor:'pointer', display:'inline-block'}} src='/info.png' alt='info' onClick={()=>this.setState({renderRhythmInfo:!this.state.renderRhythmInfo})} />
            <br/>
            {this.renderRhythmInfo()}
            <select value={this.state.rhythm} onChange={(e)=>this.setState({rhythm:e.target.value})}>
              <option value="Note">Note</option>
              <option value="Measure">Measure</option>
            </select>
          </div>
      </div>
      )
    }
  }

  render() {
    return (
      <div className="Upload">
        <div className='closeButton' onClick={()=>this.props.closeUpload(true)}>X</div>
        <span className="Title">Upload Files</span>
        <div className="Content">
          <div>
            <Dropzone
              onFilesAdded={this.onFilesAdded}
              disabled={this.state.uploading || this.state.successfullUploaded}
            />
          </div>
          <div className="Files">
            {this.state.files.map(file => {
              return (
                <div key={file.name} className="Row">
                  <span className="Filename">{file.name}</span>
                  {this.renderProgress(file)}
                </div>
              );
            })}

            {this.renderPiano()}
          </div>
        </div>
        <div className="Actions">{this.renderActions()}</div>
      </div>
    );
  }
}

export default Upload;
