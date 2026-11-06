---
schema: qual/card@1
id: E-HAT-3.H-4
kind: problem
title: "Proper homotopy equivalence of universal covers"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.H, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof repaired: lift compatibility, previously asserted, is now proved via the deck transformation of a lift of the identity and a two-out-of-three argument; the unproved properness step is replaced by an argument from Hatcher's Proposition A.1 and the free deck action. The unproved version fails for the pinch S^1 v S^1 -> S^1.
---

::: {.problem}
Show that if finite connected CW complexes $X$ and $Y$ are homotopy equivalent, then their universal covers $\tilde{X}$ and $\tilde{Y}$ are proper homotopy equivalent.
:::

::: {.solution}
Let
$$
f:X\to Y,
\qquad
g:Y\to X
$$
be homotopy inverse maps between finite connected CW complexes. Choose basepoints and lifts
$$
\widetilde f:\widetilde X\to\widetilde Y,
\qquad
\widetilde g:\widetilde Y\to\widetilde X.
$$
Since $f_*$ is an isomorphism on fundamental groups, after identifying the deck groups through $f_*$ the lift $\widetilde f$ is equivariant:
$$
\widetilde f(\gamma x)=f_*(\gamma)\widetilde f(x).
$$
Similarly for $\widetilde g$.

We first record the properness criterion that the argument actually needs. Its hypothesis that $h$ be injective on $\pi_1$ cannot be dropped: the pinch $S^1\vee S^1\to S^1$ induces $\ZZ*\ZZ\twoheadrightarrow\ZZ$, and its lift to universal covers is a map from the $4$-valent tree onto $\RR$ whose fibre over a vertex is infinite, hence not proper.

**Lemma.** Let $W$ and $Z$ be finite CW complexes, $h\colon W\to Z$ a map with $h(w_0)=z_0$, and $\widetilde h\colon\widetilde W\to\widetilde Z$ a lift of $h$ to universal covers with $\widetilde h(\widetilde w_0)=\widetilde z_0$. If $h_*\colon\pi_1(W,w_0)\to\pi_1(Z,z_0)$ is injective, then $\widetilde h$ is proper.

*Proof.* Give $\widetilde W,\widetilde Z$ the CW structures lifting those of $W,Z$ (as in Hatcher's proof of Proposition 3H.5, p. 334). Identify $\pi_1(W,w_0)$ and $\pi_1(Z,z_0)$ with the respective deck groups by Proposition 1.39 (p. 71). Then
$$
\widetilde h(\alpha x)=h_*(\alpha)\,\widetilde h(x)\qquad\text{for all }\alpha\in\pi_1(W,w_0),\ x\in\widetilde W :
$$
both sides are lifts of $h\circ p$ and they agree at $x=\widetilde w_0$, so Proposition 1.34 (p. 62) applies. Fix one lift $\tilde e\subset\widetilde Z$ of each cell $e$ of $Z$. Because a nontrivial deck transformation fixes no point (Proposition 1.34 again, p. 62; deck transformations are determined by their value at one point), every cell of $\widetilde Z$ is $\beta\tilde e$ for a *unique* $\beta\in\pi_1(Z,z_0)$ and a unique cell $e$; the same holds in $\widetilde W$.

Let $C\subset\widetilde Z$ be compact. By Proposition A.1 (p. 520) the set $C$ lies in a finite subcomplex, so it meets only finitely many cells, so $C$ lies in a finite subcomplex $c_1\cup\cdots\cup c_m$. Fix a cell $e$ of $W$, with lift $\tilde e$, and put $L_e:=\widetilde h(\tilde e)$, a compact subset of $\widetilde Z$. If a cell $\alpha\tilde e$ of $\widetilde W$ meets $\widetilde h^{-1}(C)$ then, by equivariance,
$$
\emptyset\neq\widetilde h(\alpha\tilde e)\cap C=h_*(\alpha)L_e\cap C .
$$
The set $S_e:=\{\beta\in\pi_1(Z,z_0):\beta L_e\cap C\neq\emptyset\}$ is finite: if $\beta L_e\cap C\neq\emptyset$ then $\beta L_e$ meets some $c_j$, so $L_e$ meets the cell $\beta^{-1}c_j$; by Proposition A.1 (p. 520) the compact set $L_e$ lies in a finite subcomplex, so it meets only finitely many cells $d_1,\dots,d_r$, and writing $d_k=\beta_k\tilde e_k$ and $c_j=\gamma_k\tilde e_k$ uniquely, $\beta^{-1}c_j=d_k$ forces $\beta=\gamma_k\beta_k^{-1}$. Hence only finitely many $\beta$ occur. Therefore the cells of $\widetilde W$ meeting $\widetilde h^{-1}(C)$ lie among the cells $\alpha\tilde e$ with $e$ a cell of $W$ (finitely many) and $\alpha\in h_*^{-1}(S_e)$, which is finite because $h_*$ is injective. So $\widetilde h^{-1}(C)$ meets only finitely many cells and is contained in a finite subcomplex; it is closed ($\widetilde h$ is continuous and $C$ is compact), hence compact. Thus $\widetilde h$ is proper. $\square$

A homotopy equivalence induces an isomorphism on $\pi_1$, so the lemma applies to $f$ and to $g$: $f_*$ is an isomorphism, and $g_*$ is injective because $(gf)_*$ is an isomorphism and $f_*$ is one. Hence the lifts $\widetilde f$ and $\widetilde g$ are proper. It applies just as well to a homotopy $H\colon X\times I\to X$ with $H_1=\operatorname{id}_X$: $X\times I$ is again a finite CW complex (Theorem A.6, p. 524), its universal cover is $\widetilde X\times I$ because $I$ is simply connected, $H_*\colon\pi_1(X\times I)\cong\pi_1(X)\to\pi_1(X)$ is an isomorphism, and so the lift $\widetilde H\colon\widetilde X\times I=\widetilde{X\times I}\to\widetilde X$ is proper; we use this below.

Choose homotopies $H\colon gf\simeq\operatorname{id}_X$ and $K\colon fg\simeq\operatorname{id}_Y$. By Proposition 1.30 (p. 60, the homotopy lifting property), applied to the covering $\widetilde X\to X$, to the homotopy $\widetilde X\times I\to X$, $(x,t)\mapsto H(p(x),t)$, whose $t=0$ term $H_0\circ p=gf\circ p$ has the lift $\widetilde g\widetilde f$, the homotopy $H$ lifts to a homotopy (proper, by the lemma applied to $H\colon X\times I\to X$)
$$
\widetilde H\colon\widetilde X\times I\longrightarrow\widetilde X,
\qquad
\widetilde H_0=\widetilde g\widetilde f .
$$
For each $x\in\widetilde X$ the point $\widetilde H_1(x)$ lies over $x$, and a deck transformation is determined by its value at one point (Proposition 1.34, p. 62), so there is a single $\gamma\in\pi_1(X,x_0)$ — identified with the deck group of $\widetilde X$ by Proposition 1.39, p. 71 — such that
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
so $\widetilde G$ is a two-sided proper homotopy inverse of $\widetilde f$. Therefore $\widetilde f$ and $\widetilde G$ are proper maps and proper homotopy inverses. Therefore
$$
\boxed{\widetilde X\simeq_{\mathrm{proper}}\widetilde Y.}
$$
:::
