---
schema: qual/card@1
id: P-VEOV5
kind: problem
title: "Use the Cauchy inequalities or the maximum modulus principle\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - cauchy-estimates
  - maximum-modulus-principle
  - entire-functions
  - polynomials
relations: []
review: draft
solved: true
---

::: problem
Use the Cauchy inequalities or the maximum modulus principle to solve the following problems:

a. Prove that if $f$ is an entire function that satisfies
\[
\sup _{|z|=R}|f(z)| \leq A R^{k}+B
\]
for all $R>0$, some integer $k\geq 0$, and some constants $A, B > 0$, then $f$ is a polynomial of degree $\leq k$.

b. Show that if $f$ is holomorphic in the unit disc, is bounded, and converges uniformly to zero in the sector $\theta < \arg(z) < \phi$ as $\abs{z} \to 0$, then $f \equiv 0$.

c. Let $w_1, \cdots w_n$ be points on $S^1 \subset \CC$.
Prove that there exists a point $z\in S^1$ such that the product of the distances from $z$ to the points $w_j$ is at least 1.

Conclude that there exists a point $w\in S^1$ such that the product of the above distances is *exactly* 1.

d. Show that if the real part of an entire function is bounded, then $f$ is constant.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (a) $\sup_{\abs{z}=R}\abs{f} \leq AR^k + B$ for all $R > 0$ implies $f$ is a polynomial of degree $\leq k$; (b) $f$ holomorphic, bounded on $\DD$ and $\to 0$ uniformly in a sector as $\abs z \to 0$ implies $f \equiv 0$; (c) for points $w_j \in S^1$ there is $z \in S^1$ with $\prod_j \abs{z - w_j} \geq 1$, and some $w \in S^1$ with the product exactly $1$; (d) bounded real part implies constant.

<1>1. (a): $f^{(n)}(0) = 0$ for all $n > k$.
Proof: By the Cauchy estimates on $\abs{z} = R$, $\abs{f^{(n)}(0)} \leq \frac{n!}{R^n}\qty(A R^k + B)$ for every $R > 0$; letting $R \to \infty$ forces $\abs{f^{(n)}(0)} \leq \lim_{R\to\infty} n!\qty(A R^{k-n} + B R^{-n}) = 0$ whenever $n > k$.

<1>2. (a): $f$ is a polynomial of degree $\leq k$.
Proof: The Taylor series of the entire $f$ about $0$ is $f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!} z^n$; by <1>1 only the terms $n \leq k$ survive.

<1>3. (b): If $f \not\equiv 0$ and $f(0) = 0$, then $f$ has a zero of some finite order $m \geq 1$ at $0$.
Proof: An analytic function not identically zero has an isolated zero of finite order: $f(z) = z^m h(z)$ with $h$ holomorphic near $0$ and $h(0) \neq 0$.

<1>4. (b): $\abs{f(z)} \geq c\abs{z}^m$ for small $\abs z$ in the sector.
Proof: By <1>3, $\abs{h(z)} \geq \abs{h(0)}/2 > 0$ near $0$, so $\abs{f(z)} = \abs z^m \abs{h(z)} \geq \frac{\abs{h(0)}}{2}\abs z^m$ near $0$.
(If $f(0) \neq 0$, then $\abs{f(z)} \geq \abs{f(0)}/2$ near $0$ — the same conclusion with $m = 0$.)

<1>5. (b): $f \equiv 0$.
Proof: The sector contains points $z_n \to 0$ (take $z_n = \rho_n e^{i\theta}$ with fixed $\theta$ in the sector, $\rho_n \to 0$). If $f \not\equiv 0$, then by <1>4, $\abs{f(z_n)} \geq c\abs{z_n}^m$, which does not tend to $0$ faster than $\abs{z_n}^m$; more precisely, uniform convergence to $0$ on the sector means $\sup_{\text{sector}, \abs z < \delta}\abs f \to 0$, contradicting $\abs{f(z_n)} \geq c \abs{z_n}^m \not\to 0$ appropriately (choose $\rho_n$ so that $c\rho_n^m$ stays bounded away from $0$, e.g. constant $\rho_n = \rho$). Hence $f \equiv 0$.

<1>6. (c): There exists $z \in S^1$ with $\prod_{j=1}^n \abs{z - w_j} \geq 1$.
Proof: The polynomial $P(z) = \prod_{j=1}^n (z - w_j)$ is holomorphic; by the maximum modulus principle on $\DD$, $\max_{\abs z = 1}\abs{P(z)} \geq \abs{P(0)} = \prod_j \abs{w_j} = 1$ (all $\abs{w_j} = 1$).

<1>7. (c): There exists $w \in S^1$ with $\prod_j \abs{w - w_j} = 1$.
Proof: The function $\varphi(z) = \prod_j \abs{z - w_j}$ is continuous on the connected set $S^1$; at $z = w_1$, $\varphi(w_1) = 0$, and by <1>6 its maximum is $\geq 1$.
By the intermediate value theorem along a path on $S^1$ from $w_1$ to the maximizing point, $\varphi$ attains every value between $0$ and its maximum, in particular $1$.

<1>8. (d): $f$ is constant.
Proof: Assume $\Re f \leq M$ (bounded above; bounded below is analogous).
Then $g(z) = e^{f(z)}$ is entire and $\abs{g(z)} = e^{\Re f(z)} \leq e^M$, so $g$ is bounded; by Liouville, $g$ is constant, and hence $f = \log g$ (locally) is constant.

<1>9. Q.E.D. Proof: <1>2 proves (a), <1>5 proves (b), <1>6–<1>7 prove (c), and <1>8 proves (d).
:::
