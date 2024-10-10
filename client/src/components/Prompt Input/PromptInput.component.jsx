import { useState } from "react"
import getResponse from "../../utils/getresponse"
import { useDispatch } from "react-redux"
import { UpdatePrompt } from "../../store/Prompt/Prompt.actions"
import {FaArrowUpLong} from "react-icons/fa6"
import "./PromptInput.Styles.scss"
import AutoResizeTextarea from "../TextArea/TextArea.component"

function PromptInput() {
    // Stores the Prompt Input Entered by USer
    const [prompt, setPrompt] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const dispatch = useDispatch()

    async function handleSumbit(){
        try{
            dispatch(UpdatePrompt(prompt))
            setPrompt("")
            const res = await getResponse(prompt)
            dispatch(UpdatePrompt(res.response))
        }catch(error){
            setErrorMessage(error)
            
        }
    }

    function HandleChange(value){
        setPrompt(value)
    }

    return (
        <div className="prompt-input-container">
            <AutoResizeTextarea value={prompt} onChange={HandleChange} />
            <button className="prompt-input-button" onClick={handleSumbit} disabled={!prompt}><FaArrowUpLong/></button>
            <p>{errorMessage}</p>
        </div>
    )
}

export default PromptInput