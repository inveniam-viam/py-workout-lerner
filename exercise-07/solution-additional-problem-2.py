def remove_authors(article: str, names: list[str]) -> str:

    # isolating all name words into a separate list

    out_names = []

    for name in names:

        for name_part in name.split():

            out_names.append(name_part)
    
    replacement = ["___" if word in out_names else word for word in article.split()]

    return ' '.join(replacement)

print(remove_authors("Treatment of Bipolar Disorder by Yevgenia Kozorovitskiy Janet Zhao Sara Freda", ["Yevgenia Kozorovitskiy", "Janet Zhao", "Sara Freda"]))
