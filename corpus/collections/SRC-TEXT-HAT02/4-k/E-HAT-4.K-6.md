---
schema: qual/card@1
id: E-HAT-4.K-6
kind: problem
title: Projection from $\Delta X$ is a quasifibration
classification:
  areas:
  - topology
  topics:
  - Symmetric Products
  - Quasifibrations
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.K, Exercise 6 and the corrected current statement of Lemma 4K.3 where relevant; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 6 of §4.K, printed p. 484, with the construction of
    $\Delta X$ in §4.G and Lemma 4K.3. Correct in structure: over a simplex the preimage is the
    iterated mapping cylinder, which deformation retracts onto the terminal vertex space while
    $\sigma$ collapses to that vertex, so the fibres are weakly equivalent to it by the edge-map
    hypothesis and the lemma's third part applies; over a finite subcomplex one adds one simplex
    at a time with a collar neighbourhood and applies the lemma's first part; and over the whole
    $\Delta$-complex, which is the union of an increasing sequence of finite subcomplexes with
    every compact set lying in one of them, the lemma's second part applies. Nothing changed.
    Not checked this session: the exact lettering of Lemma 4K.3's three parts, which is quoted
    rather than re-read; the argument is the standard one. Not claimed: a published solution,
    and no certificate.
---

::: {.problem}
Let $X$ be a complex of spaces over a $\Delta$-complex $\Gamma$, as defined in §4.G. Show that the natural projection $\Delta X \to \Gamma$ is a quasifibration if all the maps in $X$ associated to edges of $\Gamma$ are weak homotopy equivalences.
:::

::: {.solution}

The argument is the card's own: the three parts of Lemma 4K.3 are used in turn, over one simplex, over a finite subcomplex, and over the whole $\Delta$-complex.

Let $X$ be a complex of spaces over the $\Delta$-complex $\Gamma$, as in §4.G, with vertex spaces $X_{v}$ and edge maps $X_{v}\to X_{w}$, and let $p:\Delta X\to\Gamma$ be the natural projection.

::: pf

::: {.pf-step #simplex}
For a simplex $\sigma=[v_{0},\ldots,v_{q}]$ of $\Gamma$, the restriction $p:p^{-1}(\sigma)\to\sigma$ is a quasifibration.

::: pf-proof
By the construction of §4.G, $p^{-1}(\sigma)$ is the iterated mapping cylinder of the sequence $X_{v_{0}}\to X_{v_{1}}\to\cdots\to X_{v_{q}}$, and $p$ is the projection of that cylinder onto $\sigma$. Collapsing $\sigma$ linearly to its terminal vertex $v_{q}$ gives a deformation of the cylinder onto $X_{v_{q}}$, covering the deformation of $\sigma$ onto $v_{q}$. The target map $X_{v_{q}}\to\{v_{q}\}$ is a quasifibration trivially, its single fibre being the whole of $X_{v_{q}}$ so that both sides of the relative homotopy groups vanish. For $b\in\sigma$ the induced map $p^{-1}(b)\to X_{v_{q}}$ is the composite of the edge maps along a path from $b$ to $v_{q}$, hence a weak homotopy equivalence by hypothesis, as is any composite of such. So all three conditions of Lemma 4K.3(c) hold, and $p$ is a quasifibration over $\sigma$. The same argument applies to each face of $\sigma$, since a face carries the corresponding initial segment of the same edge sequence.
:::

:::

::: {.pf-step #finite}
For every finite subcomplex $L\subseteq\Gamma$, the restriction $p:p^{-1}(L)\to L$ is a quasifibration.

::: pf-proof
Induct on the number of simplices of $L$, adding one simplex $\sigma$ at a time. Write $V_{1}$ for the open star of $\sigma$ inside $L$ — a collar neighbourhood obtained by removing a small collar of $\partial\sigma$ — and $V_{2}=L\setminus\sigma$, so that $V_{1}\cup V_{2}=L$ and $V_{1}\cap V_{2}$ is a collar of the boundary, homeomorphic to $\partial\sigma\times(0,1)$. Then $V_{1}$ meets the simplices other than $\sigma$ only in that collar, so the restriction over $V_{1}$ is a quasifibration by step [](#simplex){.pf-ref} together with the collar deformation, the restriction over $V_{2}$ is a quasifibration by the induction hypothesis, and the restriction over $V_{1}\cap V_{2}$ is a quasifibration over pieces of the boundary, again by step [](#simplex){.pf-ref}. Lemma 4K.3(a) then makes $p$ a quasifibration over $L$.
:::

:::

::: {.pf-step #union}
$p:\Delta X\to\Gamma$ is a quasifibration.

::: pf-proof
$\Gamma$ is the union of an increasing sequence of finite subcomplexes $L_{1}\subset L_{2}\subset\cdots$, and every compact subset of a CW complex lies in a finite subcomplex, so every compact set in $\Gamma$ lies in some $L_{n}$ and every compact set in $\Delta X$ lies in some $p^{-1}(L_{n})$. Each restriction $p:p^{-1}(L_{n})\to L_{n}$ is a quasifibration by step [](#finite){.pf-ref}, so Lemma 4K.3(b) applies and gives that $p$ is a quasifibration. Hence
$$
\boxed{\Delta X\longrightarrow\Gamma\ \text{is a quasifibration}.}
$$
The fibre over a vertex $v$ is the vertex space $X_{v}$, and the fibre over an arbitrary point is weakly equivalent to the vertex spaces it maps to along the edge maps, by the same weak-equivalence hypothesis.
:::

:::

:::
:::
