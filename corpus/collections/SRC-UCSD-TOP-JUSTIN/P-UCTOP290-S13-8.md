---
schema: qual/card@1
id: P-UCTOP290-S13-8
kind: problem
title: A simply connected closed three-manifold is a homology sphere
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Homology
  - Poincaré Duality
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 13, Problem 8 in its checked-in extraction.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 13, problem 8
    (assets/attachments/UCSD_290_F14_sheet13.pdf, printed page 389), from the
    checked-in extraction and a 300 dpi render. The printed problem asks to show
    that any closed 1-connected, meaning path-connected and simply-connected,
    3-manifold is a homology sphere, that is it has the same homology groups as
    the 3-sphere. The card states this, so no repair was needed.
---

::: {.problem}
Show that a closed connected simply connected $3$-manifold
has the same integral homology groups as $S^3$.
:::

::: {.solution}

Let $M$ be a closed, path-connected and simply connected $3$-manifold.

::: pf

::: {.pf-step #low}

$H_0(M;\ZZ)=\ZZ$ and $H_1(M;\ZZ)=0$.

::: pf-proof

$M$ is path-connected, so $H_0=\ZZ$. The Hurewicz theorem in degree one
identifies $H_1(M;\ZZ)$ with the abelianisation of $\pi_1(M)$, which is
trivial because $M$ is simply connected.

:::

:::

::: {.pf-step #orientable}

$M$ is orientable.

::: pf-proof

The orientation character is a homomorphism $\pi_1(M)\to\ZZ/2$ recording
whether a loop reverses orientation, and it is trivial because $\pi_1(M)$ is
trivial; a closed connected manifold with trivial orientation character is
orientable.

:::

:::

::: {.pf-step #duality}

$H_3(M;\ZZ)\cong\ZZ$ and $H_2(M;\ZZ)=0$.

::: pf-proof

$M$ is a closed connected orientable $3$-manifold, so Poincaré duality gives
$H_3(M;\ZZ)\cong H^0(M;\ZZ)=\ZZ$ and $H_2(M;\ZZ)\cong H^1(M;\ZZ)$. The
universal coefficient theorem gives the exact sequence
$0\to\Ext(H_0(M),\ZZ)\to H^1(M;\ZZ)\to\Hom(H_1(M),\ZZ)\to0$, and both ends
vanish: $\Hom(0,\ZZ)=0$, and $\Ext(\ZZ,\ZZ)=0$ because $\ZZ$ is free. So
$H^1(M;\ZZ)=0$ and $H_2(M;\ZZ)=0$.

:::

:::

::: {.pf-step #sphere}

$H_k(M;\ZZ)$ equals $\ZZ$ for $k=0,3$ and $0$ otherwise, which is the homology
of $S^3$.

::: pf-proof

Steps [](#low){.pf-ref}, [](#orientable){.pf-ref} and [](#duality){.pf-ref}
settle degrees $0$ through $3$; a $3$-manifold has no homology above degree
$3$. The sphere has $H_0=H_3=\ZZ$ and $H_1=H_2=0$ by the same duality
computation, or by its cell structure with one cell in dimensions $0$ and $3$.
So $M$ is a homology sphere, and nothing here used more than simple
connectivity.

:::

:::

:::


:::
