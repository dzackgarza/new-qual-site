---
schema: qual/card@1
id: P-LATEST2-15
kind: problem
title: Evaluate a linear functional from two values
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained PDF extraction for linear_algebra_from_test2.pdf; the source PDF has no usable text layer, so this audit is limited to the preserved extraction generated from that PDF.
---

::: {.problem}
Let $f:\mathbb R^2\to\mathbb R$ be linear, with $f(1,1)=1$ and $f(-1,0)=2$.
Find $f(3,5)$.

(A) $-6$  (B) $-5$  (C) $0$  (D) $8$  (E) $9$
:::

::: {.solution}
<1>1. Express $(3,5)$ as a linear combination of the two vectors on which $f$ is known:
$$
(3,5)=5(1,1)+2(-1,0).
$$

::: {.proof}
Compute
$$
5(1,1)+2(-1,0)
=(5,5)+(-2,0)
=(3,5).
$$
:::

<1>2. By linearity,
$$
f(3,5)
=
5f(1,1)+2f(-1,0).
$$

::: {.proof}
Apply $f$ to the decomposition in step <1>1 and use linearity of $f$.
:::

<1>3. Therefore
$$
f(3,5)
=
5\cdot1+2\cdot2
=
9.
$$

::: {.proof}
Substitute the given values
$$
f(1,1)=1,
\qquad
f(-1,0)=2
$$
into step <1>2.
:::

<1>4. Hence
$$
\boxed{f(3,5)=9}.
$$

::: {.proof}
This is answer choice $\boxed{\text{(E)}}$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required value.
:::
:::
