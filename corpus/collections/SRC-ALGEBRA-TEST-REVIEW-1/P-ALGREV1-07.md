---
schema: qual/card@1
id: P-ALGREV1-07
kind: problem
title: Classify abelian groups of order 200
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Review1.md, open-ended question 7."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Applied the finite abelian group classification to the 2-primary and 5-primary parts and obtained six pairwise nonisomorphic groups."
---
::: {.problem}
Find all abelian groups of order $200$, up to isomorphism.
:::

::: {.solution}
Since
$$
200=2^3\cdot5^2,
$$
the classification theorem for finite abelian groups separates the problem
into the $2$-primary and $5$-primary parts.

::: pf

::: {.pf-step #s1}

Classify the abelian groups of order $2^3$.

::: pf-proof

The partitions of $3$ are
$$
3,\qquad 2+1,\qquad 1+1+1.
$$
Therefore the three possibilities are
$$
\ZZ_8,
\qquad
\ZZ_4\times\ZZ_2,
\qquad
\ZZ_2\times\ZZ_2\times\ZZ_2.
$$

:::

:::

::: {.pf-step #s2}

Classify the abelian groups of order $5^2$.

::: pf-proof

The partitions of $2$ are
$$
2,\qquad1+1.
$$
Hence the two possibilities are
$$
\ZZ_{25},
\qquad
\ZZ_5\times\ZZ_5.
$$

:::

:::

::: {.pf-step #s3}

Combine the independent primary components.

::: pf-proof

Every finite abelian group of order $200$ is uniquely the direct product of
one group from step [](#s1){.pf-ref} and one group from step [](#s2){.pf-ref}. Thus there are exactly
$3\cdot2=6$ isomorphism types:
$$
\boxed{
\begin{aligned}
&\ZZ_8\times\ZZ_{25},\\
&\ZZ_8\times\ZZ_5\times\ZZ_5,\\
&\ZZ_4\times\ZZ_2\times\ZZ_{25},\\
&\ZZ_4\times\ZZ_2\times\ZZ_5\times\ZZ_5,\\
&\ZZ_2\times\ZZ_2\times\ZZ_2\times\ZZ_{25},\\
&\ZZ_2\times\ZZ_2\times\ZZ_2\times\ZZ_5\times\ZZ_5.
\end{aligned}}
$$
The primary decomposition theorem also shows that no two groups in this list
are isomorphic.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the complete classification up to isomorphism.

:::

:::

:::

::: {.remark title="Variations"}
A common form asks for the number of isomorphism classes and lists each class in both invariant factor form and elementary divisor form.
:::
