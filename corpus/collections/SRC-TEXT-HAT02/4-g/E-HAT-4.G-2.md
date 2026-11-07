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
---

::: {.problem}
Show that if $X$ is a complex of spaces in which all the maps are homeomorphisms, then the projection $\Delta X \to \Gamma$ is a fiber bundle.
:::

::: {.solution}

::: pf

::: pf-step

Common fiber:

::: pf-proof

All vertex and edge spaces of the complex are homeomorphic to a common fiber $F$.
Indeed, $\Gamma$ is connected and every attaching map is a homeomorphism, so composing
homeomorphisms along paths joins any two vertex or edge spaces.

:::
:::

::: pf-step

Iterated mapping cylinder of a string of homeomorphisms is a product:

::: pf-proof

For $n=1$, $M(f_1)$ with $f_1$ a homeomorphism is $X_0\times I$ with
$X_0\times\{1\}$ identified to $X_1$ via $f_1$; since $f_1$ is a homeomorphism,
$(x,t)\mapsto (f_1(x),t)$ gives a homeomorphism $M(f_1)\cong X_0\times I\cong
F\times\Delta^1$ commuting with projection to $\Delta^1$.

Inductively, let $X_0\xrightarrow{f_1}\cdots\xrightarrow{f_n}X_n$ with each $f_i$ a
homeomorphism and $M_{n-1}=M(f_1,\ldots,f_{n-1})\cong F\times\Delta^{n-1}$ by
induction, respecting projection to $\Delta^{n-1}$. The iterated cylinder
$M(f_1,\ldots,f_n)$ is defined (p.458–459) as the mapping cylinder of
$M_{n-1}\xrightarrow{\pi}X_{n-1}\xrightarrow{f_n}X_n$, where $\pi$ is the
canonical projection onto the target end. Under the product identifications
$M_{n-1}\cong F\times\Delta^{n-1}$ and $X_{n-1},X_n\cong F$, the composition is
$(y,s)\mapsto f_n(\pi_F(y,s))=f_n(y)$ with $\pi_F$ the $F$-projection; its
mapping cylinder is $F\times C(\Delta^{n-1})=F\times(\Delta^{n-1}\star\{pt\})
\cong F\times\Delta^n$, the cone on $\Delta^{n-1}$ (join with a point, not
$\Delta^{n-1}\star I$, which has dimension $n+1$). Explicitly
$((y,s),t)\mapsto (y,(1-t)s+t e_n)$ with $s\in\Delta^{n-1}$, $t\in I$, gives a
homeomorphism $M(f_1,\ldots,f_n)\cong F\times\Delta^n$ over $\Delta^n$.
Thus for the $n$-simplex $\sigma$ corresponding to this string,
$p^{-1}(\sigma)=M(f_1,\ldots,f_n)\cong F\times\sigma$, and on each face the
identification is the product of the fiber homeomorphism $F\to F$ given by the
corresponding edge map.

:::

:::

::: pf-step

Local triviality:

::: pf-proof

Fix $n$-simplex $\sigma$ and its interior $\operatorname{int}\sigma$: no
identifications from other simplices meet $\operatorname{int}\sigma$, so
$p^{-1}(\operatorname{int}\sigma)=F\times\operatorname{int}\sigma$ as above,
trivial over $\operatorname{int}\sigma$. For general local triviality,
use the barycentric subdivision $\Gamma'$: every point $x\in\Gamma$ lies in the
open star $\operatorname{St}(b_\tau)$ of the barycenter $b_\tau$ of a unique
simplex $\tau$ of $\Gamma$, and $\operatorname{St}(b_\tau)$ meets only those
simplices containing $\tau$ as a face. Choose a maximal simplex
$\sigma\supset\tau$ containing $x$ in its interior (if $x$ is in $\operatorname{int}
\tau$, take $\sigma=\tau$). The fiber over each simplex $\rho\supset\tau$ in
$\operatorname{St}(b_\tau)$ is $F\times\rho$ with face identifications given by
the edge homeomorphisms of $\Gamma$; since $\tau$ is a common face, all those
identifications agree on $\tau$: for two $n$-simplices $\sigma_1,\sigma_2$
containing $\tau$, the compositions of edge homeomorphisms along any path in
$\sigma_1$ from a vertex of $\tau$ to the corresponding vertex coincide on
$\tau$ because $\Gamma$ is a $\Delta$-complex (its simplices have ordered
vertices and face maps are inclusions, so the diagram of spaces over $\tau$ is
commutative; the repeated-face case is the consistency of the $\Delta$-complex
structure). Hence $p^{-1}(\operatorname{St}(b_\tau))$ is obtained by gluing the
products $F\times(\operatorname{St}(b_\tau)\cap\rho)$ along fiber
homeomorphisms that agree on overlaps, giving $p^{-1}(\operatorname{St}(b_\tau))
\cong F\times\operatorname{St}(b_\tau)$. These barycentric stars cover
$\Gamma$ and are open, so $p$ is locally trivial. In particular, a loop edge
with distinct attaching homeomorphisms $f_{e,0},f_{e,1}:F\to F$ has monodromy
$f_{e,1}^{-1}f_{e,0}$ around the loop, but its bundle over $S^1$ is still locally
trivial over arcs $U_e=\operatorname{int}e$ and over $U_v$ as above, with
transition function the monodromy on overlaps; the vertex-star $U_v$ alone need
not trivialize the loop, which is why the barycentric-star cover is used.

:::

:::

::: pf-step

Hence $p:\Delta X\to\Gamma$ is a fiber bundle with fiber $F$.

::: pf-proof

Fiber bundle definition: locally $F\times U$ as above, with $F$ the common
fiber from the first step.

:::

:::

:::

:::
