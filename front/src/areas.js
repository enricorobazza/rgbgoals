import React from 'react';
import ReactDOM from 'react-dom';
import Area from '../components/area';

const Areas = ({areas, form, urls}) => {
    console.log(form);
    return (
        <div style={{padding: 30}}>
            <h2>Áreas</h2>
            {areas.map((area, i) => {
                return <Area key={i}
                            form={form}  
                            area={area} 
                            urls={urls}
                        />
            })}
        </div>
    )
}

ReactDOM.render(<Areas {...context}></Areas>, document.getElementById('areas'));;