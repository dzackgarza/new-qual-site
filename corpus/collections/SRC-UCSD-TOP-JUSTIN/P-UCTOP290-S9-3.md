---
schema: qual/card@1
id: P-UCTOP290-S9-3
kind: problem
title: Euler characteristic and Betti numbers under surface covers
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Covering Spaces
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 9, Problem 3 in its checked-in extraction; its requested decrease of a homology rank under a finite cover is false.
---

::: {.problem}
Show that the genus-ten orientable surface
$\Sigma_{10}$ cannot cover $\Sigma_5$.
Determine how individual rational homology
ranks can change under a finite covering.
:::

::: {.solution}

If $p:\Sigma_{10}\to\Sigma_5$ were a
$d$-sheeted cover, multiplicativity of
Euler characteristic would give
$$
-18=\chi(\Sigma_{10})
=d\,\chi(\Sigma_5)=-8d.
$$
This forces $d=9/4$, which is impossible
for a covering degree.

For any $d$-sheeted cover $p:Y\to X$,
the cohomological transfer satisfies
$\operatorname{tr}\circ p^*=d\,1$ on
$H^i(X;\QQ)$. Thus $p^*$ is injective,
and
$$
\dim_{\QQ}H_i(Y;\QQ)\ge
\dim_{\QQ}H_i(X;\QQ)
$$
for every $i$. The equality of homology
and cohomology dimensions follows from
the universal coefficient theorem over
$\QQ$. Individual ranks may increase:
a connected double cover
$\Sigma_3\to\Sigma_2$ has first Betti
numbers $6$ and $4$, respectively.
They can also stay equal, as for any
finite cover of $S^1$.
:::

::: {.remark}
The source asks for an example in which an
individual rank decreases from base to
cover. Such an example cannot exist for
a finite cover, by the transfer argument.
:::
