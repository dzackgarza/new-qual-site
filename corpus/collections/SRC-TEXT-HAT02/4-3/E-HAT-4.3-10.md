---
schema: qual/card@1
id: E-HAT-4.3-10
kind: problem
title: "Action of $\\pi_1(E)$ on $\\pi_n(F)$ for fibrations"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the action and its two properties, which is what Queue D asks for on this card. The transport is a step (the datum on the cofibration, the extension of its projection over the disc times the interval, and the lift), well-definedness is a step, the homomorphism property is a step with both the concatenation and the inverse, and the restriction to loops in the fibre and the vanishing when pi_1(E) = 0 is the last. No retained set covers this exercise; the card now says so. Locators checked: the exercise on printed p. 419. No statement repair.
---

::: {.problem}
Given a fibration $F \to E \to B$, use the homotopy lifting property to define an action of $\pi_1(E)$ on $\pi_n(F)$, a homomorphism $\pi_1(E) \to \operatorname{Aut}\bigl(\pi_n(F)\bigr)$, such that the composition $\pi_1(F) \to \pi_1(E) \to \operatorname{Aut}\bigl(\pi_n(F)\bigr)$ is the usual action of $\pi_1(F)$ on $\pi_n(F)$.
Deduce that if $\pi_1(E) = 0$, then the action of $\pi_1(F)$ on $\pi_n(F)$ is trivial.
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout hold nothing from §4.3. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.3 Exercise 10, printed p. 419, and it uses only the homotopy lifting property of the fibration.

Fix $e_0\in F=p^{-1}(b_0)$ and let $p:E\to B$ be the fibration.

::: pf

::: {.pf-step #transport}
For $[\beta]\in\pi_1(E,e_0)$ and $[\alpha]\in\pi_n(F,e_0)$ the homotopy lifting property produces a based map $\alpha_1:S^n\to F$, and $[\beta]\cdot[\alpha]:=[\alpha_1]$ defines an element of $\pi_n(F,e_0)$.

::: pf-proof
Represent $\alpha$ by a based map $S^n\to F$ and $\beta$ by a loop at $e_0$. On the subcomplex $S^n\times\{0\}\cup\{*\}\times I$ of $S^n\times I$, which is the inclusion of a cofibration, define a map to $E$ as $\alpha$ on $S^n\times\{0\}$ and as $\beta$ on $\{*\}\times I$; the two agree at $(*,0)$. Its composite with $p$ is $b_0$ on $S^n\times\{0\}$ and $p\beta(t)$ on $\{*\}\times I$, and the formula $(x,t)\mapsto p\beta(t)$ extends it over $S^n\times I$ because at $t=0$ it gives $p\beta(0)=b_0$ on all of $S^n$. The homotopy lifting property for the cofibration $S^n\times\{0\}\cup\{*\}\times I\subset S^n\times I$ lifts this homotopy, relative to the subspace, to $\widetilde H:S^n\times I\to E$ with $\widetilde H(-,0)=\alpha$ and $\widetilde H(*,t)=\beta(t)$. At $t=1$ the map $\alpha_1=\widetilde H(-,1)$ lands in $F$, since $p\alpha_1(x)=p\beta(1)=b_0$, and it is based, since $\alpha_1(*)=\beta(1)=e_0$.
:::

:::

::: {.pf-step #well-defined}
The class $[\alpha_1]$ depends only on $[\alpha]$ and $[\beta]$.

::: pf-proof
A homotopy of $\alpha$ rel basepoint, or of $\beta$ rel endpoints, changes the data on the subcomplex by a homotopy rel the subcomplex, and the homotopy lifting property applied to a homotopy of homotopies — equivalently the naturality of the lift in the data — carries the corresponding lifts to one another; so the resulting based maps $S^n\to F$ are homotopic. Hence the assignment is well defined on homotopy classes.
:::

:::

::: {.pf-step #homomorphism}
$[\beta]\mapsto\bigl([\alpha]\mapsto[\beta]\cdot[\alpha]\bigr)$ is a homomorphism $\pi_1(E,e_0)\to\operatorname{Aut}\bigl(\pi_n(F,e_0)\bigr)$.

::: pf-proof
Concatenating loops concatenates the transports: the lift for $\beta\gamma$ restricts over the first half of the $t$-interval to the lift used for $\gamma$ applied to $\alpha$, and over the second half to the lift for $\beta$ applied to that, by uniqueness of lifts rel the subcomplex; so $(\beta\gamma)\cdot\alpha=\beta\cdot(\gamma\cdot\alpha)$. Taking $\beta^{-1}$ gives the inverse operation, since $\beta\beta^{-1}$ is homotopic to the constant loop and the constant loop acts as the identity — its lift is the constant homotopy on $\alpha$. So the assignment is a homomorphism into the automorphism group.
:::

:::

::: {.pf-step #restriction}
The composite $\pi_1(F,e_0)\to\pi_1(E,e_0)\to\operatorname{Aut}(\pi_n(F,e_0))$ is the usual action, so if $\pi_1(E)=0$ that action is trivial.

::: pf-proof
A loop $\beta$ in $F$ has $p\beta$ constant at $b_0$, so the homotopy $(x,t)\mapsto p\beta(t)$ is the constant homotopy and its lift is a homotopy of $\alpha$ within $F$ from $\alpha$ to $\alpha_1$; that is exactly the basepoint-change action of $[\beta]\in\pi_1(F,e_0)$ on $\pi_n(F,e_0)$. Hence the composite is the usual action, by the very construction of that action, and it is the trivial action whenever $\pi_1(E,e_0)=0$, since the homomorphism then has trivial domain.
:::

:::

:::
:::
