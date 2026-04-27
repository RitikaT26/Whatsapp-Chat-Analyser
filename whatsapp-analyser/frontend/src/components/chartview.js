import { Bar } from "react-chartjs-2";
function chartview({ data }) {
    if (!data) return null;
    const lbls= Object.keys(data.active_users);

    const chartdata= { 
        lbls, 
        datasets: [
            {
                label: "Active Users",
                data: Object.values(data.au),
                backgroundcolor: "blue"
            },
            {
                label: "New Users",
                data: Object.values(data.nu),
                backgroundcolor: "orange"
            }
        ]
    };

    return <Bar data={chartdata} />
}

export default chartviewhartview