---
schema: qual/card@1
id: P-B7CIT
kind: problem
title: Analytic functions of equal modulus differ by a unimodular constant
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Open Mapping Theorem
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Let $f$ and $g$ be non-zero analytic functions on a region $\Omega$.
Assume $|f(z)| = |g(z)|$ for all $z$ in $\Omega$.
Show that $f(z) = e^{i \theta} g(z)$ in $\Omega$ for some $0 \leq \theta < 2 \pi$.
:::

::: {.solution}
**Goal:** Prove that if $f, g$ are nonzero analytic functions on a region $\Omega$ with $\abs{f(z)} = \abs{g(z)}$ for all $z \in \Omega$, then $f(z) = e^{i\theta} g(z)$ for some $0 \leq \theta < 2\pi$.

<1>1. Define $h := f / g$; then $h$ is analytic and never vanishes on $\Omega$.
::: {.proof}
$g \neq 0$ on $\Omega$ by hypothesis, and quotients of analytic functions are analytic.
:::

<1>2. $\abs{h(z)} = 1$ for all $z \in \Omega$.
::: {.proof}
$\abs h = \abs f / \abs g = 1$ by hypothesis.
:::

<1>3. $h$ is constant.
<2>1. $h(\Omega)$ is contained in the unit circle $S^1$.
::: {.proof}
<1>2. <2>2. $h(\Omega)$ is open in $\CC$ if $h$ is nonconstant.
:::
::: {.proof}
Open mapping theorem: a nonconstant holomorphic map on a region is open.
:::
<2>3. $S^1$ has empty interior in $\CC$.
::: {.proof}
The unit circle contains no open disk.
:::
<2>4. Hence $h$ is constant.
::: {.proof}
<2>1--<2>3: a nonconstant $h$ would map $\Omega$ onto an open set inside $S^1$, impossible.
:::

<1>4. $h \equiv e^{i\theta}$ for some $0 \leq \theta < 2\pi$.
::: {.proof}
<1>3 and $\abs h \equiv 1$ (<1>2): the constant value lies on the unit circle.
:::

<1>5. Q.E.D.
::: {.proof}
<1>1 and <1>4 give $f = hg = e^{i\theta} g$ on $\Omega$.
:::
:::

::: {.solution}
Define $F(z) \da {f(z) \over g(z)}$.

::: {.claim}
$F$ is holomorphic on $\Omega$.
:::

::: {.proof title="of claim"}
Note that $g(a) = 0$ iff $f(a) = 0$, so $F$ has no poles.
If $F$ has a singularity at $z_0$, noting that $\abs{F(z_0)} = 1$, $F$ is bounded in a neighborhood of $z_0$ and thus the singularity must be removable.
By Riemann's removable singularity theorem, $F$ extends to a holomorphic function.
:::

Given this, note that $\abs{F(z)} = 1$ for all $z$, so $F(\Omega) \subseteq S^1$, which is codimension 1 in $\CC$ and not open.
By the open mapping theorem, $F$ must be constant, so $F(z) = \lambda$, and in particular since $\abs{F(z)} = 1$, $\lambda = e^{it}\in S^1$ for some $t$.
Then $f(z) = \lambda g(z)$.
:::
