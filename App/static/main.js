
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}

async function loadSignUpForm(){
    if(document.getElementById('option1').checked == true) {   
        console.log("ps");   
} else {  
       console.log("rec");   
}  

}

main();