---
schema: qual/card@1
id: E-HAT-4.F-1
kind: problem
title: "Direct limit axiom vs. wedge sum axiom"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.F, Exercise 1; the stored statement matches.
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
    Restructured the prose solution into Lamport steps and checked the statement against Hatcher, *Algebraic Topology* (2002), §4.F Exercise 1, printed p. 455, both halves matching the printed text. The collection's provenance is the book, and no retained solution set covers the exercise; the argument is the card's own beyond the two results it cites from the book: that axioms (1) and (2) give the wedge sum axiom for finite wedges (p. 160), and the definition of the direct limit axiom over finite subcomplexes (p. 455). Checked: a finite subcomplex of a wedge lies in a finite subwedge; filtered colimits commute with fixed direct sums; the telescope is homotopy equivalent to $X$; $1-s_*$ is injective on the direct sum by the first-nonzero-coordinate argument; and exactness identifies $\widetilde h_n(T)$ with the colimit.
---

::: {.problem}
Assuming the first two axioms for a homology theory on the CW category, show that the direct limit axiom implies the wedge sum axiom.
Show that the converse also holds for countable CW complexes.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, using only the first two axioms and the two facts Hatcher records on pp. 160 and 455. The statement is Hatcher, *Algebraic Topology* (2002), §4.F Exercise 1, printed p. 455.

::: pf

::: {.pf-step #axioms}
Let $\widetilde h_*$ satisfy the homotopy and exactness axioms (1) and (2) of Hatcher's list; the wedge sum axiom (3) and the direct limit axiom are the two statements to be compared.

::: pf-proof
These are the axioms as Hatcher states them: (1) homotopy invariance, (2) exactness for a CW pair, (3) $\widetilde h_n(\bigvee_\alpha X_\alpha)\cong\bigoplus_\alpha\widetilde h_n(X_\alpha)$; the direct limit axiom identifies $\widetilde h_n(X)$ with the colimit over the finite subcomplexes of $X$ (p. 455).
:::
:::

::: {.pf-step #finite}
Axioms (1) and (2) already give the wedge sum axiom for finite wedge sums.

::: pf-proof
Apply exactness to the pair $(X_1\vee X_2,X_1)$: the quotient is $X_2$ and the pair is a CW pair, so the long exact sequence splits because the inclusion of $X_1$ into the wedge is a retract up to homotopy; the splitting gives $\widetilde h_n(X_1\vee X_2)\cong\widetilde h_n(X_1)\oplus\widetilde h_n(X_2)$, and induction extends this to finitely many summands. This is Hatcher's remark on p. 160.
:::
:::

::: {.pf-step #forward}
The direct limit axiom implies the wedge sum axiom.

::: pf-proof
Let $X=\bigvee_\alpha X_\alpha$. Each finite subcomplex $K\subset X$ lies in a finite wedge $K_{\alpha_1}\vee\cdots\vee K_{\alpha_r}$ with $K_{\alpha_i}\subset X_{\alpha_i}$ finite, so by step [](#finite){.pf-ref} $\widetilde h_n(K)\cong\bigoplus_i\widetilde h_n(K_{\alpha_i})$. The finite subcomplexes of $X$ are cofinal among those of the wedge, so the direct limit axiom gives $\widetilde h_n(X)\cong\varinjlim_K\widetilde h_n(K)$, and a filtered colimit of the groups $\bigoplus_i\widetilde h_n(K_{\alpha_i})$ over varying finite index sets is the direct sum $\bigoplus_\alpha\widetilde h_n(X_\alpha)$, because each finite set of summands eventually appears and the colimit of a fixed-summand direct system is the direct sum of the colimits.
:::
:::

::: {.pf-step #telescope}
Conversely, let $X$ be a countable CW complex with an exhaustion $X_1\subset X_2\subset\cdots$ by finite subcomplexes, and let $T$ be the based mapping telescope with the basepoint track collapsed. Then $\widetilde h_*(T)\cong\widetilde h_*(X)$.

::: pf-proof
The inclusions $X_i\subset X_{i+1}$ are cofibrations, so the telescope deformation retracts onto $X$ (the argument of §3.F); a homotopy equivalence induces an isomorphism on any homology theory by axiom (1).
:::
:::

::: {.pf-step #mv}
Writing $s_*$ for the shift on $\bigoplus_i\widetilde h_n(X_i)$ induced by the inclusions, Mayer--Vietoris for the even/odd cover of $T$ and the wedge axiom (3) give an exact sequence $\bigoplus_i\widetilde h_n(X_i)\xrightarrow{1-s_*}\bigoplus_i\widetilde h_n(X_i)\to\widetilde h_n(T)\to\bigoplus_i\widetilde h_{n-1}(X_i)$.

::: pf-proof
Cover $T$ by the unions of neighbourhoods of its even and odd mapping cylinders; after collapsing the basepoint track, each union and their intersection retract onto wedges of the corresponding $X_i$, so their homology is computed by axiom (3). Mayer--Vietoris for this cover, available from axiom (2) applied to the pair of the union with one side, gives the sequence, and the connecting map is $1-s_*$ because the intersection sits in each side by the shift.
:::
:::

::: {.pf-step #injective}
$1-s_*$ is injective on the direct sum $\bigoplus_i\widetilde h_n(X_i)$.

::: pf-proof
Let $x$ be a finite-support element with $(1-s_*)x=0$ and let $i$ be the least index with $x_i\neq0$. The $i$-th coordinate of $(1-s_*)x$ is $x_i$ minus a contribution from the $(i-1)$-st coordinate, which is $0$ by minimality, so that coordinate is $x_i\neq0$, a contradiction. Hence $x=0$.
:::
:::

::: {.pf-step #colimit}
$\widetilde h_n(X)\cong\varinjlim_i\widetilde h_n(X_i)$.

::: pf-proof
By step [](#mv){.pf-ref} and injectivity of $1-s_*$ from step [](#injective){.pf-ref}, $\widetilde h_n(T)\cong\operatorname{coker}(1-s_*)$, which is the colimit of the sequence $\widetilde h_n(X_1)\to\widetilde h_n(X_2)\to\cdots$; with step [](#telescope){.pf-ref} this is $\widetilde h_n(X)$, the direct limit axiom for the countable case.
:::
:::

::: {.pf-step}
The direct limit axiom implies the wedge sum axiom, and conversely for countable CW complexes.

::: pf-proof
Step [](#forward){.pf-ref} is the first implication and step [](#colimit){.pf-ref} the second.
:::
:::

:::
:::
