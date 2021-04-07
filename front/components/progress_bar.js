import React from 'react';

const ProgressBar = ({percentage}) => {
    // return (percentage)
    return (<div style={{height: 30}} className="bg-white p-1 mt-2">
        <div className="bg-dark h-100 progress-bar d-flex align-items-end">
            <div style={{width: `${(1-percentage)*100}%`}} className="bg-white h-100"></div>
        </div>
    </div>)
}

export default ProgressBar;