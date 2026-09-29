---
schema: qual/card@1
id: P-BF8JM
kind: problem
title: $\mathrm{Gal}(M/L)$ is normal in $\mathrm{Gal}(M/K)$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $M/K$ be a finite Galois extension and let $K\subseteq L\subseteq M$ be an intermediate field such that $L/K$ is Galois. Prove that
\[
\Gal(M/L)\trianglelefteq \Gal(M/K).
\]
:::

::: {.solution}
Set
\[
G=\Gal(M/K),
\qquad
H=\Gal(M/L).
\]

::: pf

::: {.pf-step #s1}

Every $\phi\in G$ preserves $L$ setwise.

::: pf-proof

Because $L/K$ is Galois, it is normal. Therefore every $K$-embedding of $L$ into an algebraic closure has image $L$. The restriction $\phi|_L$ is such a $K$-embedding, so
\[
\phi(L)=L.
\]

:::

:::

::: {.pf-step #s2}

For every $\phi\in G$ and $\sigma\in H$, the conjugate $\phi\sigma\phi^{-1}$ fixes $L$ pointwise.

::: pf-proof

Let $\ell\in L$. By step [](#s1){.pf-ref}, $\phi^{-1}(\ell)\in L$. Since $\sigma\in H$, it fixes every element of $L$, hence
\[
\sigma(\phi^{-1}(\ell))=\phi^{-1}(\ell).
\]
Applying $\phi$ gives
\[
(\phi\sigma\phi^{-1})(\ell)=\ell.
\]
Thus $\phi\sigma\phi^{-1}\in H$.

:::

:::

::: pf-step

Therefore $H\trianglelefteq G$.

::: pf-proof

By step [](#s2){.pf-ref},
\[
\phi H\phi^{-1}\subseteq H
\]
for every $\phi\in G$. Applying the same inclusion to $\phi^{-1}$ gives the reverse containment, hence equality.

:::

:::

:::

:::
