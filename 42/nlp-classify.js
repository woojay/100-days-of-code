let fs = require('fs');
let natural = require('natural');

// Classify JSON text w/ Naive Bayes classifier
let classifier = new natural.BayesClassifier();

// or with Logistic Regression classifier
// let classifier = new natural.LogisticRegressionClassifier();

fs.readFile('training_data.json', 'utf-8', (err, data) => {
  if (err)
    console.log(err);
  else
    trainingData = JSON.parse(data);
  train(trainingData);
});

function train(trainingData) {
  console.log('Training Data');
  trainingData.forEach((item) => {
    classifier.addDocument(item.text, item.label);
  });

  let startTime = new Date();
  classifier.train();
  let endTime = new Date()
  const trainTime = (endTime - startTime) / 1000.0;
  console.log('Train time: ', trainTime, ' seconds');
  loadTestData();
}

function loadTestData() {
  console.log(' Loading test data');

  fs.readFile('test_data.json', 'utf-8', (err, data) => {
    if (err)
      console.log(err);
    else {
      const testData = JSON.parse(data);
      testClassifier(testData);
    }
  })
}

function testClassifier(testData) {
  console.log('Testing Classifier');

  let numCorrect = 0;

  testData.forEach((item) => {
    const labelGuess = classifier.classify(item.text);

    if (labelGuess === item.label)
      numCorrect++;
  })

  console.log('Correct % : ', numCorrect / testData.length);

  saveClassifier(classifier);
}

function saveClassifier(classifier) {
  classifier.save('classifier.json', (err, classifier) => {
    if (err)
      console.log(err);
    else
      console.log('Classifier saved.');
  })
}