---
schema: qual/card@1
id: P-COS2L
kind: problem
title: Let $p_1,\dots,p_n$ be distinct points in $\mathbb{C}$ and let $U$ be…
classification:
  areas:
  - real-analysis
  topics:
  - harmonic-functions
relations: []
review: draft
---

::: {.problem title="?"}
Let $p_1,\dots,p_n$ be distinct points in $\mathbb{C}$ and let $U$ be the domain $\mathbb{C}\setminus\{p_1,\dots,p_n\}$.
Let $A$ be the vector space of real harmonic functions on $U$ and let $B\subseteq A$ be the subspace of real parts of complex analytic functions on $U$.
Find the dimension of the quotient space $A/B$ and give a basis.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $U = \CC \setminus \{p_1, \dots, p_n\}$, let $A$ be the real harmonic functions on $U$, and $B \subseteq A$ the real parts of complex analytic functions on $U$. Find $\dim(A/B)$ and a basis.

<1>1. Characterize $B$: a real harmonic $u \in A$ lies in $B$ iff the closed form $*du = -u_y\, dx + u_x\, dy$ is exact on $U$.
<2>1. If $u = \Re F$ with $F$ analytic on $U$, then $*du$ is exact.
    Proof: locally $F = u + iv$ with $v$ a harmonic conjugate, and $*du = dv$; since $F$ is single-valued on $U$, $v$ is single-valued on $U$, so $dv$ is exact.
<2>2. If $*du$ is exact, then $u \in B$.
    Proof: write $*du = dv$ with $v \in C^\infty(U)$; then $F = u + iv$ satisfies the Cauchy--Riemann equations (as $dv = *du$), so $F$ is analytic on $U$ and $u = \Re F$.

<1>2. The period map $\omega: A \to \RR^n$, $\omega(u) = \qty{\oint_{\gamma_k} *du}_{k=1}^{n}$, where $\gamma_k$ is a small positively oriented circle around $p_k$, is well defined and linear.
    Proof: each $*du$ is closed on $U$ (harmonicity: $d(*du) = \Delta u\, dx\wedge dy = 0$), so the integral around $\gamma_k$ depends only on the homology class of $\gamma_k$; the $\gamma_k$'s generate $H_1(U; \RR) \cong \RR^n$.

<1>3. $\ker \omega = B$.
    Proof: $u \in B$ iff $*du$ is exact (<1>1) iff all its periods vanish (<1>2), i.e. $\omega(u) = 0$.

<1>4. $\omega$ is surjective.
    Proof: for $u_k(z) = \log|z - p_k| \in A$, the conjugate is $\arg(z - p_k)$ locally, so $\oint_{\gamma_j} *du_k = 2\pi \delta_{jk}$: the images of $u_1, \dots, u_n$ form the basis $\{2\pi e_k\}$ of $\RR^n$.

<1>5. $A/B \cong \RR^n$, so $\dim(A/B) = n$ with basis $\qty{[\log|z - p_1|], \dots, [\log|z - p_n|]}$.
    Proof: by the first isomorphism theorem, $A/B \cong \operatorname{im}\omega = \RR^n$ (<1>3, <1>4); <1>4 shows the listed classes are linearly independent and span.

<1>6. Q.E.D.
    Proof: <1>5 answers the question.
:::
