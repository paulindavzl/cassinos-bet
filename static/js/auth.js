//analisa o resultado da tentativa de login
function analyzeLogin(response) {
    const url = response.url_game;
    const result = response.result;
    
    if(result === "Success") {
        location.href = url;
    };
}