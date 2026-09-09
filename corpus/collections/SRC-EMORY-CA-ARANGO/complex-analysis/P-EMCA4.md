---
schema: qual/card@1
id: P-EMCA4
kind: problem
title: "Entire function with quadratic growth is polynomial"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f$ be an entire function and suppose that $|f(z)| \leq A|z|^2$ for all $z$ and some constant $A$.
Show that $f$ is a polynomial of degree $\leq 2$.
:::

::: solution
For every $R>0$, Cauchy's estimate on the circle $|z|=R$ gives, for $n\ge0$,
\[
|f^{(n)}(0)|
\le \frac{n!}{R^n}\max_{|z|=R}|f(z)|
\le n!A R^{2-n}.
\]
If $n\ge3$, letting $R\to\infty$ yields $f^{(n)}(0)=0$. Therefore the Taylor
series of the entire function $f$ terminates after its quadratic term:
\[
f(z)=f(0)+f'(0)z+\frac{f''(0)}2z^2.
\]
Hence $f$ is a polynomial of degree at most $2$.

In fact the stated bound at $z=0$ also gives $f(0)=0$, but this stronger
conclusion is not needed.
:::
