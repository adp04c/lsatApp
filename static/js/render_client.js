const React = require('react');
const ReactDOM = require('react-dom');
window.renderApp = function(props) {
    const component = require('./src/'+store.component);
    const domContainerNode = document.getElementById('app-container');
    // Unmounting the component before mounting it again
    ReactDOM.unmountComponentAtNode(domContainerNode);
    ReactDOM.render(React.createFactory(component)(props), domContainerNode);
}


renderApp(store.props);

window.renderApp = function(props) {
    const component = require('./src/'+store2.component);
    const domContainerNode = document.getElementById('app-container2');
    // Unmounting the component before mounting it again
    ReactDOM.unmountComponentAtNode(domContainerNode);
    ReactDOM.render(React.createFactory(component)(props), domContainerNode);
}


renderApp(store2.props);
