let natural = require('natural');

natural.BayesClassifier.load('classifier.json', null, (err, classifier) => {
  if (err)
    console.log(err);
  else {
    const testComment = 'is this about the sun and the moon';

    // Is this about space or politics?
    console.log(classifier.classify(testComment));
  };

});