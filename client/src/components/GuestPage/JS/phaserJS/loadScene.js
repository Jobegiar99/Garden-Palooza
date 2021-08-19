import Phaser from 'phaser';
import socket from '../multiplayer'

class LoadScene extends Phaser.Scene
{
    constructor ()
    {
      super({key:"LoadScene"});
    }

    preload(){
      this.load.spritesheet('loadingImage','assets/loading.png',{frameWidth: 300, frameHeight: 300});
    }

    create ()
    {
      this.anims.create({
        key: 'loadingAnim',
        frames: this.anims.generateFrameNumbers('loadingImage', { start: 0, end: 7 }),
        frameRate: 10,
        repeat: -1
      });

      let loadImage = this.physics.add.sprite(816/2,624/2,'loadingImage')
      loadImage.anims.play('loadingAnim',true);
      var self = this
      socket.emit('gameLoaded', 'ok', (level) => {
        self.game.level = level;
        self.scene.start('Garden', { level });
      });
    }
}


export default LoadScene;
