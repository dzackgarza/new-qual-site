---
schema: qual/card@1
id: P-CAFA19E
kind: problem
title: "Runge approximation with restricted pole locations"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f = \frac{1}{(z-1)(z-5)}$.

(a) Prove that there is a sequence of rational functions $R_n(z)$ whose poles can only occur at 2 and 6 such that $$\lim_{n \to \infty} \sup_{3 \leq |z| \leq 4} |f(z) - R_n(z)| = 0.$$

(b) Does there exist a sequence of rational functions $R_n(z)$ whose poles can only occur at 6 such that the above holds?
Justify your answer.
:::

::: solution
Let
\[
K=\{z:3\le |z|\le4\}.
\]
The complement $\mathbb C\setminus K$ has two components: the bounded
component $|z|<3$ and the unbounded component $|z|>4$. The points $2$ and $6$
lie in these two components respectively. Since $f$ is holomorphic on a
neighborhood of $K$, Runge's theorem with prescribed pole set therefore gives
rational functions $R_n$ whose poles lie only at $2$ and $6$ and such that
$R_n\to f$ uniformly on $K$.

For part (b), suppose instead that rational functions with poles only at $6$
converged uniformly to $f$ on $K$. Take the circle $\gamma(t)=\frac72e^{it}$.
Every such $R_n$ is holomorphic inside $\gamma$, so
\[
\int_\gamma R_n(z)\,dz=0.
\]
Uniform convergence on $\gamma\subset K$ would imply
\[
\int_\gamma f(z)\,dz=0.
\]
But $\gamma$ encloses the pole at $1$ and not the pole at $5$, so
\[
\int_\gamma f(z)\,dz
=2\pi i\operatorname{Res}(f,1)
=2\pi i\frac1{1-5}
=-\frac{\pi i}{2}\ne0,
\]
a contradiction. Hence approximation with poles allowed only at $6$ is
impossible.
:::
