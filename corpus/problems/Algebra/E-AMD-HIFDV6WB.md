---
schema: qual/card@1
id: E-AMD-HIFDV6WB
kind: problem
title: Galois group of $x^3+4x+2$ over $\QQ$ is $S_3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that $\operatorname{Gal}(x^3+4x+2 / \mathbb{Q}) \cong S_3$.
:::

::: {.solution}
Let
\[
f(x)=x^3+4x+2.
\]
By Eisenstein's criterion at $2$, $f$ is irreducible over $\QQ$. Therefore its Galois group $G$ acts transitively on the three roots, so
\[
G\cong A_3\quad\text{or}\quad S_3.
\]

For a depressed cubic $x^3+px+q$, the discriminant is
\[
\Delta=-4p^3-27q^2.
\]
Here
\[
\Delta=-4\cdot4^3-27\cdot2^2=-364.
\]
This is not a square in $\QQ$. For an irreducible cubic over a field of characteristic different from $2$, the Galois group lies in $A_3$ exactly when the discriminant is a square. Hence $G\not\subseteq A_3$.

Therefore
\[
\boxed{\Gal(f/\QQ)\cong S_3}.
\]
:::
