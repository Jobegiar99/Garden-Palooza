import { io } from "socket.io-client";

let socket = io.connect(process.env.REACT_APP_SOCKET_SERVER + process.env.REACT_APP_SOCKET_PORT);

export default socket

