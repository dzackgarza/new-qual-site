---
schema: qual/card@1
id: P-WESTOP07-10
kind: problem
title: Closed orientable surfaces of distinct genus are not homeomorphic
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $T_n$ denote the closed orientable surface of genus $n$, for $n\ge1$. Prove that if $p$ and $q$ are distinct positive integers, then $T_p$ and $T_q$ are not homeomorphic.
:::

::: {.solution}
<1>1. The closed orientable surface
$$
T_n
$$
admits a CW decomposition with one $0$-cell, $2n$ $1$-cells, and one $2$-cell.

::: {.proof}
Use the standard polygonal presentation
$$
a_1b_1a_1^{-1}b_1^{-1}
\cdots
a_nb_na_n^{-1}b_n^{-1}
$$
of the genus-$n$ orientable surface.

All polygon vertices are identified to one vertex, giving one $0$-cell. The paired edges give
$$
2n
$$
distinct $1$-cells, namely
$$
a_1,b_1,\ldots,a_n,b_n.
$$
The polygon interior gives one $2$-cell.
:::

<1>2. Therefore
$$
\boxed{\chi(T_n)=2-2n}.
$$

::: {.proof}
By step <1>1,
$$
\chi(T_n)
=
1-2n+1
=
2-2n.
$$
:::

<1>3. Euler characteristic is invariant under homeomorphism.

::: {.proof}
Homeomorphic finite CW complexes have the same singular homology groups, hence the same Euler characteristic
$$
\chi
=
\sum_k(-1)^k\operatorname{rank}H_k(-;\mathbb Z).
$$
Thus homeomorphic closed surfaces have equal Euler characteristic.
:::

<1>4. If
$$
T_p\cong T_q,
$$
then
$$
p=q.
$$

::: {.proof}
By step <1>3,
$$
\chi(T_p)=\chi(T_q).
$$
Using step <1>2,
$$
2-2p
=
2-2q.
$$
Hence
$$
p=q.
$$
:::

<1>5. Consequently, if
$$
p\ne q,
$$
then
$$
\boxed{T_p\not\cong T_q}.
$$

::: {.proof}
This is the contrapositive of step <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
