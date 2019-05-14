import React, { Component } from 'react';
import './App.css';
import './About.css'
import Nav from './Nav'

class About extends Component {

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <Nav current='about'/>
          <video src='/wave.mov' autoPlay loop className="App-logo" alt="logo"/>
          <div style={{height: '60px'}}></div>
          <div className='title'>
            <span className='titleBlue'>&lt;</span>
            &nbsp;about&nbsp;
            <span className='titleBlue'> &#47;&gt;</span>
          </div>

          <div className='cardContainer'>
            <div>
              <b>DESIGNED @:</b> <br/><br/>
            <span style={{fontWeight:100}}>
              Northwestern University<br/>
              Interactive Audio Lab<br/>
              Prof. Bryan Pardo<br/>
              Spring, 2019
            </span>
            </div>

            <br/><br/>



            <div className='bodyText right' style={{width: '30%'}}>
              <b style={{fontSize:'1.3em'}}>The Tool:</b><br/><br/>
              Accompani is a tool that provides users with harmonized versions of basic melodies. The user inputs a monophonic Musical Instrument Digital Interface (MIDI) file, and the key of the melody. We assume that the given melody only uses notes within the given key signature. Accompani returns a harmonized polyphonic MIDI file for download.
            </div>
            <div className='tint'>
              <img className='group' src='/group.jpeg' alt='group' />
            </div>


            <br/><br/><br/>

            <div className='tint'>
              <img className='group' src='/ableton.png' alt='ableton' />
            </div>
            <div className='bodyText left'>
              <b style={{fontSize:'1.3em'}}>The Purpose:</b><br/><br/>
               Accompani is built to be particularly useful for a few specific sets of users. Firstly, Accompani allows young or inexperienced musicians to experiment with the fundamentals of chordal structure and harmony. As students learn and begin to create their own compositions, Accompani provides them with a baseline comparison for their work. Instead of having to check with friends or professors, these users can measure the “legality” of chords and chord progressions with Accompani itself.
              <br/><br/>
              Secondly, Accompani caters to experienced composers who often need to perform mundane harmonization tasks by providing them the opportunity to automate these processes. We hope that these professionals can leverage Accompani to expedite their tedious workflows, allowing them to instead focus on more creative musical pursuits.

            </div>



            <br/><br/><br/>



            <div className='bodyText right'>
              <b style={{fontSize:'1.3em'}}>The Workflow:</b><br/><br/>
                Our user-friendly interface takes the two inputs and passes this information to the Accompani algorithm which is detailed in the stages below.
              <br/><br/>
              <b>1. Chord Mapping:</b> After parsing and extracting each note in our melody, our algorithm decides which chords (the I or the V in the key, for example) are best played with it. These chord mappings are stored, and the chord to accompany the very first note in the melody is noted.
              <br/><br/>
              <b>2. Progression Matrix:</b> We create a matrix assigning probabilities to all the chord mappings we have created. These probabilities dictate the likelihood a certain chord will be selected, given a specific chord that was played immediately prior.
              <br/><br/>
              <b>3. Write to MIDI:</b> Our algorithm then creates and edits the original MIDI file by adding a “legal” progression of non-inverted triads to it. This step provides an appropriate harmonization of the input melody.
              <br/><br/>
              Because Accompani aims to get young or inexperienced musicians more excited about composing, the algorithm incorporates an element of randomness. More specifically, Accompani keeps it interesting by choosing the next chord in a progression based on probabilities on our progression matrix. This means a user may input the same melody twice and obtain two different output harmonizations.
            </div>
            <div className='tint'>
              <img className='group' src='/workflow.png' alt='setup' />
            </div>

            <br/><br/><br/>



              <div className='tintuser'>
                <img className='groupuser' src='/user.jpeg' alt='setup' />
              </div>
              <div className='bodyText left'>
              <b style={{fontSize:'1.3em'}}>User Testing:</b>

              <br/><br/>
              Our testing phase considered three sources:
              <br/><br/>
              <b>Non-Musicians:</b> Five Northwestern students were randomly selected, and each was given three output files from Accompani. None of the students had an extensive background in music theory, and all of the songs were familiar children’s rhymes (ex. Row Row Row Your Boat). We asked each user to rank each output MIDI file on a scale of 1 to 3, with 1 representing poorly harmonized/disjoint sounds, and 3 representing a cohesive, error-free sound.
              <div style={{padding:'10px 30px'}}>
                <b>Result:</b> For this group, we received an average score of 2.6 for our harmonized melodies. In the cases where we received a score of “2”, users commented that “only one or two parts” seemed out of place. Of the 15 songs we tested, only two received a score of “1”.
              </div>

              <b>Musicians:</b> Three music students were each asked to about a few theoretical factors of the three output MIDI files generated by Accompani. We asked them to comment on the flow and intuitiveness of the chord progression, the sound of the overall harmonization, and what they would change overall.
              <div style={{padding:'10px 30px'}}>
                <b>General Positive Feedback:</b> Yes! On a micro level, all the progressions are legal and the chords are compatible with the melody.
                <br/>
                <b>General Constructive Feedback:</b> The macro level movements seem flawed. It seems as though there is a lack of overall direction in the harmonized melodies. For example, there are big tonic expansions that don’t lead anywhere.
              </div>

              <b>Ground Truth:</b> Because Accompani aims to provide an appropriate harmonization but not necessarily the same one every time, we do not believe a numerical accuracy measurement is sufficient to fully capture the success of our tool. However, in order to compare our harmonizations against existing ones, we performed a simple accuracy measurement on two well-known tunes. We manually wrote the chords we generated (in numbers) along with the lyrics and compared this set of chords to the chords listed on the Acoustic Music Archive (ground truth). We generated an accuracy measurement by computing the number of beats playing the same chord (as is played in the ground truth) divided by the total beats in the excerpt.
              <div style={{padding:'10px 30px'}}>
                <b>Result:</b> For the song “Row, Row, Row Your Boat,” we obtained an accuracy measurement of 69%. For the song “Jingle Bells,” we obtained an accuracy measurement of 78%. Note that these accuracy measurements do not mean that Harmoni’s solution is inappropriate for the melody. Also note that much of the disparity between our harmonizations and ground truth is Harmoni’s disregard for harmonic rhythm.
              </div>

            </div>




            <br/><br/><br/>



            <div className='bodyText right'>
              <b style={{fontSize:'1.3em'}}>The Future:</b>

              <br/><br/>
              <b>Key Detection:</b> In order to successfully cater to inexperienced composers and musicians, we hope to incorporate an element of heuristic or machine-learning-based key detection instead of asking for the key as an input. Removing this input will help the tool’s success among novice composers who may not know what key the melody they have created is in.
              <br/><br/>
              <b>Harmonic Improvements:</b> We hope to move toward a version of the algorithm that creates more exciting-sounding harmonies for input melodies. We can achieve this by using chord inversions instead of only non-inverted triads. Additionally, we can allow the usage of accidentals and more interesting chords in any given key (V7/IV, for example).
              <br/><br/>
              <b>Rhythmic Improvements:</b> Accompani currently does not use harmonic rhythm to determine where a chord should be placed in a measure. We hope to change this in the future instead of simply placing a new chord under each melody note. This will improve the sound of the harmonized tune, and will help novice musicians understand concepts of orchestration and harmonic voice.
            </div>
            <div className='tint'>
              <img className='group' src='/setup.jpeg' alt='setup' />
            </div>


            <div style={{height:'100px'}}></div>

          </div>
        </header>
      </div>
    );
  }
}

export default About;
