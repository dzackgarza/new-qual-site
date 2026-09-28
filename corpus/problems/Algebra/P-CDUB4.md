---
schema: qual/card@1
id: P-CDUB4
kind: problem
title: $[K(\alpha):K]$ equals the degree of the minimal polynomial of algebraic $\alpha$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Why is $[K(\alpha): K]$ equal to the degree of the minimal polynomial of $\alpha$ when it is algebraic?
:::

::: {.solution}
Let $m\in K[x]$ be the minimal polynomial of $\alpha$, of degree $d$.

<1>1. $K(\alpha)=K[\alpha]\cong K[x]/(m)$.

::: {.proof}
Evaluation $K[x]\to K[\alpha]$, $f\mapsto f(\alpha)$, is surjective with kernel $(m)$, since $m$ generates the ideal of polynomials vanishing at $\alpha$.
Since $m$ is irreducible, $(m)$ is maximal, so $K[\alpha]$ is a field and equals $K(\alpha)$.
:::

<1>2. $1,\alpha,\dots,\alpha^{d-1}$ is a $K$-basis of $K(\alpha)$.

::: {.proof}
They span: for $f\in K[x]$, division gives $f=qm+r$ with $\deg r<d$, so $f(\alpha)=r(\alpha)$.
They are independent: a relation $\sum_{i<d}c_i\alpha^i=0$ is a polynomial of degree less than $d$ vanishing at $\alpha$, hence zero by minimality of $m$.
:::

<1>3. Q.E.D.

::: {.proof}
By step <1>2, $[K(\alpha):K]=d=\deg m$.
:::
:::
