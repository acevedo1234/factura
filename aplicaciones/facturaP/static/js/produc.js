const mostrarData = (data) => {
    console.log(data)
    let body = ""
   
       body+=`<tr><td>${data.description}</td><td>${data.id}</td><td>${data.price}</td><td>${data.unit_name}</td><td>${data.unit_key} </td><td>${data.product_key} </td></tr>`
    
    document.getElementById('dataa').innerHTML = body
    //console.log(body)

}




const listproduct= async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/list_producto/");
        const clientes = await response.json();
        
    
         
      console.log(clientes)

       fetch('https://www.facturapi.io/v2/products',{

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
    await listproduct();
});