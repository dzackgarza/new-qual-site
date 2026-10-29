---
schema: qual/card@1
id: P-UGAP09F-05
kind: problem
title: Existing partial derivatives need not imply continuity, and a sufficient differentiability criterion
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
(a) Let
\[
f(x,y)=
\begin{cases}
\dfrac{xy}{x^2+y^2},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0).
\end{cases}
\]
Show that
\[
\frac{\partial f}{\partial x}(0,0)=
\frac{\partial f}{\partial y}(0,0)=0,
\]
but $f$ is not continuous at $(0,0)$.

(b) Give a sufficient condition, stated in terms of the partial derivatives, for a function $g:\RR^2\to\RR$ to be differentiable at a point $P$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
$$
\frac{\partial f}{\partial x}(0,0)
=\frac{\partial f}{\partial y}(0,0)=0.
$$


::: pf-proof

By the definitions of the partial derivatives,
$$
\frac{\partial f}{\partial x}(0,0)
=\lim_{h\to0}\frac{f(h,0)-f(0,0)}{h}
=\lim_{h\to0}0=0,
$$
because $f(h,0)=0$ for every $h$. Likewise,
$$
\frac{\partial f}{\partial y}(0,0)
=\lim_{k\to0}\frac{f(0,k)-f(0,0)}{k}
=0.
$$

:::

:::

::: {.pf-step #s1-2}

The function $f$ is not continuous at $(0,0)$.


::: pf-proof

Along the line $y=x$, for every $t\ne0$,
$$
f(t,t)=\frac{t^2}{2t^2}=\frac12.
$$
Hence
$$
\lim_{t\to0}f(t,t)=\frac12\ne0=f(0,0).
$$
Therefore the two-variable limit of $f(x,y)$ at $(0,0)$ cannot equal $f(0,0)$, so $f$ is not continuous there.

:::

:::

::: {.pf-step #s1-3}

A sufficient condition for $g:\RR^2\to\RR$ to be differentiable at $P=(a,b)$ is that $g_x$ and $g_y$ exist on a neighborhood of $P$ and are continuous at $P$.


::: pf-proof

Assume this condition. For $(h,k)$ sufficiently small, apply the one-variable mean value theorem first along the horizontal segment from $(a,b+k)$ to $(a+h,b+k)$ and then along the vertical segment from $(a,b)$ to $(a,b+k)$. There exist $\theta,\eta\in(0,1)$ such that
$$
\begin{aligned}
g(a+h,b+k)-g(a,b)
&=g_x(a+\theta h,b+k)h
+g_y(a,b+\eta k)k.
\end{aligned}
$$
Subtracting $g_x(a,b)h+g_y(a,b)k$ gives an error $E(h,k)$ satisfying
$$
\frac{|E(h,k)|}{\sqrt{h^2+k^2}}
\le
|g_x(a+\theta h,b+k)-g_x(a,b)|
+|g_y(a,b+\eta k)-g_y(a,b)|.
$$
As $(h,k)\to(0,0)$, both terms on the right tend to $0$ by continuity of the partial derivatives at $P$. Hence
$$
g(a+h,b+k)
=g(a,b)+g_x(a,b)h+g_y(a,b)k+o\!\left(\sqrt{h^2+k^2}\right),
$$
which is precisely differentiability of $g$ at $P$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} prove part (a), and step [](#s1-3){.pf-ref} gives and justifies the sufficient condition requested in part (b).

:::

:::

:::
