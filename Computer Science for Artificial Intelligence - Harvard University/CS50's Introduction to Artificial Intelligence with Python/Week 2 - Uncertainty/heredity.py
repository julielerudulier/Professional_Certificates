import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


# A function that will check if a person has parents in the 'people' dictionary or not:
def check_parents(person, people):
    
    # Check to see if the person we are looking at has parents in the dictionary:
    if person in people.keys(): 
        parents = list(people[person].values())[1:3]
            
    # Return parents no matter of their existence in the dictionary
    return parents


# A function that will return the probability for a specific parent, to apply when calculting the child's probability:
def parents_genes(parent, one_gene, two_genes, have_trait):
    if parent not in one_gene and parent not in two_genes:
        proba_parent = PROBS["mutation"]
        
    elif parent in one_gene:
        proba_parent = 0.5
       
    elif parent in two_genes:
        proba_parent = 1 - PROBS["mutation"]
        
    return proba_parent


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # Get list of all people contained in 'people' dictionary:
    list_people = list(people.keys())

    # Initialize a variable that represents the joint probability that we are going to calculate:
    p = 1

    # For each person in the dictionary:
    for person in list_people:

        # Check if person has parents:
        parents = check_parents(person, people)

        # If no parents in dictionary:
        if parents[0] == parents[1] == None:

            if person not in one_gene and person not in two_genes:
                p *= PROBS["gene"][0]

                if person not in have_trait:
                    p *= PROBS["trait"][0][False]

                elif person in have_trait:
                    p *= PROBS["trait"][0][True]

            elif person in one_gene:
                p *= PROBS["gene"][1]

                if person not in have_trait:
                    p *= PROBS["trait"][1][False]

                elif person in have_trait:
                    p *= PROBS["trait"][1][True]

            elif person in two_genes:
                p *= PROBS["gene"][2]

                if person not in have_trait:
                    p *= PROBS["trait"][2][False]

                elif person in have_trait:
                    p *= PROBS["trait"][2][True]


        # If person has parents in dictionary, we get parents probability values from parents_genes function and apply them to the calculus:
        else:
            proba_mother = parents_genes(parents[0], one_gene, two_genes, have_trait)
            proba_father = parents_genes(parents[1], one_gene, two_genes, have_trait)

            if person not in one_gene and person not in two_genes:
                p *= (1 - proba_mother) * (1 - proba_father)
                if person not in have_trait:
                    p *= PROBS["trait"][0][False]
                elif person in have_trait:
                    p *= PROBS["trait"][0][True]

            elif person in one_gene:
                p *= (proba_mother * (1 - proba_father)) + ((1 - proba_mother) * proba_father)
                if person not in have_trait:
                    p *= PROBS["trait"][1][False]
                elif person in have_trait:
                    p *= PROBS["trait"][1][True]

            elif person in two_genes:
                p *= proba_mother * proba_father
                if person not in have_trait:
                    p *= PROBS["trait"][2][False]
                elif person in have_trait:
                    p *= PROBS["trait"][2][True]

    return p


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    # For each person in 'probabilities' dictionary:
    for person in probabilities.keys():

        # Check whether they have one, two or no copy at all of the gene:
        if person not in one_gene and person not in two_genes:

            # Update 'probabilities' with the corresponding joint probability
            probabilities[person]["gene"][0] += p
        
        elif person in one_gene and person not in two_genes:
            probabilities[person]["gene"][1] += p
            
        elif person not in one_gene and person in two_genes:
            probabilities[person]["gene"][2] += p
        
        if person not in have_trait:
            probabilities[person]["trait"][False] += p
        
        elif person in have_trait:
            probabilities[person]["trait"][True] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    # For each person in 'probabilities' dictionary:
    for person in probabilities.keys():

        # Calculate the sum of their present probabilities of having the gene:
        sum_gene = probabilities[person]["gene"][0] + probabilities[person]["gene"][1] + probabilities[person]["gene"][2]

        # Calculate the normalizing factor accordingly:
        factor_gene = 1 / sum_gene

        # Apply factor to each probability and update 'probabilities' dictionary:
        probabilities[person]["gene"][0] = probabilities[person]["gene"][0] * factor_gene
        probabilities[person]["gene"][1] = probabilities[person]["gene"][1] * factor_gene
        probabilities[person]["gene"][2] = probabilities[person]["gene"][2] * factor_gene

        # Repeat process for 'trait' probabilities:
        sum_trait = probabilities[person]["trait"][True] + probabilities[person]["trait"][False]
        factor_trait = 1 / sum_trait
        probabilities[person]["trait"][True] = probabilities[person]["trait"][True] * factor_trait
        probabilities[person]["trait"][False] = probabilities[person]["trait"][False] * factor_trait


if __name__ == "__main__":
    main()
