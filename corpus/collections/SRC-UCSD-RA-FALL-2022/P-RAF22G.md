---
schema: qual/card@1
id: P-RAF22G
kind: problem
title: "A distribution supported at the origin is a finite linear combination of derivatives of delta"
classification:
  areas:
  - real-analysis
  topics:
  - Distributions
  - Dirac Delta
  - Support of Distributions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the official UCSD Fall 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $F$ be a distribution on $\mathbb{R}^n$ such that the support of $F$, $\operatorname{supp}(F) = \{0\}$.
Let $\alpha = (\alpha_1, \cdots, \alpha_n)$ with $\alpha_i$ nonnegative integers, and $\delta$ be the delta distribution centered at $0$.

1. Prove that there exists a natural number $N$ and $C > 0$ such that
$$
|\langle F, \varphi \rangle| \leq C \sum_{|\alpha| \leq N} \sup_x |\partial^\alpha \varphi(x)|, \quad \forall \varphi \in C_c^\infty.
$$

2. If $\varphi \in C_c^\infty$ and $\partial^\alpha \varphi(0) = 0$ for all $|\alpha| \leq N$, then $\langle F, \varphi \rangle = 0$.

3. There exist constants $c_\alpha$ ($|\alpha| \leq N$) such that $F = \sum_{|\alpha| \leq N} c_\alpha \partial^\alpha \delta$.
:::

::: solution
<1>1. A distribution supported at the origin has finite order.
::: proof
Choose $\chi\in C_c^\infty(\mathbb R^n)$ with $\chi=1$ on a neighborhood of $0$, and let $K=\operatorname{supp}\chi$. Since
\[
\operatorname{supp}F=\{0\},
\]
we have
\[
\langle F,\varphi\rangle
=\langle F,\chi\varphi\rangle
\]
for every $\varphi\in C_c^\infty$: the function $(1-\chi)\varphi$ is supported away from $0$ and is therefore annihilated by $F$.

The restriction of a distribution to the Fréchet space
\[
\mathcal D_K:=\{\psi\in C_c^\infty:\operatorname{supp}\psi\subset K\}
\]
is continuous. Hence there exist $N\in\mathbb N$ and $C_0>0$ such that
\[
|\langle F,\psi\rangle|
\le C_0\sum_{|\alpha|\le N}
\sup_x|\partial^\alpha\psi(x)|
\qquad(\psi\in\mathcal D_K).
\]
Applying this to $\psi=\chi\varphi$ and using Leibniz's rule gives, after absorbing the finitely many derivatives of $\chi$ into the constant,
\[
\boxed{
|\langle F,\varphi\rangle|
\le C\sum_{|\alpha|\le N}
\sup_x|\partial^\alpha\varphi(x)|.}
\]
:::

<1>2. Vanishing of the $N$-jet at the origin forces annihilation.
::: proof
Suppose
\[
\partial^\alpha\varphi(0)=0
\qquad(|\alpha|\le N).
\]
Choose $\eta\in C_c^\infty(\mathbb R^n)$ with $\eta=1$ near $0$, and put
\[
\eta_\varepsilon(x):=\eta(x/\varepsilon).
\]
Since $\eta_\varepsilon=1$ on a neighborhood of $0$,
\[
\langle F,\varphi\rangle
=\langle F,\eta_\varepsilon\varphi\rangle
\]
for every $\varepsilon>0$.

Taylor's theorem and the vanishing jet imply that for every multi-index $\gamma$ with $|\gamma|\le N$,
\[
|\partial^\gamma\varphi(x)|
\le C_\varphi |x|^{N+1-|\gamma|}
\]
for $x$ near $0$. On the support of $\eta_\varepsilon$ we have $|x|=O(\varepsilon)$, while
\[
|\partial^\beta\eta_\varepsilon(x)|
\le C_\beta\varepsilon^{-|\beta|}.
\]
Therefore Leibniz's rule gives, for every $|\alpha|\le N$,
\[
\sup_x|\partial^\alpha(\eta_\varepsilon\varphi)(x)|
\le C_\alpha\varepsilon^{N+1-|\alpha|}
\le C_\alpha\varepsilon.
\]
Using the estimate from Step 1,
\[
|\langle F,\varphi\rangle|
=|\langle F,\eta_\varepsilon\varphi\rangle|
\le C'\varepsilon.
\]
Letting $\varepsilon\downarrow0$ yields
\[
\boxed{\langle F,\varphi\rangle=0.}
\]
:::

<1>3. Identify $F$ with a finite linear combination of derivatives of $\delta$.
::: proof
Choose $\rho\in C_c^\infty(\mathbb R^n)$ with $\rho=1$ near $0$. For $|\alpha|\le N$, set
\[
a_\alpha
:=\left\langle F,\rho(x)\frac{x^\alpha}{\alpha!}\right\rangle.
\]
For any test function $\varphi$, let
\[
P_N\varphi(x)
=\sum_{|\alpha|\le N}
\frac{\partial^\alpha\varphi(0)}{\alpha!}x^\alpha
\]
be its Taylor polynomial of degree $N$ at $0$. The function
\[
\varphi-\rho P_N\varphi
\]
has all derivatives of order at most $N$ equal to zero at $0$. By Step 2,
\[
\langle F,\varphi\rangle
=\langle F,\rho P_N\varphi\rangle
=\sum_{|\alpha|\le N}
a_\alpha\,\partial^\alpha\varphi(0).
\]

Since
\[
\langle \partial^\alpha\delta,\varphi\rangle
=(-1)^{|\alpha|}\partial^\alpha\varphi(0),
\]
define
\[
c_\alpha:=(-1)^{|\alpha|}a_\alpha.
\]
Then for every test function $\varphi$,
\[
\langle F,\varphi\rangle
=\left\langle
\sum_{|\alpha|\le N}c_\alpha\partial^\alpha\delta,
\varphi
\right\rangle.
\]
Hence
\[
\boxed{F=\sum_{|\alpha|\le N}c_\alpha\partial^\alpha\delta.}
\]
:::
:::
