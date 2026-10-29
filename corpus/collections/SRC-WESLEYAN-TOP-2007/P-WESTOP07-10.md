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

::: pf

::: {.pf-step #s1-1}

The closed orientable surface
$$
T_n
$$
admits a CW decomposition with one $0$-cell, $2n$ $1$-cells, and one $2$-cell.


::: pf-proof

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

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{\chi(T_n)=2-2n}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\chi(T_n)
=
1-2n+1
=
2-2n.
$$

:::

:::

::: {.pf-step #s1-3}

Euler characteristic is invariant under homeomorphism.


::: pf-proof

Homeomorphic finite CW complexes have the same singular homology groups, hence the same Euler characteristic
$$
\chi
=
\sum_k(-1)^k\operatorname{rank}H_k(-;\ZZ).
$$
Thus homeomorphic closed surfaces have equal Euler characteristic.

:::

:::

::: {.pf-step #s1-4}

If
$$
T_p\cong T_q,
$$
then
$$
p=q.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\chi(T_p)=\chi(T_q).
$$
Using step [](#s1-2){.pf-ref},
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

:::

::: {.pf-step #s1-5}

Consequently, if
$$
p\ne q,
$$
then
$$
\boxed{T_p\not\cong T_q}.
$$


::: pf-proof

This is the contrapositive of step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
