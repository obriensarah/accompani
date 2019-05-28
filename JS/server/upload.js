const IncomingForm = require("formidable").IncomingForm;
const fs = require('fs');

module.exports = async function upload(req, res) {
  var form = new IncomingForm();

  form.on("file", async (field, file) => {
    let complete = false
    let errors = false

    if (fs.exists('accompani.xml')){
      fs.unlinkSync('accompani.xml'); //delete old solution files
    }

    const key = file.name.split('-')[0]
    const tonality = file.name.split('-')[1]
    if (tonality === 'minor'){tonality = 'harmonic_minor'}
    const genre = file.name.split('-')[2]
    const rhythm = file.name.split('-')[3].toLowerCase()
    console.log('file name is : ', file.name)
    console.log('key is ', key, ' type is ', tonality, 'genre is ', genre, 'rhythm is ', rhythm)

    //change filename to input.xml
    inputFile = 'input.xml'
    fs.copyFile(file.path,inputFile,console.log)

    console.log('running python on file ', inputFile)
    var child = await require('child_process').spawn('python',['../Python/accompani.py', inputFile, key, tonality, genre, rhythm]);

    child.stdout.on('data', (data) => {
      console.log(`child stdout:\n${data}`);
    });

    child.stderr.on('data', (data) => {
      if (fs.exists('./accompani.xml')){
        fs.unlinkSync('./accompani.xml'); //delete old solution files
      }
      console.error(`child stderr:\n${data}`);
    });

    setTimeout(async ()=> {
      fs.unlinkSync('input.xml'); //delete old input files
    }, 6000);

  });
  form.on("end", () => {
    console.log('sending response')
    res.send('complete.')
  });
  form.parse(req);
};
