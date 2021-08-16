import { io } from "socket.io-client";

let socket = io.connect('http://' + document.domain + ':443/socket');

export default socket

