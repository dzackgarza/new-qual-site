---
schema: qual/card@1
id: P-RYJ3K
kind: problem
title: An everywhere differentiable function with $f'$ discontinuous at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Counterexamples
  - Continuity
relations: []
review: draft
---

::: problem
Give an example of a function $f:\RR\to \RR$ that is everywhere differentiable but $f'$ is not continuous at 0.
:::

::: solution
Take
\[
f(x)=
\begin{cases}
x^2\sin(1/x),&x\ne0,\\
0,&x=0.
\end{cases}
\]
At $0$,
\[
f'(0)=\lim_{h\to0}\frac{h^2\sin(1/h)}h
=\lim_{h\to0}h\sin(1/h)=0.
\]
For $x\ne0$,
\[
f'(x)=2x\sin(1/x)-\cos(1/x).
\]
Thus $f$ is differentiable everywhere, but $f'(x)$ has no limit as $x\to0$
because the term $\cos(1/x)$ oscillates. Hence $f'$ is not continuous at $0$.
:::
