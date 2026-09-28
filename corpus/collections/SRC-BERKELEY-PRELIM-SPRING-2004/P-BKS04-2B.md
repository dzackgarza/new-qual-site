---
schema: qual/card@1
id: P-BKS04-2B
kind: problem
title: Maximum of $|f'(1)|$ for $f$ holomorphic with $|f|\le1$ on $|z|=2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Find the maximum possible value of $\abs{f'(1)}$ given that $f$ is holomorphic on an open neighborhood of $\{z\in\CC:\abs{z}\leq2\}$ and satisfies $\abs{f(z)}\leq1$ when $\abs{z}=2$.
:::

::: {.solution}
We will use a fractional linear transformation to change the problem to one where the derivative is evaluated at the center of a disk.

The function $z\mapsto\frac2z\left(\frac{z-1}{\bar z-1}\right)$ on $\abs{z}=2$ has absolute value $1$, and it extends to a fractional linear transformation $g(z)=2\left(\frac{z-1}{4-z}\right)$. Since it also maps $z=1$ to the interior of the unit disk, it must map the region $\abs{z}\leq2$ bijectively onto the unit disk.
We calculate $\abs{g'(1)}=2/3$.

Now, for any other $f$ mapping the circle $\abs{z}=2$ into $\abs{z}\leq1$, the composition $h\coloneqq f\circ g^{-1}$ is holomorphic on a neighborhood of $\abs{z}\leq1$, and maps $\abs{z}=1$ into $\abs{z}\leq1$. Taking absolute values in

$$
h'(0)=\frac{1}{2\pi i}\int_{\abs{z}=1}\frac{h(z)}{z^2}\,dz
$$

gives $\abs{h'(0)}\leq1$. Since $g^{-1}(0)=1$, the chain rule gives $h'(0)=f'(1)g'(1)^{-1}$. Thus $\abs{f'(1)}=\abs{h'(0)}\abs{g'(1)}\leq\abs{g'(1)}=2/3$. Thus $2/3$ is the maximum possible value of $\abs{f'(1)}$.
:::
