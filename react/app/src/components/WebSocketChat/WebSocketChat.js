import React, {useState} from 'react';
import useWebSocket, {ReadyState} from 'react-use-websocket';

import './WebSocketChat.css';

const WSLogsSocketURL = "ws://0.0.0.0:80/ws/logs/uploading/";


export const WebSocketChat = () => {
    const [messages, setMessages] = useState([]);

    function handleOnStart(event) {
        // get last messages
    }

    function handleOnMessage(event) {
        setMessages(previous => [...previous, JSON.parse(event.data)]);
        if (messages.length > 10) {
            let element = document.querySelector('.WebSocketChat__log-list');
            element.removeChild(element.firstChild);
        }
    }

    const {readyState} = useWebSocket(
        WSLogsSocketURL,
        {
            onOpen: (e) => handleOnStart(),
            onMessage: (e) => handleOnMessage(e),
            onError: (e) => alert(e),
        }
    );

    const connectionStatus = {
        [ReadyState.CONNECTING]: 'Connecting',
        [ReadyState.OPEN]: 'Open',
        [ReadyState.CLOSING]: 'Closing',
        [ReadyState.CLOSED]: 'Closed',
        [ReadyState.UNINSTANTIATED]: 'Uninstantiated',
    }[readyState];

    return (
        <div className="WebSocketChat__container">
            <p className="WebSocketChat__header-text">{
                connectionStatus
                    ? 'Установлено подключение'
                    : 'Нет подключения'
            }</p>
            <hr/>
            <div className="WebSocketChat__log-list">
                {messages.map((message, idx) => (
                    <p className="WebSocketChat__log-list-item" key={idx}>
                        В базе создан объект с идентификатором <b>{message.uuid}</b>,
                        в облачном сервисе файл доступен по ссылке <b>{message.url}</b>
                    </p>
                ))}
            </div>
        </div>
    );
};
