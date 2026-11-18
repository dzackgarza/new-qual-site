---
schema: qual/card@1
id: P-PBXAK
kind: problem
title: Maximum principle for harmonic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Harmonic Functions
  - Open Mapping Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The local harmonic conjugate is now constructed (the closed 1-form -u_y dx + u_x dy is exact on a disc because its curl vanishes by harmonicity), which the prose simply assumed; the open-mapping step is spelled out (an open set cannot lie in a closed half-plane containing a point of its boundary); and the passage from "u constant on the disc" to "u constant on the region" now names both the holomorphic function u_x - i u_y and the identity theorem. Part (b) is proved with the max/min argument rather than from |u| directly, and the constant case is the separate line the prose mentioned without writing. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Prove the maximum principle for harmonic functions:

(a) If $u$ is a non-constant real-valued harmonic function in a region $\Omega$, then $u$ can not attain a maximum or a minimum in $\Omega$.

(b) Suppose $\Omega$ is a region with compact closure $\bar \Omega$.
If $u$ is harmonic in $\Omega$ and continuous in $\bar \Omega$, then $$ \sup _{z \in \Omega}\abs{u(z)} \leq \sup _{z \in \bar \Omega -\Omega}\abs{u(z)} .$$

> Hint: to prove (a), assume $u$ attains a local maximum at $z_0$.
> Let $f$ be holomorphic near $z_0$ with $\Re(f) = u$, and show that $f$ is not an open map.
> Then (a) implies (b).
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own, following the hint.

::: pf

::: {.pf-step #conj}
Near a point of a region there is a local harmonic conjugate: for $z_0\in\Omega$ there is a disc $D\Subset\Omega$ about $z_0$ and a real harmonic $v$ on $D$ with $F=u+iv$ holomorphic on $D$.

::: pf-proof
$D$ is a disc, hence simply connected, so the closed $1$-form $-u_y\,dx+u_x\,dy$ on $D$ is exact: its coefficients are $C^1$ on $D$ and its curl is $-u_{yy}-u_{xx}=0$ since $u$ is harmonic. A primitive $v$ satisfies $v_x=-u_y$, $v_y=u_x$, which are the Cauchy-Riemann equations for $u+iv$.
:::

:::

::: {.pf-step #noextremum}
A nonconstant harmonic $u$ on a region $\Omega$ has no local maximum and no local minimum in $\Omega$.

::: pf-proof
Suppose $u$ has a local maximum at $z_0\in\Omega$; take $D$ as in step [](#conj){.pf-ref}, shrunk so that $u\le u(z_0)$ on $D$. Then $F(D)\subseteq\{w:\operatorname{Re}w\le u(z_0)\}$ while $F(z_0)=u(z_0)+iv(z_0)$ lies on the boundary line of that half-plane; since $F(D)$ is open when $F$ is nonconstant (open mapping theorem) it cannot be contained in a closed half-plane with a point of its boundary, so $F$ is constant on $D$. Hence $u$ is constant on $D$. Now $G=u_x-iu_y$ is holomorphic on $\Omega$ (the Cauchy-Riemann equations for $u_x$ and $-u_y$ hold because $u$ is harmonic) and $G=F'\equiv0$ on $D$; by the identity theorem on the connected $\Omega$, $G\equiv0$ and $u$ is constant on $\Omega$, contrary to hypothesis. Applying the same argument to the harmonic function $-u$ excludes an interior local minimum.
:::

:::

::: {.pf-step #boundary}
If $\Omega$ is a region with compact closure, $u$ is harmonic on $\Omega$ and continuous on $\overline\Omega$, then $\sup_{z\in\Omega}\abs{u(z)}\le\sup_{z\in\overline\Omega\setminus\Omega}\abs{u(z)}$.

::: pf-proof
$\overline\Omega$ is compact and $u$ is continuous there, so $u$ attains a maximum and a minimum on $\overline\Omega$. If $u$ is nonconstant on $\Omega$, step [](#noextremum){.pf-ref} shows that neither is attained in the open set $\Omega$, so both are attained on $\partial\Omega=\overline\Omega\setminus\Omega$; then for every $z\in\Omega$,
$$
\abs{u(z)}\le\max\Bigl(\max_{\overline\Omega}u,\ -\min_{\overline\Omega}u\Bigr)\le\sup_{\partial\Omega}\abs u .
$$
If $u$ is constant, say $u\equiv c$ on $\Omega$, then by continuity $u\equiv c$ on $\overline\Omega$ and both sides equal $\abs c$.
:::

:::

:::
:::
