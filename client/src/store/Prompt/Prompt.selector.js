// To Easily Access the data from the state Selector functions are created

// Returns user array from the state directly
export const userPromptSelector = (state) => state.prompts.user; 

// Returns response array from the state directly
export const responsePromptSelector = (state) => state.prompts.response; 