import React, {useState} from "react";
import {FileUploader} from "react-drag-drop-files";
import LoadingBar from "react-top-loading-bar";

import './Loader.css';
import AppNavigation from "../AppNavigation/AppNavigation";
import {WebSocketChat} from "../WebSocketChat/WebSocketChat";

const fileTypes = ["JPG", "PNG", "GIF"];
const uploadURL = "http://0.0.0.0:80/api/images/";


export default function Loader() {
    const [submitting, setSubmitting] = useState(false);
    const [progress, setProgress] = useState(0);
    const [file, setFile] = useState(null);

    const handleLoaderChange = (file) => {
        setFile(file);
        setSubmitting(true);
    };

    const reset = () => {
        setSubmitting(false);
        setProgress(0);
        setFile(null);
    };

    const upload = (file: File, url: string, options?: { onProgress?: (progress: number) => void }): Promise => {
        return new Promise((resolve, reject) => {
            const xhr = new XMLHttpRequest();

            xhr.open('POST', url);

            xhr.upload.onprogress = function (event) {
                console.log(Math.round((event.loaded / event.total) * 100));
                setProgress(Math.round((event.loaded / event.total) * 100));
            }

            const myData = new FormData();
            myData.append('file', file);

            xhr.send(myData);
        })
    }

    const handleFormSubmit = (e) => {
        e.preventDefault();
        const uploading = upload(file, uploadURL);
        uploading
            .finally(reset)
    };

    return (
        <div>
            <LoadingBar
                color="#f11946"
                height={10}
                progress={progress}
                onLoaderFinished={() => setProgress(0)}
            />
            <AppNavigation/>
            <div className="Loader__container">
                <h2>Загрузчик</h2>
                <form className="Loader__form" onSubmit={handleFormSubmit}>
                    <FileUploader
                        handleChange={handleLoaderChange}
                        name="file"
                        types={fileTypes}
                        label="Загрузите или перетащите файл"
                        uploadedLabel="Файл выбран"
                        // maxSize="10"
                        onSizeError={() => alert("Неподходящий размер файла")}
                        onTypeError={() => alert("Неподходящий тип файла")}
                    />
                    <p>{file ? `Название файла: ${file.name}` : "нет загруженных файлов"}</p>
                    <button
                        className="Loader__submit-button"
                        type='submit'
                        disabled={!submitting}
                    >{
                        progress > 0
                            ? <p>Загрузка {progress} %</p>
                            : <p>Загрузить на сервер</p>
                    }
                    </button>
                </form>
                <div className="Loader__log-block">
                    <WebSocketChat />
                </div>
            </div>
        </div>
    );
}
