---
schema: qual/card@1
id: E-AWEWJ
kind: problem
title: An affine coordinate homeomorphism of R^omega
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §19 Exercise 8, printed p. 118, with Theorem 19.6
    and Theorem 18.2; the stored statement is the printed one, including the question about
    the box topology.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 19.8, printed pp.
    195-196. In the product topology his argument is used: the coordinate functions of h are
    continuous and Theorem 19.6 applies, and the inverse is the coordinatewise map with
    g_i(t) = (t-b_i)/a_i. The answer for the box topology is his too: h is still a
    homeomorphism, by his lemma that a coordinatewise product of continuous maps is
    continuous for the box topology, since the preimage of a box is the box of the
    preimages. (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured both parts into numbered steps: continuity of h in the product topology through the
    coordinate functions, the explicit two-sided inverse k, and the box-topology lemma with its
    proof (the preimage of a box is a box). The mathematics is the earlier transcription's; nothing
    needed correcting. Checked while restructuring: a_i > 0 is used exactly twice, to define g_i and
    to keep g_i affine, and the conclusion in the box topology is a homeomorphism, so the two
    topologies agree for these maps. Not re-read this session: the Whitman pages, printed pp. 195-196.

---

::: {.exercise}

Given sequences $(a_1, a_2, \ldots)$ and $(b_1, b_2, \ldots)$ of real numbers with $a_i > 0$ for all $i$, define $h: \RR^\omega \to \RR^\omega$ by the equation

$$
h((x_1, x_2, \dots)) = (a_1 x_1 + b_1, a_2 x_2 + b_2, \dots).
$$

Show that if $\RR^\omega$ is given the product topology, $h$ is a homeomorphism of $\RR^\omega$ with itself.
What happens if $\RR^\omega$ is given the box topology?
:::

::: {.solution}

The lemma, the product-topology proof and the box-topology answer are those of **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.8, printed pp. 195--196** (`tmp/sources/munkres-solutions-whitman.pdf`); the steps below are his argument.

Throughout $\mathbf{x}=(x_{1},x_{2},\dots)$, $f_{i}(t)=a_{i}t+b_{i}$ with $a_{i}>0$, $h(\mathbf{x})=(f_{1}(x_{1}),f_{2}(x_{2}),\dots)$, and $h_{i}=f_{i}\circ\pi_{i}$ is the $i$-th coordinate function of $h$. Note that $a_{i}>0$ is what makes $f_{i}$ invertible with inverse $g_{i}(t)=(t-b_{i})/a_{i}$.

::: pf

::: {.pf-step #coordinatewise}
Lemma. If $f_{\alpha}\colon X_{\alpha}\to Y_{\alpha}$ are continuous, then $f=\prod_{\alpha}f_{\alpha}\colon\prod_{\alpha}X_{\alpha}\to\prod_{\alpha}Y_{\alpha}$, $f((x_{\alpha}))=(f_{\alpha}(x_{\alpha}))$, is continuous for the box topologies, and likewise for the product topologies.

::: pf-proof
For box topologies: a box basis element is $\prod_{\alpha}V_{\alpha}$ with every $V_{\alpha}$ open, and $f(\mathbf{x})\in\prod V_{\alpha}$ if and only if $f_{\alpha}(x_{\alpha})\in V_{\alpha}$ for every $\alpha$, that is $\mathbf{x}\in\prod_{\alpha}f_{\alpha}^{-1}(V_{\alpha})$, and each $f_{\alpha}^{-1}(V_{\alpha})$ is open, so the preimage of a box basis element is a box basis element. For product topologies the same computation applies with all but finitely many $V_{\alpha}$ equal to $Y_{\alpha}$, in which case the corresponding $f_{\alpha}^{-1}(V_{\alpha})=X_{\alpha}$.
:::

:::

::: {.pf-step #h-continuous}
$h$ is continuous in both topologies.

::: pf-proof
Each $f_{i}$ is continuous, being affine with $a_{i}\neq0$, so step [](#coordinatewise){.pf-ref} applies to $h=\prod_{i}f_{i}$. In the product topology the same conclusion also follows from Theorem 19.6: a map into a product is continuous when each of its coordinate functions is, and $h_{i}=f_{i}\circ\pi_{i}$ is a composite of continuous maps.
:::

:::

::: {.pf-step #inverse}
The map $k(\mathbf{x})=(g_{1}(x_{1}),g_{2}(x_{2}),\dots)$ with $g_{i}(t)=(t-b_{i})/a_{i}$ satisfies $k\circ h=\mathrm{id}=h\circ k$.

::: pf-proof
Since $a_{i}>0$, $g_{i}$ is defined and $g_{i}(f_{i}(x_{i}))=((a_{i}x_{i}+b_{i})-b_{i})/a_{i}=x_{i}$ and $f_{i}(g_{i}(x_{i}))=a_{i}(x_{i}-b_{i})/a_{i}+b_{i}=x_{i}$ for every $i$. Two sequences agree when they agree in every coordinate, so both composites are the identity. Hence $h$ is a bijection with inverse $k$.
:::

:::

::: {.pf-step #k-continuous}
$k$ is continuous in both topologies.

::: pf-proof
Each $g_{i}$ is affine with nonzero leading coefficient $1/a_{i}$, hence continuous, and step [](#coordinatewise){.pf-ref} applied to $k=\prod_{i}g_{i}$ gives continuity in the box and in the product topologies.
:::

:::

::: {.pf-step #homeo}
$h$ is a homeomorphism of $\RR^{\omega}$ with itself, in the product topology and in the box topology.

::: pf-proof
Steps [](#h-continuous){.pf-ref} and [](#k-continuous){.pf-ref} make $h$ and $k$ continuous in either topology, and step [](#inverse){.pf-ref} makes them mutually inverse. A continuous bijection whose inverse is continuous is a homeomorphism, so $h$ is one for the product topology and, by the same three steps, for the box topology: in the box topology the answer to the second question is that $h$ is again a homeomorphism.
:::

:::

:::

:::
