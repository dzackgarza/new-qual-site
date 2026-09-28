---
schema: qual/card@1
id: E-L9XR0
kind: problem
title: Subspace topologies on lines in the Sorgenfrey plane
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

If $L$ is a straight line in the plane, describe the topology $L$ inherits as a subspace of $\mathbb{R}_\ell \times \mathbb{R}$ and as a subspace of $\mathbb{R}_\ell \times \mathbb{R}_\ell$.
In each case it is a familiar topology.
:::

::: {.solution}
Parametrize a nonvertical line $L=\{(x,mx+k):x\in\mathbb R\}$ by its first coordinate $x$, and a vertical line by its second coordinate.

For $\mathbb R_\ell\times\mathbb R$, a basic rectangle is
\[
[a,b)\times(c,d).
\]
If $L$ is vertical, intersection with such rectangles gives ordinary open intervals in the second coordinate, so the induced topology is the standard topology on $\mathbb R$. If $L$ is nonvertical (including horizontal lines), the trace of $[a,b)\times(c,d)$ on $L$ is
\[
\{x\in[a,b):mx+k\in(c,d)\},
\]
the intersection of $[a,b)$ with a standard open set, hence open in $\mathbb R_\ell$. Conversely, $[x_0,x_0+\varepsilon)$ is the trace of $[x_0,x_0+\varepsilon)\times(c,d)$ for any open interval $(c,d)$ containing $\{mx+k:x_0\le x\le x_0+\varepsilon\}$. So the induced topology is the lower-limit topology. Hence
\[
L\cong
\begin{cases}
\mathbb R,&L\text{ vertical},\\
\mathbb R_\ell,&L\text{ nonvertical}.
\end{cases}
\]

For $\mathbb R_\ell\times\mathbb R_\ell$, basic rectangles are
\[
[a,b)\times[c,d).
\]
A vertical or horizontal line inherits $\mathbb R_\ell$. A line of positive slope $m$ also inherits $\mathbb R_\ell$: the trace of $[a,b)\times[c,d)$ is
\[
[a,b)\cap\Bigl[\tfrac{c-k}{m},\tfrac{d-k}{m}\Bigr),
\]
a half-open interval, and $[x_0,x_0+\varepsilon)$ is the trace of $[x_0,x_0+\varepsilon)\times[mx_0+k,\,mx_0+k+m\varepsilon)$. A line of negative slope is discrete. Indeed, at $(x_0,y_0)$ on such a line, for sufficiently small $\varepsilon,\delta>0$ the rectangle
\[
[x_0,x_0+\varepsilon)\times[y_0,y_0+\delta)
\]
meets the line only at $(x_0,y_0)$, since moving to larger $x$ forces $y<y_0$. Therefore
\[
L\cong
\begin{cases}
\mathbb R_\ell,&L\text{ vertical, horizontal, or of positive slope},\\
\mathbb R_d,&L\text{ of negative slope}.
\end{cases}
\]
:::
