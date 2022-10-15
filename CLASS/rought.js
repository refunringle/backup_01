const axios = require('axios')

const tiny_scrapper = () => {
window.onload = () => {
    const urlF = document.getElementById('urlF');
    const url = document.getElementById('url');
    const result = document.getElementById('result');
    const copyB = document.getElementById('compyB');

    urlF.addEventListener('submit', (event) => {
        event.preventDefault();
        axios({
            url: 'http://localhost:8000/url1',
            method: 'post',
            data: {
                url: url.value,         
                
            }
        })
        .then(({ data }) => {
            copyB.classList.remove('invisible');
            result.innerHTML = `<pre>${JSON.stringify(data, null, ' ')}</pre>`;
        })
    })

    copyB.addEventListener('click', () => {
        navigator.clipboard.writeText(result.innerText)
        copyB.innerText = 'Great'
        setTimeout(() => {
            copyB.innerText = 'Copied'
        }, 2000);
    })
}
    
const getInfo = function (options, callback) {
	var error = null;
	var data = {};
	var that = this;

	if (!options.url) {
		return callback(new Error('Invalid URL'));
	}

	options.url = this.validateUrl_(options.url);
	options.timeout = !isNaN(parseFloat(options.timeout)) ? parseFloat(options.timeout) : 2000;
	options.encoding = 'binary';
	options.maxRedirects = 20;
	options.jar = true;

	that.getOpenGraph_(options, function (err, results) {
		if (err) {
			return callback(err);
		}

		callback(null, results);
		
		that.processData_(results, function (err, results) {
			callback(err, results);
		});
		
	});
};

}

export default tiny_scrapper;

  
var original = Runner.prototype.gameOver
Runner.prototype.gameOver = function(){}