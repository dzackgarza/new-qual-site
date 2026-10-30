---
schema: qual/card@1
id: P-QYCPP
kind: problem
title: Sylow $p$-subgroups of $\GL_3(\FF_p)$, their conjugates, and their normalizers
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $G = \GL_3(\FF_p)$ for $p$ prime.

(a) What is the order of $G$, and what is the order of a Sylow $p$-subgroup?

(b) Give the standard matrix form for the canonical Sylow $p$-subgroup $P \le G$.

(c) Give the matrix form for the normalizer $N_G(P)$ and compute the number of conjugates (Sylow $p$-subgroups) $n_p$.

(d) Explain conjugacy of Sylow $p$-subgroups in terms of complete flags / eigenspaces.
:::

::: {.solution}
Let $e_1,e_2,e_3$ be the standard basis of $V\coloneqq\FF_p^3$.

::: pf

::: pf-step
(a) $\cardinality{G}=\boxed{p^3(p-1)^3(p+1)(p^2+p+1)}$, and a Sylow $p$-subgroup has order $\boxed{p^3}$.

::: pf-proof
An invertible matrix is a choice of a nonzero first column, a second column outside its span, and a third outside the span of the first two, so $\cardinality{G}=(p^3-1)(p^3-p)(p^3-p^2)$, which factors as stated. The factor $(p-1)^3(p+1)(p^2+p+1)$ is prime to $p$.
:::

:::

::: pf-step
(b) The upper unitriangular group
$$
P=\left\{\begin{pmatrix}1&a&b\\0&1&c\\0&0&1\end{pmatrix}:a,b,c\in\FF_p\right\}
$$
is a Sylow $p$-subgroup.

::: pf-proof
It is a subgroup of order $p^3$.
:::

:::

::: {.pf-step #flag}
The flag $0<\langle e_1\rangle<\langle e_1,e_2\rangle<V$ is determined by $P$: $\langle e_1\rangle=\{v:gv=v\text{ for all }g\in P\}$ and $\langle e_1,e_2\rangle=\{v:(g-1)v\in\langle e_1\rangle\text{ for all }g\in P\}$.

::: pf-proof
For $g\in P$ with entries $a,b,c$ and $v=(x,y,z)^T$, $(g-1)v=(ay+bz,\,cz,\,0)^T$. This vanishes for all $a,b,c$ exactly when $y=z=0$, and lies in $\langle e_1\rangle$ for all $a,b,c$ exactly when $z=0$.
:::

:::

::: {.pf-step #normalizer}
(c) $N_G(P)$ is the upper triangular group
$$
B=\left\{\begin{pmatrix}d_1&a&b\\0&d_2&c\\0&0&d_3\end{pmatrix}:d_i\in\FF_p^\times,\ a,b,c\in\FF_p\right\},
$$
and $n_p=[G:B]=\boxed{(p+1)(p^2+p+1)}$.

::: pf-proof
$P$ is the kernel of the homomorphism $B\to(\FF_p^\times)^3$ that takes the diagonal, so $B\le N_G(P)$. Conversely, if $hPh^{-1}=P$, then $h$ maps each subspace that step [](#flag){.pf-ref} defines from $P$ to itself, so $h$ stabilizes $\langle e_1\rangle$ and $\langle e_1,e_2\rangle$ and is upper triangular. Then $n_p=[G:N_G(P)]=\cardinality{G}/(p^3(p-1)^3)$.
:::

:::

::: pf-step
(d) Sylow $p$-subgroups correspond bijectively to complete flags in $V$, by $F\mapsto P_F\coloneqq\{g:g$ fixes $F$ and acts as the identity on each successive quotient$\}$, and conjugation of Sylow subgroups corresponds to the transitive action of $G$ on complete flags.

::: pf-proof
For $g\in G$, $gP_Fg^{-1}=P_{gF}$, and $G$ acts transitively on complete flags because any basis adapted to a flag can be carried to any other. Hence the $P_F$ are exactly the conjugates of $P=P_{F_0}$ for the standard flag $F_0$. By step [](#flag){.pf-ref}, translated by $g$, the flag $F$ is recovered from $P_F$, so $F\mapsto P_F$ is injective. In particular, the number of complete flags, $(p^2+p+1)(p+1)$ (a line, then a plane containing it), equals $n_p$ from step [](#normalizer){.pf-ref}.
:::

:::

:::
:::
