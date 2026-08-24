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
---

::: problem
Let $f$ and $g$ be non-zero analytic functions on a region $\Omega$.
Assume $|f(z)| = |g(z)|$ for all $z$ in $\Omega$.
Show that $f(z) = e^{i \theta} g(z)$ in $\Omega$ for some $0 \leq \theta < 2 \pi$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that if $f, g$ are nonzero analytic functions on a region $\Omega$ with $\abs{f(z)} = \abs{g(z)}$ for all $z \in \Omega$, then $f(z) = e^{i\theta} g(z)$ for some $0 \leq \theta < 2\pi$.

<1>1. Define $h := f / g$; then $h$ is analytic and never vanishes on $\Omega$.
Proof: $g \neq 0$ on $\Omega$ by hypothesis, and quotients of analytic functions are analytic.

<1>2. $\abs{h(z)} = 1$ for all $z \in \Omega$.
Proof: $\abs h = \abs f / \abs g = 1$ by hypothesis.

<1>3. $h$ is constant.
<2>1. $h(\Omega)$ is contained in the unit circle $S^1$.
Proof: <1>2. <2>2. $h(\Omega)$ is open in $\CC$ if $h$ is nonconstant.
Proof: Open mapping theorem: a nonconstant holomorphic map on a region is open.
<2>3. $S^1$ has empty interior in $\CC$.
Proof: The unit circle contains no open disk.
<2>4. Hence $h$ is constant.
Proof: <2>1--<2>3: a nonconstant $h$ would map $\Omega$ onto an open set inside $S^1$, impossible.

<1>4. $h \equiv e^{i\theta}$ for some $0 \leq \theta < 2\pi$.
Proof: <1>3 and $\abs h \equiv 1$ (<1>2): the constant value lies on the unit circle.

<1>5. Q.E.D. Proof: <1>1 and <1>4 give $f = hg = e^{i\theta} g$ on $\Omega$.
:::
