import axios from "axios";


async function getResponse(prompt){
    try{
        const res = axios.post('http:127.0.0.1:8000/chat', {'prompt': prompt})
        return res
    }catch(error){
        return error
    }
}

export default getResponse