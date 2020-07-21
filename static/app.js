  // Your web app's Firebase configuration

//const firebase = require("firebase");
// Required for side-effects
//require("firebase/firestore");
const Config = {
    apiKey: "AIzaSyDIjpZ_nnITsd0pJRRPsWVujyBFUZNSlr0",
    authDomain: "online-diabetes-predicto-6655e.firebaseapp.com",
    databaseURL: "https://online-diabetes-predicto-6655e.firebaseio.com",
    projectId: "online-diabetes-predicto-6655e",
    storageBucket: "online-diabetes-predicto-6655e.appspot.com",
    messagingSenderId: "408013840085",
    appId: "1:408013840085:web:ee433a58b31f16e0d68c5c"
};
  // Initialize Firebase
firebase.initializeApp(Config);

var firestore = firebase.firestore ();

const docRef = firestore.doc("Users/#name");
const outputHeader = document.querySelector("#hotdogstatus");
const inputName = document.querySelector("#name");
const inputPlasma = document.querySelector("#plasma");
const inputBP = document.querySelector("#bp");
const inputTriceps = document.querySelector("#triceps");
const inputInsulin = document.querySelector("#insulin");
const inputBMI = document.querySelector("#bmi");
const getResult = document.querySelector("#Get_result");

getResult.addEventListener("click", function () {
    const nameToSave = inputName.value;
    const plasmaToSave = inputPlasma.value;
    const bpToSave = inputBP.value;
    const tricepsToSave = inputTriceps.value;
    const insulinToSave = inputInsulin.value;
    const bmiToSave = inputBMI.value;

    console.log("I am going to save "+nameToSave+" in Firestore.");
    docRef.set({
        Name: nameToSave,
        Plasma: plasmaToSave,
        BP: bpToSave,
        Triceps: tricepsToSave,
        Insulin: insulinToSave,
        BMI: bmiToSave
        
    }).then(function(docRef) {
        console.log("Data written successfully.");
    }).catch(function(error) {
        console.error("Error adding data: ", error);
    });
})


