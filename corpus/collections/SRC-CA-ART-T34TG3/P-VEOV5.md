---
schema: qual/card@1
id: P-VEOV5
kind: problem
title: Polynomial growth of entire functions, vanishing in a sector, products of distances
  on $S^1$, and bounded real part
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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Use the Cauchy inequalities or the maximum modulus principle to solve the following problems:

a. Prove that if $f$ is an entire function that satisfies
\[
\sup _{|z|=R}|f(z)| \leq A R^{k}+B
\]
for all $R>0$, some integer $k\geq 0$, and some constants $A, B > 0$, then $f$ is a polynomial of degree $\leq k$.

b. Show that if $f$ is holomorphic in the unit disc, is bounded, and converges uniformly to zero in the sector $\theta < \arg(z) < \phi$ as $\abs{z} \to 1$, then $f \equiv 0$.

c. Let $w_1, \cdots w_n$ be points on $S^1 \subset \CC$.
Prove that there exists a point $z\in S^1$ such that the product of the distances from $z$ to the points $w_j$ is at least 1.

Conclude that there exists a point $w\in S^1$ such that the product of the above distances is *exactly* 1.

d. Show that if the real part of an entire function is bounded, then $f$ is constant.
:::

::: {.solution}

::: pf

::: {.pf-step #cauchy-derivative-vanishing}
(a) $f^{(n)}(0) = 0$ for all $n > k$.

::: pf-proof
By the Cauchy estimates on $\abs{z} = R$, $\abs{f^{(n)}(0)} \leq \frac{n!}{R^n}\qty(A R^k + B) = n!\qty(A R^{k-n} + B R^{-n})$ for every $R > 0$. For $n > k$ the right-hand side tends to $0$ as $R \to \infty$.
:::

:::

::: {.pf-step #f-is-polynomial}
(a) $f$ is a polynomial of degree $\leq k$.

::: pf-proof
The Taylor series of the entire function $f$ about $0$ converges on $\CC$: $f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!} z^n$. By step [](#cauchy-derivative-vanishing){.pf-ref}, only the terms with $n \leq k$ are nonzero.
:::

:::

::: {.pf-step #rotated-product-vanishes}
(b) Let $S=\{z\in\DD:\theta<\arg z<\phi\}$ and choose an integer $N$ with $2\pi/N<\phi-\theta$. Then $g(z)\coloneqq\prod_{j=0}^{N-1} f\qty(e^{2\pi i j/N}z)$ is identically zero on $\DD$.

::: pf-proof
Put $M=\sup_{\DD}\abs f<\infty$. For every $z\neq0$, some rotation $e^{2\pi ij/N}z$ has argument in $(\theta,\phi)$, because consecutive rotations differ in argument by $2\pi/N<\phi-\theta$. Fix $\varepsilon>0$. By hypothesis there is $\rho<1$ with $\abs{f(z)}<\varepsilon$ for $z\in S$ and $\rho<\abs z<1$. Hence $\abs{g(z)}\le\varepsilon M^{N-1}$ for $\rho<\abs z<1$. For each $r\in(\rho,1)$, the maximum modulus principle on $\abs z\le r$ extends this bound to $\abs z\le r$, so it holds on all of $\DD$. Since $\varepsilon$ is arbitrary, $g\equiv0$.
:::

:::

::: {.pf-step #f-is-zero}
(b) $f \equiv 0$.

::: pf-proof
The holomorphic functions on the connected disc $\DD$ form an integral domain, so by step [](#rotated-product-vanishes){.pf-ref} one factor $f(e^{2\pi ij/N}z)$ is identically zero on $\DD$. Rotation is a bijection of $\DD$, hence $f\equiv0$.
:::

:::

::: {.pf-step #product-distances-at-least-one}
(c) There exists $z \in S^1$ with $\prod_{j=1}^n \abs{z - w_j} \geq 1$.

::: pf-proof
The polynomial $P(z) = \prod_{j=1}^n (z - w_j)$ is holomorphic, and $\abs{P(0)} = \prod_j \abs{w_j} = 1$. By the maximum modulus principle on $\overline\DD$, $\max_{\abs z = 1}\abs{P(z)} \geq 1$.
:::

:::

::: {.pf-step #product-distances-equal-one}
(c) There exists $w \in S^1$ with $\prod_j \abs{w - w_j} = 1$.

::: pf-proof
The function $\varphi(z) = \prod_j \abs{z - w_j}$ is continuous on $S^1$, $\varphi(w_1) = 0$, and $\varphi(z)\ge1$ at the point $z$ of step [](#product-distances-at-least-one){.pf-ref}. By the intermediate value theorem along an arc of $S^1$ from $w_1$ to $z$, $\varphi$ takes the value $1$.
:::

:::

::: {.pf-step #bounded-real-part-constant}
(d) If $\Re f$ is bounded, then $f$ is constant.

::: pf-proof
Suppose $\Re f \leq M$. Then $g(z) = e^{f(z)}$ is entire and $\abs{g(z)} = e^{\Re f(z)} \leq e^M$, so $g$ is constant by Liouville's theorem. Hence $0=g' = f'e^{f}$, and $e^f\neq0$, so $f'\equiv0$ and $f$ is constant. (If instead $\Re f$ is bounded below, apply this to $-f$.)
:::

:::

::: pf-qed
Step [](#f-is-polynomial){.pf-ref} proves (a), step [](#f-is-zero){.pf-ref} proves (b), steps [](#product-distances-at-least-one){.pf-ref} and [](#product-distances-equal-one){.pf-ref} prove (c), and step [](#bounded-real-part-constant){.pf-ref} proves (d).
:::

:::
:::

::: {.remark}
Part (b) requires the limit $\abs z\to1$. With $\abs z\to0$ the conclusion fails: $f(z)=z$ is bounded on $\DD$ and tends to $0$ uniformly as $\abs z\to0$.
:::
