import Phaser from 'phaser';
import socket from "../multiplayer";
import AStar from './Astar';
class Garden extends Phaser.Scene
{
    constructor ()
    {
      super({key: "Garden"});
    }

    init(levelTiles){
      let levelInfo = levelTiles.level;
      this.game.level = levelInfo
      this.firstLayer = levelInfo.firstLayer;
      this.secondLayer = levelInfo.secondLayer;
      this.playerRow = levelInfo.playerRow;
      this.playerColumn = levelInfo.playerColumn;
    }

    preload ()
    {
      debugger
      this.load.image("gardenTile","assets/global.png");
      this.load.image("playerStill","assets/characterStill.png");
      this.load.spritesheet('playerMovement','assets/characterMovementSheet.png',{frameWidth:32, frameHeight:48});
    }

    create ()
    {
          
      //TILEMAP
      let map = this.make.tilemap({ data: this.firstLayer, tileWidth: 16, tileHeight: 16 });
      let map2 = this.make.tilemap({ data: this.secondLayer, tileWidth: 16, tileHeight: 16 })
      let tiles = map.addTilesetImage('gardenTile');
      let tiles2 = map2.addTilesetImage('gardenTile');
      let layer = map.createLayer(0, tiles, 0, 0)
      this.game.layer2 = map2.createLayer(0,tiles2,0,0).setInteractive();

      let notValidClickTiles = [2717,2896, 2897, 2898, 2899]

      //PLAYER ANIMATIONS
      this.anims.create({
        key: 'up',
        frames: this.anims.generateFrameNumbers('playerMovement', { start: 0, end: 3 }),
        frameRate: 10,
        repeat: -1
      });

      this.anims.create({
        key: 'down',
        frames: this.anims.generateFrameNumbers('playerMovement', { start: 12, end: 15 }),
        frameRate: 10,
        repeat: -1
      });

      this.anims.create({
        key: 'sides',
        frames: this.anims.generateFrameNumbers('playerMovement', { start: 8, end: 11 }),
        frameRate: 10,
        repeat: -1
      });

      this.game.player = this.physics.add.sprite(8,8,'playerStill')
      this.game.player.originY = 0.8;
      if( this.playerRow != null){
        this.game.player.x = this.playerRow ;
        this.game.player.y = this.playerColumn - 14.4;
      }

      this.game.cursors = this.input.keyboard.createCursorKeys();

      var self = this;
      this.game.layer2.on('pointerup', function (pointer ) {
          let row = Math.floor(pointer.downX);
          let column = Math.floor(pointer.downY);
          let spriteIndex = self.game.layer2.getTileAtWorldXY(row,column).index;
          if( !notValidClickTiles.includes(spriteIndex)){
            
            let levelInformation = {
              startRow: Math.floor(self.game.player.y / 16),
              startCol: Math.floor(self.game.player.x / 16),
              endRow: Math.floor(column / 16),
              endColumn: Math.floor(row / 16),
              levelMatrix: self.firstLayer
            };

          
            self.game.path = new AStar().getPath(levelInformation.startRow, levelInformation.startCol, levelInformation.endRow, levelInformation.endColumn, levelInformation.levelMatrix);          
            if( !self.game.player.anims.isPlaying && self.game.path[0] != "NO PATH"){
               self.game.player.y += 14.4;
            }
          }    
      });
    }

    update(){
      if( this.game.path != null && this.game.path.length > 0 ){

        let moveSpeed = 1;

        let move = this.game.path[this.game.path.length - 1];
        console.log(move)
        if( move == "NO PATH"){
          this.game.player.anims.stop();
          return;
        }
        let playerX = this.game.player.x;
        let playerY = this.game.player.y;

        //matrix information
        let playerRow = Math.floor(playerY  / 16) ;
        let playerColumn = Math.floor( playerX  / 16) ;

        
        if(move != "STOP"){

          if (move[0] == playerRow) {

            if(move[1] < playerColumn){
              this.game.player.x -= moveSpeed;
              this.game.player.anims.play('sides',true);
              this.game.player.flipX = true;

            }
            
            else if( move[1] > playerColumn){
              this.game.player.x += moveSpeed;
              this.game.player.anims.play('sides',true);
              this.game.player.flipX = false;
            }
            
            else{
              this.game.path.pop();
            }

          }

          else if (move[0] < playerRow) {
            this.game.player.y -= moveSpeed;
            this.game.player.anims.play('down',true);
          }

          else {
            this.game.player.y += moveSpeed;
            this.game.player.anims.play('up',true);
          }

        }else if (move == "STOP"){

            this.game.path.pop();

            let spriteIndex = this.game.layer2.getTileAtWorldXY(playerX,playerY).index;
            let firstLayer = this.firstLayer;
            let secondLayer = this.secondLayer
            this.game.player.anims.stop();
            this.scene.stop('Garden')
            
            this.scene.start('TileUI', {
                    
                                          row: playerRow, 
                                          column: playerColumn , 
                                          spriteIndex: spriteIndex, 
                                          firstLayer: firstLayer,
                                          secondLayer: secondLayer ,
                                          playerX: playerX,
                                          playerY: playerY
                                       });
        }
      }
    }
}


export default Garden;
