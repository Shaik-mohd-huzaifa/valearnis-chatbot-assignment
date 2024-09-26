import { PromptActionTypes } from "./Prompt.actionTypes";

// Inital State for the prompt object when the application loads
const Initial_State = {
    user: [],
    response: []
}


// Prompt Reducer
export const promptReducer = (state = Initial_State, action) => {
    const {payload, type} = action;

    switch (type) {
        case PromptActionTypes.UPDATE_USER_PROMPT:
            return {
                ...state,
                user: [...state.user, payload]
            }       
        case PromptActionTypes.UPDATE_RESPONSE_PROMPT:
            return {
                ...state,
                response: [...state.response, payload]
            }
        default:
            return state
    }
} 