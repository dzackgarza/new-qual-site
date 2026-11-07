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
  date: 2026-11-08
  note: >-
    Read Hatcher p.459: complex of spaces over Δ-complex Γ with n-simplex data X_0->...->X_n and iterated mapping cylinder M(f1,...,fn)->Δ^n; definition for n=1 as M(f1) and for n>1 as mapping cylinder of M(f1,...,fn-1)->X_{n-1}->X_n via canonical projection. The statement's hypothesis is all maps are homeomorphisms.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Previous proof handled only the graph case (vertex/edge spaces, edge cylinders). Extended to general n: by induction M(f1,...,fn) ≅ F×Δ^n when each f_i is a homeomorphism, using M(f1)≅F×I and the join description F×(Δ^{n-1}⋆I)≅F×Δ^n. Local triviality over int σ and over open stars U_v then gives F×U, so projection is a fiber bundle with fiber F, the common homeomorphism type of all vertex/edge spaces.
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
$(x,t)\mapsto (f_1(x),t)$ for $t$ in the cylinder coordinate gives a
homeomorphism $M(f_1)\cong X_0\times I\cong F\times\Delta^1$.

Inductively, let $X_0\xrightarrow{f_1}\cdots\xrightarrow{f_n}X_n$ with each $f_i$ a
homeomorphism, and let $M_{n-1}=M(f_1,\ldots,f_{n-1})$. By induction
$M_{n-1}\cong F\times\Delta^{n-1}$ compatibly with its projection to
$\Delta^{n-1}$. The iterated cylinder $M(f_1,\ldots,f_n)$ is defined (p.459) as
the mapping cylinder of the composition
$M_{n-1}\xrightarrow{\pi}X_{n-1}\xrightarrow{f_n}X_n$, where $\pi$ is the
canonical projection of a mapping cylinder onto its target end. Since $\pi$
is a homotopy equivalence and $f_n$ a homeomorphism, the composition is a
homotopy equivalence that is in fact a homeomorphism on the $F$-factor:
using $M_{n-1}\cong F\times\Delta^{n-1}$ and $X_n\cong F$, the mapping cylinder
of $F\times\Delta^{n-1}\to F$ (projection to $F$ followed by $f_n$) is
$F\times (\Delta^{n-1}\star I)\cong F\times\Delta^n$, star denoting join with
an interval, i.e. the cone on the base simplex. Explicitly,
$(y,s,t)\mapsto (y, (1-t)s + t e_n)$ with $s\in\Delta^{n-1}$, $t\in I$, gives the
homeomorphism $M(f_1,\ldots,f_n)\cong F\times\Delta^n$ commuting with
projection to $\Delta^n$. Thus for every $n$-simplex $\sigma$ of $\Gamma$,
$p^{-1}(\sigma)=M(f_1,\ldots,f_n)$ is $F\times\sigma$.

:::

:::

::: pf-step

Local triviality:

::: pf-proof

Let $\sigma$ be any simplex of $\Gamma$ and let $\operatorname{int}\sigma$ be its
open interior; no identifications occur there, so
$p^{-1}(\operatorname{int}\sigma)=F\times\operatorname{int}\sigma$
as above. For a vertex $v$ let $U_v$ be its open star in $\Gamma$ (all open
simplices incident to $v$ together with $v$). Each such open simplex
contributes $F\times\operatorname{int}\tau$ glued along homeomorphisms at faces,
hence $p^{-1}(U_v)$ is obtained by gluing copies of $F\times\operatorname{int}\tau$
along the identity on $F$, giving $p^{-1}(U_v)\cong F\times U_v$ via the
product of the fiber identifications. The $U_v$ cover $\Gamma$, and the same
holds for the open star of any simplex. Hence every $x\in\Gamma$ has a
neighborhood $U$ with $p^{-1}(U)\cong F\times U$.

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
