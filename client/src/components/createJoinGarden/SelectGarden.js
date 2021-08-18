import React from "react";
import * as BS from "react-bootstrap";
import GardenCard  from "./gardenCard";
export default class SelectGarden extends React.Component{
    render(){
        
        let gardens = this.props.gardens;
        let cards = [];
        
        for( let i = 0; i < gardens.length; i++){

            cards.push(
                <div>
                    <GardenCard
                        gardenName = {gardens[i]}
                    />
                    <br></br> 
                </div>);
        }
    
        return(
            <BS.Container align = "center" style = {{overflow: "auto"}}>
    
                {cards}
            </BS.Container>
        )
    }
}