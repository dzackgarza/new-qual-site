---
schema: qual/card@1
id: E-AMD-CCULHKQJ
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
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $K/E/F$ with $K/F$ Galois then $K/E$ is always Galois with $g(K/E) \leq g(K/F)$.

- Show additionally $E/F$ is Galois $\iff g(K/E) \normal g(K/F)$.

- Show that in this case, $g(E/F) = g(K/F) / g(K/E)$.
:::

::: {.solution}
Let
\[
G=\Gal(K/F),\qquad H=\Gal(K/E).
\]
Because $K/F$ is finite Galois, $K$ is the splitting field over $F$ of a separable polynomial. The same polynomial lies in $E[x]$ and still splits in $K$, so $K/E$ is Galois. Also every $E$-automorphism of $K$ fixes $F$, hence
\[
H\le G.
\]

Under the fundamental Galois correspondence, the fixed field of $H$ is $E$. For $\sigma\in G$,
\[
\Fix(\sigma H\sigma^{-1})=\sigma(E).
\]
Therefore
\[
H\trianglelefteq G
\iff \sigma(E)=E\ \text{for all }\sigma\in G.
\]
Since $E/F$ is automatically separable, the right-hand condition is equivalent to $E/F$ being normal, hence Galois. Thus
\[
E/F\text{ is Galois}\iff H\trianglelefteq G.
\]

When these equivalent conditions hold, restriction gives a homomorphism
\[
\rho:G\to\Gal(E/F),\qquad \sigma\mapsto \sigma|_E.
\]
Its kernel is $H$. Every $F$-automorphism of $E$ extends to an $F$-automorphism of the normal extension $K/F$, so $\rho$ is surjective. By the first isomorphism theorem,
\[
\boxed{\Gal(E/F)\cong G/H}
=\frac{\Gal(K/F)}{\Gal(K/E)}.
\]
:::
