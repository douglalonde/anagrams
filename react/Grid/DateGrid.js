'use strict'

import React from 'react'
import { Input,Button,Modal,Header,Icon,Image } from 'semantic-ui-react'

import Moment from 'moment'
import { extendMoment } from 'moment-range'
const moment = extendMoment(Moment);

import DateSummaryModal from './DateSummaryModal'

class DateGrid extends React.Component {

    constructor(){
        super()
        this.state = {
        }
    }

    componentDidMount(){
        console.log("datagrid")
        // rows = transformToRows(tables,files)
    }

    generateHeaders(range){
        let style = {
                    textAlign:'center',
                    transform: 'rotate(-45deg)',
                    width: '50px'
            }
        let headers = [<td style={{textAlign:'center'}}>Table name</td>]
        for (let day of range.by('day')) {
          headers.push(<td style={style}>{day.format('MM-DD')}</td>);
        }
        return <tr>{headers}</tr>
    }

    indexRowByKey(row, indexKey){
        let reverseIndexedRow = {}
        if(!Array.isArray(row)){
            throw Error('Not an Array.')
        }
        
        // If indexKey doesnt exist, then returns {}
        if(!row[0][indexKey]){
            return {}
        }

        row.forEach(function(entry){
            if( !Array.isArray(reverseIndexedRow[entry[indexKey]]) ){
                reverseIndexedRow[entry[indexKey]] = []
            }
            reverseIndexedRow[entry[indexKey]].push(entry)
        })

        return reverseIndexedRow
    }
    
    generateBody(rows, range){
        
        let rowHTML = [ ]
        // Generating row values
        for(let tableEntry in rows){
                
            let tableEntryIndexedByDate = this.indexRowByKey(rows[tableEntry],'date')

            let columnCellStyle = {
                    backgroundColor: 'black',
                    color: 'white',
                    borderRadius: '30px',
                    textAlign: 'center',
                    margin: 'auto',
                    width: '60%'
            }
            
            // Generating column values
            let columns = [ <td>{tableEntry}</td> ]
            for (let day of range.by('day')) {
                let currentDate = day.format('YYYYMMDD')
                if( !!tableEntryIndexedByDate[currentDate] ) {
                    let modalTriggerHTML = <div style={columnCellStyle}>{tableEntryIndexedByDate[currentDate].length}</div>
                    columns.push(
                        <td style={{textAlign:'center',width:'100px',height:'50px'}}>
                          <DateSummaryModal filesIndexedBySerial={this.indexRowByKey(tableEntryIndexedByDate[currentDate],'serial') } modalTriggerHTML={modalTriggerHTML} date={currentDate} tableName={tableEntry}/>
                        </td>
                    )
                } else {
                    columns.push(
                        <td style={{textAlign:'center',width:'100px',height:'50px'}}> - </td>
                    )
                }
            }
            
            rowHTML.push(
                <tr> {columns} </tr>
            )
        }
        
        return rowHTML   
    }

    render(){
        const range = moment.range(this.props.startDate, this.props.endDate)
        let tableStyle = {
            tableLayout: "fixed"
        }
        return (
            <div className="row">
                <table style={tableStyle}>
                    <thead>
                        {this.generateHeaders(range)}
                    </thead>
                    <tbody>
                        {this.generateBody(this.props.rows, range) }
                    </tbody>           
                </table>
            </div>
        )
    }
}

export default DateGrid