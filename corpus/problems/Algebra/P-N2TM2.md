---
schema: qual/card@1
id: P-N2TM2
kind: problem
title: Orbits, stabilizers, and kernels of the standard $G$-actions
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Conjugacy
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source leaves G undeclared; the statement declares G as a group.
---

::: {.problem}
Let $G$ be a group. For each standard action below, identify the orbits, stabilizers, global fixed points, kernel, and image in the relevant symmetric group:

(1) left translation of $G$ on itself;

(2) conjugation of $G$ on itself;

(3) conjugation of $G$ on its set of subgroups;

(4) left translation of $G$ on $G/H$ for a fixed subgroup $H\le G$.
:::

::: {.solution}
For an action of $G$ on a set $X$, the kernel is the set of $g$ acting as the identity on $X$, and the image in $\Sym(X)$ is isomorphic to $G$ modulo the kernel.

::: pf

::: pf-step
(1) Left translation on $G$ has the single orbit $G$, trivial stabilizers and trivial kernel, and its image is the left regular copy of $G$ in $\Sym(G)$; it has no global fixed point unless $G=1$.

::: pf-proof
For $x,y\in G$, $(yx^{-1})x=y$, so the action is transitive.
$gx=x$ holds only for $g=e$, so every stabilizer, and hence the kernel, is trivial.
A global fixed point $x$ would have stabilizer $G$, so $G=1$.
:::

:::

::: pf-step
(2) Conjugation on $G$ has the conjugacy classes as orbits and the centralizers $C_G(x)$ as stabilizers; its global fixed points and its kernel are both $Z(G)$, and its image is $\Inn(G)\cong G/Z(G)$.

::: pf-proof
The orbit of $x$ is $\{gxg^{-1}:g\in G\}$, and $gxg^{-1}=x$ exactly when $g\in C_G(x)$.
An element $x$ is fixed by every $g$ exactly when $x\in Z(G)$, and $g$ fixes every $x$ exactly when $g\in Z(G)$.
The image consists of the inner automorphisms.
:::

:::

::: pf-step
(3) Conjugation on subgroups has orbits the conjugacy classes $\{gHg^{-1}:g\in G\}$ and stabilizers the normalizers $N_G(H)$; its global fixed points are the normal subgroups, its kernel is $\bigcap_{H\le G}N_G(H)$, and its image is $G$ modulo that kernel.

::: pf-proof
$gHg^{-1}=H$ exactly when $g\in N_G(H)$, so this is the stabilizer; a subgroup fixed by every $g$ is normal; and $g$ fixes every subgroup exactly when it lies in every normalizer.
:::

:::

::: pf-step
(4) Left translation on $G/H$ is transitive, with stabilizer $xHx^{-1}$ at $xH$; its kernel is the core $\bigcap_{x\in G}xHx^{-1}$, the largest normal subgroup of $G$ contained in $H$, and its image is $G$ modulo the core; there is a global fixed coset only when $H=G$.

::: pf-proof
$(yx^{-1})xH=yH$, so the action is transitive.
$gxH=xH$ exactly when $x^{-1}gx\in H$, that is, $g\in xHx^{-1}$.
The kernel is the intersection of the stabilizers; it is normal, and any normal subgroup $N\subseteq H$ satisfies $N=xNx^{-1}\subseteq xHx^{-1}$ for every $x$.
A global fixed coset has stabilizer $G$, so $xHx^{-1}=G$ and $H=G$.
:::

:::

:::

:::
