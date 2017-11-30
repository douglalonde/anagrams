'use strict';

import React from 'react';
import ReactDOM from 'react-dom';
//import AppRoutes from './routes';
import TableView from './TableView'

window.onload = ()=> {
	
    ReactDOM.render( <TableView/>, document.getElementById('react-main'));
}