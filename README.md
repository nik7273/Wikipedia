wikipedia-access-thru-API

Summary
=====

  This module retrieves articles from Wikipedia. It then extracts the text from those articles and readies that text for deeper linguistic analysis by 

   - [ ] removing stopwords
   - [ ] ignoring case 
   - [ ] lemmatizing words
 
 The module then performs latent Dirichlet allocation to identify the probability distributions of words that underly each article.

Code Example
====

    python access_wikipedia.py 'TITLE NAME'

 -or-

     ./access_wikipedia.sh

Motivation
====

 This module explores whether a computable representation of illness can be created from online content and how these representations differ from those created from traditional sources of medical knowledge. Combining these two may help to dispel misinformation in online content and update archaic descriptions of ilnesses. 


_Access_wikipedia.(py|sh)_ extract the text of a Wikipedia article though Wikipedia's API. 

Open Issues
====

 - [] Disambiguation of pages 

 