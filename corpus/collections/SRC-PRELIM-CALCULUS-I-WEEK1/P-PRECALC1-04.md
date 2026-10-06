---
schema: qual/card@1
id: P-PRECALC1-04
kind: problem
title: Minimum of $e^x-cx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $c > 0$ . Find the minimum value of $f ( x ) = e ^ { x } - c x$ among $x \in \mathbb { R }$
:::

::: {.solution}
Let
\[
f(x)=e^x-cx,
\qquad
c>0.
\]

<1>1. The derivative is
\[
\boxed{
f'(x)=e^x-c}.
\]

::: {.proof}
Differentiate term by term.
:::

<1>2. The critical-point equation
\[
f'(x)=0
\]
is equivalent to
\[
e^x=c.
\]

::: {.proof}
Use step <1>1.
:::

<1>3. Since \(c>0\), the unique critical point is
\[
\boxed{
x=\log c}.
\]

::: {.proof}
The exponential function is a bijection
\[
\mathbb R\to(0,\infty),
\]
with inverse \(\log\).
:::

<1>4. The second derivative is
\[
\boxed{
f''(x)=e^x>0}
\]
for every \(x\in\mathbb R\).

::: {.proof}
Differentiate step <1>1.
:::

<1>5. Hence \(f\) is strictly convex on \(\mathbb R\).

::: {.proof}
A twice differentiable function with
\[
f''(x)>0
\]
everywhere is strictly convex.
:::

<1>6. Therefore the unique critical point \(x=\log c\) is the global
minimum point.

::: {.proof}
A strictly convex differentiable function has at most one critical point,
and any critical point is its global minimizer.
:::

<1>7. Evaluate:
\[
\begin{aligned}
f(\log c)
&=
e^{\log c}
-c\log c\\
&=
c-c\log c.
\end{aligned}
\]

::: {.proof}
Use
\[
e^{\log c}=c.
\]
:::

<1>8. Hence the minimum value is
\[
\boxed{
c(1-\log c)}.
\]

::: {.proof}
Factor \(c\) from step <1>7.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the requested minimum value.
:::
:::
