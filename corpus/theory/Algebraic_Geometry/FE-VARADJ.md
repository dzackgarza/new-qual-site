---
schema: qual/card@1
id: FE-VARADJ
kind: example
title: Hypersurfaces in $\PP^n$, classified by adjunction
classification:
  areas:
  - algebraic-geometry
  topics:
  - Adjunction Formula
  - Fano Varieties
  - Calabi-Yau Varieties
relations:
- kind: uses
  target: D-VARFANO
review: draft
prompts:
- Give several examples of Fano varieties.
- Give examples of Calabi--Yau varieties.
- Which hypersurfaces in $\PP^n$ are Fano, and which are Calabi--Yau?
---

::: {.example title="One computation, three answers"}
$K_{\PP^n} = -(n+1)H$, so $-K_{\PP^n} = \OO(n+1)$ is very ample and $\PP^n$ is Fano.
For $D \subseteq \PP^n$ a smooth hypersurface of degree $d$, adjunction gives
\[
K_D = \restrictionof{ (K_{\PP^n} + D) }{D} = \restrictionof{ \qty{ -(n+1)H + dH } }{D} = (d - n - 1) \restrictionof{H}{D} .
\]
So $D$ is Fano for $d < n+1$, Calabi--Yau for $d = n+1$, and of general type for $d > n+1$.
:::

::: {.remark}
This one line answers every request for examples in either class, which is why it is worth having rather than a list.
The quadric surface in $\PP^3$ is $d = 2 < 4$, hence del Pezzo, and indeed $\PP^1 \times \PP^1$; the quartic surface in $\PP^3$ is $d = 4 = n+1$, the K3 surface; the quintic threefold in $\PP^4$ is the Calabi--Yau of mirror symmetry.
For $n = 2$ the same computation is the plane-curve genus formula $g = \binom{d-1}{2}$, with $d \leq 2$ rational, $d = 3$ elliptic, $d \geq 4$ general type.

The vanishing $h^j(\OO_D) = 0$ demanded by the strict Calabi--Yau convention is not part of the adjunction computation; it comes from Lefschetz, which says the middle-dimension cohomology is the only new one.
:::
