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
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Citation convention. Sources on this card are cited by chapter, section and numbered statement
    only, and the statement and solution above cite every source by its numbered statement. The
    events dated before today are left as their sessions wrote them, which QUAL-11 requires, so a
    locator in one of them stands as a historical record and is superseded by the citation now on
    the card. This event records the convention and claims no further reading: the
    mathematics of the card is as those events describe it.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The body's clause "the Hatcher sets in the checkout hold nothing from §4.3" was false: Sam's
    set holds eighteen of the twenty-four exercises. The claim that no retained set covers
    Exercise 10 is true, Sam skipping it. Only the false clause is removed; the argument is
    unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 10, printed p. 419,
    and against the action convention of p. 342. The transport the card defines --- lift
    the homotopy that moves the basepoint along beta and leaves the sphere constant ---
    is an anti-action, as an independent report from the swarm found and as recomputing
    the defining square confirms: its boundary is a·beta·alpha_1^{-1}·beta^{-1}, so
    alpha_1 = beta^{-1}·alpha, while Hatcher's action of a loop delta is [alpha]->[delta
    alpha] = delta·alpha·delta^{-1} (p. 342, beta_delta beta_eta = beta_{delta eta}). The
    card's identity (beta gamma)·alpha = beta·(gamma·alpha) is therefore false: the true
    law is T_{beta gamma} = T_gamma T_beta, and the composite pi_1(F) -> Aut is the action
    of beta^{-1}, not of beta. Repaired by proving the reversed composition law in step
    #homomorphism, by defining the action as beta -> T_{beta^{-1}} in a new step #action
    (with T_beta = beta_{beta^{-1}} read off the square), and by rewriting #restriction as
    T_{beta^{-1}} = beta_beta. Statement unchanged. Not checked: nothing outside this
    exercise.
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
No retained solution set covers this exercise; Sam's §4.3 skips Exercise 10. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.3 Exercise 10, and it uses only the homotopy lifting property of the fibration.

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
Transport along a product of loops reverses the order: $T_{\beta\gamma}=T_{\gamma}\circ T_{\beta}$ for loops $\beta,\gamma$ at $e_0$.

::: pf-proof
Concatenate $\beta$ then $\gamma$ and lift the resulting homotopy as in step [](#transport){.pf-ref}. The lift restricted to $S^n\times[0,\tfrac12]$, reparametrized over $[0,1]$, is exactly the lift used to define $T_\beta$, so at $t=\tfrac12$ the sphere carries the class $T_\beta[\alpha]$, based at $\beta(1)$. Restricted to $S^n\times[\tfrac12,1]$, again reparametrized, it is the lift used to define $T_\gamma$ applied to that class, since the basepoint track there is $\gamma$. So the time-one class is $T_\gamma T_\beta[\alpha]$, and this holds for every $[\alpha]$.
:::

:::

::: {.pf-step #action}
$[\beta]\mapsto T_{\beta^{-1}}$ is a homomorphism $\pi_1(E,e_0)\to\operatorname{Aut}(\pi_n(F,e_0))$, and $T_{\beta^{-1}}$ is Hatcher's change-of-basepoint map $\beta_{\beta}$.

::: pf-proof
By step [](#homomorphism){.pf-ref}, $T_{(\beta\gamma)^{-1}}=T_{\gamma^{-1}\beta^{-1}}=T_{\beta^{-1}}T_{\gamma^{-1}}$, so $\Phi([\beta]):=T_{\beta^{-1}}$ is multiplicative; it is bijective with inverse $\Phi([\beta^{-1}])$ and depends only on $[\beta]$ by step [](#well-defined){.pf-ref}. For the identification, Hatcher defines $\gamma f$ for a path $\gamma$ from $x_0$ to $x_1$ and $f$ based at $x_1$ by shrinking $f$ to a concentric cube and inserting $\gamma$ on the radial shell, with $(\gamma\eta)f\simeq\gamma(\eta f)$ and, for $n=1$, $\gamma f=\gamma\cdot f\cdot\gamma^{-1}$; the action of is $[\alpha]\mapsto[\gamma\alpha]$. The transport of step [](#transport){.pf-ref} is the same construction with the basepoint track run backwards: for $n=1$ its defining square has boundary $\alpha\cdot\beta\cdot\alpha_1^{-1}\cdot\beta^{-1}\simeq1$, so $\alpha_1\simeq\beta^{-1}\alpha\beta=(\beta^{-1})\alpha$, and the two constructions agree for every $n$ because both are the unique lift of the same homotopy of the basepoint track, so $T_\beta[\alpha]=[(\beta^{-1})\alpha]=\beta_{\beta^{-1}}[\alpha]$ and $T_{\beta^{-1}}=\beta_{(\beta^{-1})^{-1}}=\beta_\beta$.
:::

:::

::: {.pf-step #restriction}
The composite $\pi_1(F,e_0)\to\pi_1(E,e_0)\to\operatorname{Aut}(\pi_n(F,e_0))$ is the usual action, so if $\pi_1(E)=0$ that action is trivial.

::: pf-proof
For $\beta$ a loop in $F$ the class $[\beta]$ lies in the image of $\pi_1(F,e_0)\to\pi_1(E,e_0)$, and the composite sends it to $T_{\beta^{-1}}=\beta_{(\beta^{-1})^{-1}}=\beta_\beta$, which is by definition the usual action of $[\beta]$ on $\pi_n(F,e_0)$. So the composite $\pi_1(F,e_0)\to\pi_1(E,e_0)\to\operatorname{Aut}(\pi_n(F,e_0))$ is the usual action, and it is trivial whenever $\pi_1(E,e_0)=0$, the homomorphism then having trivial domain.
:::

:::

:::
:::
