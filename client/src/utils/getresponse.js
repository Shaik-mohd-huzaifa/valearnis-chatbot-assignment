import axios from "axios";


async function getResponse(prompt){
    try{
        const res = await axios.post("https://valearnis-chatbot-a61ab76025b4.herokuapp.com/valearns/chat", {"user_input": prompt})
        return res.data
    }catch(error){
            // return {response: `Connection Error ! \n ${error.response.status}`}
            if (error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);

                return 

              } else if (error.request) {
                // The request was made but no response was received
                // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                // http.ClientRequest in node.js
                console.log(error.request);
              } else {
                // Something happened in setting up the request that triggered an Error
                console.log('Error', error.message);
              }
              console.log(error.config);
              return {"response": "Server Error"}
            }
}

export default getResponse