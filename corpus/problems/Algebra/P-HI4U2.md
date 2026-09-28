---
schema: qual/card@1
id: P-HI4U2
kind: problem
title: The rings and fields $K[x]$, $K(x)$, $K[\alpha]$, and $K(\alpha)$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
  - Fields
relations: []
review: draft
---

::: {.problem}
What are the following objects?

- $K(x)$

- $K[x]$

- $K( \alpha)$

- $K[ \alpha]$
:::

::: {.solution}
For a field $K$ and a variable $x$, $K[x]$ is the ring of polynomials in $x$ with coefficients in $K$, and $K(x)=\operatorname{Frac}(K[x])$ is the field of rational functions $p/q$ with $p,q\in K[x]$, $q\neq0$.

For a field extension $K\subseteq F$ and $\alpha\in F$, $K[\alpha]$ is the smallest subring of $F$ containing $K$ and $\alpha$, and $K(\alpha)$ is the smallest subfield of $F$ containing $K$ and $\alpha$.
Evaluation $x\mapsto\alpha$ is the unique $K$-algebra homomorphism $K[x]\to K[\alpha]$ sending $x$ to $\alpha$, and it is surjective.
If $\alpha$ is transcendental over $K$, it is injective, so $K[\alpha]\cong K[x]$ and $K(\alpha)\cong K(x)$.
If $\alpha$ is algebraic with minimal polynomial $m$, its kernel is $(m)$, and $K[\alpha]\cong K[x]/(m)$ is already a field, so $K[\alpha]=K(\alpha)$.
:::
