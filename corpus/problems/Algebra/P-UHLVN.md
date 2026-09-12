---
schema: qual/card@1
id: P-UHLVN
kind: problem
title: Galois groups of cubics
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
  - Polynomials
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
What are the possible Galois groups for a cubic polynomial $f(x) \in K[x]$ over a field $K$ (of characteristic $\ne 2, 3$)?
Classify them completely using the discriminant and irreducibility.
:::

::: solution
Let $L$ be the splitting field of a cubic $f\in K[x]$, with $\operatorname{char}K\ne2,3$.

If $f$ splits over $K$, then $L=K$ and the Galois group is trivial. If
\[
f=(x-a)q(x)
\]
with $q$ irreducible quadratic, then $L$ is the quadratic splitting field of $q$, so
\[
\operatorname{Gal}(L/K)\cong C_2.
\]

Now suppose $f$ is irreducible. Then its roots are distinct and the Galois group $G\le S_3$ acts transitively, so
\[
G\cong A_3\quad\text{or}\quad S_3.
\]
Let
\[
\delta=(\alpha_1-\alpha_2)(\alpha_1-\alpha_3)(\alpha_2-\alpha_3),
\qquad \Delta(f)=\delta^2.
\]
A permutation of the roots sends $\delta$ to its sign times $\delta$. Therefore
\[
G\subseteq A_3
\iff \delta\in K
\iff \Delta(f)\in K^{\times2}.
\]
Consequently,
\[
\operatorname{Gal}(L/K)\cong
\begin{cases}
C_3,& f\text{ irreducible and }\Delta(f)\text{ is a square in }K,\\
S_3,& f\text{ irreducible and }\Delta(f)\text{ is not a square in }K.
\end{cases}
\]
These, together with the trivial and $C_2$ reducible cases, are all possibilities.
:::
