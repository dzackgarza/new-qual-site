---
schema: qual/card@1
id: E-HAT-4.2-39
kind: problem
title: "Indeterminacy of Toda brackets"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 39; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. The two variation computations are now
    steps with their reasons: the nullhomotopies of hg form a torsor over pi^s_{j+k+1}, and the
    change of representative is composition on the left with f, giving f alpha; the nullhomotopies
    of gf similarly give beta h, which equals +- h beta in the stable homotopy ring, so the
    subgroup is the same. Added that the two choices are independent and exhaustive, which is what
    makes the set of values a coset rather than merely a set with two families of translations.
    Recorded in the first step that the construction of the bracket itself is not re-derived here,
    only the dependence on the two nullhomotopies; the card does not claim a proof of the
    existence of the bracket. Statement unchanged; the card says the argument is its own.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    One degree corrected, from an independent review. The step wrote the composite $hg$ as
    $hg\colon S^{i+j}\to\bullet$ while calling the torsor of nullhomotopies a $\pi_{j+k+1}$-torsor;
    $hg$ has degree $j+k$, so its source is $S^{j+k}$, and the step now says so. The graded sign in
    the stable ring, $\beta h=(-1)^{|\beta||h|}h\beta$, and the two indeterminacy subgroups,
    $f\cdot\pi^s_{j+k+1}$ and $h\cdot\pi^s_{i+j+1}$, are unchanged and correct.
---

::: {.problem}
Show that the indeterminacy of a Toda bracket $\langle f, g, h \rangle$ with $f \in \pi_i^s$, $g \in \pi_j^s$, $h \in \pi_k^s$ is the subgroup $f \cdot \pi_{j+k+1}^s + h \cdot \pi_{i+j+1}^s$ of $\pi_{i+j+k+1}^s$.
:::

::: {.solution}
A Toda bracket is well defined only up to the choices of the two nullhomotopies, and this card computes how the value changes when they are varied: changing the nullhomotopy of $hg$ changes the representative by $f\alpha$ with $\alpha$ stable of degree $j+k+1$, and changing the nullhomotopy of $gf$ changes it by $\beta h$ with $\beta$ of degree $i+j+1$. The two choices are independent, and passing to the stable range turns $\beta h$ into $h\beta$ up to the graded sign, so the indeterminacy is the displayed subgroup. The argument is this card's own: no retained solution set covers this exercise.

::: pf

::: {.pf-step #construction}
A representative of $\langle f,g,h\rangle$ is obtained by choosing nullhomotopies of $hg$ and of $gf$ and gluing the resulting extensions across the two cones; on the level of spectra, the choices are a nullhomotopy of $hg$ and a nullhomotopy of $gf$.

::: pf-proof
This is the standard construction of the Toda bracket: if $gf\simeq\ast$ and $hg\simeq\ast$, the composite $hgf$ can be built in two ways, one extending $hg$ over the cone on $f$ and one extending $gf$ over the cone on $h$, and the difference of the two yields a class in the next degree. In the stable range all the constructions commute with suspension, so the bracket is a stable operation and its values form a coset of a subgroup of $\pi^s_{i+j+k+1}$. Nothing more about the construction is used below than that it depends on exactly these two nullhomotopies.
:::

:::


::: {.pf-step #first}
Two choices of nullhomotopy of $hg$ differing by $\alpha\in\pi^s_{j+k+1}$ give representatives differing by $f\alpha\in f\cdot\pi^s_{j+k+1}$.

::: pf-proof
The nullhomotopies of $hg$ — a map of degree $j+k$, so of the sphere $S^{j+k}$ — form a torsor over $\pi_{j+k+1}$: the difference of two nullhomotopies of the same map is the class of a map on the cone, i.e. of $S^{j+k+1}$, and in the stable range that group is $\pi^s_{j+k+1}$ with no dependence on $i$. Replacing the nullhomotopy of $hg$ by another changes the gluing only in the part of the construction that extends over the cone on $f$, which is composing on the left with $f$; hence the representative changes by $f\alpha$.
:::

:::


::: {.pf-step #second}
Two choices of nullhomotopy of $gf$ differing by $\beta\in\pi^s_{i+j+1}$ give representatives differing by $\beta h$, which in the stable range is $\pm h\beta\in h\cdot\pi^s_{i+j+1}$.

::: pf-proof
The same argument applied to the other nullhomotopy: two nullhomotopies of $gf$ differ by a class $\beta\in\pi^s_{i+j+1}$, and the change in the construction is composition on the right with $h$, so the representative changes by $\beta h$. Since $h$ is stable, the product in the stable homotopy ring satisfies $(-\beta)h=(\pm1)h\beta$ — precisely $\beta h=(-1)^{\abs\beta\abs h}h\beta$ for stable classes of the indicated degrees — so the set of values $\beta h$ is the subgroup $h\cdot\pi^s_{i+j+1}$ up to sign, hence the same subgroup additively.
:::

:::


::: {.pf-step #independence}
The two choices are independent, and they are the only choices entering the construction.

::: pf-proof
A pair of nullhomotopies determines a representative, and every representative arises from such a pair; varying one nullhomotopy while holding the other fixed varies the representative by the corresponding subgroup, and the two variations can be performed separately. Hence the set of values is the set of sums of a fixed representative and an element of $f\cdot\pi^s_{j+k+1}+h\cdot\pi^s_{i+j+1}$.
:::

:::


::: {.pf-step #conclusion}
The indeterminacy of $\langle f,g,h\rangle$ is the subgroup $f\cdot\pi^s_{j+k+1}+h\cdot\pi^s_{i+j+1}$ of $\pi^s_{i+j+k+1}$.

::: pf-proof
By steps [](#first){.pf-ref} and [](#second){.pf-ref} the values of the bracket form a coset of the sum of the two subgroups, and by step [](#independence){.pf-ref} nothing else varies; a coset of a subgroup is determined by that subgroup, which is the indeterminacy as defined.
:::

:::

:::
:::
