---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-INT1
kind: problem
title: 'A jump integrator evaluates a Riemann–Stieltjes integral at zero'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

:::{.problem title="?"}
(June 2014, 1) Define $\alpha:[-1,1]\to\mathbb R$ by
$$
\alpha(x):=
\begin{cases}
-1,&x\in[-1,0],\\
1,&x\in(0,1].
\end{cases}
$$
Let $f:[-1,1]\to\mathbb R$ be a function that is uniformly bounded on $[-1,1]$ and continuous at $x=0$,
but not necessarily continuous for $x\ne0$. Prove that $f$ is Riemann--Stieltjes integrable with respect to
$\alpha$ over $[-1,1]$ and that
$$
\int_{-1}^{1}f(x)\,d\alpha(x)=2f(0).
$$
:::
