import React, {useState} from 'react';
import ReactDOM from 'react-dom';

import {Header} from '../components/header';

const TextInput = ({value, id}) => {
    const [_value, setValue] = useState(value || "");
    return (<div><input id={id} name={id} type="text" value={_value} onChange={(e) => setValue(e.target.value)}/></div>)
}

const NumberInput = ({value, id}) => {
    const [_value, setValue] = useState(value || "");
    return (<div><input id={id} name={id} type="number" value={_value} onChange={(e) => setValue(e.target.value)}/></div>)
}

const MyComponent = ({fields: _fields, title}) => {
    const [fields, setFields] = useState(_fields);

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;   
    console.log(_fields);

    return (
        <div style={{marginBottom: 40}}>
            <Header />
            <h1>{title}</h1>
            <div style={{padding: 20}}>
                <form method="post">
                    <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
                    {fields.map(field => {
                        console.log(field.field);

                        if(field.type === "text") return (<TextInput id={field.id}/>)
                        else if(field.type === "number") return (<NumberInput id={field.id}/>)
                        else return (<div>{field.id} {"->"} {field.type}</div>)
                    })}
                    <button type="submit">Cadastrar</button>
                </form>
            </div>
        </div>
    )
}

const Footer = (props) => {
    return (<div style={{marginTop: 50}}>Rodapé</div>)
}

ReactDOM.render(<MyComponent {...context}></MyComponent>, document.getElementById('root'))
ReactDOM.render(<Footer></Footer>, document.getElementById('footer'))