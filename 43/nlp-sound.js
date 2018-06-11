let natural = require('natural');
let soundex = natural.SoundEx;
let metaphone = natural.Metaphone;

let word1 = 'pair';
let word2 = 'pear';

// Check w/ Soundex if sounds similar
if (soundex.compare(word1, word2)) {
  console.log('Soundex: Alike');
} else {
  console.log('Soundex: Unlike');
}

// Check w/ Metaphone if sounds similar - More powerful.
if (metaphone.compare(word1, word2)) {
  console.log('Metaphone: Alike');
} else {
  console.log('Metaphone: Unlike');
}

// Encoding
console.log(soundex.process(word1));
console.log(soundex.process(word2));
console.log(metaphone.process(word1));
console.log(metaphone.process(word2));