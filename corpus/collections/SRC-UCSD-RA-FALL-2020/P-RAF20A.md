---
schema: qual/card@1
id: P-RAF20A
kind: problem
title: "True or false: weakly closed sets, nested compacts, vague convergence, Schwartz convolution"
classification:
  areas:
  - real-analysis
  topics:
  - Weak Topology
  - Compactness
  - Vague Convergence
  - Radon Measures
  - Schwartz Space
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Fall 2020 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Determine if each of the following statements is true or false.
If true, give a brief proof.
If false, give a counterexample or prove your assertion.

(1) Let $X$ be a Banach space and $A$ a closed subset of $X$.
Then $A$ is sequentially weakly closed, i.e., if $u_n \in A$ ($n = 1, 2, \ldots$) and $u_n \to u$ weakly for some $u \in X$, then $u \in A$.

(2) Let $X$ be a compact Hausdorff topological space.
Let $\{K_j\}$ ($j = 1, 2, \ldots$) be a sequence of decreasing, nonempty compact subsets of $X$.
Then $\bigcap_{j=1}^\infty K_j \neq \emptyset$.

(3) Let $X$ be a locally compact Hausdorff space and $M(X)$ the Banach space of all complex Radon measures on $X$.
Let $\mu \in M(X)$ and $\mu_n \in M(X)$ ($n = 1, 2, \ldots$) and assume that $\mu_n \to \mu$ vaguely in $M(X)$.
Then $\mu_n(E) \to \mu(E)$ for any Borel set $E \subseteq X$.

(4) Let $\mathcal{S}$ denote the Schwartz space on $\mathbb{R}^n$.
Let $f, g \in \mathcal{S}$.
If $f * g = 0$ in $\mathbb{R}^n$ then either $f = 0$ identically in $\mathbb{R}^n$ or $g = 0$ identically in $\mathbb{R}^n$.
:::

::: solution
<1>1. Statement (1) is false.
::: proof
Take $X=\ell^2$ and let
\[
A:=\{e_n:n\ge1\},
\]
where $(e_n)$ is the standard orthonormal basis. Since
\[
\|e_n-e_m\|_2=\sqrt2
\qquad(n\ne m),
\]
the set $A$ is norm closed.

For every $x=(x_k)\in\ell^2$,
\[
\langle e_n,x\rangle=x_n\longrightarrow0,
\]
so $e_n\rightharpoonup0$ weakly. But $0\notin A$. Hence a norm-closed subset of a Banach space need not be sequentially weakly closed.
:::

<1>2. Statement (2) is true.
::: proof
Because $X$ is Hausdorff, every compact subset $K_j$ is closed. The nested family $(K_j)$ has the finite-intersection property: for every $N$,
\[
\bigcap_{j=1}^N K_j=K_N\ne\varnothing.
\]
Since $X$ is compact, every family of closed subsets with the finite-intersection property has nonempty total intersection. Therefore
\[
\boxed{\bigcap_{j=1}^\infty K_j\ne\varnothing.}
\]
:::

<1>3. Statement (3) is false.
::: proof
Take $X=\mathbb R$ and
\[
\mu_n=\delta_{1/n},
\qquad
\mu=\delta_0.
\]
For every $\varphi\in C_c(\mathbb R)$,
\[
\int\varphi\,d\mu_n=\varphi(1/n)\longrightarrow\varphi(0)=\int\varphi\,d\mu,
\]
so $\mu_n\to\mu$ vaguely.

However, for the Borel set $E=\{0\}$,
\[
\mu_n(E)=0
\qquad\text{for every }n,
\]
whereas
\[
\mu(E)=1.
\]
Thus vague convergence does not imply convergence on every Borel set.
:::

<1>4. Statement (4) is false.
::: proof
Choose nonzero functions
\[
\phi,\psi\in C_c^\infty(\mathbb R^n)
\]
with disjoint supports. Let
\[
f=\mathcal F^{-1}\phi,
\qquad
g=\mathcal F^{-1}\psi.
\]
The inverse Fourier transform maps $C_c^\infty$ into the Schwartz space, so $f,g\in\mathcal S$ and neither is identically zero.

By the convolution theorem,
\[
\widehat{f*g}=\widehat f\,\widehat g=\phi\psi=0.
\]
Since the Fourier transform is injective on $\mathcal S$,
\[
f*g=0.
\]
Thus two nonzero Schwartz functions can have zero convolution.
:::
:::
