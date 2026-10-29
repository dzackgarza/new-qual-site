---
schema: qual/card@1
id: P-UCLAB02W-01
kind: problem
title: Differentiation under the integral sign
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1 of the official UCLA Basic Examination, Winter 2002 PDF.
---

::: {.problem}
(a) State reasonably general conditions under which
$$
\frac{d}{dx}\int_a^b f(x,y)\,dy
=
\int_a^b \frac{\partial f}{\partial x}(x,y)\,dy
$$
is valid.

(b) Prove the formula under the conditions you stated in part (a).
:::

::: {.solution}

Let $I\subset\RR$ be an open interval containing the point $x$ under consideration. A sufficient set of hypotheses is that $f:I\times[a,b]\to\RR$ is continuous, that $\partial f/\partial x$ exists on $I\times[a,b]$, and that $\partial f/\partial x$ is continuous there.

::: pf

::: pf-step

Under these hypotheses, for each $x\in I$ the function $y\mapsto f(x,y)$ is Riemann integrable on $[a,b]$, so
$$
F(x)\coloneqq\int_a^b f(x,y)\,dy
$$
is well defined.


::: pf-proof

For fixed $x\in I$, continuity of $f$ on $I\times[a,b]$ implies continuity of the restriction $y\mapsto f(x,y)$ on the compact interval $[a,b]$. Every continuous function on a compact interval is Riemann integrable.

:::

:::

::: {.pf-step #s1-2}

Fix $x_0\in I$. There is $r>0$ such that
$$
[x_0-r,x_0+r]\subset I,
$$
and $\partial f/\partial x$ is uniformly continuous on
$$
K=[x_0-r,x_0+r]\times[a,b].
$$


::: pf-proof

Because $I$ is open, choose $r>0$ with the displayed inclusion. The set $K$ is compact, and $\partial f/\partial x$ is continuous on $K$. By the Heine--Cantor theorem, it is uniformly continuous on $K$.

:::

:::

::: {.pf-step #s1-3}

For $0<\abs h<r$ and every $y\in[a,b]$, there exists a point $\xi_{h,y}$ between $x_0$ and $x_0+h$ such that
$$
\frac{f(x_0+h,y)-f(x_0,y)}{h}
=\frac{\partial f}{\partial x}(\xi_{h,y},y).
$$


::: pf-proof

For fixed $y$, the one-variable function $t\mapsto f(t,y)$ is continuous on the closed interval with endpoints $x_0$ and $x_0+h$ and differentiable in its interior. The ordinary mean value theorem therefore gives such a point $\xi_{h,y}$.

:::

:::

::: {.pf-step #s1-4}

As $h\to0$,
$$
\frac{f(x_0+h,y)-f(x_0,y)}{h}
\longrightarrow
\frac{\partial f}{\partial x}(x_0,y)
$$
uniformly for $y\in[a,b]$.


::: pf-proof

Let $\varepsilon>0$. By uniform continuity from step [](#s1-2){.pf-ref}, there exists $\delta>0$ such that whenever $(s,y),(t,y)\in K$ and $\abs{s-t}<\delta$,
$$
\abs{\frac{\partial f}{\partial x}(s,y)-\frac{\partial f}{\partial x}(t,y)}<\varepsilon.
$$
If $0<\abs h<\min\{r,\delta\}$, then step [](#s1-3){.pf-ref} gives $\abs{\xi_{h,y}-x_0}\le\abs h<\delta$ for every $y\in[a,b]$. Hence
$$
\abs{
\frac{f(x_0+h,y)-f(x_0,y)}{h}
-
\frac{\partial f}{\partial x}(x_0,y)
}<\varepsilon
$$
for every $y\in[a,b]$. This is uniform convergence.

:::

:::

::: {.pf-step #s1-5}

The function $F$ is differentiable at $x_0$ and
$$
F'(x_0)
=
\int_a^b\frac{\partial f}{\partial x}(x_0,y)\,dy.
$$


::: pf-proof

For $0<\abs h<r$,
$$
\frac{F(x_0+h)-F(x_0)}{h}
=
\int_a^b
\frac{f(x_0+h,y)-f(x_0,y)}{h}
\,dy.
$$
Therefore
$$
\begin{aligned}
&\abs{
\frac{F(x_0+h)-F(x_0)}{h}
-
\int_a^b\frac{\partial f}{\partial x}(x_0,y)\,dy
}\\
&\qquad\le
(b-a)
\sup_{y\in[a,b]}
\abs{
\frac{f(x_0+h,y)-f(x_0,y)}{h}
-
\frac{\partial f}{\partial x}(x_0,y)
}.
\end{aligned}
$$
The supremum tends to $0$ by step [](#s1-4){.pf-ref}. Hence the difference quotient for $F$ converges to the displayed integral.

:::

:::

::: {.pf-step #s1-6}

Thus, under the hypotheses stated above,
$$
\boxed{
\frac{d}{dx}\int_a^b f(x,y)\,dy
=
\int_a^b\frac{\partial f}{\partial x}(x,y)\,dy
}
$$
for every $x\in I$.


::: pf-proof

The point $x_0\in I$ was arbitrary, and step [](#s1-5){.pf-ref} proves the formula at every such point.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives the requested differentiation-under-the-integral formula under the sufficient hypotheses stated at the beginning of the solution.

:::

:::

:::
