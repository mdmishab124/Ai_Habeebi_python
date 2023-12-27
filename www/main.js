// $(document).ready(function () {

//     $('.text').textillate({
//         loop: true,
//         sync: true,
//         in: {
//             effect: "bounceIn",
//         },
//         out: {
//             effect: "bounceOut",
//         },

//     });

//     // Siri configuration
//     var siriWave = new SiriWave({
//         container: document.getElementById("siri-container"),
//         width: 800,
//         height: 200,
//         style: "ios9",
//         amplitude: "1",
//         speed: "0.30",
//         autostart: true
//       });

//       // Siri message animation
//     $('.siri-message').textillate({
//         loop: true,
//         sync: true,
//         in: {
//             effect: "bounceIn",
//             sync: false,
//         },
//         out: {
//             effect: "bounceOut",
//             sync: false,
//         },

//     });

//     // Speech recognition setup
//     const recognition = new webkitSpeechRecognition();
//     recognition.continuous = true;
//     recognition.lang = 'en-in';

//     recognition.onresult = function (event) {
//         const transcript = event.results[event.results.length - 1][0].transcript.trim().toLowerCase();

//         // Check if the transcript contains the keyword "habibi"
//         if (transcript.includes('habibi')) {
//             // Show SiriWave section and hide Oval section
//             $('#Oval').attr('hidden', 'true');
//             $('#SiriWave').removeAttr('hidden');

//             // Restart Siri message animation
//             $('.siri-message').textillate('in');

//             eel.takecommand()()
//         }
//     };

//     // Start speech recognition
//     recognition.start();

//     function js_function_to_show_siriwave() {
//         $('#SiriWave').removeAttr('hidden');
//     }
// });

$(document).ready(function () {
  // ... (existing code)

  $(".text").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "bounceIn",
    },
    out: {
      effect: "bounceOut",
    },
  });

  // Siri configuration
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude: "1",
    speed: "0.30",
    autostart: true,
  });

  // Siri message animation
  $(".siri-message").textillate({
    loop: true,
    sync: true,
    in: {
      effect: "bounceIn",
      sync: false,
    },
    out: {
      effect: "bounceOut",
      sync: false,
    },
  });
});
