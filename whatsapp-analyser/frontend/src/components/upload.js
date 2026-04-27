import axios from 'axios';
import { useState } from 'react';

function Upload({ setData }) {
    const handlefile = async (e) => {
        const formdata = new FormData();
        formdata.append("file", e.target.files[0]);
        const res= await axios.post("http://localhost:5000/analyse", formdata);
        setData(res.data);
    };
    return <input type="file" onChange={handlefile} />;
}
export default Upload;