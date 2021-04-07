import React from 'react';
import ReactDOM from 'react-dom';
import Area from '../components/area';

const Areas = ({areas, form, urls}) => {
    console.log(areas);
    return (
        <div className="container col-12 areas-container">
            <div className="row p-0 w-100 m-0">
                {areas.map((area, i) => {
                    return <Area key={i}
                                form={form}  
                                area={area} 
                                urls={urls}
                            />
                })}
            </div>
        </div>
    )
}

ReactDOM.render(<Areas {...context}></Areas>, document.getElementById('areas'));;