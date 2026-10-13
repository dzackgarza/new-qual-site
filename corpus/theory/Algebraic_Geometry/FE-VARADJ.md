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

::: {.example title="Hypersurface canonical classes"}
Let $H$ be the hyperplane class on $\PP^n$. Since $K_{\PP^n}\sim-(n+1)H$, the anticanonical class is $(n+1)H$ and is ample; hence $\PP^n$ is Fano.

Let $n\geq2$ and let $D\subseteq\PP^n$ be a smooth hypersurface of degree $d$. Adjunction gives
$$
K_D\sim\restrictionof{(K_{\PP^n}+D)}{D}\sim(d-n-1)\restrictionof{H}{D}.
$$
Consequently, $D$ is Fano for $d<n+1$, is Calabi--Yau in the weak $K$-trivial convention for $d=n+1$, and is of general type for $d>n+1$.
:::

::: {.remark}
The smooth quadric surface in $\PP^3$ is del Pezzo and is isomorphic to $\PP^1\times\PP^1$. A smooth quartic surface in $\PP^3$ is a K3 surface, and a smooth quintic threefold in $\PP^4$ has trivial canonical bundle.
For $n = 2$ the same computation is the plane-curve genus formula $g = \binom{d-1}{2}$, with $d \leq 2$ rational, $d = 3$ elliptic, $d \geq 4$ general type.

When $d=n+1$, the exact sequence
$$
0\to\OO_{\PP^n}(-n-1)\to\OO_{\PP^n}\to\OO_D\to0
$$
and the cohomology of line bundles on $\PP^n$ give $H^j(D,\OO_D)=0$ for $1\leq j\leq n-2$. Together with $\omega_D\cong\OO_D$ from adjunction, this also satisfies the stricter Calabi--Yau convention on [[D-VARFANO]].
:::
