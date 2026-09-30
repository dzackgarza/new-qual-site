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

::: {.problem}
Let $f$ and $g$ be non-zero analytic functions on a region $\Omega$.
Assume $|f(z)| = |g(z)|$ for all $z$ in $\Omega$.
Show that $f(z) = e^{i \theta} g(z)$ in $\Omega$ for some $0 \leq \theta < 2 \pi$.
:::

::: {.solution}
**Goal:** Prove that if $f, g$ are nonzero analytic functions on a region $\Omega$ with $\abs{f(z)} = \abs{g(z)}$ for all $z \in \Omega$, then $f(z) = e^{i\theta} g(z)$ for some $0 \leq \theta < 2\pi$.

::: pf

::: {.pf-step #define-h}
Define $h := f / g$; then $h$ is analytic and never vanishes on $\Omega$.

::: pf-proof
$g \neq 0$ on $\Omega$ by hypothesis, and quotients of analytic functions are analytic.
:::

:::

::: {.pf-step #h-modulus-one}
$\abs{h(z)} = 1$ for all $z \in \Omega$.

::: pf-proof
$\abs h = \abs f / \abs g = 1$ by hypothesis.
:::

:::

::: {.pf-step #h-constant}
$h$ is constant.

::: pf-proof

::: {.pf-step #h-image-in-circle}
$h(\Omega)$ is contained in the unit circle $S^1$.

::: pf-proof
Step [](#h-modulus-one){.pf-ref}.
:::

:::

::: {.pf-step #image-open-if-nonconstant}
$h(\Omega)$ is open in $\CC$ if $h$ is nonconstant.

::: pf-proof
Open mapping theorem: a nonconstant holomorphic map on a region is open.
:::

:::

::: {.pf-step #circle-empty-interior}
$S^1$ has empty interior in $\CC$.

::: pf-proof
The unit circle contains no open disk.
:::

:::

::: pf-step
Hence $h$ is constant.

::: pf-proof
Steps [](#h-image-in-circle){.pf-ref}, [](#image-open-if-nonconstant){.pf-ref} and [](#circle-empty-interior){.pf-ref}: a nonconstant $h$ would map $\Omega$ onto an open set inside $S^1$, impossible.
:::

:::

:::

:::

::: {.pf-step #h-equals-unimodular}
$h \equiv e^{i\theta}$ for some $0 \leq \theta < 2\pi$.

::: pf-proof
Step [](#h-constant){.pf-ref} and $\abs h \equiv 1$ (step [](#h-modulus-one){.pf-ref}): the constant value lies on the unit circle.
:::

:::

::: pf-qed
Steps [](#define-h){.pf-ref} and [](#h-equals-unimodular){.pf-ref} give $f = hg = e^{i\theta} g$ on $\Omega$.
:::

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
