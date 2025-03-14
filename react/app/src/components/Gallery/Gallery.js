import React from 'react';

import './Gallery.css';
import AppNavigation from "../AppNavigation/AppNavigation";


class Gallery extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            images: [],
            images_page_num: 1,
        };
    }

    upload_images() {
        fetch(`http://0.0.0.0:80/api/images/`)
            .then(response => response.json())
            .then(response => this.setState({images: response.results}));
    }

    componentDidMount() {
        this.upload_images();
    }

    render() {

        let getImages = () => {
            return (
                <div className="Gallery__image-list">
                    {
                        this.state.images.length > 0
                            ? this.state.images.map((image, i) => {
                                return (
                                    <img key={image.uuid}
                                         className="Gallery__image-list-item"
                                         src={image.file}
                                         alt={image.uuid}

                                    />
                                )})
                            : <p>Нет загруженных изображений</p>
                    }
                </div>
            );
        }

        return (
            <div>
                <AppNavigation/>
                <div className="Gallery__container">
                    {getImages()}
                </div>
            </div>
        );
    }
}

export default Gallery;
