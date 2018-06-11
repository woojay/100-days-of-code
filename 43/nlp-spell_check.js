let natural = require('natural');
let fs = require('fs');
let tokenizer = new natural.WordTokenizer();

let text = fs.readFileSync('lotsofwords.txt', 'utf-8');
let corpus = tokenizer.tokenize(text);
let spellcheck = new natural.Spellcheck(corpus);

// Spell check a word
console.log(spellcheck.isCorrect('birthday'));

// Get corrections
console.log(spellcheck.getCorrections('birhday'));


var sentence = "Tey hade truble fiinding th thng".split(" ");
sentence.forEach(word => {
  // Get suggestions
  // console.log(spellcheck.getCorrections(word));

  // Get only the first suggestions
  console.log(spellcheck.getCorrections(word)[0]);

  // Corrections w/in 2 edits
  // console.log(spellcheck.getCorrections(word));
});
