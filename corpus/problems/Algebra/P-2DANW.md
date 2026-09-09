---
schema: qual/card@1
id: P-2DANW
kind: problem
title: 'Groups of order $240$: Sylow numbers and subgroups of order $15$'
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Semidirect Products
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the missing n_3=16 Sylow possibility and retained the normalizer argument for the final restriction.
---

::: {.exercise}
Let $|G|=240=2^4\cdot3\cdot5$.

1. Determine the Sylow-number possibilities for $p=2,3,5$.
2. Show that a subgroup of order $15$ is cyclic.
3. If $G$ has no subgroup of order $15$, show that $n_3\in\{10,40\}$.
:::

::: {.solution}
Sylow's theorem gives
\[
n_2\mid15,\quad n_2\equiv1\pmod2,
\]
so
\[
n_2\in\{1,3,5,15\}.
\]
Also
\[
n_3\mid80,\quad n_3\equiv1\pmod3,
\]
so
\[
n_3\in\{1,4,10,16,40\},
\]
and
\[
n_5\mid48,\quad n_5\equiv1\pmod5,
\]
so
\[
n_5\in\{1,6,16\}.
\]

Now let $H\le G$ have order $15$. In $H$, the Sylow $5$-subgroup is unique because its number divides $3$ and is $1$ modulo $5$. The Sylow $3$-subgroup is also unique because its number divides $5$ and is $1$ modulo $3$. Hence both are normal, commute, and have trivial intersection. Therefore
\[
H\cong C_5\times C_3\cong C_{15}.
\]

Finally suppose $G$ has no subgroup of order $15$. Let $P$ be a Sylow $3$-subgroup. If $5\mid|N_G(P)|$, Cauchy's theorem gives an element $y\in N_G(P)$ of order $5$. Then $P\trianglelefteq\langle P,y\rangle$ and
\[
|\langle P,y\rangle|=15,
\]
a contradiction. Thus
\[
5\nmid |N_G(P)|=\frac{240}{n_3}.
\]
Therefore $5\mid n_3$. Among
\[
\{1,4,10,16,40\},
\]
this leaves exactly
\[
n_3\in\{10,40\}.
\]
:::
