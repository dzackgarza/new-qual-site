---
schema: qual/card@1
id: P-AMD-F7UPRCWM
kind: problem
title: $S^2$ is not homeomorphic to $S^3$
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The stored solution computed the homology of S^2 and S^3 and then concluded the result, but it
    never stated that homology distinguishes spaces: nothing in it connected the two computations to
    the non-existence of a homeomorphism, and the justification for the groups sat in a qed block
    instead of a step. The proof now separates the four moves: the CW structure on S^n with one 0-cell
    and one n-cell and the vanishing of its boundary maps, which gives the groups; the two
    computations for n = 2 and n = 3; the functoriality statement that a homeomorphism induces an
    isomorphism, with the two composites written out; and the conclusion that Z is not the trivial
    group, so no homeomorphism exists. Checked against the cellular chain complex of a CW structure
    with cells in degrees 0 and n and against the functoriality of singular homology. Not checked: no
    published solution of this problem was located or consulted, so the argument is the card's own;
    no printed page is cited because the course source is not retained in this checkout.
---

::: {.problem}
Show that $S^2 \not\cong S^3$.
:::

::: {.solution}

::: pf

::: {.pf-step #spheres}
For every $n\ge1$ the sphere $S^n$ has a CW structure with one $0$-cell and one $n$-cell, so $H_0(S^n;\ZZ)\cong\ZZ$, $H_n(S^n;\ZZ)\cong\ZZ$ for $n\ge1$, and $H_k(S^n;\ZZ)=0$ for all other $k$.

::: pf-proof
Let $e^0$ be a point of $S^n$ and let $e^n=S^n\setminus\{e^0}$, with characteristic map $\Phi:D^n\to S^n$ the map that sends the interior of $D^n$ homeomorphically onto $e^n$ and the whole boundary sphere to $e^0$; this is a CW structure whose $n$-skeleton is already $S^n$, with $n\ge1$ so that $e^0$ is not an interior point of $e^n$. The cellular chain complex of this structure has $C_0\cong\ZZ$, $C_n\cong\ZZ$ and $C_k=0$ for every other $k$, and every boundary map is zero: from $d_1$ because $C_{-1}$ does not occur and $C_1=0$ for $n\ge2$, from $d_n$ because $C_{n-1}=0$, and from $d_k$ for the remaining $k$ because the source or the target is $0$. Hence $H_k$ is the chain group itself in degrees $0$ and $n$, and $0$ otherwise.
:::

:::

::: {.pf-step #two-three}
$H_2(S^2;\ZZ)\cong\ZZ$ and $H_2(S^3;\ZZ)=0$.

::: pf-proof
Apply step [](#spheres){.pf-ref} with $n=2$: degree $2$ is neither $0$ nor $3$, so $H_2(S^2)\cong\ZZ$. Apply it with $n=3$: degree $2$ is neither $0$ nor $3$, so $H_2(S^3)=0$.
:::

:::

::: {.pf-step #invariance}
A homeomorphism $f:X\to Y$ induces an isomorphism $f_*:H_2(X;\ZZ)\to H_2(Y;\ZZ)$.

::: pf-proof
Homology is a functor: a continuous map induces a homomorphism, and composition is carried to composition, $(g\circ f)_*=g_*\circ f_*$, with $(\mathrm{id}_X)_*=(\mathrm{id}_{H_2(X)})$. If $f$ is a homeomorphism with inverse $h$, then $h_*\circ f_*=(h\circ f)_*=(\mathrm{id}_X)_*\mathrm{id}$ and $f_*\circ h_*=(f\circ h)_*=(\mathrm{id}_Y)_*\mathrm{id}$, so $f_*$ is an isomorphism with inverse $h_*$.
:::

:::

::: {.pf-step #not-homeomorphic}
$S^2$ is not homeomorphic to $S^3$.

::: pf-proof
If $f:S^2\to S^3$ were a homeomorphism, step [](#invariance){.pf-ref} would make $H_2(S^2;\ZZ)$ isomorphic to $H_2(S^3;\ZZ)$, that is $\ZZ$ isomorphic to the trivial group by step [](#two-three){.pf-ref}. No such isomorphism exists: the image of $1\in\ZZ$ would have to be the identity element $0$, and injectivity would then force $1=0$.
:::

:::

::: pf-qed
Steps [](#two-three){.pf-ref} and [](#invariance){.pf-ref} give the two homology groups and their invariance, and step [](#not-homeomorphic){.pf-ref} draws the conclusion.
:::

:::
:::
