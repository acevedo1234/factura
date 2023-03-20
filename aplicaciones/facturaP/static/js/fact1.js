


const mostrarData = (data) => {
    console.log(data)
    let body = ""
    for (let i = 0; i < data.length; i++) {
       body+=`<tr><td>${data[i].legal_name}</td><td>${data[i].tax_id}</td><td>${data[i].tax_system}</td><td>${data[i].email}</td><td>${data[i].phone} </td></tr>`
    
    
    }
    document.getElementById('datab').innerHTML = body
    //console.log(body)

}


(async () => {

    const parametro = new URLSearchParams({
        q: 'Dunder',
        
          page: 0

      }
      )
      
     
   hola=parametro.toString()
    
    const response = await fetch('https://www.facturapi.io/v2/invoices',{
        method: 'GET',
        
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
            'Authorization':'Bearer sk_test_v3rnMZqGldzDb7pKJlVPyBG5e0ExB4eyWLAaj0kQRm'
        },
    })

    const data = await response.json()

    console.log(data)
    let body = ""
    for (let i = 0; i < data.data.length; i++)
       body+=`<tr><td>${data.data[i].cfdi_version}</td><td>${data.data[i].type}</td><td>${data.data[i].stamp.sat_cert_number}</td><td>${data.data[i].stamp.sat_signature}</td><td>${data.data[i].stamp.signature} </td><td>${data.data[i].date} </td></tr>`
    
    

    document.getElementById('datab').innerHTML = body
    //console.log(body)


    
})()