import { PromptContainer } from "../Prompt Container/PromptContainer.component";
import PromptInput from "../Prompt Input/PromptInput.component";
import "./main.styles.scss";

export const Main = () => {
    return(
        <div className="container">
            <div className="header">
                <div className="image">
                <img src="./valearnis.png"/>
                </div>
                <p className="header-text">ValeAssist</p>
            </div>
            <div className="chat-container">
                <PromptContainer/>
                <PromptInput/>
            </div>
            {/* <img className="bee" src="./bee.png" alt="" /> */}
            <img className="panda" src="./panda.png" alt=""/>
            <img className="lion" src="./lion.png" alt=""/>
        </div>
    )
}