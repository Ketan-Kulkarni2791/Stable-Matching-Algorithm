# The women that the men prefer
preferred_ranking_men = {

    "Ketan": ["Katrina", "Vidya", "Tabu", "Nithya"],
    "Ajinkya": ["Tabu", "Nithya", "Vidya", "Katrina"],
    "Rahul": ["Vidya", "Katrina", "Tabu", "Nithya"],
    "Abhijit": ["Vidya", "Katrina", "Tabu", "Nithya"]
}

# The men that women prefer
preferred_ranking_women = {

    "Katrina": ["Ketan", "Rahul", "Ajinkya", "Abhijit"],
    "Vidya": ["Rahul", "Ketan", "Abhijit", "Ajinkya"],
    "Nithya": ["Abhijit", "Ketan", "Rahul", "Ajinkya"],
    "Tabu": ["Ketan", "Ajinkya", "Abhijit", "Rahul"],
}

# Keeps track of people that 'may' end up together
tentative_engagements = []

# The men that still need to select any women and get accepted
free_men = []


def init_free_men():
    for man in preferred_ranking_men.keys():  # Removed dict.iteritems(), dict.iterkeys(),
        # and dict.itervalues(). Instead: use dict.items(), dict.keys(), and dict.values() respectively.

        free_men.append(man)


def stable_matching():
    while len(free_men) > 0:
        for man in free_men:
            begin_matching(man)


def begin_matching(man):
    print(f"DEALING WITH : {man} !")
    for woman in preferred_ranking_men[man]:
        taken_match = [couple for couple in tentative_engagements if woman in couple]

        # If the woman is not in tentative engagements list, then she is single & can be mingle.
        if len(taken_match) == 0:
            tentative_engagements.append([man, woman])
            # Then remove the 'man' from free_men list.
            free_men.remove(man)
            print(f"{man} is no longer a free man and engaged with {woman} !")
            break
        # If the woman is not single..
        elif len(taken_match) > 0:
            print(f'The {woman} is taken already....')

            # The current guy is equal to the person that she is currently engaged to. Bcz taken_match is a tuple
            # of woman and man and we r getting the order at which he is ranked for this woman.
            # For example, if Tabu is currently with Ajinkya, this index will return 1.
            current_guy = preferred_ranking_women[woman].index(taken_match[0][0])
            potential_guy = preferred_ranking_women[woman].index(man)

            # Let's compare to see who's better
            if current_guy < potential_guy:
                print(f"She is satisfied with {taken_match[0][0]}.")
            else:
                print(f"The {man} is better than {taken_match[0][0]} !")
                print(f"So making the {taken_match[0][0]} free again, and tentatively accepts dance between"
                      f"{man} and {woman} !")

                # The new guy is engaged
                free_men.remove(man)

                # The old guy is single now.
                free_men.append(taken_match[0][0])

                # Update the man for the woman's choice list
                taken_match[0][0] = man
                break


def main():
    init_free_men()
    stable_matching()

    print("Comple list of stable couples\n ")
    print(tentative_engagements)


if __name__ == "__main__":
    main()
