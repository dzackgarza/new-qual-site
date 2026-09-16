---
schema: qual/card@1
id: L-W5S2W
kind: lemma
title: Elementary divisors are the minimal polynomials of the Jordan blocks
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Structure Theorem
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: {.lemma}
Let $k$ be a field and let $A\in\Mat_n(k)$ have characteristic polynomial that splits over $k$, so that $A$ is similar to its Jordan canonical form $\JCF(A)$.
Then the elementary divisors of $A$, the prime-power factors in the decomposition of the $k[x]$-module $k^n$ with $x$ acting as $A$, are the [[D-GK5SF|minimal polynomials]] $(x-\lambda)^s$ of the Jordan blocks $J_s(\lambda)$ of $\JCF(A)$, listed with multiplicity.
:::

::: {.proof}
A Jordan block $J_s(\lambda)$ is the matrix of multiplication by $x$ on $k[x]/((x-\lambda)^s)$ in the basis $(x-\lambda)^{s-1},\ldots,(x-\lambda),1$, and its minimal polynomial is $(x-\lambda)^s$.
So the block decomposition of $\JCF(A)$ is a decomposition $k^n\cong\bigoplus k[x]/((x-\lambda)^s)$, one summand for each block, and the elementary divisors are unique up to order.
:::
