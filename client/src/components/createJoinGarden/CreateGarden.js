import React, {Component} from "react";
import * as BS from "react-bootstrap";
import {io} from "socket.io-client";

export default class CreateGarden extends React.Component{

    constructor(){
        super();
        this.state = {
            gardenName: ""
        };
    }

    updateInput = (event) =>{
        this.setState({ [event.target.name] : event.target.value});
    }

    createLevel = () => {
        console.log(this.state.gardenName)
        
    }

    render(){
        return(
            <BS.Container align = "center">

                <BS.Form>
                    <BS.Row>
                        <BS.FormLabel>
                            Garden Name
                        </BS.FormLabel>
                    </BS.Row>
                    <br></br>
                    <br></br>
                    <BS.Row>
                        <input 
                            name = "gardenName" 
                            maxLength = "30"
                            type = "text"
                            value = {this.state.commentBody} 
                            onChange = {this.updateInput}/>
                    </BS.Row>
                    <br></br>
                    <br></br>
                    <BS.Row>
                        <BS.Button onClick = {this.createLevel}>
                            Submit
                        </BS.Button>
                    </BS.Row>
                    <br></br>
                    <br></br>
                </BS.Form>

            </BS.Container>
        )
    }

}