# Writeprints-Static Feature Set

Script to extract important features from the Writeprint-Static Feature Set for (Adverserial) Stylometry.

(Adapted from the Whiteprints approach [Abbasi and Chen, 2008])


| Group     | Category            | No. of Features | Description |
| :-------: |:-------------------:| :--------------:| :---------: |
| Lexical   | Word level          | 3               | Total words, average word length, number of short words |
|           | Character level     | 3               | Total char, percentage of digits, percentage of uppercase letters |
|           | Special characters  | 22              | Frequency of each of the 21 special characters |
|           | Letters             | 26              | Letter frequency |
|           | Digits              | 10              | Digit frequency |
|           | Vocabulary richness | 1               | Ratio of hapax and dis legomena |
| Syntactic | Function Words      | 153             | Frequency of function words |
|           | POS tags            | 12              | Frequency of parts of speech tags (universal) |
|           | Punctuation         | 9               | Frequency and percentage of colon, semicolon, qmark, period, exclamation, comma, single inverted comma, double inverted comma |
