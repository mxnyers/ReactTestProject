import { useForm, Controller } from "react-hook-form"
import TextField from '@mui/material/TextField';
import Select from '@mui/material/Select';
import { FormControl, InputLabel, MenuItem } from "@mui/material";
import { PlatlistGenre } from "../enum/playlist-genre.js";
import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

const AddPlaylists = () => {
    const { control, handleSubmit } = useForm()
    const { control: modalControl, handleSubmit: handleModalSubmit } = useForm()
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    const style = {
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 400,
        bgcolor: 'background.paper',
        border: '2px solid #000',
        boxShadow: 24,
        p: 4,
    };

    const onSubmit = (data) => {
        if (data.genre === "new") {
            // Open Modal
            handleOpen()
        }
        else {
            console.log(data)
        }

    }

    const onModalSubmit = (modalData) => {
        console.log()
        PlatlistGenre.splice(-1, 0, modalData)
        PlatlistGenre.forEach(element => {
            if (element.id === modalData.id) console.log(element);
        });
        console.log()
        handleClose()
    }


    return (
        <div>
            <form onSubmit={handleSubmit(onSubmit)} className="add-playlist-form">
                <div className="row">
                    <label>Playlist Information</label>
                </div>
                <div className="general-playlist-info">
                    <div className="row">
                        <div className="controller-container">
                            <Controller
                                name="playlistName"
                                control={control}
                                defaultValue=""
                                render={({ field }) =>
                                    <TextField
                                        label="Playlist Name"
                                        {...field} />}
                            />
                        </div>
                        <div className="controller-container">
                            <Controller
                                name="social"
                                control={control}
                                defaultValue=""
                                render={({ field }) =>
                                    <TextField
                                        label="Social Media"
                                        {...field} />}
                            />
                        </div>
                    </div>
                    <div className="row">
                        <div className="controller-container">
                            <Controller
                                name="email"
                                control={control}
                                defaultValue=""
                                render={({ field }) =>
                                    <TextField
                                        label="Email"
                                        {...field} />}
                            />
                        </div>
                        <div className="controller-container">
                            <Controller
                                name="genre"
                                control={control}
                                defaultValue=""
                                render={({ field }) => (
                                    <FormControl>
                                        <InputLabel>Playlist Genre</InputLabel>
                                        <Select
                                            label="Playlist Genre"
                                            variant="outlined"
                                            {...field}>

                                            {Object.keys(PlatlistGenre).map(key => (
                                                <MenuItem key={key} value={PlatlistGenre[key].id}>{PlatlistGenre[key].string}</MenuItem>
                                            ))}
                                            {/* <MenuItem value="sad">Sad Playlist</MenuItem>
                                        <MenuItem value="hard">Hard Playlists</MenuItem>
                                        <MenuItem value="euphoric">Euphoric Playlists</MenuItem> */}
                                        </Select>
                                    </FormControl>

                                )}
                            />
                        </div>
                    </div>
                </div>
                <div className="row mt-3">
                    <label>
                        Additional Information
                    </label>
                </div>
                <div className="general-playlist-info">
                    <div className="row">
                        <label>No Info to Add</label>
                    </div>
                    <div className="row">
                        <label>No Info to Add</label>
                    </div>
                </div>
                <div className="button-container">
                    <input type="submit" />
                </div>
            </form>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <Typography id="modal-modal-title" variant="h6" component="h2">
                        Create a New Genre
                    </Typography>
                    <form onSubmit={handleModalSubmit(onModalSubmit)} className="add-playlist-form">
                        <label>Playlist Information</label>
                        <div className="general-playlist-info">
                            <div className="row">
                                <div className="controller-container">
                                    <Controller
                                        name="id"
                                        control={modalControl}
                                        defaultValue=""
                                        render={({ field }) =>
                                            <TextField

                                                label="Playlist ID"
                                                {...field} />}
                                    />
                                </div>
                                <div className="controller-container">
                                    <Controller
                                        name="string"
                                        control={modalControl}
                                        defaultValue=""
                                        render={({ field }) =>
                                            <TextField
                                                label="Playlist Name"
                                                {...field} />}
                                    />
                                </div>
                            </div>
                        </div>
                        <input type="submit" />
                    </form>
                </Box>
            </Modal>
        </div>
    )
}

export default AddPlaylists;