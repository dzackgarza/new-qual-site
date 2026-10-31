---
schema: qual/card@1
id: E-HAT-4.3-22
kind: problem
title: "Principal fibrations with sections split"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that a principal fibration $\Omega C \to E \xrightarrow{p} B$ is fiber homotopy equivalent to the product $\Omega C \times B$ if it has a section, a map $s: B \to E$ with $ps = \id$.
:::

::: {.solution}
By definition, a principal fibration is fiber homotopy equivalent to the pullback of the path-space fibration
$$
\Omega C\longrightarrow PC\xrightarrow{\operatorname{ev}_1}C
$$
along a map $f:B\to C$. Thus its total space can be represented by pairs $(b,\gamma)$ with $\gamma(0)=c_0$ and $\gamma(1)=f(b)$.

A section assigns to each $b$ such a path $\gamma_b$, continuously in $b$. The formula
$$
H(b,t)=\gamma_b(t)
$$
is a homotopy from the constant map at $c_0$ to $f$. By homotopy invariance of pullback fibrations (Exercise 11), pulling the path-space fibration back along $f$ gives a fibration fiber homotopy equivalent to its pullback along the constant map. The latter is
$$
B\times\Omega C\longrightarrow B.
$$
Consequently $E\to B$ is fiber homotopy equivalent to the stated product fibration.
:::
