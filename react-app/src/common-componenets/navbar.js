import React, { Component } from 'react';
import logoImage from "./../resources/logo.png"
import hoverImage from "./../resources/black-logo.png"
import { FaCaretDown } from "react-icons/fa";
import { getPlaylistGenres } from "../enum/playlist-genre.js";

class Navbar extends Component {

  constructor(props) {
    super(props);
    this.state = {
      playlistGenres: [],
    };
  }
  async componentDidMount() {
    try {
      const genres = await getPlaylistGenres(); // Await API response
      this.setState({ playlistGenres: genres });
    } catch (error) {
      console.error("Error loading genres", error);
    }
  }

  render() {
    return (
      <div className="navbar">
        <a
          href="/"
          id="logo"
          onMouseOver={e => (e.currentTarget.firstElementChild.src = hoverImage)}
          onMouseOut={e => (e.currentTarget.firstElementChild.src = logoImage)} >
          <img
            src={logoImage}
            alt="home" />
        </a>
        <div className="playlist-dropdown">
          <button className='dropbtn'>Playlists
            <FaCaretDown className='FaCaretDown' />
          </button>
          <div className="playlist-submenu">
            {this.state.playlistGenres.length > 0 ? (
              this.state.playlistGenres.map((item, index) => (
                <a key={index} href={`/playlists/${item.genre}`}>
                  {item.genre}
                </a>
              ))
            ) : (
              <p>Loading...</p>
            )}

          </div>
        </div>
        <a href="/add-playlist" className="right">Add Playlist</a>

      </div>
    );
  }
}

export default Navbar;