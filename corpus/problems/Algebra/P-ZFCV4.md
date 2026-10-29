---
schema: qual/card@1
id: P-ZFCV4
kind: problem
title: Galois-group conditions implied by irreducibility of a polynomial, and by a
  root in the base field
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Group Actions
  - Irreducibility Criteria
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.problem}
Tell me a condition on the Galois group which is implied by irreducibility of the polynomial.
What happens when the polynomial has a root in the base field?
:::

::: {.solution}
Let $f\in F[x]$ be irreducible of degree $n\ge1$, let $L$ be its splitting field over $F$, and let $G=\Gal(L/F)$.

::: pf

::: pf-step

$G$ acts transitively on the roots of $f$ in $L$.

::: pf-proof

Let $\alpha,\beta\in L$ be roots of $f$. Since $f$ is irreducible, it is the minimal polynomial of both up to a scalar, so there is an $F$-isomorphism $F(\alpha)\to F(\beta)\subseteq L$ with $\alpha\mapsto\beta$. Because $L/F$ is normal, this embedding extends to an $F$-automorphism $\sigma\in G$, and $\sigma(\alpha)=\beta$.

:::

:::

::: pf-step

If $f$ has a root in $F$, then $f$ has degree $1$, $L=F$, and $G$ is trivial.

::: pf-proof

If $\alpha\in F$ is a root, then $x-\alpha$ divides $f$ in $F[x]$, and irreducibility forces $f=c(x-\alpha)$ with $c\in F^\times$. Its only root lies in $F$, so $L=F$ and $G=\{1\}$.

:::

:::

:::

:::
