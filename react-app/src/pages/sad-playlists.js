
import React, { Component } from 'react';

class SadPlaylists extends Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
      isLoaded: false,
    }
  }

  componentDidMount() {
    fetch('http://127.0.0.1:5000/sad-playlists')
      .then(res => res.json())
      .then(json => {
        this.setState({
          isLoaded: true,
          items: json,
        })
      });
  }

  render() {
    var { isLoaded, items } = this.state;

    if (!isLoaded) {
      return <div>Loading...</div>;
    }

    else {
      return (
        <div className="App">
          <ul>
            {items.map(item => (
              <li key={item.id}>
                Playlist Name: {item.playlist_name} | Contact: {item.email} {item.social_media}   
              </li>
            ))}
          </ul>
        </div>
      );
    };
  };
}
  
export default SadPlaylists;