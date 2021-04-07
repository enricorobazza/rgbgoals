import React, {useState} from 'react';
import axios from 'axios';

const Goal = ({goal: _goal, urls}) => {
    const [showUpdateGoal, setShowUpdateGoal] = useState(false);
    const [value, setValue] = useState("");
    const [goal, setGoal] = useState(_goal);

    const toggleShowUpdateGoal = () => {
        setShowUpdateGoal(!showUpdateGoal);
    } 

    const updateGoal = (e) => {
        e.preventDefault();
        if(value.trim() === "") return;

        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        axios.post(urls['update_goal'].replace('0', goal.pk), {value}, {headers: {'X-CSRFToken': csrftoken}}).then(result => {
            if(result.data.success) {
                let __goal = {...goal};
                __goal.last_value = value;
                setValue(0);
                setGoal(__goal);
            }
            else{
                alert('erro ao atualizar')
            }
        });
    }

    const deleteGoal = () => {
        window.location.href = urls['delete_goal'].replace('0', goal.pk);
    }

    return <div style={{marginBottom: 10}}>
        {goal.title} : {`${Math.round(goal.percentage_completed * 100)}% (${goal.last_value}/${goal.value})`}
        
        <button style={{marginLeft: 20}} onClick={toggleShowUpdateGoal}>{showUpdateGoal ? "Cancelar" : "Atualizar Valor"}</button>
        <button style={{marginLeft: 20}} onClick={deleteGoal}>Apagar Meta</button>

        {showUpdateGoal && 
            <div style={{marginBottom: 20, marginTop: 5}}>
                <form onSubmit={updateGoal}>
                    <input value={value} onChange={(e) => setValue(e.target.value)} type="number" name="value" />
                    <button type="submit">Atualizar</button>
                </form>
            </div>
        }
    </div>
}

export default Goal;