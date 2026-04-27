import { useState } from "react";
import Upload from "./components/upload";
import Chartview from "./components/chartview";
import Activeusers from "./components/activeusers";

function App() {
    const [data, setdata] = useState(null);
    return (
        <div>
            <h1>WhatsApp Chat Analyser</h1>
            <Upload setdata={setdata} />
            <Chartview data={data} />
            <Activeusers users={data?.cu} />
        </div>
    );
}

export default App;