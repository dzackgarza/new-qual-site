---
schema: qual/card@1
id: E-YTG4V
kind: problem
title: Continuity of the field operations on R
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Prove continuity of the algebraic operations on $\mathbb{R}$, as follows.
Use the metric $d(a, b) = \abs{a - b}$ on $\mathbb{R}$ and the metric on $\mathbb{R}^2$ given by the equation

$$
\rho((x, y), (x_0, y_0)) = \max\ts{\abs{x - x_0}, \abs{y - y_0}}.
$$

(a) Show that addition is continuous.
[Hint: Given $\epsilon$, let $\delta = \epsilon/2$ and note that

$$
d(x + y, x_0 + y_0) \leq \abs{x - x_0} + \abs{y - y_0}.]
$$

(b) Show that multiplication is continuous.
[Hint: Given $(x_0, y_0)$ and $0 < \epsilon < 1$, let

$$
3\delta = \epsilon/(\abs{x_0} + \abs{y_0} + 1)
$$

and note that

$$
d(xy, x_0y_0) \leq \abs{x_0}\abs{y - y_0} + \abs{y_0}\abs{x - x_0} + \abs{x - x_0}\abs{y - y_0}.]
$$

(c) Show that the operation of taking reciprocals is a continuous map from $\mathbb{R} - \ts{0}$ to $\mathbb{R}$.
[Hint: Show the inverse image of the interval $(a, b)$ is open. Consider five cases, according as $a$ and $b$ are positive, negative, or zero.]

(d) Show that the subtraction and quotient operations are continuous.
:::

::: {.solution}
**(a).**

<1>1. Given $\varepsilon > 0$, let $\delta = \varepsilon/2$.
::: {.proof}
choose $\delta$.
:::

<1>2. If $\rho((x,y), (x_0, y_0)) < \delta$, then $|x - x_0| < \delta$ and $|y - y_0| < \delta$.
::: {.proof}
$\rho = \max(|x - x_0|, |y - y_0|)$.
:::

<1>3. Then $d(x + y, x_0 + y_0) = |(x + y) - (x_0 + y_0)| \le |x - x_0| + |y - y_0| < \delta + \delta = \varepsilon$.
::: {.proof}
triangle inequality and <1>2.
:::

<1>4. Hence addition is continuous.
::: {.proof}
<1>3 (for every $\varepsilon$ there is $\delta$).
:::

**(b).**

<1>1. Given $(x_0, y_0)$ and $0 < \varepsilon < 1$, let $3\delta = \varepsilon/(|x_0| + |y_0| + 1)$.
::: {.proof}
choose $\delta$.
:::

<1>2. If $\rho((x,y), (x_0, y_0)) < \delta$, then $|x - x_0| < \delta$ and $|y - y_0| < \delta$.
::: {.proof}
definition of $\rho$.
:::

<1>3. $d(xy, x_0 y_0) = |xy - x_0 y_0| \le |x_0||y - y_0| + |y_0||x - x_0| + |x - x_0||y - y_0|$.
::: {.proof}
$xy - x_0 y_0 = x_0(y - y_0) + y_0(x - x_0) + (x - x_0)(y - y_0)$.
:::

<1>4. Hence $d(xy, x_0 y_0) < |x_0|\delta + |y_0|\delta + \delta^2 < (|x_0| + |y_0| + 1)\delta = \varepsilon/3 < \varepsilon$.
::: {.proof}
<1>2 and <1>3, using $\delta < 1$ (so $\delta^2 < \delta$) and the definition of $\delta$.
:::

<1>5. Hence multiplication is continuous.
::: {.proof}
<1>4.
:::

**(c).**

<1>1. The reciprocal map $r(x) = 1/x$ is continuous on $\mathbb{R} - \{0\}$.
::: {.proof}
for $x_0 \neq 0$, $|1/x - 1/x_0| = \frac{|x - x_0|}{|x||x_0|}$; choosing $\delta$ small so that $|x| > |x_0|/2$ (possible by continuity of $x \mapsto |x|$), we get $|1/x - 1/x_0| < \frac{2|x - x_0|}{|x_0|^2}$, which tends to $0$ as $x \to x_0$.
:::

<1>2. Hence the reciprocal is continuous.
::: {.proof}
<1>1.
:::

**(d).**

<1>1. Subtraction $x - y = x + (-y)$ is continuous.
::: {.proof}
it is the composition of addition with the continuous map $y \mapsto -y$ (negation is continuous).
:::

<1>2. Quotient $x/y = x \cdot (1/y)$ is continuous on $\mathbb{R} \times (\mathbb{R} - \{0\})$.
::: {.proof}
it is the composition of multiplication with the continuous reciprocal map (c).
:::

<1>3. Q.E.D.
::: {.proof}
<1>4 (a), <1>5 (b), <1>2 (c), <1>1–<1>2 (d).
:::
:::
