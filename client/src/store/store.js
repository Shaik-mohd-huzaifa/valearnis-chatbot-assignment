import { applyMiddleware, compose, createStore } from "redux";
import { persistReducer, persistStore } from "redux-persist";
import storage from "redux-persist/lib/storage";
import RootReducer from "./root.reducer";

// Storing prompts in the users local storage using Redux Persist library to reduce delay in accessing data
// const persistConfig = {
//   key: "root",
//   storage,
//   blacklist: ["user", "prompts", "response"],
// };

// MiddleWare to log the states before the actions and after the actions
const loggerMiddleware = (store) => (next) => (action) => {
  if (!action.type) {
    return next(action);
  }

  console.log("type: ", action.type);
  console.log("payload: ", action.payload);
  console.log("currentState: ", store.getState());

  next(action);

  console.log("next state: ", store.getState());
};

// Combining Reducers into a form of array
const middleWares = [loggerMiddleware];

// Create a Persisted Reducer to make use of Redux Persist Functionalities
// const persistedReducer = persistReducer(persistConfig, rootreducer);

// Composing MiddleWares together as Enhancers
const composedEnhancers = compose(applyMiddleware(...middleWares));


// Creating a Store by passing RootReducer and composed Enhancers to log the Activities
export const store = createStore(RootReducer, undefined, composedEnhancers);