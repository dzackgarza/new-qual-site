---
schema: qual/card@1
id: P-BKF04-3A
kind: problem
title: UC Berkeley Fall 2004 prelim 3A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f$ and $g$ be functions that are holomorphic on all of $\mathbb { C } .$ except that g has an essential singularity at the complex number c. Prove that either $f$ is constant, or the composition $f \circ g$ has an essential singularity at c. (Hint: you may assume the Casorati-Weierstrass Theorem, which states that if a function $f$ has an essential singularity at ${ \mathit { c } } ,$ then for any punctured neighborhood N of c on which f is holomorphic, the image $f ( N )$ is dense in C.)
:::

::: {.solution}
Suppose that f is not constant. Choose a, $b \in \mathbb { C }$ such that $f ( a ) \neq f ( b )$ . If N is any punctured neighborhood of $c ,$ then $g ( N )$ is dense in C, by the Casorati-Weierstrass Theorem. In particular, the closure of $g ( N )$ contains a and $b ,$ so the closure of $f ( g ( N ) )$ ) contains $f ( a )$ and $f ( b )$ . Since this holds for every N , the limit $\scriptstyle \operatorname* { l i m } _ { z \to c } f ( g ( z ) )$ is not ∞, and does not exist as a complex number either. Thus $f \circ g$ has neither a pole nor a removable singularity at ${ \mathit { c } } ,$ so it has an essential singularity at c.
:::
