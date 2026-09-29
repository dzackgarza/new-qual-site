---
schema: qual/card@1
id: P-APAF21E
kind: problem
title: Central group elements act by scalars on an irreducible representation
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $G$ be a finite group and let $V$ be an irreducible complex representation of $G$.
If $g\in G$ lies in the center of $G$, show that there exists $c\in\mathbb{C}$ with
\[
g\cdot v=cv
\]
for all $v\in V$.
:::

::: {.solution}

Let $\rho:G\to\operatorname{GL}(V)$ denote the representation.

::: pf

::: {.pf-step #rho-g-commutes-with-rho-h}
The operator $\rho(g)$ commutes with $\rho(h)$ for every $h\in G$.

::: pf-proof
Since $g\in Z(G)$,
\[
gh=hg
\]
for every $h\in G$. Therefore
\[
\rho(g)\rho(h)=\rho(gh)=\rho(hg)=\rho(h)\rho(g).
\]
Thus $\rho(g)$ is an endomorphism of the $G$-module $V$.
:::

:::

::: {.pf-step #rho-g-is-scalar}
There exists $c\in\mathbb C$ such that
\[
\rho(g)=cI_V.
\]

::: pf-proof
The representation $V$ is irreducible over the algebraically closed field $\mathbb C$. By Schur's lemma,
\[
\operatorname{End}_G(V)=\mathbb C\,I_V.
\]
By step [](#rho-g-commutes-with-rho-h){.pf-ref}, $\rho(g)\in\operatorname{End}_G(V)$, so $\rho(g)=cI_V$ for some $c\in\mathbb C$.
:::

:::

::: pf-step
Hence
\[
g\cdot v=cv
\qquad\text{for every }v\in V.
\]

::: pf-proof
This is exactly the statement $\rho(g)=cI_V$ from step [](#rho-g-is-scalar){.pf-ref} evaluated on $v$.
:::

:::

:::

:::
