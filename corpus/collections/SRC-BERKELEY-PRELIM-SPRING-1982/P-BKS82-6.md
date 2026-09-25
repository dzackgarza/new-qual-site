---
schema: qual/card@1
id: P-BKS82-6
kind: problem
title: Multiply a real polynomial to normalize its value and first two derivatives at a point
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

<1>1. The polynomial $g$ satisfies
$$
g(a)=\frac1A,
\qquad
g'(a)=-\frac{B}{A^2},
\qquad
g''(a)=\frac{2B^2}{A^3}-\frac{C}{A^2}.
$$

::: {.proof}
These identities follow by differentiating the displayed quadratic
polynomial and substituting $x=a$.
:::

<1>2. For $p=fg$, one has
$$
p(a)=1.
$$

::: {.proof}
By the definition of $A$ and step <1>1,
$$
p(a)=f(a)g(a)=A\frac1A=1.
$$
:::

<1>3. One has
$$
p'(a)=0.
$$

::: {.proof}
The product rule and step <1>1 give
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

<1>4. One has
$$
p''(a)=0.
$$

::: {.proof}
Differentiating the product twice gives
$$
p''=f''g+2f'g'+fg''.
$$
Therefore, by step <1>1,
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

<1>5. Thus the real polynomial
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

::: {.proof}
Its coefficients are real because $f$ and $a$ are real. Steps <1>2--<1>4
show that $p=fg$ satisfies
$$
p(a)=1,
\qquad
p'(a)=0,
\qquad
p''(a)=0.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the required polynomial.
:::
:::
