import React from "react";
import Phaser from "phaser";
import config from "./JS/phaserJS/game";
import socket from "./JS/multiplayer.js"
import {
  Container,
  Wrap,
  Window,
  Chat
} from "./GuestPage";

// CHAT COMPONENT
const ChatWrapper = () => {
  const [message, setMessage] = React.useState('')
  const [chats, setChats] = React.useState([
    {username: 'Server', message: 'Welcome to Garden Palooza!'},
    {username: 'Server', message: 'We hope you enjoy your stay.'},
  ])

  const handleMessage = (e) => {
      var newMessage = e.currentTarget.value
      // console.log(newMessage)
      setMessage(newMessage)
  }
    
  const listener = (message) => {
    console.log("new message ", message);
    setChats([...chats, message]);
  }

  React.useEffect(() => {
    socket.on("response", listener);
    return () => {
      socket.off("response", listener)
    }
  });


  return (
    <Chat>
      {
        chats.map(chat => (
          <div>{chat.username}: {chat.message}</div>
        ))
      }
      <form onSubmit={(e) => {
        e.preventDefault()
        const formData = new FormData(e.target)
        const message = formData.get('message')
        setChats([...chats, {username: 'Guest', message}]);
        socket.emit("chat", {username: 'Guest', message});
        setMessage("")
      }}>
        <input type="text" name="message" value={message} onChange={handleMessage} />
        <button>Send Message</button>
      </form>
    </Chat>
  )
}


//GAME COMPONENT
const GuestPage = () => {

  React.useEffect(()=>{
    window.game = new Phaser.Game(config);
  },[])

  return (
    <>
      <Container>
        <Wrap>
            <Window id="phaser"/>
            <ChatWrapper />
        </Wrap>
      </Container>
    </>
  );
};


export default GuestPage;
