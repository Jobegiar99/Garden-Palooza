import Phaser from 'phaser';
import matrix from "../matrixInfo"



class MainScene extends Phaser.Scene
{
    constructor ()
    {
        super("App");
        this.updateMap = false;
        this.level = matrix;
    }

    preload ()
    {
      this.load.image("gardenTile","assets/free.png");
    }

    create ()
    {

      let map = this.make.tilemap({ data: this.level, tileWidth: 16, tileHeight: 16 });
      let tiles = map.addTilesetImage('gardenTile');
      let layer = map.createLayer(0, tiles, 0, 0).setInteractive();
      let info = this.level;

      layer.on('pointerdown', function (pointer ) {
           
        let display = document.getElementById("hola")
        let xP = Math.floor(pointer.downX);
        let yP = Math.floor(pointer.downY);
        layer.getTileAtWorldXY(xP,yP).index = 24;
       
      });
    }
}

const config = {
  type: Phaser.AUTO,
  parent: 'phaser-example',
  width: 816,
  height: 624,
  scene: MainScene
};

const game = new Phaser.Game(config);


export default MainScene;
