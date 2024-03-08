import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Create a dictionary with pages from the corpus as keys:
    model = dict.fromkeys(corpus.keys())

    # Initialize a variable that reprensents the potential number of links a page has:
    links_page = len(corpus[page])
    
    # If the page does have at least one link:
    if links_page > 0:

        # For each page in the corpus:
        for link in corpus:

            # Calculate the difference between 1 and the damping_factor divided by the total number of pages in the corpus, that we apply to all pages:
            model[link] = (1 - damping_factor) / len(corpus)

        # For each link the page has:
        for link in corpus[page]:

            # Calculate the probability that this page gets chosen to which we add its original probability value:
            model[link] = model[link] + (damping_factor / links_page)

    # If the page does not have any links:
    else:

        # For each page in the corpus:
        for link in corpus:

            # Calculate a probability distribution that chooses all pages with equal probability. 
            model[link] = 1 / len(corpus)

    return model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Initialize the list of keys/pages in the corpus:
    list_keys = list(corpus.keys())

    # Initialize a dictionary with pages in the corpus as keys:
    ranking = dict.fromkeys(list_keys)

    # Initialize a ranking value for each key equal to 0:
    for key in list_keys:
        ranking[key] = 0

    # Initialize an empty list that will contain all pages sampled:
    list_samples = []

    # Iterate over the number n of samples:
    for i in range(n):

        # If we iterate over the very first sample:
        if i == 0:

            # The first page is chosen randomly:
            page = random.sample(list_keys, 1)

            # Its ranking is # / n:
            ranking[page[0]] = 1 / n

            # Add the page to the list of pages being sampled:
            list_samples.append(page[0])
            
        # For all other samples:    
        elif i != 0:

            # Initialize a variable that is based on the previous sample:
            previous_page = str(list_samples[i-1])

            # Pass the previous sample into the transition_model function to get the probabilities for the next sample:
            model = transition_model(corpus, previous_page, damping_factor)

            # Get the list of pages from the transition model:
            list_pages = list(model.keys())

            # Get the list of probabilities (weights) from the transition model:
            list_weights = list(model.values())

            # Choose the next page randomly, depending on the weight (probability) of each page:
            next_page = random.choices(list_pages, weights=list_weights, k=1)

            # Update rankings:
            ranking[next_page[0]] = (1 / n) + ranking[next_page[0]]

            # Append the list of samples:
            list_samples.append(next_page[0])

    return ranking


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Get list of pages/keys from corpus:
    list_keys = list(corpus.keys())

    # Initialize a dictionary with all pages in the corpus as keys:
    iteration = dict.fromkeys(list_keys)

    # Initialize a variable N where N is the total number of pages in the corpus:
    N = len(corpus)

    # Iterate over each key and assign each page a rank of 1 / N:
    for key in list_keys:
        iteration[key] = 1 / N
        
    # Initialize the point at which PageRank values do not change by more than the value of the variable (0.001) between the current rank values and the new rank values:
    threshold = 0.001

    # Initialize a variable that reprensents the first condition of the Iterative Algorithm - a 1 - d probability of choosing a page at random, split evenly among all N possible pages:
    proba = (1 - damping_factor) / N

    # Iterate until threshold has been reached:
    while True:

        # Initialize a variable that represents the count of iterations:
        count = 0

        # For each key in the corpus:
        for key in corpus:

            # Initialize a variable that represents the sigma symbol in the Iterative Algorithm - for all pages that link to a specific page, sigma (or here totalSum) is the sum of all probabilities that we were on a number of pages i and chose the link to page p:
            totalSum = 0

            # For each page in the corpus:
            for page in corpus:

                # If the page we're looking at is a link in another page:
                if key in corpus[page]:

                    # We calculate the total number of links this/these pages have: 
                    numLinks = len(corpus[page])

                    # Update the totalSum value:
                    totalSum = totalSum + (iteration[page] / numLinks)

            # Initialize a variable that represents the new ranking value for the starting page, and calculate its new value by applying the formula:
            newRanking = proba + (damping_factor * totalSum)

            # Check to see if threshold is reached:
            if (iteration[key] - newRanking) < threshold:
                count += 1
            
            # Update ranking value of the page in the dictionary:
            iteration[key] = newRanking

        # When all pages have been iterated over, break the loop:
        if count == N:
            break

    return iteration


if __name__ == "__main__":
    main()
