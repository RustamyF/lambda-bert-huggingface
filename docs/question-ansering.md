# Question Answering NLP Applications
Have you ever wondered what happens when you ask a question on google and you immediately get an answer for it?
For example, we ask `who is the president of united states` on google search bar and we get this answer

<img src="assets/president-search.png" width="600" height="300">

We can see that Google first searched and ranked 1.6 billion pages in 1.08 secs, and then performed an addition processing step
to find the answer snippet from the page. The first taks is the core product of Google as a search engin. The second
processing technique (finding answer to a question from a webpage) is called question and answering (QA).
Modern QA systems, including semantic search engines, intelligent assistants, and automated information extractors.

The question and a context is given to the model, and it returns the answer to the question in the context. This can be
used built enterprise level QA system. For example, a document search engin, such as Elastic Search, can be used to
rank the documents, and QA model to find the answer within the document. The Haystack library developed by deepset,
a German company focused on NLP can be used to build both document ranking and answering question within the document.
Here is an example of reader-retriever archetecture for question answering systems.

<img src="assets/document-reader.JPG" width="600" height="300">
