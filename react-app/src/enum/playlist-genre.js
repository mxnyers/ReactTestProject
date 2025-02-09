async function getPlaylistGenres() {
    try {
        const apiResponse = await fetch('http://127.0.0.1:5000/playlist_genres');
        if(!apiResponse.ok){
            throw new Error(`HTTP error! Status: ${apiResponse.status}`);
        }
        const apiData = await apiResponse.json();
        const genres = apiData.map(item => ({ ...item}));
        // console.log(PlatlistGenre)
        return genres;
    }catch (error) {
        console.error("Error fetching playlist_genres table. the following error was given:", error);
        return [];
    }
}

export { getPlaylistGenres };
