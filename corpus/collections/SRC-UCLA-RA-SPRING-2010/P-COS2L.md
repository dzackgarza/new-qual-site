---
schema: qual/card@1
id: P-COS2L
kind: problem
title: Dimension and a basis of harmonic functions modulo real parts of analytic functions
  on $\mathbb{C}\setminus\{p_1,\dots,p_n\}$
classification:
  areas:
  - real-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $p_1,\dots,p_n$ be distinct points in $\mathbb{C}$ and let $U$ be the domain $\mathbb{C}\setminus\{p_1,\dots,p_n\}$.
Let $A$ be the vector space of real harmonic functions on $U$ and let $B\subseteq A$ be the subspace of real parts of complex analytic functions on $U$.
Find the dimension of the quotient space $A/B$ and give a basis.
:::

::: {.solution}
**Goal:** Let $U = \CC \setminus \{p_1, \dots, p_n\}$, let $A$ be the real harmonic functions on $U$, and $B \subseteq A$ the real parts of complex analytic functions on $U$.
Find $\dim(A/B)$ and a basis.

::: pf

::: {.pf-step #s1}

Characterize $B$: a real harmonic $u \in A$ lies in $B$ iff the closed form $*du = -u_y\, dx + u_x\, dy$ is exact on $U$.

::: pf-proof

::: pf-step

If $u = \Re F$ with $F$ analytic on $U$, then $*du$ is exact.

::: pf-proof

locally $F = u + iv$ with $v$ a harmonic conjugate, and $*du = dv$; since $F$ is single-valued on $U$, $v$ is single-valued on $U$, so $dv$ is exact.

:::

:::

::: pf-step

If $*du$ is exact, then $u \in B$.

::: pf-proof

write $*du = dv$ with $v \in C^\infty(U)$; then $F = u + iv$ satisfies the Cauchy--Riemann equations (as $dv = *du$), so $F$ is analytic on $U$ and $u = \Re F$.

:::

:::

:::

:::

::: {.pf-step #s2}

The period map $\omega: A \to \RR^n$, $\omega(u) = \qty{\oint_{\gamma_k} *du}_{k=1}^{n}$, where $\gamma_k$ is a small positively oriented circle around $p_k$, is well defined and linear.

::: pf-proof

each $*du$ is closed on $U$ (harmonicity: $d(*du) = \Delta u\, dx\wedge dy = 0$), so the integral around $\gamma_k$ depends only on the homology class of $\gamma_k$; the $\gamma_k$'s generate $H_1(U; \RR) \cong \RR^n$.

:::

:::

::: {.pf-step #s3}

$\ker \omega = B$.

::: pf-proof

$u \in B$ iff $*du$ is exact (step [](#s1){.pf-ref}) iff all its periods vanish (step [](#s2){.pf-ref}), i.e. $\omega(u) = 0$.

:::

:::

::: {.pf-step #s4}

$\omega$ is surjective.

::: pf-proof

for $u_k(z) = \log|z - p_k| \in A$, the conjugate is $\arg(z - p_k)$ locally, so $\oint_{\gamma_j} *du_k = 2\pi \delta_{jk}$: the images of $u_1, \dots, u_n$ form the basis $\{2\pi e_k\}$ of $\RR^n$.

:::

:::

::: {.pf-step #s5}

$A/B \cong \RR^n$, so $\dim(A/B) = n$ with basis $\qty{[\log|z - p_1|], \dots, [\log|z - p_n|]}$.

::: pf-proof

by the first isomorphism theorem, $A/B \cong \operatorname{im}\omega = \RR^n$ (steps [](#s3){.pf-ref} and [](#s4){.pf-ref}); step [](#s4){.pf-ref} shows the listed classes are linearly independent and span.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} answers the question.

:::

:::

:::
