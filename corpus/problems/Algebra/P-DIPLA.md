---
schema: qual/card@1
id: P-DIPLA
kind: problem
title: Fundamental theorem of Galois theory
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $K/F$ be a finite Galois extension and let $E$ be an intermediate field ($F \subseteq E \subseteq K$).
(1) Prove that $K/E$ is always Galois with $\operatorname{Gal}(K/E) \le \operatorname{Gal}(K/F)$.
(2) Prove that $E/F$ is Galois if and only if $\operatorname{Gal}(K/E) \trianglelefteq \operatorname{Gal}(K/F)$.
(3) Prove that when $E/F$ is Galois, $\operatorname{Gal}(E/F) \cong \operatorname{Gal}(K/F) / \operatorname{Gal}(K/E)$.
:::

::: {.solution}
Write
\[
G=\operatorname{Gal}(K/F),\qquad H=\operatorname{Gal}(K/E).
\]

Because $K/F$ is finite Galois, every element of $K$ is separable over $F$, hence also over $E$. Moreover, if $K$ is the splitting field over $F$ of a separable polynomial $f\in F[x]$, then
\[
K=F(\text{roots of }f)=E(\text{roots of }f),
\]
so $K$ is also the splitting field of $f$ over $E$. Thus $K/E$ is Galois. Every automorphism fixing $E$ fixes $F$, so $H\le G$.

Under the Galois correspondence, the fixed field of $\sigma H\sigma^{-1}$ is $\sigma(E)$. Therefore
\[
H\trianglelefteq G
\iff \sigma(E)=E\quad\text{for every }\sigma\in G.
\]
Since $E/F$ is separable, the latter condition is equivalent to $E/F$ being normal, hence Galois. This proves
\[
E/F\text{ is Galois}\iff H\trianglelefteq G.
\]

Assume now that $E/F$ is Galois. Restriction defines
\[
\rho:G\longrightarrow \operatorname{Gal}(E/F),\qquad \rho(\sigma)=\sigma|_E.
\]
Its kernel is exactly $H$. Every $F$-automorphism of $E$ extends to an $F$-automorphism of the normal extension $K/F$, so $\rho$ is surjective. Hence the first isomorphism theorem gives
\[
\operatorname{Gal}(E/F)\cong G/H
=\operatorname{Gal}(K/F)/\operatorname{Gal}(K/E).
\]
:::
