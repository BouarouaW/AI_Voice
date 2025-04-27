$(document).ready(function () {

    // Appelle une fonction exposée en Python si elle existe
    // eel.init(); <-- à commenter ou supprimer si non définie en Python

    $('.text').textillate({
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
        width: 640,
        height: 200,
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true
        },
        out: {
            effect: "fadeInUp",
            sync: true
        },
    });

    // mic button click
    $("#MicBtn").click(function () {
        eel.playAssistantSound(); // sans ()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands();
    });

});
