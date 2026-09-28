---
schema: qual/card@1
id: P-BERK87S-16
kind: problem
title: The pointwise supremum of a uniformly bounded equicontinuous family is continuous
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used uniform boundedness to make the pointwise supremum finite. At an
    arbitrary point, equicontinuity bounds every member of the family by
    the same epsilon-delta estimate; taking suprema in both directions
    transfers that estimate to g.
---

::: {.problem}
Let $\mathcal F$ be a uniformly bounded, equicontinuous family of real-valued functions on a metric space $(X,d)$. Prove that
\[
g(x)=\sup\{f(x):f\in\mathcal F\}
\]
is continuous.
:::

::: {.solution}
<1>1. The value $g(x)$ is finite for every $x\in X$.

::: {.proof}
Uniform boundedness gives a constant $M>0$ such that
$$
\abs{f(x)}\leq M
$$
for every $f\in\mathcal F$ and every $x\in X$. Hence
$$
-M\leq f(x)\leq M
$$
for all $f\in\mathcal F$, so the supremum defining $g(x)$ is a finite
real number.
:::

<1>2. Fix $x_0\in X$ and $\varepsilon>0$. There exists $\delta>0$ such
that, whenever $d(x,x_0)<\delta$,
$$
g(x)\leq g(x_0)+\frac{\varepsilon}{2}.
$$

::: {.proof}
By equicontinuity at $x_0$, there exists $\delta>0$ such that
$$
d(x,x_0)<\delta
\quad\Longrightarrow\quad
\abs{f(x)-f(x_0)}<\frac{\varepsilon}{2}
$$
for every $f\in\mathcal F$. Thus, for such $x$ and every
$f\in\mathcal F$,
$$
f(x)
<
f(x_0)+\frac{\varepsilon}{2}
\leq
g(x_0)+\frac{\varepsilon}{2}.
$$
Taking the supremum over $f\in\mathcal F$ gives
$$
g(x)\leq g(x_0)+\frac{\varepsilon}{2}.
$$
:::

<1>3. For the same $\delta$, whenever $d(x,x_0)<\delta$,
$$
g(x_0)\leq g(x)+\frac{\varepsilon}{2}.
$$

::: {.proof}
The equicontinuity estimate from step <1>2 also gives, for every
$f\in\mathcal F$,
$$
f(x_0)
<
f(x)+\frac{\varepsilon}{2}
\leq
g(x)+\frac{\varepsilon}{2}.
$$
Taking the supremum over $f\in\mathcal F$ yields the stated inequality.
:::

<1>4. The function $g$ is continuous at $x_0$.

::: {.proof}
By steps <1>2 and <1>3, if $d(x,x_0)<\delta$, then
$$
\abs{g(x)-g(x_0)}
\leq
\frac{\varepsilon}{2}
<
\varepsilon.
$$
This is continuity at $x_0$.
:::

<1>5. Q.E.D.

::: {.proof}
The point $x_0\in X$ was arbitrary, so step <1>4 proves that $g$ is
continuous on $X$.
:::
:::
