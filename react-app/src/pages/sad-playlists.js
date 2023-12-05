
import React, { Component } from 'react';
import DataTable from 'react-data-table-component'

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
    const columns = [
      {
        name: "Playlist Name",
        selector: row => row.playlist_name
      },
      {
        name: "Email",
        selector: row => row.placement_email
      },
      {
        name: "Social Media",
        selector: row => row.social_media
      },
      {
        name: "Approved Song",
        selector: row => row.approved_song
      }

    ]

    if (!isLoaded) {
      return <div>Loading...</div>;
    }

    else {
      return (
        <div className="App">
          {/* <ul>
            {items.map(item => (
              <li key={item.id}>
                Playlist Name: {item.playlist_name} | Contact: {item.email} {item.social_media}   
              </li>
            ))}
          </ul> */}
          <DataTable columns={columns} data={items} selectableRows />;
        </div>
      );
    };
  };
}
  
export default SadPlaylists;