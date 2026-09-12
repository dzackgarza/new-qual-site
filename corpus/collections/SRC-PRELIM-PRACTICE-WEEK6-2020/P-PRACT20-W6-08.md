---
schema: qual/card@1
id: P-PRACT20-W6-08
kind: problem
title: "Week 6: Miscellaneous Topics, problem 8"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Which of the following exist?

(A) A continuous function from (0, 1) onto [0, 1]

(B) A continuous function from [0, 1] onto (0, 1)

(C) A continuous bijection from (0, 1) to [0, 1]
:::

::: {.solution}
For (A), such a function does exist.
Indeed, $f ( x ) = \sin ( 1 0 0 x )$ is an example of such a function.

For (B), no such function exists.
The continuous image of a compact set remains compact, so a continuous function cannot map [0, 1] onto (0, 1) since [0, 1] is compact and (0, 1) isn’t.

For (C), again no such function exists.
If $f : ( 0 , 1 )  [ 0 , 1 ]$ is a continuous surjection, there is $a \in ( 0 , 1 )$ such that $f ( a ) = 0$ and $b \in ( 0 , 1 )$ such that $f ( b ) = 1$ . But then by the intermediate value theorem, $f$ maps the interval $I = [ \operatorname* { m i n } \{ a , b \} , \operatorname* { m a x } \{ a , b \} ]$ onto [0, 1]. Thus it cannot be injective since for any $x \in ( 0 , 1 ) \backslash I$ , the image f(x) will already have been met by another value $y \in I$
:::
