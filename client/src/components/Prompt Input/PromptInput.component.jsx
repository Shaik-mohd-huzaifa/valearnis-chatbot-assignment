import { useState } from "react"
import getResponse from "../../utils/get.response"
import { useDispatch } from "react-redux"
import { UpdateResponsePrompt, UpdateUserPrompt } from "../../store/Prompt/Prompt.actions"
import {FaArrowUpLong} from "react-icons/fa6"
import AutoResizeTextarea from "../TextArea/TextArea.component"

function PromptInput() {
    // Stores the Prompt Input Entered by USer
    const [prompt, setPrompt] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const dispatch = useDispatch()

    async function handleSumbit(){
        try{
            dispatch(UpdateUserPrompt(prompt))
            const res = await getResponse(prompt)
            dispatch(UpdateResponsePrompt(res['response']))
        }catch(error){
            setErrorMessage(error)
        }
    }

    return (
        <div className="prompt-input-container">
            <textarea name="prompt-input" id="" value={prompt} onChange={(e) => setPrompt(e.target.value)}>

            </textarea>
            <AutoResizeTextarea/>
            <button className="prompt-input-button" onClick={handleSumbit}><FaArrowUpLong/></button>
            <p>{errorMessage}</p>
        </div>
    )
}

export default PromptInput