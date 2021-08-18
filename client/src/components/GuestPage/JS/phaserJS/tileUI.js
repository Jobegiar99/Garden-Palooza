import Phaser from 'phaser';

class TileUI extends Phaser.Scene
{
    constructor ()
    {
      debugger
        super({key: "TileUI"});
    }

    init(data){

      this.tileInfo = data;
      console.log("DATA",data)
      
    }

    preload ()
    {
      debugger
      this.load.image('button','assets/plantUIButton.png');
      this.load.image('background','assets/plantUIBackground.png');
    }

    create ()
    {
      //Variables that will be used ahead
      let groundSprites = [2363,2483,2484,2485]
      let grassSprites = [2420,2186,2187, 2306,2307,2308,2309,2310]
      let seeds = [ 2609, 2610, 2611];

      let self = this;

      let row = self.tileInfo.row;
      let column = self.tileInfo.column;
      let currentSprite = self.tileInfo.spriteIndex;


      let tileFree = ( (groundSprites.includes(currentSprite)) || (grassSprites.includes(currentSprite)));
      let needToWater = false;
      let needToDisinfect = false;
      let tileAlive = true;

      let level = self.game.level;
      level.playerRow = self.tileInfo.playerX;
      level.playerColumn = self.tileInfo.playerY;

      let tileStatus = {'tileFree': tileFree, 'tileAlive': tileAlive, 'needToWater':needToWater,'needToDisinfect': needToDisinfect}
      this.add.image(430,200,'background');
      
      //PLANT SOMETHING BUTTON
      {
        let plantSomethingButton = this.add.image(20,40,'button');
        plantSomethingButton.setScale(0.3,0.15);
        plantSomethingButton.setOrigin(0,0);
        plantSomethingButton.setInteractive();
        let plantSomethingButtonText = this.add.text(70,85,"   Plant \n Something");
        plantSomethingButtonText.setFontSize(30);

        if( !tileStatus['tileFree'] ){
          plantSomethingButton.visible = false;
          plantSomethingButtonText.visible = false;
        }

        plantSomethingButton.on('pointerup',() =>{
          
          self.game.level.secondLayer[row][column] = seeds[Math.floor(Math.random() * seeds.length)];;

          self.scene.stop('TileUI');
          self.scene.start("Garden",{level});
        });
      }

      //WATER THE PLANT BUTTON
      {
        let waterButton = this.add.image(20,250,'button');
        waterButton.setScale(0.3,0.15);
        waterButton.setOrigin(0,0);
        waterButton.setInteractive();
        let waterButtonText = this.add.text(39,306,"Water the Plant");
        waterButtonText.setFontSize(30);

        if( !tileStatus['needToWater'] ){
          waterButton.visible = false;
          waterButtonText.visible = false;
        }
      }

      //REMOVE PLANT BUTTON
      {
        let removePlant = this.add.image(496,40,'button');
        removePlant.setScale(0.3,0.15);
        removePlant.setOrigin(0,0);
        removePlant.setInteractive();
        let removePlantText = this.add.text(545,90,"Remove Plant");
        removePlantText.setFontSize(30);

        if( tileStatus['tileAlive'] ){
          removePlant.visible = false;
          removePlantText.visible = false;
        }
      }

      //DISINFECT BUTTON
      {
        let disinfectButton = this.add.image(496,250,'button');
        disinfectButton.setScale(0.3,0.15);
        disinfectButton.setOrigin(0,0);
        disinfectButton.setInteractive();
        let disinfectButtonText = this.add.text(515,306,"Disinfect Plant");
        disinfectButtonText.setFontSize(30);

        if( !tileStatus['needToDisinfect'] ){
          disinfectButton.visible = false;
          disinfectButtonText.visible = false;
        }
      }

      //RETURN BUTTON
      {
        let returnButton = this.add.image(250,450,'button');
        returnButton.setScale(0.3,0.15);
        returnButton.setOrigin(0,0);
        returnButton.setInteractive();
        let returnButtonText = this.add.text(240,490,"      Return\n    (Do nothing)");
        returnButtonText.setFontSize(30);
        
        returnButton.on('pointerup', () =>{
            
            this.scene.stop("TileUI");
            this.scene.start("Garden",{level});
        
        });
      }
    }
}

export default TileUI;