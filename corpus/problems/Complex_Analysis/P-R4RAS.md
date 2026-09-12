---
schema: qual/card@1
id: P-R4RAS
kind: problem
title: Continuity, differentiability, and $C^1$ regularity of $\frac{xy}{\sqrt{x^2+y^2}}$
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Continuity
  - Counterexamples
relations: []
review: draft
---

::: problem
Is the following function continuous, differentiable, continuously differentiable?
\[  
f: \RR^2 &\to \RR  \\
f(x, y) &= 
\begin{cases}
{xy \over \sqrt{x^2 + y^2}} & (x, y) \neq (0, 0) \\
0 & \text{else}.
\end{cases}
\]
:::

::: solution
Away from $(0,0)$ the function is smooth. At the origin,
\[
|f(x,y)|=\frac{|xy|}{\sqrt{x^2+y^2}}
\le \frac{x^2+y^2}{2\sqrt{x^2+y^2}}
=\frac12\sqrt{x^2+y^2},
\]
so $f(x,y)\to0=f(0,0)$. Hence $f$ is continuous everywhere.

The partial derivatives at the origin are both $0$, so if $f$ were
differentiable there, its derivative would be the zero map. Differentiability
would then require
\[
\frac{|f(x,y)|}{\sqrt{x^2+y^2}}\to0.
\]
But along $y=x\ne0$,
\[
\frac{|f(x,x)|}{\sqrt{2x^2}}
=\frac{x^2/(\sqrt2|x|)}{\sqrt2|x|}
=\frac12.
\]
Thus $f$ is not differentiable at $(0,0)$.

Therefore $f$ is continuous everywhere, differentiable on
$\mathbb R^2\setminus\{0\}$ but not at the origin, and consequently is not
continuously differentiable on $\mathbb R^2$.
:::
