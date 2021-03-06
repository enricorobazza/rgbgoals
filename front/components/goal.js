import React, {useState} from 'react';
import axios from 'axios';
import ProgressBar from './progress_bar';

const Goal = ({goal: _goal, urls}) => {
    const [showUpdateGoal, setShowUpdateGoal] = useState(false);
    const [value, setValue] = useState("");
    const [goal, setGoal] = useState(_goal);
    const [loading, setLoading] = useState(false);

    const toggleShowUpdateGoal = () => {
        setShowUpdateGoal(!showUpdateGoal);
    } 

    const updateGoal = (e) => {
        e.preventDefault();
        if(value.trim() === "") return;

        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        setLoading(true);
        axios.post(urls['update_goal'].replace('0', goal.pk), {value}, {headers: {'X-CSRFToken': csrftoken}}).then(result => {
            setLoading(false);
            if(result.data.success) {
                setGoal(result.data.goal);
                setValue("");
                setShowUpdateGoal(false);
            }
            else{
                alert('erro ao atualizar')
            }
        }).error((e) => {
            alert(e);
            setLoading(false);
        });
    }

    const deleteGoal = () => {
        window.location.href = urls['delete_goal'].replace('0', goal.pk);
    }

    const listGoal = () => {
        window.location.href = urls['list_one_goal'].replace('0', goal.pk);
    }

    const getBackground = (percentage) => {
        let i;
        for(i = 1; i<=10; i+=1){
            if(percentage <= i/10) return `${i*10}`;
        }
        return `${100}`;
    }

    return (<div className="goal-container col-xl-4 col-lg-6 col-md-6 col-12">
        <div className={`goal bg-success-gradient-${getBackground(goal.percentage_completed)}`}>
            {/* {goal.title} : {`${Math.round(goal.percentage_completed * 100)}% (${goal.last_value}/${goal.value})`} */}
            <div className="goal-title">{goal.title}</div>

            <div className="progress-value d-flex justify-content-around align-items-center">
                <div className="value-container d-flex flex-column">
                    <span className="value">
                        {goal.last_value_display}
                    </span>
                    <span>Atual</span>
                </div>
                <div className="arrow"><i className="fa fa-arrow-right"></i></div>
                <div className="value-container d-flex flex-column"><span className="value">{goal.value_display}</span><span>Meta</span></div>
            </div>

            <ProgressBar percentage={goal.percentage_completed} />

            {/* <div className="goal-info row mt-3">
                <div className="col-12 col-lg-6">Recorr??ncia: <br /> {goal.recurrence}</div>
                <div className="col-12 col-lg-6">In??cio: <br /> {goal.start_date}</div>
            </div> */}

            <div className="goal-info row mt-3">
                <div className="col-12 text-center">{goal.recurrence}</div>
            </div>
            
            <div className="d-flex justify-content-end mt-3">
                {goal.history_count > 0 && <button onClick={listGoal} 
                className={`btn btn-${goal.percentage_completed < 0.4 ? "secondary" : "info"} mr-2`}>
                        <i className="fas fa-book"></i>
                </button>}
                {goal.has_perm && !showUpdateGoal && <button className="btn btn-primary mr-2" onClick={toggleShowUpdateGoal}><i className="fa fa-pencil-alt"></i></button>}
                {goal.has_perm && <button className="btn btn-danger" onClick={deleteGoal}><i className="fa fa-trash"></i></button>}
            </div>

            {showUpdateGoal && goal.has_perm && 
                <div style={{marginBottom: 20, marginTop: 5}}>
                    <form onSubmit={updateGoal}>
                        <div class="col-12 p-0">
                            <label for="value">Valor:</label>
                            <input className="form-control" value={value} onChange={(e) => setValue(e.target.value)} type="number" name="value" />
                        </div>
                        <div className="row p-0 mt-2">
                            <div className="col-12">
                                <button className="btn btn-primary w-100" type="submit">
                                    {loading ? <i className="fas fa-spinner fa-spin"></i> : "Atualizar"}
                                </button>
                            </div>
                            <div className="col-12 mt-2">
                                <button onClick={toggleShowUpdateGoal} className="btn btn-dark w-100" type="button">Cancelar</button>
                            </div>
                        </div>
                    </form>
                </div>
            }
        </div>
    </div>)
}

export default Goal;