import React, { Component } from 'react';
import { render } from "react-dom";
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("tasks/api")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <ul>
        {this.state.data.map(tasks => {
          return (
            <li key={tasks.id}>
              {tasks.name_task} - {tasks.soderzhanie}
            </li>
          );
        })}
      </ul>
    );
  }
}