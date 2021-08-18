import React, {Component} from "react";
import * as BS from "react-bootstrap";
import CreateGarden from "./CreateGarden";
import SelectGarden from "./SelectGarden";
import {io} from "socket.io-client";

export default class CreateJoinGardenContainer extends React.Component{
    constructor(){
        super();
        let socket = io.connect('http://localhost:5000');
        this.gardens = []

        socket.once('getGardenNames',this.props.username,(gardens)=> {
            this.gardens = gardens;
        });

        this.selectGarden = <SelectGarden gardens = {this.gardens} />
        this.createGarden = <CreateGarden/>

        this.state = {
            currentView: this.selectGarden
        };
    }

    changeToSelectGarden = () =>{
        this.gardens.push("GARDEN_NAME")
        this.setState({  currentView : this.selectGarden});
    }

    changeToCreateGarden = () =>{
        this.setState({ currentView: this.createGarden });
    }
    render(){
        return(
            <BS.Container>
                <BS.Row>

                    <BS.Col>
                        <BS.Button onClick ={this.changeToSelectGarden}>Select Garden</BS.Button>
                    </BS.Col>


                    <BS.Col>
                        <BS.Button onClick = {this.changeToCreateGarden}>Create Garden</BS.Button>
                    </BS.Col>
                </BS.Row>
                {this.state.currentView}
            </BS.Container>
        )
    }
}