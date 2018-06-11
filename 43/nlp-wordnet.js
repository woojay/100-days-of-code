let natural = require('natural');
let wordnet = new natural.WordNet();

var myWord = 'desert';

wordnet.lookup(myWord, (results) => {
  results.forEach(result => {
    console.log();
    console.log(result.synsetOffset);
    console.log(result.pos);
    console.log(result.synonyms);
    console.log(result.gloss);
  });
});

console.log('synset');
wordnet.get(8522594, 'n', result => {
  console.log(result.gloss);
})
