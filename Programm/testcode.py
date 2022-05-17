import playsound

bool engineRunning = false;

if(btnLock.Clicked){
playsound.playsound('../Sounds/KeyLock.mp3')
}

if(btnStartup.Clicked){
    if(engineRunning == false){
        playsound.playsound('../Sounds/StartupSound.mp3')
        engineRunning = True;
    }
    if(engineRunning == true){
        engineRunning = False;
    }
}
