---
schema: qual/card@1
id: P-BKF04-3B
kind: problem
title: Sizes of rational matrices satisfying $A^3+A+I=0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
For which positive integers $n$ does there exist an $n\times n$ matrix $A$ with rational entries such that $A^3+A+I=0$?
:::

::: {.solution}
The polynomial $f(x)=x^3+x+1$ is irreducible over $\QQ$: it is a cubic, and by the rational root test its only possible rational roots $\pm1$ are not roots. Since $f(A)=0$, the minimal polynomial of $A$ divides $f$ and hence equals $f$, so every irreducible factor of the characteristic polynomial of $A$ is $f$. Thus the characteristic polynomial of $A$ is a power of $f$, and $n$ is a multiple of $3$.

Conversely, if $n=3$, let $V=\QQ[x]/(x^3+x+1)$, and let $A$ be the matrix, with respect to some basis, of the $\QQ$-linear map $V\to V$ given by multiplication by the image of $x$. For $n$ any larger multiple of $3$, take $A$ block-diagonal with each $3\times3$ diagonal block equal to the matrix for $n=3$. The answer is $\boxed{n\equiv0\pmod3}$.
:::
