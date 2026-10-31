---
schema: qual/card@1
id: P-UCTOP290-S7-9
kind: problem
title: Homology of a knotted solid torus exterior
classification:
  areas:
  - topology
  topics:
  - Homology
  - Knots
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 7, Problem 9 in its checked-in extraction.
---

::: {.problem}
Let $N$ be a knotted solid torus in $S^3$, let $T=\partial N$,
and let $X=\overline{S^3\setminus N}$ be its exterior.
Use Mayer–Vietoris to compute $H_*(X;\ZZ)$.
:::

::: {.solution}

Use the Mayer–Vietoris sequence for $S^3=N\cup X$,
with intersection homotopy equivalent to $T$.
The relevant groups are
$$
H_2(T)=\ZZ,\quad H_1(T)=\ZZ^2,\quad
H_1(N)=\ZZ,\quad H_2(N)=H_3(N)=0.
$$

The connecting map
$$
H_3(S^3)\longrightarrow H_2(T)
$$
sends the oriented fundamental class of $S^3$ to the oriented
fundamental class of the common boundary $T$. It is an
isomorphism $\ZZ\to\ZZ$. Exactness therefore gives
$H_3(X)=0$ and $H_2(X)=0$.

The next part of the sequence is
$$
0=H_2(S^3)\longrightarrow H_1(T)
\longrightarrow H_1(N)\oplus H_1(X)
\longrightarrow H_1(S^3)=0.
$$
Thus $\ZZ^2\cong\ZZ\oplus H_1(X)$, and the structure
theorem for finitely generated abelian groups gives
$H_1(X)\cong\ZZ$.
The degree-zero part of Mayer–Vietoris, using that $T$ and
$N$ are connected, gives $H_0(X)\cong\ZZ$.
Higher homology vanishes by dimension. Hence
$$
H_k(X;\ZZ)\cong
\begin{cases}
\ZZ,&k=0,1,\\
0,&k\ge2.
\end{cases}
$$
The knot type does not change these homology groups.

:::
