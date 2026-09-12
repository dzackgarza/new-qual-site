---
schema: qual/card@1
id: E-G4N4D
kind: problem
title: A holomorphic function with a vanishing Taylor coefficient at every point is
  a polynomial
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Integral Formula
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: exercise
Let $\Omega \subseteq \mathbb{C}$ be a connected open region, and let $f: \Omega \to \mathbb{C}$ be a holomorphic function.
Suppose that for every point $z_0 \in \Omega$, at least one coefficient in the Taylor series expansion:
$$f(z) = \sum_{n=0}^\infty c_n(z_0) (z - z_0)^n$$
is zero (i.e. for every $z_0 \in \Omega$, there exists some $n \in \mathbb{N}$ such that $f^{(n)}(z_0) = 0$).
Prove that $f$ is a polynomial.
:::

::: solution
For $n\ge0$, set
\[
E_n=\{z\in\Omega:f^{(n)}(z)=0\}.
\]
Each $E_n$ is closed in $\Omega$ because $f^{(n)}$ is continuous, and the hypothesis says
\[
\Omega=\bigcup_{n=0}^{\infty}E_n.
\]

<1>1. The region $\Omega$ is a locally compact Hausdorff space, hence a Baire space. Therefore a countable union of closed subsets with empty interior cannot equal $\Omega$. Thus some $E_N$ has nonempty interior.

<1>2. Hence $f^{(N)}$ vanishes on a nonempty open subset of $\Omega$. Since $f^{(N)}$ is holomorphic and $\Omega$ is connected, the identity theorem gives
\[
f^{(N)}\equiv0\quad\text{on }\Omega.
\]

<1>3. If $N=0$, then $f\equiv0$, which is a polynomial. If $N\ge1$, then $f^{(N)}\equiv0$, so the Taylor expansion of $f$ at any point terminates after degree at most $N-1$. Equivalently, repeated integration gives a polynomial $P$ of degree at most $N-1$ such that $f=P$ on $\Omega$.

Therefore $f$ is a polynomial.
:::
