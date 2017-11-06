import React from "react";
import ReactDom from 'react-dom';
import Button from './Button.jsx';
import ChildComponent from './ChildComponent.jsx';

class banner extends React.Component {
    constructor () {
        super();
        this.state = {
            clicked: false
        }
        this.toggle = this.toggle.bind(this);
        this.changeChildText = this.changeChildText.bind(this);
    }
    toggle () {
        this.setState( { clicked: !this.state.clicked } );
    }
    changeChildText(){
        return this.state.clicked ? 'i\'m a good child':"i'm a naughty child!";
    }
    render() {
        return (
            <div>
                <ChildComponent childText={this.changeChildText()} />
                <Button onClick={this.toggle} />
            </div>
        )
    }
}
module.exports = banner;
