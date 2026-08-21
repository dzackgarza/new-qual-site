---
schema: qual/card@1
id: E-PAQWN
kind: exercise
title: Polynomial growth of entire functions and Liouville for bounded real part
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
  - Liouville's Theorem
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
a.
Let Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire function. Assume the existence of a non-negative integer $m$, and of positive constants $L$ and $R$, such that for all $z$ with $|z|>R$ the inequality $$|f(z)| \leq L |z|^m$$ holds. 
Prove that $f$ is a polynomial of degree $\leq m$.

b.
Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire function. Suppose that there exists a real number $M$ such that for all $z\in {\mathbb C}, \Re(f) \leq M$.
Prove that $f$ must be a constant.
:::

:::{.solution}
\[
\abs{f^{(n)}(z)} 
&= \abs{ {1\over 2\pi i} \oint_\gamma {f(\xi) \over (\xi - z)^{n+1}} \dxi } \\
&\leq  {1\over 2\pi i} \oint_\gamma { \abs{ f(\xi) } \over \abs{\xi - z}^{n+1}} \dxi \\
&\leq {1\over 2\pi i } \oint_\gamma {LR^m \over R^{n+1} } \dxi \\
&= {L\over 2\pi i} R^{m-(n+1)} \cdot 2\pi R \\
&= LR^{m-n} \\
&\convergesto{R\to\infty} 0 \qquad \iff m-n<0 \iff n>m
,\]
so $f$ is a polynomial of degree at most $m$.

Now if $f$ is entire, $g(z) \da e^{f(z)}$ is entire and
\[
\abs{g(z)} = \abs{e^{f(z)}} = e^{\Re(f)} \leq e^M
,\]
so $g$ is an entire bounded function and thus constant by Liouville, making $f$ constant.
Why this is true:
\[
e^{f} = C \implies e^f \cdot f' = 0 \implies f'\equiv 0
,\]
since $e^f$ is nonvanishing, and $f'\equiv 0$ implies $f$ is constant.
:::
