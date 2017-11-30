import React from 'react'
import {Modal} from 'semantic-ui-react'

class DateSummaryModal extends React.Component {

	generateDateSummaryHTML(filesIndexedBySerial){
        let HTML = [            
        ]
        let style = {}, serials = [], serialHTML = [], successCount = 0

        for ( let serial in filesIndexedBySerial){

        	serialHTML = [], successCount = 0
            filesIndexedBySerial[serial].forEach(function(file){
                if( file.metadata.t1 == 'Success') {
                    successCount++;
                }
                style = (file.metadata.t1 == 'Success')? {color:'green'} : {color:'red'}
                serialHTML.push(<p><strong style={style}>{file.metadata.t1}</strong> - {file.file_name}</p>)
            })
            serialHTML.unshift(<p>serial: {serial} &nbsp;&nbsp; success count : <span style={{color:'green'}}>{successCount}/{filesIndexedBySerial[serial].length}</span></p>)
            HTML.push( <div>{serialHTML}</div> )
            HTML.push( <hr></hr>)
        }        
        return HTML
    }

	render(){
		return (
			<Modal size="large" trigger={this.props.modalTriggerHTML}>
                <Modal.Header>
                <div>
                    <span>Serials: <strong>{Object.keys(this.props.filesIndexedBySerial).join(', ')}</strong></span>
                    &nbsp;&nbsp;&nbsp;
                    <span>Table: <strong>{this.props.tableName}</strong></span>
                    &nbsp;&nbsp;&nbsp;
                    <span>Table: <strong>{this.props.date}</strong></span>
                </div>
                </Modal.Header>
                <Modal.Content>
                	<Modal.Description style={{overflowY:"scroll", height:window.innerHeight}}>
                    	{ this.generateDateSummaryHTML(this.props.filesIndexedBySerial) }
                  	</Modal.Description>
                </Modal.Content>
            </Modal>		
        )
	}
}
export default DateSummaryModal