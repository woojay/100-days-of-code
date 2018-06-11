let natural = require('natural');

let trie = new natural.Trie();

const birdNames = ['albatross', 'anhinga', 'auklet', 'avocet', 'bishop', 'bittern', 'blackbird', 'bluebird', 'bobolink', 'booby', 'brant', 'bufflehead', 'bunting', 'canvasback', 'cardinal', 'catbird', 'chat', 'chickadee', 'chukar', 'coot', 'cormorant', 'cowbird', 'crane', 'creeper', 'crossbill', 'crow', 'cuckoo'];

birdNames.forEach(item => {
  trie.addString(item);
})

// Contains word 'crane'
console.log(trie.contains("crane"));

// Starts w/ 'cr'
console.log(trie.keysWithPrefix("cr"));

// Find matches that contain part of 'cuckoohead'
console.log(trie.findMatchesOnPath("cuckooohead"));