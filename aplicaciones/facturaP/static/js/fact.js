
const mostrarData = (data) => {
    console.log(data)
    let body = ""
   
       body+=`<tr><td>${data.cfdi_version}</td><td>${data.id}</td><td>${data.stamp.sat_cert_number}</td><td>${data.stamp.sat_signature}</td><td>${data.verification_url} </td><td>${data.stamp.date} </td></tr>`
    
    document.getElementById('data').innerHTML = body
    //console.log(body)

}




const listclientes= async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/list_factura/");
        const fac = await response.json();
        
    
         
      console.log(fac)

       fetch('https://www.facturapi.io/v2/invoices',{

method:'POST',
body:JSON.stringify(fac),
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