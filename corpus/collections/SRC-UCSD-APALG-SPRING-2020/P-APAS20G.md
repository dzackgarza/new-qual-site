---
schema: qual/card@1
id: P-APAS20G
kind: problem
title: Haar average of a unitary representation is projection onto invariants
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the Haar average defines a bounded
    operator with norm at most one, that its image lies in the invariant subspace by left
    invariance of Haar measure, that it fixes the invariants by normalisation so that the
    image is exactly the invariants, that it is idempotent, that it is self-adjoint using
    unitarity and invariance of Haar measure under inversion, and that a self-adjoint
    idempotent is the orthogonal projection onto its image since its kernel is the
    orthogonal complement of the image. The argument is the card's own; no retained set is
    cited. No repair needed.
---

::: {.problem}
Let $(H,U)$ be a unitary representation of a compact group $G$.
Show that the operator
$$
P=\int_G U(g)\,dg
$$
is the orthogonal projection of $H$ onto the space of $G$-invariants in $H$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. Normalize Haar measure on $G$ so that $\int_{G}dg=1$, and write $H^{G}=\{v\in H: U(g)v=v\ \text{for all } g\in G\}$.

::: pf

::: {.pf-step #definition}
For $v\in H$ the vector $Pv=\int_{G}U(g)v\,dg$ is defined, and $P$ is linear with $\norm{Pv}\le\norm{v}$.

::: pf-proof
$g\mapsto U(g)v$ is continuous into $H$ because a unitary representation is strongly continuous, and $G$ is compact with a finite Haar measure, so the Bochner integral exists. Then $\norm{Pv}\le\int_{G}\norm{U(g)v}\,dg=\int_{G}\norm{v}\,dg=\norm{v}$, since each $U(g)$ is unitary and the measure is normalized; linearity is linearity of the integral.
:::

:::

::: {.pf-step #image-invariants}
$Pv\in H^{G}$ for every $v\in H$.

::: pf-proof
For $h\in G$, continuity of $U(h)$ and the substitution $g\mapsto h^{-1}g$ give
$$
U(h)Pv=\int_{G}U(h)U(g)v\,dg=\int_{G}U(hg)v\,dg=\int_{G}U(g)v\,dg=Pv,
$$
where the last equality is left invariance of Haar measure; so $Pv$ is fixed by every $h$.
:::

:::

::: {.pf-step #invariants-image}
If $v\in H^{G}$ then $Pv=v$; hence $H^{G}\subset\operatorname{im}P$ and $\operatorname{im}P=H^{G}$.

::: pf-proof
$U(g)v=v$ for every $g$, so $Pv=\int_{G}v\,dg=v\int_{G}dg=v$ by normalization. With step [](#image-invariants){.pf-ref} this gives both inclusions.
:::

:::

::: {.pf-step #idempotent}
$P^{2}=P$.

::: pf-proof
For any $v$, the vector $Pv$ lies in $H^{G}$ by step [](#image-invariants){.pf-ref}, so $P(Pv)=Pv$ by step [](#invariants-image){.pf-ref}.
:::

:::

::: {.pf-step #self-adjoint}
$P^{*}=P$.

::: pf-proof
For $v,w\in H$ one has $\langle Tv,w\rangle=\int_{G}\langle U(g)v,w\rangle\,dg$ for the operator $T=\int_{G}U(g)\,dg$, by continuity of the inner product and the definition of the vector integral; hence
$$
\langle P^{*}v,w\rangle=\overline{\langle Pw,v\rangle}=\overline{\int_{G}\langle U(g)w,v\rangle\,dg}=\int_{G}\langle v,U(g)w\rangle\,dg=\int_{G}\langle U(g)^{*}v,w\rangle\,dg .
$$
Since $U$ is unitary, $U(g)^{*}=U(g)^{-1}=U(g^{-1})$, so
$$
\langle P^{*}v,w\rangle=\int_{G}\langle U(g^{-1})v,w\rangle\,dg=\int_{G}\langle U(g)v,w\rangle\,dg=\langle Pv,w\rangle,
$$
the middle equality by invariance of Haar measure under inversion. As $w$ is arbitrary, $P^{*}v=Pv$, and as $v$ is arbitrary, $P^{*}=P$.
:::

:::

::: {.pf-step #orthogonal}
A self-adjoint idempotent is the orthogonal projection onto its image: if $P^{2}=P=P^{*}$, then $\ker P=(\operatorname{im}P)^{\perp}$.

::: pf-proof
If $v\in\ker P$ and $w\in\operatorname{im}P$, say $w=Pu$, then $\langle v,w\rangle=\langle v,Pu\rangle=\langle Pv,u\rangle=0$, so $\ker P\subset(\operatorname{im}P)^{\perp}$. Conversely if $v\perp\operatorname{im}P$ then $\langle Pv,Pv\rangle=\langle v,P^{2}v\rangle=\langle v,Pv\rangle=0$, so $Pv=0$ and $v\in\ker P$. Equal subspaces give the orthogonal decomposition $H=\operatorname{im}P\oplus\ker P$, and $P$ is the projection along $\ker P$, hence the orthogonal projection onto $\operatorname{im}P$.
:::

:::

::: {.pf-step}
$P$ is the orthogonal projection of $H$ onto $H^{G}$.

::: pf-proof
Steps [](#image-invariants){.pf-ref} and [](#invariants-image){.pf-ref} identify $\operatorname{im}P$ with $H^{G}$, step [](#self-adjoint){.pf-ref} gives $P^{*}=P$ and step [](#idempotent){.pf-ref} gives $P^{2}=P$; by step [](#orthogonal){.pf-ref} such an operator is the orthogonal projection onto its image.
:::

:::

:::
:::
