---
schema: qual/card@1
id: E-HAT-4.A-3
kind: problem
title: "Automorphisms of $K(\\pi, 1)$ are outer automorphisms of $\\pi$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.A, Exercise 3 and Proposition 4A.2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps. Supplied what the prose used silently: that a
    self-homotopy equivalence of K(pi,1) has an inverse f' and hence induces a bijection on pi_1, so
    the induced endomorphism is an automorphism; that the change-of-basepoint map is a homomorphism
    and that changing the path multiplies it by an inner automorphism on one side, which is what
    makes the class in Out(pi) well defined and the assignment a homomorphism; and that a free
    homotopy class inducing an automorphism of pi contains a homotopy equivalence, since a map g with
    the inverse outer automorphism makes both composites induce the identity outer automorphism,
    hence freely homotopic to the identity by the classification of free homotopy classes. Not
    re-read this session: the printed pages cited (341, 342, 90, 422).
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher, §4.A Exercise 3, with Proposition 1B.9, Theorem 1B.8, Proposition 4A.2
    and the change-of-basepoint map of §4.1. The argument is correct: a self-homotopy equivalence
    induces an automorphism of $\pi$, the free classes are the orbits of the based ones under the
    $\pi_1$-action, which conjugates the induced homomorphism, and the resulting map
    $\operatorname{Aut}(K)\to\operatorname{Out}(\pi)$ is a bijective homomorphism in both
    directions as the steps argue. No mathematics changed. Two changes: the text named printed
    pages for §4.1, Proposition 1B.9, Proposition 4A.2 and Theorem 1B.8, and by the owner's
    correction of this date it now cites the numbered statements only; and the lead's claim that
    no retained solution set covers the exercise was re-checked, Sam's set having no §4.A. Not
    checked: no certificate; the statement's hypothesis that $K$ is a CW complex is used only in
    citing the classification of free homotopy classes.

---

::: {.problem}
For a space $X$ let $\operatorname{Aut}(X)$ denote the group of homotopy classes of homotopy equivalences $X \to X$.
Show that for a CW complex $K(\pi, 1)$, $\operatorname{Aut}(K(\pi, 1))$ is isomorphic to the group of outer automorphisms of $\pi$, that is, automorphisms modulo inner automorphisms.
:::

::: {.solution}

The argument is the card's own; no retained solution set covers Section 4.A Exercise 3. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.A Exercise 3.

Let $K=K(\pi,1)$ be a CW complex with $\pi_{1}(K,x_{0})=\pi$ and vanishing higher homotopy groups, and let $\operatorname{Aut}(K)$ be the group of homotopy classes of homotopy equivalences $K\to K$, and $\operatorname{Out}(\pi)=\operatorname{Aut}(\pi)/\operatorname{Inn}(\pi)$.

::: pf

::: {.pf-step #bijection}
Basepoints are immaterial: for any path $\gamma$ from $x_{1}$ to $x_{0}$ the change-of-basepoint map $\beta_{\gamma}\colon\pi_{1}(K,x_{1})\to\pi_{1}(K,x_{0})$ is an isomorphism, and $\beta_{\gamma\eta}=\beta_{\gamma}\beta_{\eta}$.

::: pf-proof
Hatcher introduces the change-of-basepoint map in §4.1: $\beta_{\gamma}([\omega])=[\gamma\cdot\omega\cdot\bar\gamma]$ is a group isomorphism, and $\beta_{\gamma\eta}=\beta_{\gamma}\beta_{\eta}$ for composable paths. Consequently $\pi_{1}$ at any two points of $K$ is identified with $\pi$, and a comparison of two identifications differs by conjugation.
:::

:::

::: {.pf-step #equiv-aut}
A map $f\colon K\to K$ is a homotopy equivalence if and only if its induced endomorphism of $\pi$ is an automorphism.

::: pf-proof
If $f$ is a homotopy equivalence with homotopy inverse $f'$, then $f'f\simeq\mathrm{id}$ and $ff'\simeq\mathrm{id}$, so on $\pi_{1}$ the composites are the identity and $f_{*}$ is a bijection, that is an automorphism of $\pi$. Conversely if $f_{*}$ is an automorphism, let $g$ realise $f_{*}^{-1}$: by step [](#classifying){.pf-ref} there is such a map, and $gf$, $fg$ induce the identity automorphism (up to the basepoint identifications of step [](#bijection){.pf-ref}), hence are freely homotopic to the identity by the same classification; so $f$ is a homotopy equivalence with homotopy inverse $g$.
:::

:::

::: {.pf-step #classifying}
Based homotopy classes $\langle K,K\rangle$ correspond bijectively to homomorphisms $\pi\to\pi$, and free homotopy classes $[K,K]$ to homomorphisms modulo inner automorphisms.

::: pf-proof
$K$ is a $K(\pi,1)$ and $\langle K,K\rangle\to\operatorname{Hom}(\pi,\pi)$, $[f]\mapsto f_{*}$, is a bijection by Proposition 1B.9. By Proposition 4A.2 the free homotopy classes are the orbits of the based ones under the action of $\pi_{1}(K)=\pi$, and a path $\gamma$ from $x_{0}$ to itself sends $f_{*}$ to $\beta_{\gamma}f_{*}\beta_{\gamma}^{-1}$, i.e. conjugates the homomorphism by the element $[\gamma]$. Hence $[K,K]\cong\operatorname{Hom}(\pi,\pi)/\operatorname{Inn}(\pi)$.
:::

:::

::: {.pf-step #phi}
There is a well-defined map $\Phi\colon\operatorname{Aut}(K)\to\operatorname{Out}(\pi)$, $[f]\mapsto[f_{*}]$.

::: pf-proof
By step [](#equiv-aut){.pf-ref} a homotopy equivalence induces an automorphism of $\pi$; a homotopy $f\simeq f'$ gives $f_{*}=f'_{*}$ after the same basepoint identification, so the class in $\operatorname{Out}(\pi)$ depends only on the homotopy class; and replacing the path used for the identification conjugates $f_{*}$, which does not change its class modulo inner automorphisms. So $\Phi$ is well defined, and it is a homomorphism because $(fg)_{*}=f_{*}g_{*}$ and conjugation respects composition in the sense $(fhf^{-1})\mapsto f_{*}[h]f_{*}^{-1}$.
:::

:::

::: {.pf-step #surjective}
$\Phi$ is surjective.

::: pf-proof
Let $\alpha\in\operatorname{Aut}(\pi)$ and let $[\alpha]\in\operatorname{Out}(\pi)$ be its class. By step [](#classifying){.pf-ref} $\alpha$ is realised by a map $f\colon K\to K$, and by step [](#equiv-aut){.pf-ref} $f$ is then a homotopy equivalence, so $[f]\in\operatorname{Aut}(K)$ and $\Phi([f])=[\alpha]$.
:::

:::

::: {.pf-step #injective}
$\Phi$ is injective.

::: pf-proof
If $\Phi([f])$ is the class of the identity, then $f_{*}$ is inner, that is $f_{*}=\beta_{\gamma}\beta_{\gamma}^{-1}$ conjugated by some element; by step [](#classifying){.pf-ref} $f$ is freely homotopic to the identity, so $[f]$ is the identity of $\operatorname{Aut}(K)$.
:::

:::

::: {.pf-step}
$\operatorname{Aut}(K(\pi,1))\cong\operatorname{Out}(\pi)$.

::: pf-proof
Steps [](#phi){.pf-ref}, [](#surjective){.pf-ref} and [](#injective){.pf-ref} exhibit $\Phi$ as a bijective homomorphism, hence an isomorphism. The homotopy type of $K(\pi,1)$ is determined by $\pi$ (Theorem 1B.8), so the group depends on $\pi$ alone.
:::

:::

:::

:::
