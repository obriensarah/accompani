const IncomingForm = require("formidable").IncomingForm;
const fs = require('fs');

module.exports = async function upload(req, res) {
  var form = new IncomingForm();

  form.on("file", async (field, file) => {
    const key = file.name.substring(0,1)
    const tonality = file.name.substring(1)
    console.log('key is ', key, ' type is ', tonality)

    //change filename to input.xyml
    inputFile = 'input.xml'
    fs.copyFile(file.path,inputFile,console.log)

    console.log('running java on file ', inputFile)
    var child = await require('child_process').spawn('python',['../../Python/accompani.py', inputFile, key, tonality]);

    child.stdout.on('data', (data) => {
      console.log(`child stdout:\n${data}`);
    });

    child.stderr.on('data', (data) => {
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
