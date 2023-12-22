import React, { Component } from 'react';
import Footer from './common-componenets/footer';
import Navbar from './common-componenets/navbar';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
// import Users from './pages/users';
import SadPlaylists from './pages/sad-playlists'
import AddPlaylists from './pages/add-playlist';
import './App.css'
import Home from './pages/home';

class App extends Component {

  render() {  
      return (
        <Router>
          <Navbar />
          <div className='app'>
            <Routes>
              <Route exact path="/" element={<Home />} />
              {/* <Route path="/users" element={<Users />} /> */}
              <Route exact path="/playlists/sad" element={<SadPlaylists />} />
              <Route exact path='/add-playlist' element={<AddPlaylists />} />
            </Routes>
          </div>
          <Footer />
        </Router>
      );
  }
}

export default App;
