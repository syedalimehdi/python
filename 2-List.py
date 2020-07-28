        "#List and List Comprehension example\n",
        "#just using List for movies starting with G\n",
        "\n",
        "movies = [\"DDLJ\", \"Gandhi\", \"Kabhi Kushi Kabhie Gham\"]\n",
        "\n",
        "gmovies=[]\n",
        "for title in movies:\n",
        "  if title.startswith(\"G\"):\n",
        "    gmovies.append(title)\n",
        "  print(gmovies)"
 
