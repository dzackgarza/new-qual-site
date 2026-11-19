---
schema: qual/card@1
id: E-HAT-3.D-1
kind: problem
title: "Topological groups with finite CW structure are manifolds"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.D, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.D Exercise 1, printed page
    302. The statement matches the book word for word, including the bracketed hint.
    Checked: the top-dimensional cell of a finite-dimensional CW group G is open,
    because the union of the other cells is a subcomplex and hence closed, so G is a
    d-manifold by transitivity of left translations. The orientability argument was
    repaired: the card asserted without proof that an isotopy cannot reverse the
    local orientation class. A lemma with proof is now on the card — a homeomorphism
    isotopic to the identity carries each local orientation to the corresponding one,
    proved from the two-sheeted covering space M̃ → M of local orientations (Hatcher,
    p. 234) by extending a section over the cylinder M × I — and it is applied to
    L_{h^{-1}g}, which fixes x and is isotopic to the identity along L_{γ(t)}. What
    the card does not do: it does not invoke Hatcher's Proposition 3.25 (p. 234)
    directly, using instead the covering-space argument that proposition rests on.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the isotopy lemma as its own step. Repaired: the
    earlier text chose a path gamma from e to hg^{-1} and then applied the lemma to L_{h^{-1}g},
    which fixes x; the path and the map must agree, and the card now takes gamma from e to
    h^{-1}g, so that t |- L_{gamma(t)} is an isotopy from the identity to L_{h^{-1}g}. Re-checked the
    rest: the complement of a top-dimensional cell is a subcomplex, hence closed, so the open cell is
    Euclidean; left translations carry it to any point; the pullback of the local-orientation cover
    to the cylinder has a section over M x {0} extending because that inclusion is a homotopy
    equivalence; and components of a CW complex are path connected, so the path gamma exists. Added:
    that an isotopy must be continuous in both variables, and the Hausdorff requirement for the
    manifold property, which the earlier text left to the reader. No defect found in the statement,
    §3.D Exercise 1.
---

::: {.problem}
Show that a topological group with a finite-dimensional CW structure is an orientable manifold.
[Consider the homeomorphisms $x \mapsto gx$ or $x \mapsto xg$ for fixed $g$ and varying $x$ in the group.]
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own; it uses the hint and the local-orientation cover of Hatcher p. 234. Let $G$ be a topological group with a finite-dimensional CW structure and let $d$ be the largest dimension of a cell.

::: pf

::: {.pf-step #manifold}
Every point of $G$ has an open neighbourhood homeomorphic to $\RR^d$.

::: pf-proof
Choose a $d$-cell $e^d$. No cell has dimension larger than $d$, so the union of all cells other than $e^d$ is a subcomplex, hence closed, and $e^d$ itself is open in $G$ and homeomorphic to $\RR^d$. Fix $x\in e^d$. For $y\in G$ the element $g=yx^{-1}$ makes left multiplication $L_g(z)=gz$ a homeomorphism of $G$ carrying $x$ to $y$, since $G$ is a topological group; so $L_g(e^d)$ is an open neighbourhood of $y$ homeomorphic to $\RR^d$. As $G$ is a CW complex it is Hausdorff, so $G$ is a $d$-manifold.
:::

:::

::: {.pf-step #lemma}
If $M$ is an $n$-manifold, $p\colon\widetilde M\to M$ its two-sheeted cover of local orientations, and $\varphi$ a homeomorphism of $M$ isotopic to the identity through homeomorphisms $H_t$, then $\varphi_*$ carries each local orientation $\mu_x$ to $\mu_{\varphi(x)}$.

::: pf-proof
Let $H\colon M\times I\to M$ be the isotopy with $H_0=\id$ and $H_1=\varphi$. The pullback $H^*\widetilde M\to M\times I$ is a two-sheeted covering space, and over $M\times\{0\}$ it has a section, namely $x\mapsto\mu_x$, because $H_0$ is the identity. The inclusion $M\times\{0\}\hookrightarrow M\times I$ is a homotopy equivalence, and a covering pulled back along it is trivialized over the cylinder, so the section extends to a section of $H^*\widetilde M$ over $M\times I$. Its value at $(x,1)$ is a local orientation at $H_1(x)=\varphi(x)$ equal to $\varphi_*(\mu_x)$ by construction of the pullback, hence $\varphi_*(\mu_x)=\mu_{\varphi(x)}$.
:::

:::

::: {.pf-step #well-defined}
The orientation of the identity component $G_0$ obtained by transporting a chosen local orientation from $e$ along left translations is well defined.

::: pf-proof
Let $g,h\in G_0$ and let $\mu_x$ be a chosen local orientation at $x\in e^d$. Put $\varphi=L_{h^{-1}g}$, which lies in $G_0$ and fixes $x$ because $h^{-1}gx=h^{-1}hx=x$. Since $G_0$ is path connected (a CW complex is locally path connected, so its components are path connected), choose a path $\gamma$ in $G_0$ from $e$ to $h^{-1}g$; then $t\mapsto L_{\gamma(t)}$ is an isotopy from the identity to $\varphi$, continuous in $(z,t)$. By step [](#lemma){.pf-ref} applied at the fixed point $x$, $\varphi_*(\mu_x)=\mu_x$. Since $L_g=L_h\circ L_{h^{-1}g}$, the two translations carry $\mu_x$ to the same local orientation at $gx=hx$.
:::

:::

::: {.pf-step}
$G$ is orientable.

::: pf-proof
Step [](#manifold){.pf-ref} makes $G$ a $d$-manifold. Choosing a local orientation $\mu_x$ at a point $x$ of a top-dimensional cell and transporting it by left translations gives, by step [](#well-defined){.pf-ref}, a well-defined local orientation at every point of $G_0$, and it is locally consistent because near any point it is a continuous translate of one local orientation. So $G_0$ is orientable. Every other component is a coset $aG_0$, homeomorphic to $G_0$ by $L_a$, and carries the transported orientation; the components are the connected components, so a choice of orientation on each orients $G$.
:::

:::

:::
:::
