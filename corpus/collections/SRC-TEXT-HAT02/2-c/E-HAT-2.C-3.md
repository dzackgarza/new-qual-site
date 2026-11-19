---
schema: qual/card@1
id: E-HAT-2.C-3
kind: problem
title: Conjugate-linear map on $\CC^{2k}$ induces fixed-point-free map on $\CP^{2k-1}$
classification:
  areas:
  - topology
  topics:
  - Lefschetz Fixed Point Theorem
  - Projective Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.C Exercise 3, printed page
    184; the statement matches word for word. Proof checked: the formula is
    conjugate-linear with F(λz) = λ̄F(z) and F² = −id on each coordinate pair, so F
    maps complex lines to complex lines and induces f on CP^{2k−1}; a fixed point
    would give F(z) = λz and hence −z = F²(z) = |λ|² z, impossible. This is the map
    Hatcher discusses on p. 180, where he also notes it is only conjugate-linear and
    that the induced CP^{2k−1} map has no fixed points. No defect.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 3 of §2.C, printed p. 184, in
    `tmp/sources/hatcher-2002-algebraic-topology.md`, and against DeMason, Hatcher 2.C.3, printed
    pp. 84--85. Two repairs of the rendering, neither to the mathematics. (1) The closing paragraph
    ended "Surjectivity and well-definedness on complex lines therefore leave no fixed point", which
    is not what the preceding steps show and mentions a surjectivity nothing uses; it now says that
    the steps give a well-defined self-map of $\CP^{2k-1}$ and that the fixed-point computation shows
    it has none. (2) It attributed the conjugate-linear construction to DeMason, who does not use
    conjugate-linearity: he checks bijectivity, that $F$ carries complex lines to complex lines by
    rewriting the real equations of a line, and then the fixed-point contradiction. The paragraph now
    says the formulation is this card's rewriting of his line-form argument. Checked in the card:
    $F(\lambda z)=\bar\lambda F(z)$ and $F^2=-\mathrm{id}$ pairwise, so $F$ is injective on lines and
    maps nonzero vectors to nonzero vectors; a fixed line gives $F(z)=\lambda z$ and then
    $-z=F^2(z)=\bar\lambda F(z)=\abs{\lambda}^2z$, impossible. No defect in the mathematics.

---

::: {.problem}
Verify that the formula $f(z_1, \cdots, z_{2k}) = (\bar{z}_2, -\bar{z}_1, \bar{z}_4, -\bar{z}_3, \cdots, \bar{z}_{2k}, -\bar{z}_{2k-1})$ defines a map $f: \CC^{2k} \to \CC^{2k}$ inducing a quotient map $\CP^{2k-1} \to \CP^{2k-1}$ without fixed points.
:::

::: {.solution}
Define
$$
F(z_1,\ldots,z_{2k})=(\bar z_2,-\bar z_1,\ldots,\bar z_{2k},-\bar z_{2k-1}).
$$

::: pf

::: pf-step

The map $F$ is conjugate-linear and satisfies
$$
F(\lambda z)=\bar\lambda F(z),
\qquad
F^2=-\operatorname{id}.
$$

::: pf-proof

Both identities follow by direct calculation on each coordinate pair $(z_{2j-1},z_{2j})$:
$$
(z_{2j-1},z_{2j})\mapsto(\bar z_{2j},-\bar z_{2j-1})
\mapsto(-z_{2j-1},-z_{2j}).
$$

:::

:::

::: pf-step

Hence $F$ induces a well-defined map
$$
f:\CP^{2k-1}\to\CP^{2k-1},
\qquad
f([z])=[F(z)].
$$

::: pf-proof

If $[z]=[\lambda z]$ with $\lambda\ne0$, then
$$
F(\lambda z)=\bar\lambda F(z),
$$
so $F(\lambda z)$ and $F(z)$ determine the same complex line. Also $F(z)\ne0$ for $z\ne0$ because $F^2=-\operatorname{id}$.

:::

:::

::: pf-step

The map $f$ has no fixed point.

::: pf-proof

If $[z]$ were fixed, then for some $\lambda\in\CC^*$ we would have
$$
F(z)=\lambda z.
$$
Applying $F$ and using conjugate-linearity gives
$$
-z=F^2(z)=F(\lambda z)=\bar\lambda F(z)=\abs{\lambda}^2z.
$$
Since $z\ne0$, this would imply $\abs{\lambda}^2=-1$, impossible.

:::

:::

:::

Thus the displayed conjugate-linear map induces a fixed-point-free self-map of $\CP^{2k-1}$.

The conjugate-linear construction and fixed-point computation are **Kenneth DeMason, *M382C Full Credit HW Problems* (2021)**, Hatcher 2.C.3, printed pp. 84--85, in the line form: he checks that $F$ is a bijection of $\CC^{2k}$, that it carries complex lines to complex lines by rewriting the real equations of a line, and that a fixed line would force $F(z)=\lambda z$ and hence a contradiction. The formulation here is the same argument in conjugate-linear coordinates — $F(\lambda z)=\bar\lambda F(z)$ and $F^2=-\mathrm{id}$ — with no new claim. Together the steps show that the formula induces a well-defined self-map of $\CP^{2k-1}$ and that it has no fixed point.


:::
