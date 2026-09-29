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

::: pf

::: pf-step

$K(\alpha)=K[\alpha]\cong K[x]/(m)$.

::: pf-proof

Evaluation $K[x]\to K[\alpha]$, $f\mapsto f(\alpha)$, is surjective with kernel $(m)$, since $m$ generates the ideal of polynomials vanishing at $\alpha$.
Since $m$ is irreducible, $(m)$ is maximal, so $K[\alpha]$ is a field and equals $K(\alpha)$.

:::

:::

::: {.pf-step #s2}

$1,\alpha,\dots,\alpha^{d-1}$ is a $K$-basis of $K(\alpha)$.

::: pf-proof

They span: for $f\in K[x]$, division gives $f=qm+r$ with $\deg r<d$, so $f(\alpha)=r(\alpha)$.
They are independent: a relation $\sum_{i<d}c_i\alpha^i=0$ is a polynomial of degree less than $d$ vanishing at $\alpha$, hence zero by minimality of $m$.

:::

:::

::: pf-qed

By step [](#s2){.pf-ref}, $[K(\alpha):K]=d=\deg m$.

:::

:::

:::
