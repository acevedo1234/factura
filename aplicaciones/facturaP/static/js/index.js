
const mostrarData = (data) => {
    console.log(data)
    let body = ""
   
       body+=`<tr><td>${data.legal_name}</td><td>${data.tax_id}</td><td>${data.tax_system}</td><td>${data.email}</td><td>${data.phone} </td></tr>`
    
    document.getElementById('data').innerHTML = body
    //console.log(body)

}




const listclientes= async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/list_cliente/");
        const clientes = await response.json();
        
    
         
      console.log(clientes)

       fetch('https://www.facturapi.io/v2/customers',{

method:'POST',
body:JSON.stringify(clientes),
headers:{
    'Content-Type': 'application/json',
    'Authorization':'Bearer sk_test_v3rnMZqGldzDb7pKJlVPyBG5e0ExB4eyWLAaj0kQRm'

}

})
.then(resp=>resp.json())
.then(data=>{

    mostrarData(data)
    
})

        
    } catch (ex) {
        alert(ex);
    }
};





window.addEventListener("load", async () => {
    await listclientes();
});