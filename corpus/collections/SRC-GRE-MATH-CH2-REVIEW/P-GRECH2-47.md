---
schema: qual/card@1
id: P-GRECH2-47
kind: problem
title: Coefficient of $x^3$ in the Taylor series of $e^{x^2-x}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 47 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The chapter extraction read e^(x^2-2); the book's Chapter 8 solution expands e^(x^2-x).
---

::: {.problem}
In the Taylor series expansion (in powers of $x$) of the function $f(x) = e^{x^2 - x}$, what is the coefficient of $x^3$?

(A) $-7$
(B) $-\frac{3}{2}$
(C) $-\frac{7}{6}$
(D) $\frac{7}{6}$
(E) $\frac{3}{2}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Up to terms of degree greater than $3$,
$$
e^{x^2}=1+x^2+O(x^4)
$$
and
$$
e^{-x}=1-x+\frac{x^2}{2}-\frac{x^3}{6}+O(x^4).
$$


::: pf-proof

These are the Taylor expansions of the exponential function after substituting $x^2$ and $-x$, respectively.

:::

:::

::: {.pf-step #s1-2}

The coefficient of $x^3$ in $e^{x^2-x}$ is
$$
\boxed{-\frac76}.
$$


::: pf-proof

Since
$$
e^{x^2-x}=e^{x^2}e^{-x},
$$
step [](#s1-1){.pf-ref} gives
$$
\begin{aligned}
e^{x^2-x}
&=(1+x^2+O(x^4))
\left(1-x+\frac{x^2}{2}-\frac{x^3}{6}+O(x^4)\right).
\end{aligned}
$$
The $x^3$ coefficient receives contributions only from
$1\cdot(-x^3/6)$ and $x^2\cdot(-x)$, so it equals
$$
-\frac16-1=-\frac76.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore the answer is (C).


::: pf-proof

Step [](#s1-2){.pf-ref} gives exactly the coefficient requested in the problem.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} identifies the corresponding choice.

:::

:::

:::
