---
schema: qual/card@1
id: P-APASP07G
kind: problem
title: "Decomposition of an induced symmetric group module into irreducibles"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $W$ be the $S_9$-module obtained by inducing up from the $S_6 \times S_3$-module $V_{(3,3)} \otimes V_{(2,1)}$; here $V_\lambda$ denotes the simple $S_n$-module labeled by the Young diagram $\lambda$.
Determine the decomposition of $W$ into a direct sum of irreducible $S_9$-modules.
:::

::: {.solution}
By the Frobenius characteristic map, induction from $S_6\times S_3$ corresponds to multiplication of Schur functions. Therefore the decomposition of $W$ is determined by
\[
s_{(3,3)}s_{(2,1)}.
\]
Use
\[
s_{(2,1)}=s_{(2)}s_{(1)}-s_{(3)},
\]
which follows from the Pieri product
\[
s_{(2)}s_{(1)}=s_{(3)}+s_{(2,1)}.
\]

First apply the horizontal-strip Pieri rule to $s_{(3,3)}s_{(2)}$. The partitions obtained by adding a horizontal $2$-strip to $(3,3)$ are
\[
(5,3),\qquad (4,3,1),\qquad (3,3,2).
\]
Hence
\[
s_{(3,3)}s_{(2)}
=s_{(5,3)}+s_{(4,3,1)}+s_{(3,3,2)}.
\]
Multiplying by $s_{(1)}$ and applying Pieri again gives
\[
\begin{aligned}
s_{(3,3)}s_{(2)}s_{(1)}
={}&s_{(6,3)}+s_{(5,4)}+2s_{(5,3,1)}+s_{(4,4,1)}\\
&+2s_{(4,3,2)}+s_{(4,3,1,1)}+s_{(3,3,3)}+s_{(3,3,2,1)}.
\end{aligned}
\]

Next apply Pieri directly to $s_{(3,3)}s_{(3)}$. The horizontal $3$-strips give
\[
s_{(3,3)}s_{(3)}
=s_{(6,3)}+s_{(5,3,1)}+s_{(4,3,2)}+s_{(3,3,3)}.
\]
Subtracting yields
\[
\boxed{
\begin{aligned}
s_{(3,3)}s_{(2,1)}
={}&s_{(5,4)}+s_{(5,3,1)}+s_{(4,4,1)}\\
&+s_{(4,3,2)}+s_{(4,3,1,1)}+s_{(3,3,2,1)}.
\end{aligned}}
\]
Thus
\[
\boxed{
W\cong
V_{(5,4)}\oplus V_{(5,3,1)}\oplus V_{(4,4,1)}\oplus
V_{(4,3,2)}\oplus V_{(4,3,1,1)}\oplus V_{(3,3,2,1)}.
}
\]
Every constituent occurs with multiplicity one.

As a dimension check, the hook-length formula gives constituent dimensions
\[
42,\ 162,\ 84,\ 168,\ 216,\ 168,
\]
whose sum is $840$. On the other hand,
\[
\dim W
=[S_9:S_6\times S_3]\dim V_{(3,3)}\dim V_{(2,1)}
=84\cdot5\cdot2
=840,
\]
so the decomposition has the correct total dimension.
:::
