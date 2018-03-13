/*

  JSON object generator

*/


const cheerio = require('cheerio');
const table   = require('cheerio-tableparser')
const fs      = require('fs');

var langs     = {}

fs.readFile('./table.html', (err, data) => {

  const $ = cheerio.load(data.toString('utf8'))
  table($);
  var data = $("#table").parsetable(true, true, true);

  for(var i = 0; i < data.length; i++){

    if(data[i][0] != 'Letter')
      langs[data[i][0]] = {}

  }

  for(language in langs){

    for(var i = 0; i < data[0].length; i++){

      if(data[0][i] != 'Letter')
          langs[language][data[0][i]] = 0;

      }

    }

    var i = 1;
    for(language in langs){
      var k = 0;
      for(value in langs[language]){

        k++;
        langs[language][value] = data[i][k];

      }

      i++;

    }

    console.log(langs)

})
