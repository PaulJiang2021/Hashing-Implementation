
Estimated Jaccard Similarity = 0.47 
Actual Jaccord Similiarity = 0.5228070175438596



Using K = 2, L = 20:
Mean Similarity: 0.24651745892922697
Mean Similarity of Top-10: 0.5889588585174628
Query time for Query Set(200): 295.92284178733826
Query time for each query: 1.4796142089366913

Using K = 2, L = 50:
Mean Similarity: 0.23279451625293204
Mean Similarity of Top-10: 0.5890330553409053
Query time for Query Set(200): 559.9315001964569
Query time for each query: 2.7996575009822844

Using K = 2, L = 100:
Mean Similarity: 0.22768754393623789
Mean Similarity of Top-10: 0.5890418272707297
Query time for Query Set(200): 627.3155422210693
Query time for each query: 3.1365777111053466

Using K = 3, L = 20:
Mean Similarity: 0.26923445591698825
Mean Similarity of Top-10: 0.5879989564173486
Query time for Query Set(200): 166.61741399765015
Query time for each query: 0.8330870699882508

Using K = 3, L = 50:
Mean Similarity: 0.25923517324051537
Mean Similarity of Top-10: 0.5887900155511016
Query time for Query Set(200): 277.82104229927063
Query time for each query: 1.3891052114963531

Using K = 3, L = 100:
Mean Similarity: 0.2463630339751695
Mean Similarity of Top-10: 0.5890349041938068
Query time for Query Set(200): 418.3407607078552
Query time for each query: 2.0917038035392763

Using K = 4, L = 20:
Mean Similarity: 0.2890648854332476
Mean Similarity of Top-10: 0.5834297354813022
Query time for Query Set(200): 158.0513060092926
Query time for each query: 0.790256530046463

Using K = 4, L = 50:
Mean Similarity: 0.2753490673143521
Mean Similarity of Top-10: 0.5868422711593277
Query time for Query Set(200): 210.5094017982483
Query time for each query: 1.0525470089912414

Using K = 4, L = 100:
Mean Similarity: 0.26550279085761713
Mean Similarity of Top-10: 0.5882548378949247
Query time for Query Set(200): 341.84133553504944
Query time for each query: 1.7092066776752473

Using K = 5, L = 20:
Mean Similarity: 0.35141115485385926
Mean Similarity of Top-10: 0.5709717954698561
Query time for Query Set(200): 16.390101194381714
Query time for each query: 0.08195050597190857

Using K = 5, L = 50:
Mean Similarity: 0.3140422787538421
Mean Similarity of Top-10: 0.5798889085926612
Query time for Query Set(200): 38.752557039260864
Query time for each query: 0.19376278519630433

Using K = 5, L = 100:
Mean Similarity: 0.2864485194957062
Mean Similarity of Top-10: 0.5855424484187608
Query time for Query Set(200): 103.96388483047485
Query time for each query: 0.5198194241523743

Using K = 6, L = 20:
Mean Similarity: 0.39815159783387627
Mean Similarity of Top-10: 0.5410704758218684
Query time for Query Set(200): 1.9901530742645264
Query time for each query: 0.009950765371322633

Using K = 6, L = 50:
Mean Similarity: 0.338546341178149
Mean Similarity of Top-10: 0.5682346050247965
Query time for Query Set(200): 14.571970701217651
Query time for each query: 0.07285985350608826

Using K = 6, L = 100:
Mean Similarity: 0.318291856211801
Mean Similarity of Top-10: 0.579652187515531
Query time for Query Set(200): 25.955729007720947
Query time for each query: 0.12977864503860473

It seems that using a larger L value will increase the Jaccard similarity of the top 10 url but decrease the similarity of all the candidates for the query, which makes sense since we have more hash tables which would increase the quality of the retrieved set from the query set. However, using larger L for the hashTable also increase the query and insertion time.

Using more hash functions increases the overall Jaccard similarity but slightly decreases the top-10 similarity, which is negligible. It also decreases the query time at the cost of increased insertion time since there are more minHash values to insert.



Query time for brute-force approach: 587.7598114013672, per query: 2.938799057006836

Expected Total time to compute pairwise similarity for all the entire urllist will take 587.7s / 200 * 200000 (size of the subset I used) = 
163.25 hours. It is much larger than the query time for our minHash Table.

# Conclusion
For large amount of data, the query time for the brute force approach is much longer than the time it takes to find similar set from MinHashtable, and as we manipulate K and L we can find an ideal balance between the runtime and the accuracy of the similar set commpared to the query set.
