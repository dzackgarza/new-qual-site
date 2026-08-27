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

:::{.solution}
\[
\abs{ f(z_0) }
&= \abs{ {1\over 2\pi i} \oint_{\abs{z-z_0} = R } {f(z) \over (z-z_0)^{n+1} }  \dz } \\
&\leq {1\over 2\pi } \oint_{\abs{z-z_0} = R } \abs{f(z)} R^{-(n+1)}   \dz \\
&\leq {1\over 2\pi }\sup_{\abs{z-z_0} = R} \abs{f(z)} R^{-(n+1)} \cdot 2\pi R \\
&= \sup_{\abs{z-z_0} = R} \abs{f(z)} R^{-n} \\
&\leq (AR^k + B)R^{-n} \qquad \text{ if } z_0 = 0 \\
&= AR^{k-n} + BR^{-n} \\
&\to 0 
,\]
provided $k-n< 0$, so $n>k$.
Since $f$ is entire, write
\[
f(z) 
= \sum_{n\geq 0} f^{(n)}(0) {z^n\over n!}
= \sum_{0\leq n\leq k} f^{(n)}(0) {z^n\over n!}
,\]
making $f$ a polynomial of degree at most $k$.
:::

:::{.solution}
Write $S_\phi \da \ts{0<\Arg(z) < \phi}$ and choose $n$ large enough so that 
\[
\DD \subseteq S \union \zeta_n S \union \zeta_n^2 S \union\cdots\union \zeta_{n}^{n-1}S
,\]
i.e. so that the rotated sectors cover the disc.
By uniform convergence of $f$ to $0$ on $S$, choose $r<1$ small enough so that $\abs{f(z)} < \eps$ for $\abs{z} < r$ in $S$.
Note that $\DD_r \subseteq \Union_{k=0}^{n-1} \zeta_n^k S_r$, where $S_r \da \ts{z\in S \st \abs{z} \leq r}$ is a subsector of radius $r$.

By the MMP, let $M$ be the maximum of $f$ on $\DD$, which is attained at some point on $S^1$.
Then $\abs{f} < M$ on every $\zeta_n^k S_r$.
Now define
\[
g(z) \da f(z) \prod_{k=1}^{n-1} f(\zeta_n^k z) \da f(z) \prod_{k=1}^{n-1}f_k(z)
.\]
Note that $\abs{f(z)}\leq \eps$ and $\abs{f_k(z)} \leq M$, so
\[
\abs{g(z)}\leq \eps \cdot M^{n-1} \convergesto{\eps\to 0} 0
.\]
since $M$ is a constant.
So $g(z) \equiv 0$ on $\DD_r$, and by the identity principle, on $\DD$.
Thus some factor $f_k(z)$ is identically zero. 
But if $f(\zeta_n^k z)\equiv 0$ on $\DD$, then $f(z) \equiv 0$ on $\DD$, since every $z\in \DD$ can be written as $\zeta_n^k w$ for some $w\in \DD$.

:::

:::{.solution}
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

:::{.solution}
Write $f=u+iv$ where by assumption $u$ is bounded.
Both $u$ and $v$ are harmonic, so if $\abs{u} \leq M$ on $\CC$, then there is some disc where $\abs{u} = M$ for some point in the interior.
By the MMP for harmonic functions, $u$ is constant on $\CC$.
So $u_x, u_y = 0$, and by Cauchy-Riemann, $v_x, v_y = 0$, so $v'=0$ and $v$ is constant, making $f$ constant.
:::

:::{.solution}

Consider $g(z) \da e^{f(z)}$, then $\abs{g(z)} = e^{\Re(z)}$ is entire and bounded and thus constant by Liouville's theorem.
So $g'(z) = 0$, but on the other hand $g'(z) = f'(z) e^{f(z)} = 0$, so $f'(z) = 0$ and $f$ must be constant since $e^f$ is nonvanishing.

:::
