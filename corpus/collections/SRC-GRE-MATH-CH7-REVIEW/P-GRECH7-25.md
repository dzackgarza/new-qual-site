---
schema: qual/card@1
id: P-GRECH7-25
kind: problem
title: Locus of $\bar z^2=z^2$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 25 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
In the complex plane, the set of all points that satisfy the equation $(\bar{z})^2 = z^2$ is

(A) a circle
(B) a point
(C) a ray
(D) a line
(E) two lines
:::

Write
$$
z=x+iy,
\qquad x,y\in\RR.
$$

::: pf

::: pf-step

The equation $(\bar z)^2=z^2$ is equivalent to
$$
xy=0.
$$


::: pf-proof

Since $\bar z=x-iy$,
$$
(x-iy)^2=(x+iy)^2.
$$
Expanding gives
$$
x^2-2ixy-y^2=x^2+2ixy-y^2,
$$
so $4ixy=0$, equivalently $xy=0$.

:::

:::

::: pf-step

The solution set is the union of the real and imaginary axes.


::: pf-proof

By step <1>1, a point $(x,y)$ is a solution exactly when $x=0$ or $y=0$. The locus $x=0$ is the imaginary axis, and the locus $y=0$ is the real axis.

:::

:::

::: pf-step

Therefore the locus is
$$
\boxed{\text{two lines}},
$$
so the answer is (E).


::: pf-proof

The two axes in step <1>2 are distinct lines through the origin.

:::

:::

::: pf-qed

Step <1>3 gives the requested geometric description.

:::

:::
