---
card: E-HAT-3.H-4
kind: gap-repair
slice: "8 — Hatcher §3.H proof gaps"
source: "Hatcher, Algebraic Topology: Prop. 1.30 (tmp/hat/AT.txt 2979), Prop. 1.34 (3129), p. 62 'a deck transformation is completely determined by where it sends a single point' (3632–3635), Prop. 1.39 (3653), Prop. A.1 and its proof (25888–25914), Prop. 3H.5's use of lifted CW structures (16767–16771), Exercise 4 (16840–16842)"
gaps-closed:
  - "lift compatibility: a lifted homotopy ends at a deck transformation, not at the identity, and one lift must be corrected by that deck transformation; then the two composites must be shown to be proper homotopy identities (the card asserted both at once)."
  - "properness of the lifts: the card's finite-fundamental-domain argument does not use π1-injectivity, and the statement it proves is false without it; replaced by a proved criterion (Prop. A.1 + freeness of the deck action)."
review: draft
---

# E-HAT-3.H-4 — repair of the lifting/properness part

**Exercise** (Hatcher §3.H exercise 4, AT.txt 16840–16842): *Show that if finite connected CW complexes
$X$ and $Y$ are homotopy equivalent, then their universal covers $\widetilde X$ and $\widetilde Y$ are
proper homotopy equivalent.*

**The flagged gap.** The card writes "They lift to homotopies
$\widetilde g\widetilde f\simeq\operatorname{id}_{\widetilde X}$,
$\widetilde f\widetilde g\simeq\operatorname{id}_{\widetilde Y}$ after the endpoint lifts are chosen
compatibly", and then treats $\widetilde f,\widetilde g$ as proper homotopy inverses. Two things are
missing, and the first is false as written:

1. A lift $\widetilde H$ of a homotopy $H\colon gf\simeq\operatorname{id}_X$ with
   $\widetilde H_0=\widetilde g\widetilde f$ ends at a map covering $\operatorname{id}_X$ that need
   *not* be $\operatorname{id}_{\widetilde X}$: it is a deck transformation $\gamma$. One must replace
   the lift of $g$ by $\gamma^{-1}\widetilde g$ and then redo the second composite; only then does one
   get *two-sided* proper homotopy inverses.
2. Properness of $\widetilde f,\widetilde g$ and of the lifted homotopies is asserted via a
   "finite fundamental domain" argument that never uses that $f,g$ induce *injections* on $\pi_1$, and
   without injectivity the conclusion is false: the pinch $S^1\vee S^1\to S^1$ induces
   $\ZZ*\ZZ\twoheadrightarrow\ZZ$, and a lift of it to the universal covers is a map from the
   $4$-valent tree onto the line whose fibre over a vertex is infinite, so it is not proper. The
   replacement below proves a properness criterion from Hatcher's Proposition A.1 and applies it to
   $f$, $g$ and to the homotopies.

Nothing about the conclusion changes: the boxed statement
$\widetilde X\simeq_{\mathrm{proper}}\widetilde Y$ stands.

---

## Repair 1 of 1 — the properness and lift-compatibility part (card lines 49–65)

OLD:
```
We first show these lifts are proper. Let $K_X\subset\widetilde X$ and $K_Y\subset\widetilde Y$ be finite unions of lifted closed cells mapping onto $X$ and $Y$. Every compact subset of a universal cover of a finite CW complex meets only finitely many deck translates of such a fundamental finite subcomplex. By equivariance, the inverse image under $\widetilde f$ of a finite union of translates of $K_Y$ lies in a finite union of translates of $K_X$. Hence inverse images of compact sets are compact, so $\widetilde f$ is proper; likewise $\widetilde g$.

Choose homotopies
$$
gf\simeq\operatorname{id}_X,
\qquad
fg\simeq\operatorname{id}_Y.
$$
They lift to homotopies
$$
\widetilde g\widetilde f\simeq\operatorname{id}_{\widetilde X},
\qquad
\widetilde f\widetilde g\simeq\operatorname{id}_{\widetilde Y}
$$
after the endpoint lifts are chosen compatibly. These lifted homotopies are proper: they are equivariant lifts of homotopies on the compact finite CW quotients $X\times I$ and $Y\times I$, so the same finite-fundamental-domain argument applies uniformly in the parameter.

Thus $\widetilde f$ and $\widetilde g$ are proper maps and proper homotopy inverses.
```

NEW:
```
We first record the properness criterion that the argument actually needs. Its hypothesis that $h$ be injective on $\pi_1$ cannot be dropped: the pinch $S^1\vee S^1\to S^1$ induces $\ZZ*\ZZ\twoheadrightarrow\ZZ$, and its lift to universal covers is a map from the $4$-valent tree onto $\RR$ whose fibre over a vertex is infinite, hence not proper.

**Lemma.** Let $W$ and $Z$ be finite CW complexes, $h\colon W\to Z$ a map with $h(w_0)=z_0$, and $\widetilde h\colon\widetilde W\to\widetilde Z$ a lift of $h$ to universal covers with $\widetilde h(\widetilde w_0)=\widetilde z_0$. If $h_*\colon\pi_1(W,w_0)\to\pi_1(Z,z_0)$ is injective, then $\widetilde h$ is proper.

*Proof.* Give $\widetilde W,\widetilde Z$ the CW structures lifting those of $W,Z$ (as in the proof of Proposition 3H.5). Identify $\pi_1(W,w_0)$ and $\pi_1(Z,z_0)$ with the respective deck groups by Proposition 1.39. Then
$$
\widetilde h(\alpha x)=h_*(\alpha)\,\widetilde h(x)\qquad\text{for all }\alpha\in\pi_1(W,w_0),\ x\in\widetilde W :
$$
both sides are lifts of $h\circ p$ and they agree at $x=\widetilde w_0$, so Proposition 1.34 applies. Fix one lift $\tilde e\subset\widetilde Z$ of each cell $e$ of $Z$. Because a nontrivial deck transformation fixes no point (Proposition 1.34 again; deck transformations are determined by their value at one point), every cell of $\widetilde Z$ is $\beta\tilde e$ for a *unique* $\beta\in\pi_1(Z,z_0)$ and a unique cell $e$; the same holds in $\widetilde W$.

Let $C\subset\widetilde Z$ be compact. By Proposition A.1 the set $C$ meets only finitely many cells, so $C$ lies in a finite subcomplex $c_1\cup\cdots\cup c_m$. Fix a cell $e$ of $W$, with lift $\tilde e$, and put $L_e:=\widetilde h(\tilde e)$, a compact subset of $\widetilde Z$. If a cell $\alpha\tilde e$ of $\widetilde W$ meets $\widetilde h^{-1}(C)$ then, by equivariance,
$$
\emptyset\neq\widetilde h(\alpha\tilde e)\cap C=h_*(\alpha)L_e\cap C .
$$
The set $S_e:=\{\beta\in\pi_1(Z,z_0):\beta L_e\cap C\neq\emptyset\}$ is finite: if $\beta L_e\cap C\neq\emptyset$ then $\beta L_e$ meets some $c_j$, so $L_e$ meets the cell $\beta^{-1}c_j$; by Proposition A.1 the compact set $L_e$ meets only finitely many cells $d_1,\dots,d_r$, and writing $d_k=\beta_k\tilde e_k$ and $c_j=\gamma_k\tilde e_k$ uniquely, $\beta^{-1}c_j=d_k$ forces $\beta=\gamma_k\beta_k^{-1}$. Hence only finitely many $\beta$ occur. Therefore the cells of $\widetilde W$ meeting $\widetilde h^{-1}(C)$ lie among the cells $\alpha\tilde e$ with $e$ a cell of $W$ (finitely many) and $\alpha\in h_*^{-1}(S_e)$, which is finite because $h_*$ is injective. So $\widetilde h^{-1}(C)$ meets only finitely many cells and is contained in a finite subcomplex; it is closed ($\widetilde h$ is continuous and $C$ is compact), hence compact. Thus $\widetilde h$ is proper. $\square$

A homotopy equivalence induces an isomorphism on $\pi_1$, so the lemma applies to $f$ and to $g$: $f_*$ is an isomorphism, and $g_*$ is injective because $(gf)_*$ is an isomorphism and $f_*$ is one. Hence the lifts $\widetilde f$ and $\widetilde g$ are proper. It applies just as well to a homotopy $H\colon X\times I\to X$ with $H_1=\operatorname{id}_X$, since then $H_*\colon\pi_1(X\times I)\to\pi_1(X)$ is an isomorphism and the lift $\widetilde H\colon\widetilde X\times I=\widetilde{X\times I}\to\widetilde X$ is proper; we use this below.

Choose homotopies $H\colon gf\simeq\operatorname{id}_X$ and $K\colon fg\simeq\operatorname{id}_Y$. By Proposition 1.30 (the homotopy lifting property), applied to the covering $\widetilde X\to X$, to the homotopy $\widetilde X\times I\to X$, $(x,t)\mapsto H(p(x),t)$, whose $t=0$ term $H_0\circ p=gf\circ p$ has the lift $\widetilde g\widetilde f$, the homotopy $H$ lifts to a homotopy (proper, by the lemma applied to $H\colon X\times I\to X$)
$$
\widetilde H\colon\widetilde X\times I\longrightarrow\widetilde X,
\qquad
\widetilde H_0=\widetilde g\widetilde f .
$$
For each $x\in\widetilde X$ the point $\widetilde H_1(x)$ lies over $x$, and a deck transformation is determined by its value at one point (Proposition 1.34), so there is a single $\gamma\in\pi_1(X,x_0)$ — identified with the deck group of $\widetilde X$ by Proposition 1.39 — such that
$$
\widetilde H_1=\gamma .
$$
So $H$ lifts to a proper homotopy $\widetilde g\widetilde f\simeq_p\gamma$, and *not* in general to one ending at $\operatorname{id}_{\widetilde X}$. This is the point the original step glossed over; the deck transformation is absorbed by changing the lift of $g$. Set
$$
\widetilde G:=\gamma^{-1}\widetilde g .
$$
Since $\gamma^{-1}$ is a deck transformation of $\widetilde X$, the map $\widetilde G$ is again a lift of $g$, hence proper by the lemma; and $\gamma^{-1}\widetilde H$ is a proper homotopy (a proper homotopy followed by the homeomorphism $\gamma^{-1}$), giving
$$
\widetilde G\widetilde f=\gamma^{-1}\widetilde g\widetilde f\ \simeq_p\ \gamma^{-1}\gamma=\operatorname{id}_{\widetilde X}.
$$
In the same way $K$ lifts to a proper homotopy $\widetilde f\widetilde g\simeq_p\delta$ with $\delta\in\pi_1(Y,y_0)$. By equivariance of $\widetilde f$ and $f_*(\gamma^{-1})=f_*(\gamma)^{-1}$,
$$
\widetilde f\widetilde G=\widetilde f\gamma^{-1}\widetilde g=f_*(\gamma)^{-1}\widetilde f\widetilde g\ \simeq_p\ f_*(\gamma)^{-1}\delta=:\varepsilon\in\pi_1(Y,y_0),
$$
a proper homotopy because $f_*(\gamma)^{-1}$ is a homeomorphism of $\widetilde Y$. Thus $\widetilde f$ has the left proper homotopy inverse $\widetilde G$ and the right proper homotopy inverse $\widetilde G\varepsilon^{-1}$:
$$
\widetilde G\widetilde f\simeq_p\operatorname{id}_{\widetilde X},
\qquad
\widetilde f\,(\widetilde G\varepsilon^{-1})\simeq_p\varepsilon\varepsilon^{-1}=\operatorname{id}_{\widetilde Y}.
$$
(In the homotopy category of spaces and proper maps, $AL\simeq1$ and $AR\simeq1$ imply $AL\simeq AL(AR)=A(LA)R\simeq A\cdot1\cdot R=AR\simeq1$; take $A=\widetilde f$, $L=\widetilde G$, $R=\widetilde G\varepsilon^{-1}$.) Hence
$$
\widetilde f\widetilde G\simeq_p\operatorname{id}_{\widetilde Y}
\qquad\text{as well,}
$$
so $\widetilde G$ is a two-sided proper homotopy inverse of $\widetilde f$. Therefore $\widetilde f$ and $\widetilde G$ are proper maps and proper homotopy inverses.
```

## Note on the final paragraph of the card

The card's closing paragraph is *"Thus $\widetilde f$ and $\widetilde g$ are proper maps and proper
homotopy inverses. Therefore"* followed by the boxed conclusion. It should read **"$\widetilde f$ and
$\widetilde G$"**, exactly as the last line of the replacement above; the boxed conclusion
$\widetilde X\simeq_{\mathrm{proper}}\widetilde Y$ is unchanged (a proper homotopy equivalence with
inverse $\widetilde G$ is one with the original inverse $\widetilde g$ composed with a homeomorphism).

### Why this closes the gaps

* Lift compatibility is now *proved*: $\widetilde H_1$ is shown to be a deck transformation, using only
  that it covers $\operatorname{id}_X$ (so it maps fibres to fibres and is bijective) and that deck
  transformations are determined by one value (Prop. 1.34, restated by Hatcher on p. 62 before Prop.
  1.39). The correction $\widetilde G=\gamma^{-1}\widetilde g$ is a lift of $g$ because post-composition
  with a deck transformation of the *target* does not change the projection. Both composites are then
  produced, not assumed: $\widetilde G\widetilde f\simeq_p\operatorname{id}$ from $H$, and
  $\widetilde f\widetilde G\simeq_p\operatorname{id}$ by the elementary two-out-of-three computation
  displayed above, using $\widetilde f\widetilde G\simeq_p\varepsilon$.
* Every properness assertion is now an instance of one proved lemma, whose only input is Proposition
  A.1 ("a compact subspace of a CW complex is contained in a finite subcomplex", AT.txt 25888–25891) and
  the freeness of the deck action (Prop. 1.34). The hypothesis that $h_*$ be injective is used exactly
  where it is needed, in passing from finitely many $\beta$ to finitely many $\alpha$.
* No statement is weakened: the conclusion is the exercise's, proper homotopy equivalence of the
  universal covers.
