import React from 'react';


const UserItem = ({users}) => {
    return (
        <tr>
            <td class="Line">
                {users.username}
            </td>
            <td class="Line">
                {users.first_name}
            </td>
            <td class="Line">
                {users.last_name}
            </td>
            <td class="Line">
                {users.email}
            </td>

        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <div className="card-body">
            <div className="popover-header">
                <ul>
                    <li><a href="App.js">Главная</a></li>
                    <li><a href="#">Some Text</a></li>
                    <li><a href="#">Some Text</a></li>
                    <li><a href="#">Личный кабинет</a></li>
                </ul>
            </div>
            <div className="legend">
                <table className="form-range">
                    <th>
                        Никнейм
                    </th>
                    <th>
                        Имя пользователя
                    </th>
                    <th>
                        Фамилия пользователя
                    </th>
                    <th>
                        Email пользователя
                    </th>
                    {users.map((user) => <UserItem user={user}/>)}

                </table>
            </div>
            <div className="carousel-indicators [data-bs-target]">
                <h1 className="display-3">FOOTER</h1>
            </div>

        </div>
    )
}


export default UserList