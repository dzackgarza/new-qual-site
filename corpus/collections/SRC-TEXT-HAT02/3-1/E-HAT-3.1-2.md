---
schema: qual/card@1
id: E-HAT-3.1-2
kind: problem
title: Multiplication by $n$ induces multiplication by $n$ on $\operatorname{Ext}$
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.1, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the resolution and Hom-complex calculations directly from the definitions.
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.1, Exercise 2; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both halves: the endomorphism $[n]_G$ acts on each cochain group as multiplication by $n$,
    and $[n]_H$ lifts to the chain endomorphism multiplying each $F_i$ by $n$, which commutes with
    the differentials, so the contravariant map is precomposition and again multiplies cochain
    values by $n$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 2 (p.204). Both halves recomputed: [n]_G acts on Hom(F_i,G) as phi -> n phi, and [n]_H lifts to the chain endomorphism n on each F_i because the differentials are homomorphisms; in both cases Ext picks up multiplication by n. Citations added: Ext = H^1(Hom(F,G)) p.195 with Lemma 3.1(b) p.194, contravariance from Exercise 1 (p.204) with Lemma 3.1(a) p.194 for the lift.
---

::: {.problem}
Show that the maps $G \xrightarrow{n} G$ and $H \xrightarrow{n} H$ multiplying each element by the integer $n$ induce multiplication by $n$ in $\operatorname{Ext}(H, G)$.
:::

::: {.solution}
Choose a free resolution
$$
\cdots\longrightarrow F_1\xrightarrow{d_1}F_0\longrightarrow H\longrightarrow0.
$$
Then
$$
\operatorname{Ext}(H,G)=H^1(\operatorname{Hom}(F_\bullet,G)).
$$

::: pf

::: pf-step

Multiplication by $n$ on $G$ induces multiplication by $n$ on $\operatorname{Ext}(H,G)$.

::: pf-proof

The map
$$
[n]_G:G\to G,\qquad g\mapsto ng
$$
induces on every cochain group the map
$$
\operatorname{Hom}(F_i,G)\to\operatorname{Hom}(F_i,G),
\qquad \varphi\mapsto [n]_G\circ\varphi=n\varphi.
$$
Thus the induced cochain map is literally multiplication by $n$ in every degree, using only the functoriality of $\operatorname{Hom}(F_i,-)$. Its map on cohomology, in particular on $H^1=\operatorname{Ext}(H,G)$, is therefore multiplication by $n$; that $\operatorname{Ext}(H,G)$ is this $H^1$, independently of the resolution, is Hatcher p.195 with Lemma 3.1(b) (p.194).

:::

:::

::: pf-step

Multiplication by $n$ on $H$ also induces multiplication by $n$ on $\operatorname{Ext}(H,G)$.

::: pf-proof

The endomorphism $[n]_H:H\to H$ lifts to the chain endomorphism $[n]_{F_i}:F_i\to F_i$ given by multiplication by $n$ in each degree, since all differentials are homomorphisms and hence commute with multiplication by $n$. Because $\operatorname{Ext}$ is contravariant in its first variable (Exercise 1, p.204), the resulting cochain map is precomposition, well defined because a lift exists by Lemma 3.1(a) (p.194) and is unique up to chain homotopy, which induces the same map on cohomology:
$$
\varphi\longmapsto \varphi\circ[n]_{F_i}=n\varphi.
$$
Again this is multiplication by $n$ on every cochain group, so it induces multiplication by $n$ on cohomology.

:::

:::

:::

Hence both endomorphisms specified in the problem induce
$$
\boxed{n\cdot\operatorname{id}_{\operatorname{Ext}(H,G)}}.
$$
:::
