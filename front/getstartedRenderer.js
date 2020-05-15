const electron      = require('electron');
const python        = require('python-shell');
const path          = require('path');
const {ipcRenderer} = electron;

const clearAllBtn = document.getElementById('clr-all-btn');
const nextPatientBtn = document.getElementById('next-pat-btn');

clearAllBtn.addEventListener('click', function() {
    let inputs = document.getElementsByTagName('input');

    for (let i=0, max=inputs.length; i < max; i++) {
        inputs[i].value = '';
    }

    let modelOutputs = document.getElementsByClassName('model-output');
    for (let i=0, max=modelOutputs.length; i < max; i++) {
        modelOutputs[i].innerHTML = '';
    }

});

let patientCounter = 1;
let maxPatients = 26;


nextPatientBtn.addEventListener('click', function() {
    if (patientCounter > maxPatients) {
        patientCounter = 1;
    }

    console.log(process.env.PY)

//     let options = {
//         scriptPath: path.join(__dirname, '../back/')
//         , args: [patientCounter]
//         // , pythonPath: "c/users/raccoon/python/python37-32",
//         , pythonPath: path.join('Users', 'RACCON', 'Python', 'Python37-32')

//     }

    patientCounter++;
    parsedJsonData = {};




// C:\\Users\\RACCOON\\Python\\Python37-32\\

    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python',["../back/reader.py", patientCounter], {windowsVerbatimArguments: true});

    // function sleep(ms) {
    //     return new Promise(resolve => setTimeout(resolve, ms));
    //   }
    //   async function demo() {
    //     console.log('Taking a break...');
    //     await sleep(2000);
    //     console.log('Two seconds later, showing sleep in a loop...');
    //     // Sleep in loop
    //     for (let i = 0; i < 5; i++) {
    //       if (i === 3)
    //         await sleep(2000);
    //       console.log(i);
    //     }
    //   }

    // demo();
    // console.log('before');

    // parsedJsonData = {};

    // pythonProcess.stdout.on('data', (data) => {
    //     console.log(data.toString());
    //     // Do something with the data returned from python script
    //     readTextFile('../back/input.json', function(text){
    //         let data = JSON.parse(text);
    //         console.log(data);
    //         parsedJsonData = data;
    //     });
    // });


    // console.log('after');


    // console.table(parsedJsonData);
    // readTextFile('../back/input.json', function(text){
    //     let data = JSON.parse(text);
    //     console.log(data);
    //     parsedJsonData = data;
    // });
    // console.table(options.args);

    // python.PythonShell.runString('import sys;f = open("a.txt", "w"); f.write(sys.version); f.close()', null, function (err) {
    //     if (err) throw err;
    //     console.log('finished');
    //   });


    // python.PythonShell.run('reader.py', options, function (err, results) {
    //     if (err) throw err;
    //     console.log('finished');
    // });

      readTextFile('../back/input.json', function(text){
        let data = JSON.parse(text);
        console.log(data);
        parsedJsonData = data;
    });

    // console.log(results);
    console.log('new: ');
    console.table(parsedJsonData);

    // console.table(parsedJsonData);
});



function readTextFile(file, callback) {
    let rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}
