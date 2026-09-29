---
schema: qual/card@1
id: E-YTG4V
kind: problem
title: Continuity of the field operations on $\RR$
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
Throughout, $\rho((x,y),(x_0,y_0))<\delta$ means $\abs{x-x_0}<\delta$ and $\abs{y-y_0}<\delta$.

::: pf

::: {.pf-step #part-a}
(a) Addition is continuous.

::: pf-proof
Given $\varepsilon>0$, let $\delta=\varepsilon/2$.
If $\rho((x,y),(x_0,y_0))<\delta$, then $\abs{(x+y)-(x_0+y_0)}\le\abs{x-x_0}+\abs{y-y_0}<2\delta=\varepsilon$.
:::

:::

::: {.pf-step #part-b}
(b) Multiplication is continuous.

::: pf-proof
Given $(x_0,y_0)$ and $0<\varepsilon<1$, let $\delta=\varepsilon/\bigl(3(\abs{x_0}+\abs{y_0}+1)\bigr)$, so $\delta<1$.
Since $xy-x_0y_0=x_0(y-y_0)+y_0(x-x_0)+(x-x_0)(y-y_0)$, if $\rho((x,y),(x_0,y_0))<\delta$ then
$$
\abs{xy-x_0y_0}<\abs{x_0}\delta+\abs{y_0}\delta+\delta^2<(\abs{x_0}+\abs{y_0}+1)\delta=\varepsilon/3<\varepsilon.
$$
:::

:::

::: {.pf-step #part-c}
(c) The reciprocal $r(x)=1/x$ is continuous on $\RR-\{0\}$.

::: pf-proof
Let $x_0\ne0$ and $\varepsilon>0$, and put $\delta=\min\{\abs{x_0}/2,\ \varepsilon\abs{x_0}^2/2\}$.
If $\abs{x-x_0}<\delta$, then $\abs x>\abs{x_0}/2$, so
$$
\Bigl\lvert\frac1x-\frac1{x_0}\Bigr\rvert=\frac{\abs{x-x_0}}{\abs x\abs{x_0}}<\frac{2\delta}{\abs{x_0}^2}\le\varepsilon.
$$
:::

:::

::: {.pf-step #part-d}
(d) Subtraction and the quotient $(x,y)\mapsto x/y$ on $\RR\times(\RR-\{0\})$ are continuous.

::: pf-proof
Negation $y\mapsto-y$ is continuous, since $\abs{(-y)-(-y_0)}=\abs{y-y_0}$.
Subtraction is addition composed with $\operatorname{id}\times(-)$, and the quotient is multiplication composed with $\operatorname{id}\times r$; a product of continuous maps is continuous by [[E-G4SRA]], and steps [](#part-a){.pf-ref}, [](#part-b){.pf-ref}, [](#part-c){.pf-ref} give the remaining factors.
:::

:::

::: pf-qed
Steps [](#part-a){.pf-ref} through [](#part-d){.pf-ref} prove (a) through (d).
:::

:::

:::
