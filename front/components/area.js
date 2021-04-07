import React, {useState} from 'react';
import Goal from './goal';

const Area = ({area, form, urls}) => {
    const [showAddGoal, setShowAddGoal] = useState(false);

    const toggleShowGoals = () => {
        setShowGoals(!showGoals);
    }

    const toggleShowAddGoal = () => {
        setShowAddGoal(!showAddGoal);
    }

    return (
        <div className="area-container col-6">
            <div className="area">
                <div className="title d-flex align-items-center">
                    <img width="40px" height="40px" src={`/static/images/icons/${area.icon}`} />
                    <h4 className="d-inline m-0 ml-2 flex-grow-1">{`${area.name} : ${Math.round(area.percentage_completed * 100)}%`}</h4>
                    {area.has_perm && <button className="btn btn-dark" onClick={toggleShowAddGoal}>
                        <span className="d-none d-md-block">{showAddGoal ? "Cancelar" : "Inserir nova Meta"}</span>
                        <span className="d-block d-md-none"><i className="fa fa-plus"></i></span>
                    </button>}
                </div>

                {showAddGoal && area.has_perm && 
                    <div className="row p-0 m-3">
                        <form method="POST">
                            <input type="hidden" name="area" value={area.pk} />
                            <div dangerouslySetInnerHTML={{__html: form}} />
                            <button className="mt-4 btn btn-primary w-100" type="submit">Adicionar</button>
                        </form>
                    </div>
                }
                
                <div className="row p-0 mx-2 my-4"> 
                    { area.goals.map((goal, i) => {
                        return <Goal key={i} goal={goal} urls={urls}/>
                    })}
                </div>
                
            </div>
        </div>
    )
}

export default Area;