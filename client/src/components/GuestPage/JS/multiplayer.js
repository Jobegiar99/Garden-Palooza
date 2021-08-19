import { io } from "socket.io-client";

const socketUrl = process.env.NODE_ENV === 'production' ? 'https://gardenpalooza.tech/' : 'http://localhost:5000';
console.log("Connecting to socket server at " + socketUrl);
let socket = io.connect(socketUrl);

export default socket

