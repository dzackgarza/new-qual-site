---
schema: qual/card@1
id: P-PRACT20-W6-21
kind: problem
title: "Week 6: Miscellaneous Topics, problem 21"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
How many surjective functions are there from {1, 2, 3, 4} to $\{ 1 , 2 , 3 \} \}$
:::

::: {.solution}
Since there are 3 choices for the image of each of the four elements, there are $3 ^ { 4 } = 8 1$ total functions from {1, 2, 3, 4} to {1, 2, 3}. It is easier to count the functions that are not surjective.
If a function is not surjective, then it maps {1, 2, 3, 4} into {1, 2}, {1, 3} or {2, 3}. There are three choices for which set to map into and there are $2 ^ { 4 }$ maps in each case, thus at first glance it seems there are 48 total maps.
However, we have double counted the constant maps which send the set to a single point (the map $x \mapsto 1$ for all $x \in \{ 1 , 2 , 3 , 4 \}$ was counted as a map from {1, 2, 3, 4} into {1, 2} and counted again as a map from {1, 2, 3, 4} into {1, 3}). Adjusting for this double counting, we find there are 45 non-surjective maps and thus $8 1 - 4 5 = 3 6$ surjective maps.
:::
