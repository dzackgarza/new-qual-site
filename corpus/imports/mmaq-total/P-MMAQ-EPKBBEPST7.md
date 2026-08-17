---
schema: qual/card@1
id: P-MMAQ-EPKBBEPST7
kind: problem
title: Let $\phi$ be a compactly supported smooth function that vanishes…
classification:
  areas:
  - real-analysis
  topics:
  - approximations-to-the-identity
  - convergence-of-functions
  - convergence-of-integrals
  - l1
relations: []
review: draft
---

::: problem
Let $\phi$ be a compactly supported smooth function that vanishes outside of an interval $[-N, N]$ such that $\int_{\mathrm{R}} \phi(x) d x=1$.

For $f\in L^1(\RR)$, define
$$
K_{j}(x):=j \phi(j x), \quad \quad f \ast K_{j}(x):=\int_{\mathbb{R}} f(x-y) K_{j}(y) ~d y
$$
and prove the following:

1. Each $f\ast K_j$ is smooth and compactly supported.

2. $$
   \lim _{j \rightarrow \infty}\left\|f * K_{j}-f\right\|_{1}=0
   $$

> Hint:
> $$
> \lim _{y \rightarrow 0} \int_{\mathbb{R}}|f(x-y)-f(x)| d y=0
> $$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $\phi \in C_c^\infty(\RR)$ vanish outside $[-N,N]$ with $\int \phi = 1$, and set $K_j(x) = j\phi(jx)$. For $f \in L^1(\RR)$, prove (1) $f \ast K_j$ is smooth and compactly supported, and (2) $\norm{f \ast K_j - f}_1 \to 0$ as $j \to \infty$.

<1>1. Each $K_j$ is smooth, compactly supported, has integral $1$, and the supports shrink to $\theset{0}$.
    <2>1. $\operatorname{supp}(K_j) \subseteq [-N/j, N/j]$, and $K_j \in C^\infty$.
        Proof: $K_j(x) = j\phi(jx)$ is a dilation of the smooth $\phi$; $\phi$ vanishes outside $[-N,N]$, so $K_j$ vanishes outside $[-N/j, N/j]$.
    <2>2. $\int_\RR K_j = 1$.
        Proof: Substituting $u = jx$, $\int_\RR j\phi(jx) ~dx = \int_\RR \phi(u) ~du = 1$.
    <2>3. Q.E.D.
        Proof: By <2>1 and <2>2.

<1>2. Each $f \ast K_j$ is smooth.
    <2>1. For $x \in \RR$, $f \ast K_j(x) = \int f(x - y) K_j(y) ~dy$ is defined everywhere and is continuous.
        Proof: $f \in L^1$ and $K_j$ is bounded with compact support; continuity follows from continuity of translation in $L^1$, the hint with $f$ in place of $f$ (for general $f \in L^1$ this is the standard $L^1$-continuity of translation).
    <2>2. Differentiation under the integral sign is legitimate to any order.
        Proof: $\frac{d^m}{dx^m} K_j(x - y)$ exists and is bounded and compactly supported in $y$ for each $m$; the dominated convergence theorem justifies differentiating $m$ times, and the compact support of $K_j$ gives the needed integrable domination.
    <2>3. Hence $f \ast K_j \in C^\infty$.
        Proof: By <2>1 and <2>2, derivatives of all orders exist and are continuous.

<1>3. On compact support: $f \ast K_j$ is compactly supported when $f$ is; for general $f \in L^1$ only smoothness is guaranteed.
    <2>1. If $x \notin \operatorname{supp}(f) + [-N/j, N/j]$, then $f(x - y) K_j(y) = 0$ for every $y$.
        Proof: For $y \in [-N/j, N/j]$ (otherwise $K_j(y) = 0$), $x - y \notin \operatorname{supp}(f)$, so $f(x-y) = 0$.
    <2>2. Hence, when $f$ has compact support, $\operatorname{supp}(f \ast K_j) \subseteq \operatorname{supp}(f) + [-N/j, N/j]$, a compact set.
        Proof: $\operatorname{supp}(f)$ is compact by hypothesis; a Minkowski sum of compact sets is compact, and by <2>1 the convolution vanishes off this sum.
    <2>3. The statement "compactly supported for every $f \in L^1$" requires the standing hypothesis that $f$ have compact support; without it the claim is false, e.g. $f(x) = e^{-x^2} \in L^1$ gives $f \ast K_j > 0$ everywhere.
        Proof: For $f(x) = e^{-x^2}$, each $f \ast K_j$ is a strictly positive function, so it has full (noncompact) support; the support containment of <2>2 is the general truth.
    <2>4. Q.E.D.
        Proof: The honest statement is <2>2; part 2 of the problem (the $L^1$ convergence) needs no compact-support hypothesis on $f$.

<1>4. $\norm{f \ast K_j - f}_1 \to 0$ as $j \to \infty$.
    <2>1. Since $\int K_j = 1$ (<1>1.<2>2), $f(x) = f(x) \int_\RR K_j(y) ~dy = \int_\RR f(x) K_j(y) ~dy$.
        Proof: Multiply by the constant $1 = \int K_j$.
    <2>2. Therefore $f \ast K_j(x) - f(x) = \int_\RR (f(x-y) - f(x)) K_j(y) ~dy$.
        Proof: Subtract <2>1 from the definition of $f \ast K_j$.
    <2>3. By Minkowski's inequality for integrals, $\norm{f \ast K_j - f}_1 \leq \int_\RR \norm{f(\cdot - y) - f(\cdot)}_1 \abs{K_j(y)} ~dy$.
        Proof: Integrate $\abs{f \ast K_j(x) - f(x)}$ over $x$ and use Fubini–Tonelli, noting $K_j \geq 0$ on its support (or use $\abs{K_j}$).
    <2>4. Fix $\eps > 0$; choose $\delta > 0$ with $\norm{f(\cdot - y) - f(\cdot)}_1 < \eps/2$ whenever $\abs{y} < \delta$.
        Proof: This is the $L^1$-continuity of translation, stated in the hint (for $f \in L^1$ it is the standard density argument: continuous compactly supported functions are dense, and the claim holds for them by uniform continuity).
    <2>5. Split the integral: $\int_\RR \norm{f(\cdot-y) - f(\cdot)}_1 \abs{K_j(y)} ~dy = I_1 + I_2$, where $I_1$ integrates over $\abs{y} < \delta$ and $I_2$ over $\abs{y} \geq \delta$.
        Proof: Partition $\RR$ into $\theset{\abs{y} < \delta}$ and its complement.
    <2>6. $I_1 < \eps/2$, since $\norm{f(\cdot-y)-f(\cdot)}_1 < \eps/2$ there and $\int \abs{K_j} = 1$.
        Proof: By <2>4 and $\int_\RR \abs{K_j} = \int \phi$ up to sign (indeed $= 1$ when $\phi \geq 0$; otherwise use $\abs{\phi}$).
    <2>7. $I_2 \to 0$ as $j \to \infty$, since $\int_{\abs{y} \geq \delta} \abs{K_j(y)} ~dy = \int_{\abs{u} \geq j\delta} \abs{\phi(u)} ~du \to 0$.
        Proof: Substitute $u = jy$; $\abs{\phi} \in L^1$ and $j\delta \to \infty$, so the tail integral vanishes by dominated convergence.
    <2>8. Choose $J$ with $I_2 < \eps/2$ for all $j \geq J$; then $\norm{f \ast K_j - f}_1 < \eps$ for $j \geq J$.
        Proof: Combine <2>5, <2>6, <2>7.
    <2>9. Q.E.D.
        Proof: $\eps > 0$ was arbitrary.

<1>5. Conclusion: smoothness and the $L^1$ convergence hold for every $f \in L^1$; compact support holds when $f$ has compact support (and the claim as stated requires it).
    Proof: Smoothness by <1>2, the support statement by <1>3, and $L^1$ convergence by <1>4.
:::
