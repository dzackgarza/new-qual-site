---
schema: qual/card@1
id: P-RMZDG
kind: problem
title: Entire functions of polynomial growth, sector vanishing on the disc, products
  of distances on $S^1$, and constancy when the real part is bounded
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Maximum Modulus Principle
  - Entire Functions
  - Polynomials
relations: []
review: draft
---

:::{.problem}
Use the Cauchy inequalities or the maximum modulus principle to solve the following problems:

a. 
Prove that if $f$ is an entire function that satisfies
\[
\sup _{|z|=R}|f(z)| \leq A R^{k}+B
\]
for all $R>0$, some integer $k\geq 0$, and some constants $A, B > 0$, then $f$ is a polynomial of degree $\leq k$.

b. 
Show that if $f$ is holomorphic in the unit disc, is bounded, and converges uniformly to zero in the sector $\theta < \arg(z) < \phi$ as $\abs{z} \to 1$, then $f \equiv 0$.

c. 
Let $w_1, \cdots w_n$ be points on $S^1 \subset \CC$.
Prove that there exists a point $z\in S^1$ such that the product of the distances from $z$ to the points $w_j$ is at least 1.
  Conclude that there exists a point $w\in S^1$ such that the product of the above distances is *exactly* 1.

d. 
Show that if the real part of an entire function is bounded, then $f$ is constant.

:::

::: {.solution title="Part 1"}
Fix an integer $m>k$. By Cauchy's estimate on the circle $|z|=R$,
\[
|f^{(m)}(0)|
\le {m!\over R^m}\max_{|z|=R}|f(z)|
\le m!\qty(AR^{k-m}+BR^{-m}).
\]
Letting $R\to\infty$ gives $f^{(m)}(0)=0$. This holds for every $m>k$, so
\[
f(z)=\sum_{m=0}^k {f^{(m)}(0)\over m!}z^m.
\]
:::

::: {.solution title="Part 2"}
Let $S=\{z\in\DD:\theta<\arg z<\phi\}$. Choose $N$ so large that the rotated sectors
\[
e^{2\pi i j/N}S,
\qquad 0\le j<N,
\]
cover every angular direction. Since $f$ is bounded, put
\[
M=\sup_{z\in\DD}|f(z)|<\infty
\]
and define
\[
g(z)=\prod_{j=0}^{N-1} f\qty(e^{2\pi i j/N}z).
\]

Fix $\varepsilon>0$. By uniform convergence to $0$ in $S$ as $|z|\to1$, there is $\rho<1$ such that
\[
|f(z)|<\varepsilon
\qquad(z\in S,\ \rho<|z|<1).
\]
For every $r\in(\rho,1)$ and every $|z|=r$, at least one rotated point $e^{2\pi i j/N}z$ lies in $S$. Hence
\[
|g(z)|\le \varepsilon M^{N-1}
\qquad(|z|=r).
\]
The maximum modulus principle gives the same bound on $|z|\le r$. Since $\varepsilon$ is arbitrary, $g\equiv0$ on $\DD$.

The ring of holomorphic functions on the connected disk is an integral domain, so one factor $f(e^{2\pi i j/N}z)$ is identically zero. Rotation is a bijection of $\DD$, hence $f\equiv0$.
:::

:::{.solution title="Part 3"}
Consider
\[
f(z) \da \prod_{1\leq k \leq n} (w_k - z)
.\]
Then $f$ is holomorphic and nonconstant on $\DD$, so attains a maximum $M$ on $S^1$.
Moreover, $\abs{f(z)} = \prod \abs{w_k-z}$ is exactly the product of distances from $z$ to the $w_k$.
Moreover, since $\abs{f(0)} = \prod\abs{w_k} = 1$, we must have $M>1$.

Now note that $f(w_k) = 0$ and $f$ is continuous in $\DD$.
So $\abs{f(z)} \in [0, M] \subseteq \RR$ where $M>1$, so by the intermediate value theorem, $\abs{f(z)} = 1$ for some $z$.
:::

::: {.solution title="Part 4"}
Suppose $|\Re f(z)|\le M$ on $\CC$ and define $g(z)=e^{f(z)}$. Then $g$ is entire and
\[
|g(z)|=e^{\Re f(z)}\le e^M.
\]
By Liouville's theorem, $g$ is constant. Since
\[
g'(z)=f'(z)e^{f(z)}
\]
and $e^{f(z)}\neq0$, we get $f'\equiv0$. Thus $f$ is constant.
:::
