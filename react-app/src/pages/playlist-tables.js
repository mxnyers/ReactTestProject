
import React, { Component } from 'react';
import DataTable from 'react-data-table-component';
import axios from 'axios';

class PlaylistPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
      isLoaded: false,
      data: null,
      error: null
    };
  }

  componentDidMount() {
    this.fetchData();
  }

  fetchData() {
    const { id } = this.props;
    this.setState({ isLoaded: true });

    axios.get(`http://127.0.0.1:5000/playlist/${id}`)
      .then(response => {
        this.setState({
          data: response.data,
          isLoaded: false
        });
      })
      .catch(error => {
        this.setState({
          error: error,
          isLoaded: false
        })
      })
        .then(res => res.json())
        .then(json => {
          this.setState({
            isLoaded: true,
            items: json,
          })
        });
      }


  // componentDidMount() {
  //   /*Mount table to given ID */
  //   fetch(`http://127.0.0.1:5000/${id}`)
  //     .then(res => res.json())
  //     .then(json => {
  //       this.setState({
  //         isLoaded: true,
  //         items: json,
  //       })
  //     });
  // }

  render() {
        var { isLoaded, items } = this.state;
        const columns = [
          {
            name: "Playlist Name",
            selector: row => row.playlist_name,
            sortable: true
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

    if(!isLoaded) {
          return <div>Loading...</div>;
        }

    else {
          return(
        <div className = "playlist-table" >
              <DataTable
                columns={columns}
                data={items}
                selectableRows
                fixedHeader
              />
        </div>
      );
  };
};
}

export default PlaylistPage;