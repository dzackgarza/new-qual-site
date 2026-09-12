---
schema: qual/card@1
id: P-BKS07-7A
kind: problem
title: UC Berkeley Spring 2007 prelim 7A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let a and b be complex numbers, and let $f \colon \mathbb { C } \to \mathbb { C }$ be a non-constant entire function such that $f ( a z + b ) = f ( z )$ for all $z \in \mathbb { C }$ . Prove that there is a positive integer n such that $a ^ { n } = 1$
:::

::: {.solution}
If $a = 1$ , we are done, so assume that $a \neq 1$ . Then $a z + b = z$ has a unique solution, say c. Define $g ( z ) : = f ( z + c )$ , so

$$
g ( a z ) = f ( a z + c ) = f ( a z + a c + b ) = f ( a ( z + c ) + b ) = f ( z + c ) = g ( z ) .
$$

If the Taylor series of $g ( z )$ at z = 0 is $\textstyle \sum _ { i \geq 0 } g _ { i } z ^ { i }$ , then equating coefficients of $z ^ { n }$ in $g ( a z ) =$ $g ( z )$ yields

$$
a ^ { n } g _ { n } = g _ { n } .
$$

Since $f$ is not constant, g is not constant.
Therefore for some $n \geq 1$ we have $g _ { n } \neq 0$ , and hence $a ^ { n } = 1$
:::
