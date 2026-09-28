---
schema: qual/card@1
id: E-3GIQS
kind: problem
title: Mapping $\DD^c \cap \HH$ conformally onto $\HH$ with prescribed boundary values
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Map $\DD^c \intersect \HH$ to $\HH$, sending 

- $-1\to -1$
- $i\to 0$
- $1\to 1$

:::

::: {.solution}

![](../../assets/Complex_Analysis/050_Conformal_Maps/figures/2021-12-10_17-13-43.png)

The Joukowski map
\[
J(z)={1\over 2}\qty{z + z\inv}
\]
does this. For $z=re^{i\theta}$ with $r>1$ and $0<\theta<\pi$,
\[
\Im J(z)={1\over2}\qty{r-r\inv}\sin\theta>0,
\]
and $J$ is injective on $\theset{\abs z>1}$ with image $\CC\setminus[-1,1]$, so $J$ maps $\DD^c\intersect\HH$ bijectively onto $\HH$. Moreover $J(-1)=-1$, $J(i)=0$ and $J(1)=1$.

:::

