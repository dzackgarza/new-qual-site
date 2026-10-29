---
schema: qual/card@1
id: P-GRECH2-27
kind: problem
title: Constant making a piecewise function integrate to $1$ on $[-1,1]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 27 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If

$$
f(x) = \begin{cases} -2(x+1) & \text{if } x \le 0 \\ k(1-x^2) & \text{if } x > 0 \end{cases}
$$

then the value of $k$ for which $\int_{-1}^{1} f(x) dx = 1$ is

(A) $-1$
(B) $0$
(C) $1$
(D) $2$
(E) $3$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The integral over $[-1,0]$ is
$$
\int_{-1}^0 -2(x+1)\,dx=-1.
$$


::: pf-proof

An antiderivative is
$$
-x^2-2x.
$$
Therefore
$$
\int_{-1}^0 -2(x+1)\,dx
=\left[-x^2-2x\right]_{-1}^0
=0-1
=-1.
$$

:::

:::

::: {.pf-step #s1-2}

The integral over $[0,1]$ is
$$
\int_0^1 k(1-x^2)\,dx=\frac{2k}{3}.
$$


::: pf-proof

Since the value at the single point $x=0$ does not affect the integral,
$$
\int_0^1 k(1-x^2)\,dx
=k\left[x-\frac{x^3}{3}\right]_0^1
=k\left(1-\frac13\right)
=\frac{2k}{3}.
$$

:::

:::

::: {.pf-step #s1-3}

The condition $\int_{-1}^1 f(x)\,dx=1$ forces
$$
\boxed{k=3},
$$
so the answer is (E).


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
$$
-1+\frac{2k}{3}=1.
$$
Thus $2k/3=2$, hence $k=3$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the unique constant satisfying the integral condition.

:::

:::

:::
