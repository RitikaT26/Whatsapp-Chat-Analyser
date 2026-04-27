function activeusers ({ users }) {
    if (!users) return null;
    return (
        <div>
            <h2>Users active {'>='} 4 days</h2>
            <ul>
                {users.map((u,i) => <li key={i}>{u}</li>)}
            </ul>
        </div>
    );
}

export default activeusers