# vAIraMuththu
Search Engine for Metaphors of Tamil Songs

I am planning to implement a search engine for the metaphors which are from the Tamil movie songs. The proposed search engine is estimated to consist of the following fields related to all the songs which were released in between 2000 to 2010 by A.R.Rahman, Ilayaraja, Vidyasagar and Yuvan Shankar Raja.  

Name - Name of the song 
Lyrics - Lyrics of the song in tamil 
Composer - Music director of the song (A.R.Rahman/ Ilayaraja/ Vidyasagar/Yuvan Shankar Raja)   
Lyricist - Lyricist of the song 
Album - Album name/ Movie name which has the song
Artist - Star of the movie
Year - Album released year 
Metaphor - Metaphors of the song (can be more than one metaphor)  
Source domain - It is the conceptual domain from which we draw metaphorical expressions. 
Target domain - It is the quality or experience described by or identified with the source domain
Type of metaphor - Metaphors can be either characteristic - based or action- based or based on the benefit. 

Scope of the project is to provide the help to the writers/ readers who would like to get the ideas of metaphors which are from the tamil songs. 

Search Engine for metaphors of tamil songs can be used to get the idea about the metaphors for the requested subject 
They can use it to search based on the source domain or target domain of the metaphor 
They can use it to search based on the type of metaphor for the subject
They can use it to get the metaphors based on the rhyming. 

Implementation: I am planning to use a minimum of 100 songs for the initial implementation where each song should have at least one metaphor. I am planning to collect the data from the Musixmatch. If there are any lyrics of the song in English then I need to preprocess and translate the fields which are in English to Tamil. I am planning to use Apache Solr for indexing and querying and planning to implement wildcard matching, keyword matching and range searching.
