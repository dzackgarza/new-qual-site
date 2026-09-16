---
schema: qual/card@1
id: P-PRACT20-W6-24
kind: problem
title: Images and preimages of unions and intersections
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f : \mathbb { R } \to \mathbb { R }$ and let $X , Y \subseteq \mathbb { R }$ . Which of these are necessarily true?

$$
f ( X \cap Y ) = f ( X ) \cap f ( Y )
$$

$$
f ^ { - 1 } ( X \cap Y ) = f ^ { - 1 } ( X ) \cap f ^ { - 1 } ( Y )
$$

$$
f ( X \cup Y ) = f ( X ) \cup f ( Y )
$$

$$
f ^ { - 1 } ( X \cup Y ) = f ^ { - 1 } ( X ) \cup f ^ { - 1 } ( Y )
$$

Here for $A \subseteq \mathbb { R } , f ( A ) = \{ f ( x ) : x \in A \}$ and $f ^ { - 1 } ( A ) = \{ x \in \mathbb { R } : f ( x ) \in A \}$
:::

::: {.solution}
Pullbacks play nicely with both unions and intersections.
Pushforwards only play nicely with unions.
Thus (B), (C) and (D) are true while (A) is false.

I won’t prove that (B), (C), (D) are true (it isn’t too difficult), but to see that (A) is false, consider the function $f : \mathbb { R } \to \mathbb { R } , f ( x ) = x ^ { 2 }$ for $x \in \mathbb { R }$ and let $X = ( - 1 , 0 )$ and $Y = ( 0 , 1 )$ . Then $X \cap Y = \emptyset$ and so $f ( X \cap Y ) = \emptyset$ . However, $f ( X ) = ( 0 , 1 )$ and $f ( Y ) = ( 0 , 1 )$ so $f ( X \cap Y ) = \emptyset \neq$ $( 0 , 1 ) = f ( X ) \cap f ( Y )$
:::
