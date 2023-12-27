$(document).ready(function () {



    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');

    }

    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#Siriwave").attr("hidden", true);
    }

//     // Function to stop assistant
// function stopAssistant() {
//   $("#Oval").removeAttr("hidden");
//   $("#SiriWave").attr("hidden", "true");
//   // Call Python function to stop assistant
//   eel.takecommand()();
// }

// // Function to start assistant
// function startAssistant() {
//   $("#Oval").attr("hidden", "true");
//   $("#SiriWave").removeAttr("hidden");
//   $(".siri-message").textillate("in");
//   // Call Python function to start assistant
//   eel.takecommand()();
// }

// // Speech recognition setup
// const recognition = new webkitSpeechRecognition();
// recognition.continuous = true;
// recognition.lang = "en-in";

// recognition.onresult = function (event) {
//   const transcript = event.results[event.results.length - 1][0].transcript
//       .trim()
//       .toLowerCase();
  
//   // if (transcript.includes("go to sleep")) {
//   //     // Stop the assistant replies
//   //     stopAssistant();} else 
//   if (transcript.includes("wake up")) {
//       // Resume the assistant replies
//       startAssistant();
//   }
// };

// // Expose functions to start and stop assistant externally
// window.startAssistant = startAssistant;
// window.stopAssistant = stopAssistant;

// // Start speech recognition
// recognition.start();


    // Function to stop SiriWave and go to Oval section
  function stopAssistant() {
    $("#Oval").removeAttr("hidden");
    $("#SiriWave").attr("hidden", "true");
  }

  
  // Function to start SiriWave and show Siri message animation
  function startAssistant() {
    $("#Oval").attr("hidden", "true");
    $("#SiriWave").removeAttr("hidden");
    $(".siri-message").textillate("in");
    eel.takecommand()();
  }

  // Speech recognition setup
  const recognition = new webkitSpeechRecognition();
  recognition.continuous = true;
  recognition.lang = "en-in";

  recognition.onresult = function (event) {
    const transcript = event.results[event.results.length - 1][0].transcript
      .trim()
      .toLowerCase();
     
    // Check if the transcript contains the keyword "habibi"
    if (transcript.includes("go to sleep")) {
       // Stop the assistant replies
       stopAssistant();} 
    else if (transcript.includes("wake up")) {
      // Resume the assistant replies
      startAssistant();
    }
  };

  // Expose functions to start and stop assistant externally
  window.startAssistant = startAssistant;
  window.stopAssistant = stopAssistant;

  // Start speech recognition
  recognition.start();

});