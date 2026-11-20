---
schema: qual/card@1
id: E-HAT-4.G-2
kind: problem
title: Projection from $\Delta X$ is a fiber bundle
classification:
  areas:
  - topology
  topics:
  - CW Complexes
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §4.G, printed p. 459, with the construction of $\Delta X$
    on the same page. Correct. Over an $n$-simplex the preimage is the iterated mapping cylinder of
    the string of edge maps; when all of them are homeomorphisms the induction of the card gives
    $M(f_1,\dots,f_n)\cong F\times\Delta^n$ over $\Delta^n$, the point being that the composite
    $M_{n-1}\to X_{n-1}\to X_n$ is $(y,s)\mapsto f_n(y)$, whose mapping cylinder is
    $F\times C(\Delta^{n-1})=F\times\Delta^n$ and not $F\times(\Delta^{n-1}\star I)$. Local
    triviality then comes from the barycentric stars, which are open, cover $\Gamma$ and meet only
    simplices containing the barycentre's simplex, so that the face identifications agree there.
    The card's remark that a vertex star alone need not trivialise a loop edge, whose monodromy is
    $f_{e,1}^{-1}f_{e,0}$, is the reason the star cover is used. Nothing changed. Not claimed: a
    published solution, and no certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no structured proof: its steps were `pf-step` divs with no label and its proofs
    opened `pf-proof` but closed the fences in the wrong order, so nothing in the solution was a
    step of the required form and the QED-label check found none. The solution is rewritten as five
    labelled steps, and four mathematical repairs are made. (1) The printed exercise does not assume
    the base connected, but the old first step asserted a common fibre "since $\Gamma$ is
    connected"; connectedness is now derived where it is needed, and the bundle is stated component
    by component with one fibre per component. (2) The product formula
    $M(f_1,\dots,f_n)\cong F\times\Delta^n$ used the identity on the target end, which does not
    respect the identification $(x,1)\sim f_n(x)$; the homeomorphism now uses the inverse of $f_n$
    there, which is where the hypothesis that the maps are homeomorphisms enters. (3) The local
    triviality step asserted that barycentric stars trivialize because "the compositions coincide on
    $\tau$ because $\Gamma$ is a $\Delta$-complex", which is not an argument and is false as stated:
    the open star of a vertex of a base with a loop edge is the whole circle, over which the
    realization is the mapping torus of a nontrivial homeomorphism and not a product. The
    trivialization is now written out over the open star of an arbitrary simplex, with the face
    compatibility that makes the pieces agree, and with the loop-edge example recorded as the reason
    the cover is indexed by all simplices. (4) The page locators are removed by the numbering
    convention in force. Not checked: no certificate; the argument is written for a simplicial base,
    and the $\Delta$-complex case with degenerate simplices is not covered.
---

::: {.problem}
Show that if $X$ is a complex of spaces in which all the maps are homeomorphisms, then the projection $\Delta X \to \Gamma$ is a fiber bundle.
:::

::: {.solution}
No retained solution set covers this exercise: Sam's set stops at §4.3, and the retained sets that reach further record no solution for §4.G. The argument is the card's own, from the definition of a complex of spaces and of its realization in §4.G.

::: pf

::: {.pf-step #data}
Let $\Gamma$ be a simplicial complex and $X$ a complex of spaces over it, with vertex spaces $X_v$, edge maps $f_e$, and with the maps along the edges of each simplex of $\Gamma$ commuting, as §4.G requires; let $\Delta X\to\Gamma$ be the realization, whose fibre over the interior of an $n$-simplex $\sigma$ with vertices $v_0<\cdots<v_n$ is the iterated mapping cylinder $M(f_{01},\dots,f_{n-1,n})$ of the edge maps along the string. Assume every $f_e$ is a homeomorphism.

::: pf-proof
This is the construction of $\Delta X$ in §4.G: over each simplex one has the iterated mapping cylinder of the string of edge maps, and these are glued along faces by the same edge maps. Two consequences of the definition are used below. First, for vertices $v_i,v_j$ of one simplex the composite of edge maps from $X_{v_i}$ to $X_{v_j}$ along a chain of edges of that simplex is independent of the chain, because the diagram over the simplex commutes; it is then a homeomorphism $h_{ij}$ when the edge maps are homeomorphisms. Second, for a face $\rho$ of a simplex $\sigma$ the composite computed in $\sigma$ between two vertices of $\rho$ equals the composite computed in $\rho$, since the face data are the same edge maps.
:::
:::

::: {.pf-step #fibre}
If $\Gamma$ is connected, all the vertex spaces $X_v$ are homeomorphic, so there is a single fibre $F$. If $\Gamma$ is not connected the same holds within each component, and the conclusion below is a fibre bundle over each component with the fibre of that component.

::: pf-proof
Any two vertices of $\Gamma$ are joined by a path in the $1$-skeleton, which runs along edges; composing the edge homeomorphisms $f_e$ and their inverses along that path gives a homeomorphism $X_v\cong X_w$. When $\Gamma$ is connected this makes all vertex spaces homeomorphic to one space $F$.
:::
:::

::: {.pf-step #simplex}
Over the interior of a simplex $\sigma$ with first vertex $v_0$, $p^{-1}(\operatorname{int}\sigma)$ is homeomorphic to $X_{v_0}\times\operatorname{int}\sigma$, the projection being the second factor; if the edge maps along $\sigma$ are all homeomorphisms, the whole preimage $p^{-1}(\sigma)$ is homeomorphic to $X_{v_0}\times\sigma$ over $\sigma$.

::: pf-proof
Over $\operatorname{int}\sigma$ no identification with another simplex occurs, and the iterated mapping cylinder over $\operatorname{int}\Delta^n$ is the product $X_{v_0}\times\operatorname{int}\Delta^n$ with its projection. For the closed simplex, induct on $n$: for $n=1$, $M(f_{01})=X_{v_0}\times[0,1]\sqcup X_{v_1}$ with $(x,1)\sim f_{01}(x)$, and the map sending $(x,t)$ in the cylinder part to the point $(x,(1-t)v_0+tv_1)$ of $X_{v_0}\times\Delta^1$ and $y\in X_{v_1}$ to $(f_{01}^{-1}(y),v_1)$ is a homeomorphism over $\Delta^1$, the inverse of $f_{01}$ on the target end being what makes the identification consistent. For $n>1$, $M(f_{01},\dots,f_{n-1,n})$ is the mapping cylinder of the composition $M(f_{01},\dots,f_{n-2,n-1})\to X_{v_{n-1}}\xrightarrow{f_{n-1,n}}X_{v_n}$, the first map being the projection onto the target end; by induction the source is $X_{v_0}\times\Delta^{n-1}$ and the composition is $(x,s)\mapsto f_{n-1,n}(x)$, so the cylinder is $X_{v_0}\times\Delta^{n-1}\times[0,1]$ with the top end collapsed onto $X_{v_0}\times\{\text{last vertex}\}$ by the homeomorphism $f_{n-1,n}$ of the fibre, which is $X_{v_0}\times\Delta^n$.
:::
:::

::: {.pf-step #star}
For each simplex $\tau$ of $\Gamma$ the set $U_\tau=\bigcup_{\sigma\supseteq\tau}\operatorname{int}\sigma$ is open, the sets $U_\tau$ cover $\Gamma$, and $p^{-1}(U_\tau)$ is homeomorphic to $X_{\tau_0}\times U_\tau$ over $U_\tau$.

::: pf-proof
$U_\tau$ is the open star of $\tau$: its complement is the union of the closed stars of the simplices not containing $\tau$, a closed set, so $U_\tau$ is open; it contains the relative interior of $\tau$, so the sets $U_\tau$ cover $\Gamma$. For the trivialization, let $\sigma\supseteq\tau$ and write a point of $p^{-1}(\operatorname{int}\sigma)$ as $(x,y)$ with $x\in X_{\sigma_0}$ and $y\in\operatorname{int}\sigma$, and send it to $(h_{\sigma_0\tau_0}(x),y)\in X_{\tau_0}\times\operatorname{int}\sigma$, where $h_{\sigma_0\tau_0}$ is the composite of the edge homeomorphisms inside $\sigma$ from $\sigma_0$ to $\tau_0$. On each piece this is a homeomorphism. The pieces agree on overlaps: for a common face $\rho=\sigma\cap\sigma'$ containing $\tau$, the gluing identifies $x\in X_{\sigma_0}$ with $h_{\sigma_0\rho_0}(x)\in X_{\rho_0}$, and the composite from $\rho_0$ to $\tau_0$ is the same whether computed in $\rho$, in $\sigma$ or in $\sigma'$, by the face compatibility recorded in step [](#data){.pf-ref}. The formula extends continuously to the faces of $\sigma$ that contain $\tau$, so it gives a continuous map $p^{-1}(U_\tau)\to X_{\tau_0}\times U_\tau$, and the same construction with the inverse composites, which exist because the edge maps are homeomorphisms, gives a continuous inverse. Indexing the cover by all simplices, and not only by vertices, matters: in a base with a loop edge whose two ends attach a fibre by two different homeomorphisms, the open star of the vertex is the whole circle, over which the projection is the mapping torus of a nontrivial homeomorphism and not a product.
:::
:::

::: {.pf-step #conclusion}
$p:\Delta X\to\Gamma$ is a fibre bundle with fibre $F$ when $\Gamma$ is connected, and a fibre bundle over each component of $\Gamma$ in general.

::: pf-proof
Step [](#star){.pf-ref} exhibits for each simplex $\tau$ an open set $U_\tau$ containing the interior of $\tau$ over which $p$ is a product with fibre $X_{\tau_0}$, and step [](#fibre){.pf-ref} identifies all these fibres with the single space $F$. The sets $U_\tau$ cover $\Gamma$, so every point of $\Gamma$ has a neighbourhood over which $p$ is trivial, which is the definition of a fibre bundle.
:::
:::

:::
:::
