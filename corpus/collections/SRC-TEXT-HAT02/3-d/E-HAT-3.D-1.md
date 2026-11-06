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
---

::: {.problem}
Show that a topological group with a finite-dimensional CW structure is an orientable manifold.
[Consider the homeomorphisms $x \mapsto gx$ or $x \mapsto xg$ for fixed $g$ and varying $x$ in the group.]
:::

::: {.solution}
Let $G$ be a topological group with a finite-dimensional CW structure, and let $d$ be the largest dimension of a cell of $G$.

Choose a $d$-cell $e^d$. Since there are no cells of dimension larger than $d$, the union of all cells other than $e^d$ is a subcomplex, hence closed. Therefore the open cell $e^d$ is an open subset of $G$, homeomorphic to $\RR^d$. Choose a point $x\in e^d$.

For any $y\in G$, left multiplication by
$$
g=yx^{-1}
$$
is a homeomorphism
$$
L_g:G\to G,
\qquad z\mapsto gz,
$$
carrying $x$ to $y$. Hence
$$
L_g(e^d)
$$
is an open neighborhood of $y$ homeomorphic to $\RR^d$. Thus every point of $G$ has a Euclidean $d$-neighborhood, so $G$ is a $d$-manifold.

It remains to orient it. Since a CW complex is locally path-connected, each connected component of $G$ is path-connected. First orient the identity component $G_0$. Choose an orientation at one point, say the identity $e$, and transport it to $g\in G_0$ by the local homeomorphism $L_g$. This is well-defined coherently: if $g,h\in G_0$, then the transition between the translated charts is a left translation
$$
L_hL_g^{-1}=L_{hg^{-1}}.
$$
Because $hg^{-1}\in G_0$, choose a path $\gamma$ from $e$ to $hg^{-1}$. The family
$$
L_{\gamma(t)}
$$
is an isotopy from the identity homeomorphism to $L_{hg^{-1}}$. What is needed is that such an isotopy preserves local orientations, which we prove from the local-orientation cover of Hatcher, p. 234.

**Lemma.** Let $M$ be an $n$-manifold, let $p:\widetilde M\to M$ be its two-sheeted covering space of local orientations (Hatcher, p. 234), and let $\varphi:M\to M$ be a homeomorphism isotopic to the identity through homeomorphisms $H_t$. Then
$$
\varphi_*:H_n(M\mid x)\to H_n(M\mid\varphi(x))
$$
carries each local orientation $\mu_x$ to $\mu_{\varphi(x)}$.

**Proof.** Let $H:M\times I\to M$ be the isotopy, with $H_0=1_M$ and $H_1=\varphi$. The pullback $H^*\widetilde M\to M\times I$ is a two-sheeted covering space. Over $M\times\{0\}$ it has a section, namely the chosen local orientations $\mu_x$, since $H_0$ is the identity. The inclusion $M\times\{0\}\hookrightarrow M\times I$ is a homotopy equivalence, and a covering space pulled back along a homotopy from the identity is trivialized over the cylinder, so that section extends to a section over $M\times I$. Its values at $(x,1)$ are local orientations at $H_1(x)=\varphi(x)$ that are the images under $\varphi$ of the orientations at $x$, so $\varphi_*(\mu_x)=\mu_{\varphi(x)}$. $\square$

Apply the lemma to $\varphi=L_{h^{-1}g}$, which fixes $x$ because $h^{-1}gx=x$. Then $(L_{h^{-1}g})_*$ is the identity on $H_d(G\mid x)$. Since
$$
L_g=L_h\circ L_{h^{-1}g},
$$
the two translations $L_g$ and $L_h$ carry the chosen local orientation at $x$ to the same local orientation at $gx= hx$. So the transported orientation is well defined on the orbit $G_0x=G_0$, and it is locally consistent because near any point it is given by a continuous family of translations of one local orientation. Hence $G_0$ is orientable.

Every other component is a left coset $aG_0$ and is homeomorphic to $G_0$ by $L_a$, so transport the orientation of $G_0$ to each component. Therefore the whole manifold $G$ is orientable.

Thus
$$
\boxed{\text{every topological group with a finite-dimensional CW structure is an orientable manifold}.}
$$
:::
