---
schema: qual/card@1
id: P-HCAO15
kind: problem
title: $\operatorname{GL}_3(\RR)$ and $\operatorname{GL}_2(\RR)$ are not isomorphic as abstract groups
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Distinguish $\operatorname{GL}_3(\RR)$ from $\operatorname{GL}_2(\RR)$ by algebraic means, without using topology.
:::

::: {.solution}
The groups are not isomorphic because $\operatorname{GL}_3(\RR)$ contains
an elementary abelian $2$-subgroup of rank $3$, whereas
$\operatorname{GL}_2(\RR)$ does not.

::: pf

::: {.pf-step #gl3-has-rank-3-elementary-abelian}
The group $\operatorname{GL}_3(\RR)$ contains a subgroup isomorphic
to $(\ZZ/2\ZZ)^3$.

::: pf-proof
Take the diagonal sign matrices
\[
\left\{
\operatorname{diag}(\varepsilon_1,\varepsilon_2,\varepsilon_3)
:\varepsilon_i\in\{\pm1\}
\right\}.
\]
They form a subgroup of order $8$ in which every nonidentity element has order
$2$, hence a copy of $(\ZZ/2\ZZ)^3$.
:::

:::

::: {.pf-step #gl2-elementary-abelian-bound}
Every elementary abelian $2$-subgroup of $\operatorname{GL}_2(\RR)$
has order at most $4$.

::: pf-proof
Let $E\le\operatorname{GL}_2(\RR)$ be elementary abelian. Every
$A\in E$ satisfies $A^2=I$, so its minimal polynomial divides
\[
T^2-1=(T-1)(T+1).
\]
The roots are distinct over $\RR$, hence every $A$ is diagonalizable.
Because the elements of $E$ commute, they are simultaneously diagonalizable:
diagonalize one non-scalar element; its eigenspaces are preserved by every
commuting element, and scalar elements preserve every basis.

Thus, after conjugation, $E$ is contained in
\[
\{\operatorname{diag}(\varepsilon_1,\varepsilon_2):
\varepsilon_i\in\{\pm1\}\},
\]
which has order $4$.
:::

:::

::: pf-step
Therefore $\operatorname{GL}_3(\RR)$ and
$\operatorname{GL}_2(\RR)$ are not isomorphic as abstract groups.

::: pf-proof
An abstract group isomorphism preserves subgroup isomorphism types. By step [](#gl3-has-rank-3-elementary-abelian){.pf-ref}
the first group has a subgroup isomorphic to $(\ZZ/2)^3$, while step [](#gl2-elementary-abelian-bound){.pf-ref}
shows the second cannot.
:::

:::

:::
:::
