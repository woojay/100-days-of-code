let natural = require('natural');

// String distance
let string1 = 'close';
let string2 = 'closer';
let string3 = ' fffaslkfd;klj';

console.log(natural.JaroWinklerDistance(string1, string2));
console.log(natural.JaroWinklerDistance(string1, string3));
console.log(natural.JaroWinklerDistance(string2, string2));
console.log();

// min edit to equalize
console.log(natural.LevenshteinDistance(string1, string2));
console.log(natural.LevenshteinDistance(string1, string3));
console.log();

// DiceCoefficient
console.log(natural.DiceCoefficient(string1, string2));
console.log(natural.DiceCoefficient(string1, string3));
console.log();

// Classify w/ Bayes
let classifier = new natural.BayesClassifier();

let trainingData = [
  { text: 'RE: Canadian drugs now on sale', label: 'spam' },
  { text: 'Earn more from home', label: 'spam' },
  { text: 'Information now available!!!', label: 'spam' },
  { text: 'Earn easy cash', label: 'spam' },
  { text: 'Your business trip is confirmed for Monday the 4th', label: 'notspam' },
  { text: 'Project planning - next steps', label: 'notspam' },
  { text: 'Birthday party next weekend', label: 'notspam' },
  { text: 'Drinks on Monday?', label: 'notspam' }
];

let testData = [
  { text: 'Drugs for cheap', label: 'spam' },
  { text: 'Next deadline due Monday', label: 'notspam' },
  { text: 'Meet me at home?', label: 'notspam' },
  { text: 'Hang out with someone near you', label: 'spam' }
];

trainingData.forEach((item) => {
  classifier.addDocument(item.text, item.label);
});

classifier.train();

testData.forEach((item) => {
  const labelGuess = classifier.classify(item.text);

  console.log(item.text);
  console.log('Label:', labelGuess);
  console.log(classifier.getClassifications(item.text));
  console.log();
})


