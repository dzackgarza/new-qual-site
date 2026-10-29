---
schema: qual/card@1
id: P-BLAR-01
kind: problem
title: Dot product and lengths of two vectors
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Review Problem 1 in the deterministic MinerU Flash extraction assets/attachments/Basic_Linear_Algebra_Review_extracted.md.
---

::: {.problem}
Let
$$
u=(4,1,3),
\qquad
v=(-2,0,1).
$$
Compute the dot product $u\cdot v$ and the length of each vector.
:::

::: {.solution}

::: pf

::: pf-step
The dot product is
$$
\boxed{u\cdot v=-5}.
$$

::: pf-proof
By the definition of the Euclidean dot product,
$$
u\cdot v
=4(-2)+1(0)+3(1)
=-8+3
=-5.
$$
:::

:::

::: pf-step
The length of $u$ is
$$
\boxed{\|u\|=\sqrt{26}}.
$$

::: pf-proof
Using $\|u\|=\sqrt{u\cdot u}$,
$$
\|u\|
=\sqrt{4^2+1^2+3^2}
=\sqrt{16+1+9}
=\sqrt{26}.
$$
:::

:::

::: pf-step
The length of $v$ is
$$
\boxed{\|v\|=\sqrt5}.
$$

::: pf-proof
Similarly,
$$
\|v\|
=\sqrt{(-2)^2+0^2+1^2}
=\sqrt{4+1}
=\sqrt5.
$$
:::

:::

:::

:::
