import styled from 'styled-components';


export const Container = styled.div`
`;

export const Wrap = styled.div`
position: relative;
width: 800px;
margin: 0 auto
`;

export const Window = styled.div`
position: relative;
`

export const Chat = styled.div`
background: white;
z-index: 200;
position: absolute;
bottom: -200px;
right: 0px;
height: 120px;
max-width: 320px;
border: 1px solid black;
display: block;
margin: 20px auto;
overflow: scroll;
padding: 10px;
line-height: 1.5;
font-size: 12px
`
