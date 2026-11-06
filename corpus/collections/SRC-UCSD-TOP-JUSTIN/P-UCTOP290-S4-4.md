---
schema: qual/card@1
id: P-UCTOP290-S4-4
kind: problem
title: Topological group structure on a connected cover
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 4, Problem 4 against the checked-in extraction and PDF page image.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 4, problem 4
    (assets/attachments/UCSD_290_F14_sheet4.pdf, page 1): the sheet asks, for
    a path-connected locally path-connected topological group G and a path-
    connected cover, for a unique topological group structure making the cover
    a homomorphism, modulo the choice of basepoint over the identity. The card
    states exactly this, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the proof is
    derived here. It uses abelianness of the fundamental group of a
    topological group to see that the kernel subgroup is closed under the
    induced multiplication and inversion, the lifting criterion to obtain the
    lifted multiplication and inversion, and uniqueness of lifts on the
    connected products to obtain the axioms and the uniqueness of the
    structure.
---

::: {.problem}
Let $G$ be a path-connected, locally path-connected topological group,
and let $p:\widetilde G\to G$ be a path-connected covering. Show, using
existence and uniqueness of lifts, that after choosing
$\widetilde e\in p^{-1}(e)$ there is a unique topological group
structure on $\widetilde G$ with identity $\widetilde e$ for which $p$
is a homomorphism.
:::

::: {.solution}
Let $G$ be a path-connected, locally path-connected topological group with multiplication $m$ and inversion $i$, let $p\colon\widetilde G\to G$ be a path-connected covering, and fix $\tilde e\in p^{-1}(e)$; write $H=p_*\pi_1(\widetilde G,\tilde e)\leq\pi_1(G,e)$.

::: pf

::: {.pf-step #abelian}
$\pi_1(G,e)$ is abelian, the map $m_*$ is addition, and $i_*$ is negation.

::: pf-proof
For a topological group, the multiplication $m\colon G\times G\to G$ induces on $\pi_1$ the group operation: identifying $\pi_1(G\times G,(e,e))\cong\pi_1(G,e)\times\pi_1(G,e)$, one has $m_*(\alpha,\beta)=\alpha\beta$, and $i_*(\alpha)=\alpha^{-1}$. The two inclusions $x\mapsto(x,e)$ and $x\mapsto(e,x)$ of $G$ into $G\times G$ commute up to homotopy through the commutativity of the group operation up to homotopy, so $\alpha\beta=\beta\alpha$ for all $\alpha,\beta\in\pi_1(G,e)$, that is $\pi_1(G,e)$ is abelian; consequently $m_*$ is addition and $i_*$ is negation in the abelian group $\pi_1(G,e)$.
:::

:::

::: {.pf-step #subgroup}
$m_*(H\times H)\subseteq H$ and $i_*(H)\subseteq H$.

::: pf-proof
$\pi_1(\widetilde G\times\widetilde G,(\tilde e,\tilde e))\cong\pi_1(\widetilde G,\tilde e)\times\pi_1(\widetilde G,\tilde e)$ and $(p\times p)_*$ is $p_*\times p_*$, so $(p\times p)_*\pi_1(\widetilde G\times\widetilde G)=H\times H$. Since $(m\circ(p\times p))_*=m_*\circ(p_*\times p_*)$ and $H$ is a subgroup of the abelian group $\pi_1(G,e)$, the image $m_*(H\times H)=H+H\subseteq H$; likewise $i_*(H)=-H=H$.
:::

:::

::: {.pf-step #lifts}
There are unique maps $\tilde m\colon\widetilde G\times\widetilde G\to\widetilde G$ and $\tilde\imath\colon\widetilde G\to\widetilde G$ with $p\circ\tilde m=m\circ(p\times p)$, $\tilde m(\tilde e,\tilde e)=\tilde e$, and $p\circ\tilde\imath=i\circ p$, $\tilde\imath(\tilde e)=\tilde e$.

::: pf-proof
$\widetilde G\times\widetilde G$ is path-connected and locally path-connected, and $p$ is a covering, so the lifting criterion applies to the map $m\circ(p\times p)\colon\widetilde G\times\widetilde G\to G$: a lift through $p$ exists exactly when the image of its fundamental group lies in $H$, which is step [](#subgroup){.pf-ref}, and then the lift is unique once its value at one point is fixed. Applying this to the point $(\tilde e,\tilde e)$, which lies over $m(e,e)=e$, gives the unique lift $\tilde m$ with $\tilde m(\tilde e,\tilde e)=\tilde e$. The same criterion applied to $i\circ p\colon\widetilde G\to G$, whose image on $\pi_1$ is $i_*(H)\subseteq H$ by step [](#subgroup){.pf-ref}, gives the unique lift $\tilde\imath$ with $\tilde\imath(\tilde e)=\tilde e$.
:::

:::

::: {.pf-step #axioms}
With these operations $\widetilde G$ is a group with identity $\tilde e$ and inversion $\tilde\imath$.

::: pf-proof
Associativity: the maps $(\tilde x,\tilde y,\tilde z)\mapsto\tilde m(\tilde m(\tilde x,\tilde y),\tilde z)$ and $\mapsto\tilde m(\tilde x,\tilde m(\tilde y,\tilde z))$ from $\widetilde G^3$ to $\widetilde G$ both lift the map $(\tilde x,\tilde y,\tilde z)\mapsto p(\tilde x)p(\tilde y)p(\tilde z)$ through $p$, because $p\tilde m=m(p\times p)$; they agree at $(\tilde e,\tilde e,\tilde e)$, where both take the value $\tilde e$; by uniqueness of lifts for the connected space $\widetilde G^3$ they are equal. Identity: $\tilde m(\tilde e,\tilde x)$ and $\tilde x$ both lift $\tilde x\mapsto p(\tilde x)$ and agree at $\tilde x=\tilde e$, so they are equal, and symmetrically for $\tilde m(\tilde x,\tilde e)$. Inverse: $\tilde m(\tilde\imath(\tilde x),\tilde x)$ lifts $\tilde x\mapsto p(\tilde x)^{-1}p(\tilde x)=e$, the constant map, and agrees with the constant map $\tilde x\mapsto\tilde e$ at $\tilde x=\tilde e$; hence it is constant, and symmetrically on the other side.
:::

:::

::: {.pf-step #homomorphism}
$p$ is a homomorphism for this structure, and the structure is the only one with identity $\tilde e$ making $p$ a homomorphism.

::: pf-proof
$p(\tilde m(\tilde x,\tilde y))=m(p(\tilde x),p(\tilde y))$ by the defining property of $\tilde m$, so $p$ is a homomorphism, and $p(\tilde e)=e$ by choice of $\tilde e$. If $\widetilde G$ carried another topological group structure with identity $\tilde e$ for which $p$ is a homomorphism, its multiplication $\tilde m'$ would satisfy $p\circ\tilde m'=m\circ(p\times p)$ and $\tilde m'(\tilde e,\tilde e)=\tilde e$, so $\tilde m'$ is a lift of $m\circ(p\times p)$ with the same value at $(\tilde e,\tilde e)$ as $\tilde m$; by the uniqueness in step [](#lifts){.pf-ref} they coincide, and likewise the inversions coincide. So the structure is unique.
:::

:::

:::

:::
