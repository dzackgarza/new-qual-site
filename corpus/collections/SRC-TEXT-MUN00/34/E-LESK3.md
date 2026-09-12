---
schema: qual/card@1
id: E-LESK3
kind: problem
title: Strong hypotheses short of metrizability
classification:
  areas:
  - topology
  topics:
  - Metrizability
relations: []
review: draft
---

::: {.exercise}

Give an example showing that a space can be completely normal, and satisfy the first countability axiom, the Lindelöf condition, and have a countable dense subset, and still not be metrizable.
:::

::: {.solution}
The Sorgenfrey line \(\mathbb R_\ell\) is such an example.

- It is completely normal: as proved in §32, every subspace of \(\mathbb R_\ell\) is regular and Lindelöf, hence normal.
- It is first countable: the intervals
\[
[x,x+1/n),\qquad n\ge1,
\]
form a countable local basis at \(x\).
- It is Lindelöf, indeed hereditarily Lindelöf.
- It is separable: \(\mathbb Q\) is dense, since every nonempty basic interval \([a,b)\) contains a rational.
- It is not metrizable. If it were, separability would imply second countability, but \(\mathbb R_\ell\) is not second countable: any basis must contain distinct elements \(B_x\) with
\[
x\in B_x\subset[x,x+1),
\]
for all real \(x\), giving an uncountable basis.

Thus all the listed hypotheses can hold without metrizability.
:::
