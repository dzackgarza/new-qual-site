---
schema: qual/card@1
id: P-WESTOP09-II4
kind: problem
title: Homology of a tame-knot exterior
classification:
  areas:
  - topology
  topics:
  - Homology
  - Knot Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $K:S^1\hookrightarrow S^3$ be a tame knot
with a tubular neighborhood $N(K)\cong S^1\times D^2$.
Compute $H_i(S^3\setminus N(K);\ZZ)$ for every $i$.
:::

::: {.solution}

The neighborhood $N(K)$ deformation retracts onto
its core circle, so
$\widetilde H^j(N(K);\ZZ)$ is $\ZZ$ for $j=1$
and zero otherwise. Since $N(K)$ is compact and
locally contractible, Alexander duality gives
$$
\widetilde H_i(S^3\setminus N(K);\ZZ)
\cong \widetilde H^{\,2-i}(N(K);\ZZ).
$$
Thus the complement has reduced homology $\ZZ$
in degree one and zero in every other degree.
In particular it is connected. Therefore
$$
H_i(S^3\setminus N(K);\ZZ)\cong
\begin{cases}
\ZZ,&i=0,1,\\
0,&\text{otherwise}.
\end{cases}
$$
:::
