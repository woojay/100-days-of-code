let natural = require('natural');
let myString = "I'm surprised I didn't know you could make it.";

// Tokenizing
let tokenizer = new natural.WordTokenizer();
// let tokenizer = new natural.TreebankWordTokenizer();
// let tokenizer = new natural.RegexpTokenizer({ pattern: /[!?.]/ });

console.log(tokenizer.tokenize(myString));


// Stemmer - find word roots
let stemmer = natural.PorterStemmer;

console.log(stemmer.stem("mangoes"));
console.log(stemmer.stem("playing"));
console.log(stemmer.stem("sandness"));


// Stem multiple words
let longString = "I am baking cakes in the ovens.";

console.log(stemmer.tokenizeAndStem(longString));


// Another stemmer, not as frequent
let lanStemmer = natural.LancasterStemmer;

console.log(lanStemmer.tokenizeAndStem(longString));


// Noun inflector
let nounInflector = new natural.NounInflector();

console.log(nounInflector.pluralize("mouse"));
console.log(nounInflector.singularize("tomatoes"));


// Count inflector
let countInflector = natural.CountInflector;

for (let i = 0; i < 10; i++) {
  console.log(countInflector.nth(i));
}


// N-grams
let nGrams = natural.NGrams;

myString = "Jane Smith, along with Mary Adams and John Black, created the project";

console.log(nGrams.bigrams(myString));
console.log(nGrams.trigrams(myString));
console.log(nGrams.ngrams(myString, 4));
console.log(nGrams.ngrams(myString, 4, '[s]', '[e]'));
console.log('');


// Tagger
let Tagger = natural.BrillPOSTagger;

myString = "Lys soldered the beautiful jewelry pieces".split(" ");

let baseFolder = './node_modules/natural/lib/natural/brill_pos_tagger';
let rulesFile = baseFolder + "/data/English/tr_from_posjs.txt";
let lexiconFile = baseFolder + "/data/English/lexicon_from_posjs.json";
let defaultCategory = 'N';

let lexicon = new natural.Lexicon(lexiconFile, defaultCategory);
let rules = new natural.RuleSet(rulesFile);
let tagger = new Tagger(lexicon, rules);

console.log(tagger.tag(myString));

