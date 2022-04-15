function ajax(src, callback){
// your code here
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var data = this.response;
            callback(data);
        }
    };
    req.open("GET", src, true);
    req.responseType = 'json';
    req.send();
}
function render(data){
// your code here.
// document.createElement() and appendChild() methods are preferred.
    for (let i = 0; i < data.length; i++) {
        h2 = document.createElement('h2');
        h2.innerHTML = 'Name: '+ data[i].name +'<br>Price:  '+ data[i].price +'<br>description: '+ data[i].description;
        document.body.appendChild(h2);
    }
}

ajax("https://appworks-school.github.io/Remote-Aassigiment-Data/products",
function(response){
    render(response);
});

//  you should get product information in JSON format and render data in the page

