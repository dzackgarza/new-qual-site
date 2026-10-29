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

::: {.exercise}
Let $\Omega \subseteq \CC$ be a connected open region, and let $f: \Omega \to \CC$ be a holomorphic function.
Suppose that for every point $z_0 \in \Omega$, at least one coefficient in the Taylor series expansion:
$$f(z) = \sum_{n=0}^\infty c_n(z_0) (z - z_0)^n$$
is zero (i.e. for every $z_0 \in \Omega$, there exists some $n \in \NN$ such that $f^{(n)}(z_0) = 0$).
Prove that $f$ is a polynomial.
:::

::: {.solution}
For $n\ge0$, set $E_n\coloneqq\theset{z\in\Omega \st f^{(n)}(z)=0}$.
Each $E_n$ is closed in $\Omega$ because $f^{(n)}$ is continuous, and the hypothesis says $\Omega=\bigcup_{n\ge0}E_n$.

::: pf

::: {.pf-step #baire}
Some $E_N$ has nonempty interior.

::: pf-proof
The open set $\Omega\subseteq\CC$ is locally compact Hausdorff, hence a Baire space, so it is not a countable union of closed subsets with empty interior.
:::

:::

::: {.pf-step #vanish}
$f^{(N)}\equiv0$ on $\Omega$.

::: pf-proof
By step [](#baire){.pf-ref}, the holomorphic function $f^{(N)}$ vanishes on a nonempty open subset of the connected set $\Omega$, so the identity theorem gives $f^{(N)}\equiv0$.
:::

:::

::: pf-step
$f$ is a polynomial of degree at most $N-1$, and $f\equiv0$ if $N=0$.

::: pf-proof
If $N=0$, step [](#vanish){.pf-ref} says $f\equiv0$.
If $N\ge1$, fix $z_0\in\Omega$; the polynomial $P(z)\coloneqq\sum_{n<N}f^{(n)}(z_0)(z-z_0)^n/n!$ satisfies $(f-P)^{(n)}(z_0)=0$ for $n<N$ and $(f-P)^{(N)}\equiv0$ by step [](#vanish){.pf-ref}, so all derivatives of $f-P$ vanish at $z_0$.
Since $\Omega$ is connected, the identity theorem gives $f=P$ on $\Omega$.
:::

:::

:::

:::
