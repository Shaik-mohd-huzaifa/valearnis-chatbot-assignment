import { PromptActionTypes } from "./Prompt.actionTypes";

// Updates New Prompt/Query Send by User to the user array
export const UpdateUserPrompt = (prompt) => {
    return {
        payload: prompt,
        type: PromptActionTypes.UPDATE_USER_PROMPT
    }
}


// Updates response prompt which is received from api for new user query
export const UpdateResponsePrompt = (prompt) => {
    return {
        payload: prompt,
        type: PromptActionTypes.UPDATE_RESPONSE_PROMPT
    }
}