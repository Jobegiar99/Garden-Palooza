import { io } from "socket.io-client";

let socket = io.connect('https://' + document.domain + '/socket');

export default socket

