import React, {useState} from 'react';
import Goal from './goal';

const Area = ({area, form, urls}) => {
    const [showGoals, setShowGoals] = useState(false);
    const [showAddGoal, setShowAddGoal] = useState(false);

    const toggleShowGoals = () => {
        setShowGoals(!showGoals);
    }

    const toggleShowAddGoal = () => {
        setShowAddGoal(!showAddGoal);
    }

    return (
        <div style={{backgroundColor: "#ccc", padding: 20, margin: "30px 0"}}>

            <h3 style={{display: 'inline'}}>{`${area.name} : ${Math.round(area.percentage_completed * 100)}%`}</h3>

            <button style={{marginLeft: 20}} onClick={toggleShowGoals}>{showGoals ? "Esconder" : "Mostrar"} Metas</button>
            <button style={{marginLeft: 20}} onClick={toggleShowAddGoal}>{showAddGoal ? "Cancelar" : "Inserir nova Meta"}</button>

            {showAddGoal && 
                <div style={{marginTop: 20}}>
                    <form method="POST">
                        <input type="hidden" name="area" value={area.pk} />
                        <div dangerouslySetInnerHTML={{__html: form}} />
                        <button type="submit">Adicionar</button>
                    </form>
                </div>
            }

            {showGoals && 
                <div style={{marginTop: 20}}> 
                    { area.goals.map((goal, i) => {
                        return <Goal key={i} goal={goal} urls={urls}/>
                    })}
                </div>
            }
        </div>
    )
}

export default Area;