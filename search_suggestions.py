def threesearchSuggestions(numReviews,repository,customQuery):
    suggests=[]
    characs=""
    repository=sorted(item.lower() for item in repository)

    for i in range(len(customQuery)):
        suggests=[]
        characs+=customQuery[i].lower()

        if len(characs)>=2:
            for item in repository:
                if item.startswith(characs):
                    suggests.append(item)
                    if len(suggests)==3:
                        break
    return suggests

numReviews=5
repository=["Osama","taqsim","tali","tareq","talal"]
customQuery="ta"
print(threesearchSuggestions(numReviews,repository,customQuery))
