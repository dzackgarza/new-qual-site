---
schema: qual/card@1
id: P-GRECH7-12
kind: problem
title: Two Newton steps approximating $\sqrt{40}$
classification:
  areas: [prelim]
  topics:
  - Newton's Method
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 12 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If $x^2 = 40$, use Newton's method twice to approximate the value of $x$ to three decimal places.

(A) $6.223$
(B) $6.225$
(C) $6.320$
(D) $6.323$
(E) $6.325$
:::

::: {.solution}

Let
$$
f(x)=x^2-40,
$$
so that $f'(x)=2x$. Since $6^2=36$ is close to $40$, take $x_0=6$.

::: pf

::: pf-step

The first Newton iterate is
$$
x_1=\frac{19}{3}.
$$


::: pf-proof

Newton's formula gives
$$
x_1=x_0-\frac{f(x_0)}{f'(x_0)}
=6-\frac{36-40}{12}
=6+\frac13
=\frac{19}{3}.
$$

:::

:::

::: {.pf-step #s1-2}

The second Newton iterate is
$$
x_2=\frac{721}{114}.
$$


::: pf-proof

At $x_1=19/3$,
$$
f(x_1)=\frac{361}{9}-40=\frac19,
\qquad
f'(x_1)=\frac{38}{3}.
$$
Therefore
$$
x_2
=\frac{19}{3}-\frac{1/9}{38/3}
=\frac{19}{3}-\frac1{114}
=\frac{721}{114}.
$$

:::

:::

::: {.pf-step #s1-3}

To three decimal places,
$$
\boxed{x\approx6.325},
$$
so the answer is (E).


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\frac{721}{114}=6.324561\ldots,
$$
which rounds to $6.325$ at three decimal places.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested approximation after two Newton iterations.

:::

:::

:::
