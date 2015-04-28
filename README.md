Wikipedia (wikipedia-access-thru-API)

Summary
=====

  This module retrieves articles from Wikipedia. It then extracts the text from those articles and readies that text for deeper linguistic analysis by 

   - [ ] removing stopwords
   - [ ] ignoring case 
   - [ ] lemmatizing words

 The Jaccard similarities between articles on Wikipedia are then calculated. 
 Also, the module subsequently performs latent Dirichlet allocation to identify the probability distributions of words that underlie each article.

Code Example
====

    python access_wikipedia.py 'TITLE NAME'
    python PlotAndSaveFrequencies.py
    python JaccardWikipediaHeart.py

 -or-

     ./access_wikipedia.sh
     ./main.sh

Motivation
====

 This module explores whether a computable representation of illness can be created from online content and how these representations differ from those created from traditional sources of medical knowledge. Combining these two may help to dispel misinformation in online content and update archaic descriptions of illnesses. 


_PlotAndSaveFrequencies.py_ extracts the text of a Wikipedia article through Wikipedia's API, saves it, calculates the frequencies of words within it (after lemmatizing and removing stopwords), and then plots these frequency distributions on separate graphs.

_JaccardWikipediaHeart.py_ calculates the Jaccard similarities between articles on Wikipedia and plots these similarity values in a heatmap.


Open Issues
====

 - [] Disambiguation of pages 

 
Dependencies
====
  - [] nltk
  - [] wikipedia
