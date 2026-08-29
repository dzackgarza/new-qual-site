---
schema: qual/card@1
id: E-DAS3L
kind: exercise
title: Cyclic groups, Euler's totient, and $\operatorname{Aut}(\mathbb{Z}/n\mathbb{Z})$
classification:
  areas:
  - algebra
  topics:
  - Cyclic Groups
  - Automorphisms
  - Number Theory
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.exercise}
\envlist

- Show that any cyclic group is abelian.

- Show that every subgroup of a cyclic group is cyclic.

- Show that $$\phi(n) = n \prod_{p\mid n}\qty{1 - {1\over p}}.$$

- Compute $\aut(\ZZ/n\ZZ)$ for $n$ composite.

- Compute $\aut(\qty{\ZZ/p\ZZ}^n)$.
:::

::: solution
*Any cyclic group is abelian.*  
If $G=\langle g\rangle$, then any elements are $g^a,g^b$. Then
$g^a g^b=g^{a+b}=g^b g^a$, so $G$ is abelian.

*Subgroups of a cyclic group are cyclic.*  
Let $H\le G=\langle g\rangle$ and let
\[
m=\min\{k>0:g^k\in H\}
\]
(the minimum over a nonempty set if $H\neq \{e\}$; take $m=0$ for $H=\{e\}$).
Then $H=\langle g^m\rangle$ by the usual Euclidean remainder argument.

\[
\phi(n)=|\mathrm{Aut}(\ZZ/n\ZZ)|=
\left|(\ZZ/n\ZZ)^\times\right|
=n\prod_{p\mid n}\left(1-\frac1p\right).
\]
This follows from the decomposition
\[
(\ZZ/n\ZZ)^\times \cong \prod_{p^a\| n}(\ZZ/p^a\ZZ)^\times
\]
and inclusion--exclusion on each prime factor.

\[
\mathrm{Aut}(\ZZ/n\ZZ)\cong (\ZZ/n\ZZ)^\times.
\]
Any automorphism is determined by where $1$ maps, and the image must be a unit mod $n$.

For $n$ composite, this group may be non-cyclic.
\[
(\ZZ/2^a\ZZ)^\times\cong
\begin{cases}
1,&a=1,\\
C_2,&a=2,\\
C_2\times C_{2^{a-2}},&a\ge3,
\end{cases}
\quad
(\ZZ/p^a\ZZ)^\times\text{ is cyclic of order }p^{a-1}(p-1)\ (p\text{ odd})
\]
and for general $n=\prod p_i^{a_i}$ we get
\[
\mathrm{Aut}(\ZZ/n\ZZ)\cong \prod_i (\ZZ/p_i^{a_i}\ZZ)^\times,\qquad
|\mathrm{Aut}(\ZZ/n\ZZ)|=\phi(n).
\]

Finally,
\[
\mathrm{Aut}((\ZZ/p\ZZ)^n)\cong \operatorname{GL}_n(\mathbb F_p),
\]
with
\[
|\operatorname{GL}_n(\mathbb F_p)|
=\prod_{i=0}^{n-1}(p^n-p^i).
\]
:::
