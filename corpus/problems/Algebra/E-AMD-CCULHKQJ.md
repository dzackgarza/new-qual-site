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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source says K/F Galois without finiteness; the solution uses the finite Galois correspondence, so the statement now says finite Galois. The bulleted parts are relabelled (a)-(c).'
---

::: {.exercise}
Let $K/E/F$ be a tower of fields with $K/F$ finite Galois, and write $g(L/M)$ for the Galois group of $L/M$.

(a) Show that $K/E$ is Galois with $g(K/E) \leq g(K/F)$.

(b) Show that $E/F$ is Galois $\iff g(K/E) \normal g(K/F)$.

(c) Show that in this case, $g(E/F) = g(K/F) / g(K/E)$.
:::

::: {.solution}
Let
$$
G=\Gal(K/F),\qquad H=\Gal(K/E).
$$

(a) Because $K/F$ is finite Galois, $K$ is the splitting field over $F$ of a separable polynomial. The same polynomial lies in $E[x]$ and still splits in $K$, so $K/E$ is Galois. Also every $E$-automorphism of $K$ fixes $F$, hence
$$
H\le G.
$$

(b) Under the fundamental Galois correspondence, the fixed field of $H$ is $E$. For $\sigma\in G$,
$$
\Fix(\sigma H\sigma^{-1})=\sigma(E).
$$
Therefore
$$
H\trianglelefteq G
\iff \sigma(E)=E\ \text{for all }\sigma\in G.
$$
Since $E/F$ is automatically separable, the right-hand condition is equivalent to $E/F$ being normal, hence Galois. Thus
$$
E/F\text{ is Galois}\iff H\trianglelefteq G.
$$

(c) When these equivalent conditions hold, every $\sigma\in G$ satisfies $\sigma(E)=E$, so restriction gives a homomorphism
$$
\rho:G\to\Gal(E/F),\qquad \sigma\mapsto \sigma\restrict_E.
$$
Its kernel is $H$. Every $F$-automorphism of $E$ extends to an $F$-automorphism of the normal extension $K/F$, so $\rho$ is surjective. By the first isomorphism theorem,
$$
\boxed{\Gal(E/F)\cong G/H}
=\frac{\Gal(K/F)}{\Gal(K/E)}.
$$
:::
