'use strict';

import React from 'react';
import { Input,Button,Icon,Label } from 'semantic-ui-react'

import TableStats from './TableStats'
import DateGrid from './Grid/DateGrid'

import Moment from 'moment';
import { extendMoment } from 'moment-range';
const moment = extendMoment(Moment);

class TableView extends React.Component {

    constructor(){
        super();
        this.state = {
            tableMapping :{},
            storageContainer:'-',
            storageAccount:'-',
            startDate: moment().subtract(14, 'weeks').format('MM-DD-YYYY'),
            endDate:moment().subtract(12, 'weeks').format('MM-DD-YYYY')
        }
    }

    componentDidMount(){
        if(!!window.blobstore_file_list){
            this.setState({
                tableMapping: window.blobstore_file_list.tableMapping,
                storageContainer: window.blobstore_file_list.storageContainer,
                storageAccount:window.blobstore_file_list.storageAccount
            })
        }
    }

    handleUpdate(){
        this.setState({
            startDate : this.refs.startDate.inputRef.value,
            endDate : this.refs.endDate.inputRef.value
        })
    }

    render(){
        return (
            <div className="row">
                <div className="row">
                    <Label>
                        <Icon name='cloud' /> {this.state.storageAccount}
                    </Label>
                    &nbsp;
                    <Label>
                        <Icon name='browser' /> {this.state.storageContainer}
                    </Label>
                    &nbsp;
                    <Input
                        ref='startDate'
                        label={{ icon: 'asterisk' }}
                        labelPosition='left corner'
                        placeholder='Start (YYYY-MM-DD)'
                      />
                      &nbsp;
                    <Input
                        ref='endDate'
                        label={{ icon: 'asterisk' }}
                        labelPosition='right corner'
                        placeholder='End (YYYY-MM-DD)'
                      />
                    &nbsp;
                    <Button animated='vertical' onClick={this.handleUpdate.bind(this)}>
                          <Button.Content visible>Search</Button.Content>
                          <Button.Content hidden>
                            <Icon name='search' />
                          </Button.Content>
                    </Button>
                    &nbsp;                  
                    <hr/>
                </div>
                <div className="row">
                       <DateGrid rows={this.state.tableMapping} startDate={this.state.startDate} endDate={this.state.endDate}/>
                </div>
            </div>
        )
    }
}

export default TableView