---
schema: qual/card@1
id: P-CASP04B
kind: problem
title: "Schwarz-Pick inequality for self-maps of the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f \in \mathcal{O}(\mathbb{D})$ and assume that $|f(z)| \leq 1$ in $\mathbb{D}$.
Show that $$\frac{|f(0)| - |z|}{1 + |f(0)||z|} \leq |f(z)| \leq \frac{|f(0)| + |z|}{1 - |f(0)||z|}.$$
:::

::: solution
Put $a=f(0)$. If $f$ is constant the inequalities are immediate. Otherwise
$f(\mathbb D)\subset\mathbb D$, and Schwarz--Pick applied at $0$ gives
\[
\left|\frac{f(z)-a}{1-\overline a f(z)}\right|\le |z|.
\]
Set $A=|a|$, $r=|z|$, and $s=|f(z)|$. Then
\[
|f(z)-a|\le r\,|1-\overline a f(z)|\le r(1+As).
\]
Using $A-s\le|a-f(z)|$ gives
\[
A-s\le r(1+As),
\]
hence
\[
s\ge\frac{A-r}{1+Ar}.
\]
Likewise $s-A\le|f(z)-a|$ gives
\[
s-A\le r(1+As),
\]
so
\[
s\le\frac{A+r}{1-Ar}.
\]
These are exactly the desired bounds.
:::
