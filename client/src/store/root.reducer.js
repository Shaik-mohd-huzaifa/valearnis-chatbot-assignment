import {combineReducers} from "redux"
import { promptReducer } from "./Prompt/Prompt.reducer"


// Combining Multiple Reducers to easily update and access them under one store.
const RootReducer = combineReducers({
    prompts: promptReducer
})


export default RootReducer