import Phaser from "phaser";
import Garden from "./garden";
import TileUI from "./tileUI";
import LoadScene from "./loadScene";

const config = {
    type: Phaser.AUTO,
    parent: 'phaser',
    width: 816,
    height: 624,
    scene: [ LoadScene,Garden,TileUI],
    physics: {
        default: 'arcade',
        arcade: {
          enableBody: true,
        }
    }
};


export default config;