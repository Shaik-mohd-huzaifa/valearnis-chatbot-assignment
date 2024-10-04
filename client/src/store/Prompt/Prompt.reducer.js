import { PromptActionTypes } from "./Prompt.actionTypes";

// Inital State for the prompt object when the application loads
const Initial_State = {
    prompts: [],
}


// Prompt Reducer
export const promptReducer = (state = Initial_State, action) => {
    const {payload, type} = action;

    if (type == PromptActionTypes.UPDATE_PROMPT){
        return {
            ...state,
            prompts: [...state.prompts, payload]
        }       
    }
    return state
} 