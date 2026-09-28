---
schema: qual/card@1
id: P-LOHM5
kind: problem
title: Groups of order $p^3$ have a normal subgroup of order $p^2$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Let $p$ be a prime and $\abs{G} = p^3$.
  Prove that $G$ has a normal subgroup $N$ of order $p^2$.

  - Suppose $N = \gens{h}$ is cyclic and classify all possibilities for $G$ if:

    - $\abs h = p^3$

    - $\abs h = p$.

    > Hint: Sylow and semidirect products.
:::

::: {.solution}
First, every group $G$ of order $p^3$ has a normal subgroup of order $p^2$. Since $G$ is a nontrivial finite $p$-group, $Z(G)\ne1$.

If $|Z(G)|\ge p^2$, then $Z(G)$ contains a subgroup of order $p^2$, and every subgroup of the center is normal.

If $|Z(G)|=p$, then $G/Z(G)$ has order $p^2$ and is abelian. Choose any subgroup
\[
L/Z(G)\le G/Z(G)
\]
of order $p$. Because $G/Z(G)$ is abelian, $L/Z(G)$ is normal, hence its inverse image $L$ is normal in $G$; moreover
\[
|L|=p^2.
\]
Thus a normal subgroup of order $p^2$ always exists.

The remaining bullets in the problem, read literally, are incompatible with the preceding hypothesis. If the same subgroup is assumed to satisfy
\[
N=\langle h\rangle,\qquad |N|=p^2,
\]
then necessarily
\[
|h|=p^2.
\]
Therefore neither case $|h|=p^3$ nor case $|h|=p$ can occur for that $N$.

If instead one merely asks what happens when **an element of $G$** has order $p^3$, then that element generates all of $G$, so
\[
G\cong C_{p^3}.
\]
The condition that $G$ merely contain an element of order $p$ gives no classification at all: every group of order $p^3$ contains such an element by Cauchy's theorem.
:::
