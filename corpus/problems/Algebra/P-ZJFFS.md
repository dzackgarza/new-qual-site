---
schema: qual/card@1
id: P-ZJFFS
kind: problem
title: Quadratic extensions in characteristic 0 are Galois; stacked quadratics need
  not be
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Normal Subgroups
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

::: problem
Take a quadratic extension of a field of characteristic 0. Is it Galois?
Take a degree 2 extension on top of that.
Does it have to be Galois over the base field?
What statement in group theory can you think of that reflects this?
:::

::: solution
Let $K/F$ be quadratic with $\operatorname{char}F=0$. If $K=F(\alpha)$ and the minimal polynomial of $\alpha$ is
\[
x^2+bx+c,
\]
then its other root is $-b-\alpha\in K$. Hence the polynomial splits in $K$, and characteristic $0$ gives separability. Thus every quadratic extension in characteristic $0$ is Galois.

A tower of quadratic extensions need not be Galois over the bottom field. For example,
\[
\mathbb Q\subset \mathbb Q(\sqrt2)\subset
L:=\mathbb Q\bigl(\sqrt{1+\sqrt2}\bigr).
\]
The second step is quadratic because $1+\sqrt2$ is not a square in $\mathbb Q(\sqrt2)$: its norm is $-1$, whereas the norm of a square is a square in $\mathbb Q$. Let
\[
\alpha=\sqrt{1+\sqrt2}.
\]
Then $\alpha$ has polynomial
\[
x^4-2x^2-1,
\]
whose other roots include
\[
\pm\sqrt{1-\sqrt2},
\]
which are nonreal. Since $L\subset\mathbb R$, those roots are not in $L$. Thus $L/\mathbb Q$ is not normal and hence not Galois.

The group-theoretic analogue is that normality is not transitive:
\[
H\trianglelefteq K,\quad K\trianglelefteq G
\centernot\implies
H\trianglelefteq G.
\]
For example,
\[
\langle(12)(34)\rangle\trianglelefteq V_4\trianglelefteq A_4,
\]
but $\langle(12)(34)\rangle$ is not normal in $A_4$.
:::
