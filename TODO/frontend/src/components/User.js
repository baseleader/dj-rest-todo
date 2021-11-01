import React from "react";

const UsersItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.user_email}
            </td>
        </tr>
    )
}

const UsersList = ({users}) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                User email
            </th>

            {users.map((user) => <UsersItem user={user}/>)}

        </table>
    )
}

export default UsersList;