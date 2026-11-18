---
schema: qual/card@1
id: E-HAT-4.K-4
kind: problem
title: $SP_2(S^1)$ is a Möbius band
classification:
  areas:
  - topology
  topics:
  - Symmetric Products
  - Quasifibrations
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.K, Exercise 4 and the corrected current statement of Lemma 4K.3 where relevant; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the identification, which is what Queue D asks for on this card. The chord model, the (theta, s) coordinates with their identification and the interval-bundle model are separate steps, and the comparison with Example 4K.5 is the last. The prose's claim that the quotient "is the standard interval-bundle model of the Mobius band" is now a step that names the bundle and its monodromy, and the mapping-cone comparison says what the attaching map is for n = 1. No retained set covers this exercise; the card now says so. Locators checked: Example 4K.5 on printed p. 482, the exercise on printed p. 486. No statement repair.
---

::: {.problem}
Show that $SP_2(S^1)$ is a Möbius band, and that this is consistent with the description of $SP_2(S^n)$ as a mapping cone given in Example 4K.5.
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout hold nothing from §4.K. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.K Exercise 4, printed p. 486, and it refers to Example 4K.5 on printed p. 482.

::: pf

::: {.pf-step #chords}
$SP_2(S^1)$ is the space of unordered pairs of points of $S^1\subset\CC$, and $\{z,w\}\mapsto[z,w]$ identifies it with the space of unoriented chords of the circle, degenerate chords $z=w$ included.

::: pf-proof
The quotient map $(S^1\times S^1)/\Sigma_2\to SP_2(S^1)$ is a bijection, and a chord determines its unordered pair of endpoints and conversely; a degenerate chord is a single point counted twice, which is the diagonal.
:::

:::

::: {.pf-step #coordinates}
A nondegenerate chord is determined by the angle $\theta$ of a unit normal to it and its signed distance $s\in(-1,1)$ from the origin, with $(\theta,s)$ and $(\theta+\pi,-s)$ giving the same chord, and the degenerate chords are $s=\pm1$.

::: pf-proof
A chord is a line segment cut out of $S^1$ by a line, and a line at distance $\abs{s}\le1$ from the origin with unit normal direction $\theta$ is $\{x:\langle x,u_\theta\rangle=s\}$; the pair $(\theta,s)$ and $(\theta+\pi,-s)$ describe the same line, and no other pair does. Distance $1$ means tangency at a single point, so $\abs{s}=1$ is the degenerate case.
:::

:::

::: {.pf-step #mobius}
$SP_2(S^1)\cong(S^1\times[-1,1])\big/\bigl((\theta,s)\sim(\theta+\pi,-s)\bigr)$, which is the Möbius band, and its boundary is the diagonal copy of $S^1$.

::: pf-proof
The parametrization of step [](#coordinates){.pf-ref} is continuous in both directions and passes to the quotient by the involution $(\theta,s)\mapsto(\theta+\pi,-s)$, which acts on the interval factor by reflection and on the circle factor by a half-turn, so the quotient is the total space of the interval bundle over $S^1=\RR/\pi\ZZ$ with monodromy $s\mapsto-s$, the standard model of the Möbius band. Its boundary is $s=\pm1$, which by step [](#coordinates){.pf-ref} is the set of degenerate chords, the diagonal $S^1$.
:::

:::

::: {.pf-step #example}
This agrees with the mapping-cone description of $SP_2(S^n)$ in Example 4K.5.

::: pf-proof
In Example 4K.5, printed p. 482, $SP_2(S^n)$ is the mapping cone of the map $S^n\to S^n/\RP^{n-1}$ written there as attaching the cone on $S^n\RP^{n-1}$ — the $n$-fold unreduced suspension of $\RP^{n-1}$ — to the diagonal $S^n$ along the identification induced by interchanging the two points. For $n=1$ the space $\RP^{0}$ is a point, so its unreduced suspension is an interval, and the map identifies the two endpoints, giving the interval bundle over $S^1$ with monodromy $-1$; the mapping cone of a map from the two endpoints of an interval onto $S^1$ is obtained by gluing a strip to the circle with a half-twist, which is exactly the Möbius band of step [](#mobius){.pf-ref}. So the two descriptions coincide, which is the consistency the exercise asks for.
:::

:::

:::
:::
