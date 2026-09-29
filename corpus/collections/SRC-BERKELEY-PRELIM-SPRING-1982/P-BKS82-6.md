---
schema: qual/card@1
id: P-BKS82-6
kind: problem
title: A polynomial multiple of $f$ with value $1$ and vanishing first two derivatives at a point
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained PDF; the extracted markdown contains a different Problem 6.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the explicit quadratic reciprocal jet and the value, first derivative, and second derivative of the product at $a$.
---

::: {.problem}
Let $f(x)$ be a polynomial with real coefficients, and let $a\in\mathbb R$ satisfy $f(a)\ne0$. Prove that there is a real polynomial $g(x)$ such that, for
\[
p(x)=f(x)g(x),
\]
one has
\[
p(a)=1,
\qquad
p'(a)=0,
\qquad
p''(a)=0.
\]
:::

::: {.solution}
Put
$$
A\coloneqq f(a),
\qquad
B\coloneqq f'(a),
\qquad
C\coloneqq f''(a).
$$
Since $A\ne0$, define
$$
g(x)
\coloneqq
\frac1A
-\frac{B}{A^2}(x-a)
+
\left(
\frac{B^2}{A^3}
-\frac{C}{2A^2}
\right)(x-a)^2.
$$

::: pf

::: {.pf-step #g-derivatives-formula}
The polynomial $g$ satisfies
$$
g(a)=\frac1A,
\qquad
g'(a)=-\frac{B}{A^2},
\qquad
g''(a)=\frac{2B^2}{A^3}-\frac{C}{A^2}.
$$

::: pf-proof
These identities follow by differentiating the displayed quadratic
polynomial and substituting $x=a$.
:::

:::

::: {.pf-step #p-value-one}
For $p=fg$, one has
$$
p(a)=1.
$$

::: pf-proof
By the definition of $A$ and step [](#g-derivatives-formula){.pf-ref},
$$
p(a)=f(a)g(a)=A\frac1A=1.
$$
:::

:::

::: {.pf-step #p-prime-zero}
One has
$$
p'(a)=0.
$$

::: pf-proof
The product rule and step [](#g-derivatives-formula){.pf-ref} give
$$
\begin{aligned}
p'(a)
&=
f'(a)g(a)+f(a)g'(a)\\
&=
B\frac1A
+
A\left(-\frac{B}{A^2}\right)
=0.
\end{aligned}
$$
:::

:::

::: {.pf-step #p-double-prime-zero}
One has
$$
p''(a)=0.
$$

::: pf-proof
Differentiating the product twice gives
$$
p''=f''g+2f'g'+fg''.
$$
Therefore, by step [](#g-derivatives-formula){.pf-ref},
$$
\begin{aligned}
p''(a)
&=
C\frac1A
+
2B\left(-\frac{B}{A^2}\right)
+
A\left(
\frac{2B^2}{A^3}-\frac{C}{A^2}
\right)\\
&=
\frac CA
-\frac{2B^2}{A^2}
+
\frac{2B^2}{A^2}
-\frac CA
=0.
\end{aligned}
$$
:::

:::

::: {.pf-step #g-boxed}
Thus the real polynomial
$$
\boxed{
g(x)
=
\frac1{f(a)}
-\frac{f'(a)}{f(a)^2}(x-a)
+
\left(
\frac{f'(a)^2}{f(a)^3}
-\frac{f''(a)}{2f(a)^2}
\right)(x-a)^2
}
$$
has all the required properties.

::: pf-proof
Its coefficients are real because $f$ and $a$ are real. Steps [](#p-value-one){.pf-ref}, [](#p-prime-zero){.pf-ref}, and [](#p-double-prime-zero){.pf-ref}
show that $p=fg$ satisfies
$$
p(a)=1,
\qquad
p'(a)=0,
\qquad
p''(a)=0.
$$
:::

:::

::: pf-qed
Step [](#g-boxed){.pf-ref} gives the required polynomial.
:::

:::
:::
