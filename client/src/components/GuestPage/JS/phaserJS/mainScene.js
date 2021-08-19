import Phaser from 'phaser';

class MainScene extends Phaser.Scene
{
    constructor ()
    {
      super("App");
      this.updateMap = false;
    }

    init (data)
    {
      this.level = data.level
    }

    preload ()
    {
      this.load.image("gardenTile","/assets/global.png");
    }

    create ()
    {

      let map = this.make.tilemap({ data: this.level, tileWidth: 16, tileHeight: 16 });
      let tiles = map.addTilesetImage('gardenTile');
      let layer = map.createLayer(0, tiles, 0, 0)
      layer.setInteractive();
      let info = this.level;

      layer.on('pointerdown', function (pointer ) {
           
        let display = document.getElementById("hola");
        let xP = Math.floor(pointer.downX);
        let yP = Math.floor(pointer.downY);
        layer.getTileAtWorldXY(xP,yP).index = 24;
       
      });
    }
}


export default MainScene;
