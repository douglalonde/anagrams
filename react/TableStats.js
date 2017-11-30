'use strict';

import React from 'react';
import { Input } from 'semantic-ui-react'

class TableStats extends React.Component {

    constructor(){
        super();
        this.state = {
            stats: []
        }
    }
    componentDidMount(){
        console.log("tablestats")
    }

    render(){
        return (
            <div className="row">
                <div className="row">
                </div>
                <div className="row">
                </div>
            </div>
        )
    }
}

export default TableStats