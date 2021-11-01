import React from "react";
import logo from './logo.svg';
import './App.css';
import UsersList from './components/User.js'

class App extends React.Component{

      constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
      }

      componentDidMount() {
        const users = [
            {'first_name': 'sergey',
            'last_name': 'vaschenko',
            'user_email': 'vaschuk@mail.ru'
            },
        ]

        this.setState(
            state:{
                'users':users
            }
        )

      }



      render (){
        return(
        <div>
            <UsersList users={this.state.users}/>
        </div>
        )
      }
}


export default App;

