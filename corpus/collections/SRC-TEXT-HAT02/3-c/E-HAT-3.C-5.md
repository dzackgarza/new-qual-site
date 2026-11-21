---
schema: qual/card@1
id: E-HAT-3.C-5
kind: problem
title: Fundamental group of an H-space is abelian
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 5; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof: the Eckmann--Hilton argument in the form the exercise asks for. Concatenation
    $*$ and the pointwise product $\odot$ are compared through the unit homotopies, which gives
    $[f*g]=[f\odot g]$ by gluing the two half-interval computations, and then $[g*f]=[f\odot g]$ by
    the same computation with the other pair of unit homotopies; hence $[f*g]=[g*f]$. The
    half-interval identities used are $(f*c_e)(t)=f(2t)$ and $(c_e*g)(t)=g(2t-1)$ on the two
    halves, which are checked.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Published source located and compared: Steven V. Sam, Solutions to Algebraic Topology (2008),
    SS3.C Exercise 5, printed p.16 — the same two-orderings argument, written with the pointwise
    product and concatenation in the opposite notation. The card's steps s2 and s3 are that
    argument, so the card now cites it; no step of the proof was changed.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 5 of §3.C, printed p. 291, and Sam, *Solutions to Algebraic
    Topology* (2008), §3.C Exercise 5, printed p. 16. The Eckmann--Hilton argument on the card was
    right and is kept: $f\odot g\simeq(f*c_e)\odot(c_e*g)\simeq f*g$ by the two unit homotopies
    read on the two halves of the interval, and $f\odot g\simeq(c_e*f)\odot(g*c_e)\simeq g*f$
    with the roles exchanged, so $[f][g]=[g][f]$. Rewritten: the card was a nest of `pf` blocks
    reopened inside one another with proofs that were noun phrases ('definition of an H-space',
    'setup', 'homotopy invariance') and it closed with a 'Conclusion' step proved by naming two
    labels, which STYLE-08 forbids. Three steps now, the first two carrying the half-interval
    computations and the third the conclusion. Not claimed: a certificate.
---

::: {.problem}
Show that if $(X, e)$ is an H-space then $\pi_1(X, e)$ is abelian.
[Compare the usual composition $f \cdot g$ of loops with the product $\mu(f(t), g(t))$ coming from the H-space multiplication $\mu$.]
:::

::: {.solution}
Let $(X,e,\mu)$ be an H-space, so $\mu\colon X\times X\to X$ and the maps $x\mapsto\mu(x,e)$, $x\mapsto\mu(e,x)$ are homotopic to the identity through homotopies fixing $e$ (printed p.~281). For based loops $f,g$ at $e$ put
$$
(f*g)(t)=\begin{cases}f(2t),&0\le t\le\tfrac12,\\ g(2t-1),&\tfrac12\le t\le1,\end{cases}
\qquad
(f\odot g)(t)=\mu\bigl(f(t),g(t)\bigr),
$$
so that $[f][g]=[f*g]$ in $\pi_1(X,e)$ and $f\odot g$ is the pointwise product the exercise names. This is the argument of Steven V. Sam, *Solutions to Algebraic Topology* (2008), §3.C Exercise 5, printed p.~16, written out on the two halves of the interval.

::: pf

::: {.pf-step #s1}

$[f\odot g]=[f*g]$.

::: pf-proof

Replacing $f$ by the homotopic loop $f*c_e$ and $g$ by $c_e*g$, where $c_e$ is the constant loop, gives $f\odot g\simeq(f*c_e)\odot(c_e*g)$ because $\mu$ is continuous. On $[0,\tfrac12]$ one has $(f*c_e)(t)=f(2t)$ and $(c_e*g)(t)=e$, so $(f*c_e)\odot(c_e*g)(t)=\mu(f(2t),e)\simeq f(2t)=(f*g)(t)$; on $[\tfrac12,1]$ one has $(f*c_e)(t)=e$ and $(c_e*g)(t)=g(2t-1)$, so the value is $\mu(e,g(2t-1))\simeq g(2t-1)=(f*g)(t)$. The homotopies are the unit homotopies of the H-space structure, applied in each half and glued at $t=\tfrac12$, so $f\odot g\simeq f*g$ relative to endpoints.

:::

:::

::: {.pf-step #s2}

$[f\odot g]=[g*f]$.

::: pf-proof

This time replace $f$ by $c_e*f$ and $g$ by $g*c_e$. On $[0,\tfrac12]$ the value of $(c_e*f)\odot(g*c_e)$ is $\mu\bigl(e,g(2t)\bigr)\simeq g(2t)=(g*f)(t)$; on $[\tfrac12,1]$ it is $\mu\bigl(f(2t-1),e\bigr)\simeq f(2t-1)=(g*f)(t)$. Gluing the two halves gives $f\odot g\simeq g*f$ relative to endpoints.

:::

:::

::: {.pf-step #s3}

$\pi_1(X,e)$ is abelian.

::: pf-proof

For classes $[f],[g]$ the two steps give
$$
[f][g]=[f*g]=[f\odot g]=[g*f]=[g][f],
$$
using that $[f][g]=[f*g]$ by definition of the group structure on $\pi_1$ and that $\odot$ depends only on the homotopy classes of $f$ and $g$ because $\mu$ is continuous. Hence every pair of elements of $\pi_1(X,e)$ commutes.

:::

:::

:::
:::
