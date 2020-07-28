{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled5.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNzd/QvKV756/Auj1oY1fX7",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/syedalimehdi/python/blob/master/2-List.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "24icBEmYV0MB",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "64a340f1-26be-428b-dad3-8e486c9a3e28"
      },
      "source": [
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
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[]\n",
            "['Gandhi']\n",
            "['Gandhi']\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}