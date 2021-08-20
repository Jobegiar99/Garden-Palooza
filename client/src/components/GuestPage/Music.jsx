import React from 'react';
import song from "./Garen_Palooza.mp3"

function Player() {
  let audio = new Audio(song)

  const start = () => {
    audio.play()
  }

  return (
    < div >
      {/* <button onClick={start}>Play</button> */}
      <audio
        autoPlay={true}
        loop={true}
        // controls={true}
        >
  <source type="audio/mp3" src={song} />
</audio>
    </div >
  );
}

export default Player