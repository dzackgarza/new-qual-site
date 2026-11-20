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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the proper homotopy equivalence of universal covers, which is what Queue D asks for on this card. The equivariance, the properness lemma (as a step with three substeps: the cell structure of the covers, the finiteness of the cells meeting a preimage, and properness with its counterexample), the properness of the two lifts, the lift of the homotopy to a proper homotopy ending at a deck transformation, the absorption of that deck transformation, and the two-sided conclusion are separate steps. The prose's inline Lemma is now step <1>2 with its proof split into substeps; its two unstated uses are now said: injectivity of h_* is what embeds the deck group of W into that of Z, and the counterexample showing the hypothesis cannot be dropped sits inside the properness substep. All six locators were re-read against the book: Proposition 3H.5 printed p. 334, Proposition 1.39 p. 71, Proposition 1.34 p. 62, Proposition 1.30 p. 60, Proposition A.1 p. 520, Theorem A.6 p. 524; the exercise is on printed p. 336. No retained set covers §3.H. No statement repair.
---

::: {.problem}
Show that if finite connected CW complexes $X$ and $Y$ are homotopy equivalent, then their universal covers $\tilde{X}$ and $\tilde{Y}$ are proper homotopy equivalent.
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout hold nothing from §3.H. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §3.H Exercise 4. A map is *proper* when the preimage of every compact set is compact, and a *proper homotopy* is a homotopy that is itself a proper map.

Let $f:X\to Y$ and $g:Y\to X$ be homotopy inverses between finite connected CW complexes, and let $\widetilde f:\widetilde X\to\widetilde Y$, $\widetilde g:\widetilde Y\to\widetilde X$ be lifts to universal covers.

::: pf

::: {.pf-step #equivariance}
$\widetilde f(\alpha x)=f_*(\alpha)\widetilde f(x)$ for $\alpha\in\pi_1(X,x_0)$, after identifying $\pi_1$ with the deck groups; likewise for $\widetilde g$.

::: pf-proof
Both sides of the displayed identity are maps $\widetilde X\to\widetilde Y$ covering $f\circ p_X=p_Y\circ\widetilde f$: the left side because $\alpha$ is a deck transformation of $\widetilde X$ and $\widetilde f$ is equivariant up to the induced map, the right because $f_*(\alpha)$ is a deck transformation of $\widetilde Y$. They agree at a chosen $\widetilde x_0$, so Proposition 1.34, gives equality. That a deck transformation is determined by its value at one point is the same proposition.
:::

:::

::: {.pf-step #lemma}
If $W,Z$ are finite CW complexes, $h:W\to Z$ is a map, and $h_*:\pi_1(W)\to\pi_1(Z)$ is injective, then any lift $\widetilde h:\widetilde W\to\widetilde Z$ is proper.

::: pf-proof

::: {.pf-step #cells}
Every cell of $\widetilde Z$ is $\beta\tilde e$ for a unique $\beta\in\pi_1(Z)$ and a unique cell $e$ of $Z$, and likewise for $\widetilde W$.

::: pf-proof
Give $\widetilde W,\widetilde Z$ the CW structures lifting those of $W,Z$, as in Hatcher's proof of Proposition 3H.5. Fix one lift $\tilde e$ of each cell $e$. A deck transformation is determined by its value at one point and a nontrivial one fixes no point (Proposition 1.34), so the translates $\beta\tilde e$ cover all cells and the pair $(\beta,e)$ is unique. Injectivity of $h_*$ is what makes the deck group of $\widetilde W$ sit inside that of $\widetilde Z$ under $h_*$, so the equivariance of step [](#equivariance){.pf-ref} relates the two cell structures.
:::

:::

::: {.pf-step #finitely-many}
For compact $C\subset\widetilde Z$ and a cell $e$ of $W$, only finitely many cells $\alpha\tilde e$ of $\widetilde W$ meet $\widetilde h^{-1}(C)$.

::: pf-proof
$C$ lies in a finite subcomplex $c_1\cup\cdots\cup c_m$ by Proposition A.1, hence meets only finitely many cells. Put $L_e=\widetilde h(\tilde e)$, compact. If $\alpha\tilde e$ meets $\widetilde h^{-1}(C)$ then by equivariance $\emptyset\ne h_*(\alpha)L_e\cap C$, so $L_e$ meets $\alpha^{-1}c_j$ for some $j$; $L_e$ is compact so it meets only finitely many cells $d_1,\dots,d_r$, and writing $d_k=\beta_k\tilde e_k$, $c_j=\gamma_k\tilde e_k$ uniquely, the equation $\alpha^{-1}c_j=d_k$ forces $\alpha=\gamma_k\beta_k^{-1}$, which gives only finitely many $\alpha$. Since $W$ has finitely many cells $e$, only finitely many cells in total occur.
:::

:::

::: {.pf-step #proper}
$\widetilde h$ is proper.

::: pf-proof
By step [](#finitely-many){.pf-ref} the set $\widetilde h^{-1}(C)$ meets only finitely many cells, so it lies in a finite subcomplex; it is closed because $\widetilde h$ is continuous and $C$ is compact, hence compact. So the preimage of every compact set is compact. The hypothesis that $h_*$ be injective cannot be dropped: the pinch $S^1\vee S^1\to S^1$ induces $\ZZ*\ZZ\twoheadrightarrow\ZZ$, and its lift to universal covers is a map from the $4$-valent tree onto $\RR$ whose fibre over a vertex is infinite, hence not proper.
:::

:::

The three substeps establish the criterion, which the rest of the proof uses.
:::

:::

::: {.pf-step #proper-lifts}
$\widetilde f$ and $\widetilde g$ are proper.

::: pf-proof
A homotopy equivalence induces an isomorphism on $\pi_1$, so $f_*$ is an isomorphism and injective, and $g_*$ is injective because $(gf)_*$ is an isomorphism. The lemma of step [](#lemma){.pf-ref} therefore applies to both.
:::

:::

::: {.pf-step #homotopy-deck}
A homotopy $H:gf\simeq\mathrm{id}_X$ lifts to a proper homotopy $\widetilde H:\widetilde X\times I\to\widetilde X$ from $\widetilde g\widetilde f$ to a deck transformation $\gamma$.

::: pf-proof
$X\times I$ is again a finite CW complex by Theorem A.6; its universal cover is $\widetilde X\times I$ because $I$ is simply connected; and $H_*$ on $\pi_1(X\times I)\cong\pi_1(X)$ is an isomorphism, so the lemma gives that the lift $\widetilde H$ of $H$ is proper. For existence, the homotopy $\widetilde X\times I\to X$, $(x,t)\mapsto H(p(x),t)$, has $t=0$ term $H_0\circ p=gf\circ p$, which is covered by the lift $\widetilde g\widetilde f$, so by the homotopy lifting property (Proposition 1.30) it lifts with $\widetilde H_0=\widetilde g\widetilde f$. For each $x$ the point $\widetilde H_1(x)$ lies over $p(x)$, so $\widetilde H_1$ is a deck transformation, and it is a single one because a deck transformation is determined by its value at one point.
:::

:::

::: {.pf-step #absorb}
With $\widetilde G=\gamma^{-1}\widetilde g$ one has $\widetilde G\widetilde f\simeq_p\mathrm{id}_{\widetilde X}$, and $\widetilde G$ is a lift of $g$, hence proper.

::: pf-proof
$\widetilde G$ is a lift of $g$ because $\gamma^{-1}$ is a deck transformation and $p\circ\gamma^{-1}=p$, so it is proper by step [](#proper-lifts){.pf-ref}. Composing the proper homotopy of step [](#homotopy-deck){.pf-ref} with the homeomorphism $\gamma^{-1}$ gives a proper homotopy $\widetilde G\widetilde f\simeq_p\gamma^{-1}\gamma=\mathrm{id}_{\widetilde X}$. Note that the lift of $H$ ends at a deck transformation and not at the identity: that is why the lift of $g$ has to be changed.
:::

:::

::: {.pf-step #two-sided}
$\widetilde f$ and $\widetilde G$ are proper homotopy inverses, so $\widetilde X\simeq_{\mathrm{proper}}\widetilde Y$.

::: pf-proof
Let $K:fg\simeq\mathrm{id}_Y$ lift to a proper homotopy $\widetilde f\widetilde g\simeq_p\delta$ with $\delta$ a deck transformation, by the argument of step [](#homotopy-deck){.pf-ref} with $Y$ in place of $X$. By equivariance and $f_*(\gamma^{-1})=f_*(\gamma)^{-1}$,
$$
\widetilde f\widetilde G=\widetilde f\gamma^{-1}\widetilde g=f_*(\gamma)^{-1}\widetilde f\widetilde g\simeq_p f_*(\gamma)^{-1}\delta=:\varepsilon\in\pi_1(Y),
$$
a proper homotopy because $f_*(\gamma)^{-1}$ is a homeomorphism of $\widetilde Y$. Then $\widetilde G\varepsilon^{-1}$ is proper and $\widetilde f(\widetilde G\varepsilon^{-1})\simeq_p\varepsilon\varepsilon^{-1}=\mathrm{id}_{\widetilde Y}$. So $\widetilde f$ has a left proper homotopy inverse $\widetilde G$ and a right one $\widetilde G\varepsilon^{-1}$. In the homotopy category of spaces and proper maps, $AL\simeq1$ and $AR\simeq1$ imply $AL\simeq AL(AR)=A(LA)R\simeq A\cdot1\cdot R=AR\simeq1$, so with $A=\widetilde f$, $L=\widetilde G$, $R=\widetilde G\varepsilon^{-1}$ we get $\widetilde f\widetilde G\simeq_p\mathrm{id}_{\widetilde Y}$ as well. Hence $\widetilde G$ is a two-sided proper homotopy inverse of the proper map $\widetilde f$, that is $\widetilde X\simeq_{\mathrm{proper}}\widetilde Y$.
:::

:::

:::
:::
