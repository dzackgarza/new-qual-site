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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.8, printed pp. 195--196** (`tmp/sources/munkres-solutions-whitman.pdf`); the lemma, the product-topology proof and the box-topology answer are his.

Throughout $\mathbf{x}=(x_{1},x_{2},\dots)$, $f_{i}(t)=a_{i}t+b_{i}$ with $a_{i}>0$, and $h(\mathbf{x})=(f_{1}(x_{1}),f_{2}(x_{2}),\dots)$; the coordinate maps of $h$ are $h_{i}=f_{i}\circ\pi_{i}$.

**In the product topology $h$ is a homeomorphism.** Each $\pi_{i}$ is continuous and each $f_{i}$ is continuous (an affine map of $\RR$), so each $h_{i}$ is continuous; by Theorem 19.6 (printed p. 117) $h$ is continuous, since a map into a product with continuous coordinate functions is continuous.

Let $g_{i}(t)=(t-b_{i})/a_{i}$, which is defined because $a_{i}>0$, and $k(\mathbf{x})=(g_{1}(x_{1}),g_{2}(x_{2}),\dots)$; by the same argument $k$ is continuous. For every $i$,
$$
k_{i}(h(\mathbf{x}))=g_{i}(f_{i}(x_{i}))=\frac{(a_{i}x_{i}+b_{i})-b_{i}}{a_{i}}=x_{i},
\qquad
h_{i}(k(\mathbf{x}))=f_{i}(g_{i}(x_{i}))=a_{i}\frac{x_{i}-b_{i}}{a_{i}}+b_{i}=x_{i},
$$
so $k\circ h$ and $h\circ k$ are both the identity. Hence $h$ is a bijection with inverse $k$, and both are continuous: $h$ is a homeomorphism.

**In the box topology $h$ is also a homeomorphism.** We use the lemma that if $f=\prod_{\alpha}f_{\alpha}:\prod X_{\alpha}\to\prod Y_{\alpha}$ acts coordinatewise, $f((x_{\alpha}))=(f_{\alpha}(x_{\alpha}))$, and each $f_{\alpha}$ is continuous, then $f$ is continuous for the box topologies: for a box basis element $\prod V_{\alpha}$ and a point $x$, $f(x)\in\prod V_{\alpha}$ if and only if $f_{\alpha}(x_{\alpha})\in V_{\alpha}$ for every $\alpha$, that is $x\in\prod f_{\alpha}^{-1}(V_{\alpha})$, which is again a box basis element because each $f_{\alpha}^{-1}(V_{\alpha})$ is open. Applying the lemma to $h=\prod f_{i}$ and to $k=\prod g_{i}$, both continuous, gives that $h$ and its inverse are continuous in the box topology as well. So on $\RR^{\omega}$ with the box topology $h$ is a homeomorphism too.
:::
