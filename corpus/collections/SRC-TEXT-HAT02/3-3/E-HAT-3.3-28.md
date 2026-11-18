---
schema: qual/card@1
id: E-HAT-3.3-28
kind: problem
title: Nondegeneracy on large subspaces
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-corrected
  by: claude
  date: 2026-10-31
  note: >-
    The card wrote `\nu` for the first vector of the pair; the book prints "all pairs of
    vectors v, w in a k dimensional subspace" (Hatcher §3.3 exercise 28).
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 28; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: nonsingularity makes $F^n\to V^*$ surjective, so $V^\perp$ has dimension
    $n-k$; vanishing on $V\times V$ means $V\subseteq V^\perp$, which forces $k\le n/2$.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained solution set is cited on the card and none was
    located for this exercise among the retained Hatcher sets, so the argument is the card's own.
    Checked against Hatcher, Section 3.3 Exercise 28, printed p. 259: the exercise assumes the
    pairing symmetric or skew-symmetric, but the proof uses only nonsingularity — the map
    $x\mapsto B(x,-)$ is an isomorphism onto the dual — so the symmetry hypothesis is unused and
    the result holds for any nonsingular bilinear pairing. Each step re-read: the restriction map
    to $V^*$ is onto by extending a functional from $V$ to $F^n$; its kernel is $V^\perp$; rank
    nullity gives $\dim V^\perp=n-k$; vanishing on $V\times V$ puts $V$ inside $V^\perp$, forcing
    $k\le n-k$. Nothing is claimed about the case $k\le n/2$, where the restriction can vanish.
---

::: {.problem}
Show that a nonsingular symmetric or skew-symmetric bilinear pairing over a field $F$, of the form $F^n \times F^n \to F$, cannot be identically zero when restricted to all pairs of vectors $v, w$ in a $k$-dimensional subspace $V \subset F^n$ if $k > n/2$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Hatcher, Algebraic Topology, Section 3.3 Exercise 28, printed p. 259, and uses only nonsingularity of the pairing, not its symmetry: the symmetry hypothesis of the exercise is not needed.

::: pf

::: {.pf-step #defs}
Let $B:F^n\times F^n\to F$ be the pairing and put $V^{\perp}=\{x\in F^n: B(x,v)=0 \text{ for every } v\in V\}$.

::: pf-proof
This is a definition; $V^{\perp}$ is a subspace because $B$ is linear in its first variable.
:::

:::

::: {.pf-step #dim}
$\dim V^{\perp}=n-k$.

:::: pf-proof

::: {.pf-step #surjective}
The map $\varphi:F^n\to V^{*}$, $\varphi(x)=B(x,-)\restrict_{V}$, is linear and surjective.

::: pf-proof
Linearity is linearity of $B$ in the first variable. For surjectivity, let $\lambda\in V^{*}$ and extend it to a linear functional $\Lambda\in(F^n)^{*}$ by choosing a basis of $V$ and completing it to a basis of $F^n$. Nonsingularity of $B$ says that $x\mapsto B(x,-)$ is an isomorphism $F^n\to(F^n)^{*}$: it is linear, and its kernel consists of the $x$ with $B(x,y)=0$ for all $y$, which is $0$. So there is $x$ with $B(x,-)=\Lambda$, and then $\varphi(x)=\Lambda\restrict_{V}=\lambda$.
:::

:::

::: {.pf-step #kernel}
$\ker\varphi=V^{\perp}$.

::: pf-proof
$\varphi(x)=0$ means $B(x,v)=0$ for every $v\in V$, which is the definition of $x\in V^{\perp}$.
:::

:::

::: {.pf-step}
$\dim V^{\perp}=n-k$.

::: pf-proof
Rank-nullity for $\varphi$ gives $\dim\ker\varphi=n-\dim V^{*}=n-k$, and steps [](#surjective){.pf-ref} and [](#kernel){.pf-ref} identify the kernel with $V^{\perp}$.
:::

:::

:::

:::

::: {.pf-step #vanish}
If $B$ vanishes on $V\times V$, then $V\subseteq V^{\perp}$ and $k\le n/2$.

::: pf-proof
Vanishing on $V\times V$ says $B(v,w)=0$ for all $v,w\in V$, so each $v\in V$ satisfies $B(v,w)=0$ for every $w\in V$, that is $v\in V^{\perp}$. Hence $V\subseteq V^{\perp}$, so $k=\dim V\le\dim V^{\perp}=n-k$ by step [](#dim){.pf-ref}, which rearranges to $k\le n/2$.
:::

:::

::: {.pf-step}
If $k>n/2$ then $B$ is not identically zero on pairs of vectors of $V$.

::: pf-proof
The contrapositive of step [](#vanish){.pf-ref} is that $k>n/2$ rules out the vanishing of $B$ on $V\times V$. This is the assertion of the exercise.
:::

:::

:::
:::
