// import React, { useEffect } from "react";
// import LoadScene from './JS/phaserJS/loadScene';
// import MainScene from './JS/phaserJS/mainScene';
// import Phaser from 'phaser';
// import { IonPhaser } from '@ion-phaser/react'
// import './Guest.css'

// class BootScene extends Phaser.Scene {
//   create() {
//     this.scene.add("LoadScene", LoadScene, true);
//     this.scene.add("MainScene", MainScene, true);

//     this.scene.run("LoadScene");
//   }
// }

// const config = {
//   type: Phaser.AUTO,
//   parent: 'phaser',
//   width: 800,
//   height: 600,
//   scene: [ BootScene ]
// };

// const GuestPage = React.memo(() => {

//   const gameRef = React.useRef(null)
//   // Call `setInitialize` when you want to initialize your game! :)
//   const [initialize, setInitialize] = React.useState(false)
//   const destroy = () => {
//     if (gameRef.current) {
//       gameRef.current.destroy()
//     }
//     setInitialize(false)
//   }

//   return (
//     <>
//       <IonPhaser ref={gameRef} game={config} initialize={initialize} />
//       <button onClick={() => setInitialize(true)}>Initialize</button>
//       <button onClick={destroy}>Destroy</button>
//     </>
//   )
// });

// export default GuestPage;

//DO NOT DELETE CODE ABOVE:
//WORKING CODE THAT shows the game screen in the window so the team 
//can continue building game


import React from "react";
import Phaser from "phaser";
import config from "./JS/phaserJS/game";
import {
  Container,
  Wrap,
  Window,
  Chat
} from "./GuestPage";

let game = new Phaser.Game(config);


const GuestPage = () => {

//   useEffect(()=>{
//   const game = new Phaser.Game(config);
//     new Phaser.Game(config);
//   },[])

  return (
    <>
      <Container>
        <Wrap>
            <Window id="phaser"/>
        </Wrap>
      </Container>
      <Chat>
          <div>Chat Window Sample</div>
        </Chat>
    </>
  );
};

export default GuestPage;
