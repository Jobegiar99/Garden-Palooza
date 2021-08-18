import React, {Component} from "react";
import * as BS from "react-bootstrap";

export default class GardenCard extends React.Component{
    render(){

        return(
            <BS.Card align = "center" style = {{ backgroundColor: "#4D82E1", border: "1px inset #30589E"}} >
                <br></br>
                <BS.Card.Title>
                    {this.props.gardenName}
                </BS.Card.Title>
                <BS.Card.Body>
                    <br></br>
                    <BS.Button>
                        JOIN
                    </BS.Button>
                </BS.Card.Body>
                <br></br>
            </BS.Card>
        )
    }
}