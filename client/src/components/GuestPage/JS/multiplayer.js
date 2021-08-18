import { io } from "socket.io-client";

console.log("Connecting to socket server at " + process.env.REACT_APP_SOCKET_URL);
let socket = io.connect(process.env.REACT_APP_SOCKET_URL);

export default socket

