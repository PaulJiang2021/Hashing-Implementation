from minHash import actualJaccard, create_trigram, estimateJaccard, minHash, HashTable
import csv
import pandas as pd
import random
from collections import OrderedDict
import time
import matplotlib.pyplot as plt
import numpy as np

def pairwise_computation(query_set, urllist):
    starttime = time.time()
    for query in query_set:
        for url in urllist:
            val = actualJaccard(query, url)
            # print(val)
    
    return time.time() - starttime, (time.time() - starttime) / len(query_set)

def calc_prob(j, k, l):
    return 1 - (1 - j**k) ** l

def main():

    s1 = "The mission statement of the WCSCC and area employers recognize the importance of good attendance on the job. Any student whose absences exceed 18 days is jeopardizing their opportunity for advanced placement as well as hindering his/her likelihood for successfully completing their program."

    s2 = "The WCSCC’s mission statement and surrounding employers recognize the importance of great attendance. Any student who is absent more than 18 days will loose the opportunity for successfully completing their trade program."

    s1hashes = minHash(s1, 100)
    s2hashes = minHash(s2, 100)
    estimated = estimateJaccard(s1hashes, s2hashes)
    actual = actualJaccard(s1, s2)

    print(estimated, actual)

    data = pd.read_csv("user-ct-test-collection-01.txt", sep="\t")
    urllist = data.ClickURL.dropna().unique()
    # print(len(urllist))
    subset_size = 200000
    random.seed(10002)
    urllist = random.sample(list(urllist), subset_size)
    query_set = random.sample(list(urllist), 200)

    b= 64
    r =2**20

    f = open("report.txt", mode="w+")
    for k in range(2, 7):
        for l in [20, 50, 100]:
            prod = k * l
            minHashTable = HashTable(k, l, b, r)

            for idx in range(len(urllist)):
                minHashTable.insert(minHash(urllist[idx], prod), idx)

            print(f"Finished inserting all {subset_size} urls into hashTable")

            meanVals = 0
            topMeanVals = 0
            start_time = time.time()

            for idx in range(len(query_set)):

                print(f'Query {idx}')
                query = query_set[idx]
                hashcodes = minHash(query, prod)

                candidate_set = minHashTable.lookup(hashcodes)
                # print(f'Looked up Query {idx}')
                # print(len(candidate_set))

                ranking_dict = {}
                avgJaccard = 0

                for cidx in candidate_set:
                    item = urllist[cidx]
                    val = actualJaccard(query, item)
                    ranking_dict[item] = val
                    avgJaccard += val

                avgJaccard /= len(candidate_set)

                # print(f'Mean q{idx} = {avgJaccard}')
                meanVals += avgJaccard

                # Getting top 10 from retrieved urls
                sorted_dict = OrderedDict(sorted(ranking_dict.items(), key=lambda kv: kv[1]))

                filtered_set = []
                for _ in range(10):
                    if sorted_dict:
                        filtered_set.append(sorted_dict.popitem()[1])
                    else:
                        break
                # print(item[1])

                avgJaccards = sum(filtered_set)
                avgJaccards /= len(filtered_set)

                # print(f'Mean top-10 q{idx} = {avgJaccard}')
                topMeanVals += avgJaccards
            
            total_time = time.time() - start_time
            f.write(f'Using K = {k}, L = {l}:\n')
            f.write(f"Mean Similarity: {meanVals / 200}\n")
            f.write(f"Mean Similarity of Top-10: {topMeanVals / 200}\n")
            f.write(f"Query time for Query Set(200): {total_time}\n")
            f.write(f"Query time for each query: {total_time / 200}\n")
            f.write("\n")

    f.close()        

    timeSpent = pairwise_computation(set(query_set), set(urllist))
    print(f"Query time for brute-force approach: {timeSpent[0]}, per query: {timeSpent[1]}")


    fig = plt.figure(1)
    j = np.linspace(0, 1, 100)

    l = 50
    for k in range(1,8):
        plt.plot(j, calc_prob(j, k, l), label=f'K = {k}')
    plt.title("Probability compared to Jaccard, varying K while holding L constant")
    plt.ylabel("Px")
    plt.xlabel("Jx")
    plt.legend()

    fig2 = plt.figure(2)
    
    k = 4
    for l in [5, 10, 20, 50, 100, 150, 200]:
        plt.plot(j, calc_prob(j, k, l), label=f'L = {l}')
    plt.title("Probability compared to Jaccard, varying L while holding K constant")
    plt.ylabel("Px")
    plt.xlabel("Jx")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

