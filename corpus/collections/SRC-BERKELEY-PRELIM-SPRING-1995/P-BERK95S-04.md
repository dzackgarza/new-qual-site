---
schema: qual/card@1
id: P-BERK95S-04
kind: problem
title: Order and Sylow-$p$ subgroups of $GL_2(\mathbb F_{p^n})$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $F$ be a finite field of cardinality $p^n$, where $p$ is prime and $n>0$, and let
\[
G=GL_2(F).
\]

1. Prove that
   \[
   |G|=(p^{2n}-1)(p^{2n}-p^n).
   \]
2. Show that every Sylow-$p$ subgroup of $G$ is isomorphic to the additive group of $F$.
:::

::: {.solution}
Put
$$
q\coloneqq\abs F=p^n.
$$

<1>1.
$$
\abs{G}=(q^2-1)(q^2-q).
$$

::: {.proof}
An invertible $2\times2$ matrix is the same as an ordered basis of
$F^2$. Its first column can be any nonzero vector, giving
$q^2-1$ choices. Once the first column is fixed, its span contains
exactly $q$ vectors, so the second column has $q^2-q$ choices outside
that span. Multiplying gives the formula.
:::

<1>2. The largest power of $p$ dividing $\abs G$ is $p^n=q$.

::: {.proof}
Step <1>1 gives
$$
\abs G
=(q^2-1)(q^2-q)
=q(q-1)^2(q+1).
$$
Since $q=p^n$,
$$
q-1\equiv-1\pmod p,
\qquad
q+1\equiv1\pmod p,
$$
so neither $q-1$ nor $q+1$ is divisible by $p$. Thus the full
$p$-part of $\abs G$ is $q=p^n$.
:::

<1>3. The subgroup
$$
U\coloneqq
\left\{
\begin{pmatrix}
1&a\\
0&1
\end{pmatrix}
:a\in F
\right\}
$$
is a Sylow-$p$ subgroup of $G$ and is isomorphic to $(F,+)$.

::: {.proof}
Matrix multiplication gives
$$
\begin{pmatrix}
1&a\\
0&1
\end{pmatrix}
\begin{pmatrix}
1&b\\
0&1
\end{pmatrix}
=
\begin{pmatrix}
1&a+b\\
0&1
\end{pmatrix}.
$$
Hence
$$
(F,+)\longrightarrow U,
\qquad
a\longmapsto
\begin{pmatrix}
1&a\\
0&1
\end{pmatrix}
$$
is a group isomorphism. In particular,
$\abs U=\abs F=q=p^n$, which is the full $p$-part of $\abs G$ by step
<1>2. Thus $U$ is Sylow-$p$.
:::

<1>4. Every Sylow-$p$ subgroup of $G$ is isomorphic to $(F,+)$.

::: {.proof}
By the Sylow conjugacy theorem, every Sylow-$p$ subgroup of $G$ is
conjugate to $U$. Conjugate subgroups are isomorphic, and step <1>3
identifies $U$ with $(F,+)$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves part 1, and step <1>4 proves part 2.
:::
:::
