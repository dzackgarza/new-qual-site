---
schema: qual/card@1
id: E-HAT-4.3-1
kind: problem
title: "Map $\\RP^\\infty \\to K(\\ZZ,2)$ trivial on homology"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 1; the stored statement matches.
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
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: $\CP^\infty$ represents $H^2(-;\ZZ)$, so
    the nonzero class $\nu$ is $f^*(c)$ for some $f$; $\widetilde H_i(\RP^\infty)=\ZZ/2$ in odd degrees
    and $0$ in even, against free groups in even degrees for $\CP^\infty$, so every homology
    homomorphism out of a torsion group into a free group is zero; and in degree $2$ the two groups
    sit in different UCT summands, $\Ext(\ZZ/2,\ZZ)$ for the projective space and
    $\Hom(\ZZ,\ZZ)$ for the complex one, whose splitting is not natural. Repaired: the earlier text
    introduced the class as $\nu$ and then wrote $f^*(c)=u\ne0$, leaving $u$ undefined; the card now
    uses $\nu$ throughout. Added: the reason a map with the stated pullback exists, the cellular
    computation behind both homology groups, and the explicit identification of the two UCT summands
    as the resolution of the apparent contradiction. No defect found in the statement, §4.3 Exercise
    1. No retained solution set covers it.
---

::: {.problem}
Show there is a map $\RP^\infty \to \CP^\infty = K(\ZZ, 2)$ which induces the trivial map on $\tilde{H}_*(-; \ZZ)$ but a nontrivial map on $\tilde{H}^*(-; \ZZ)$.
How is this consistent with the universal coefficient theorem?
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own; it uses that $\CP^\infty$ represents $H^2(-;\ZZ)$ and that the universal coefficient splitting is not natural. Write $\nu$ for the nonzero class of $H^2(\RP^\infty;\ZZ)\cong\ZZ/2$ and $c$ for the canonical generator of $H^2(\CP^\infty;\ZZ)$.

::: pf

::: {.pf-step #map}
There is a map $f\colon\RP^\infty\to\CP^\infty$ with $f^*(c)=\nu\ne0$.

::: pf-proof
$\CP^\infty=K(\ZZ,2)$, so homotopy classes of maps into it correspond to classes in $H^2(-;\ZZ)$: there is $f$ with $f^*(c)=\nu$, the class $\nu$ being nonzero. As $c$ generates $H^2(\CP^\infty;\ZZ)\cong\ZZ$, its pullback $\nu\ne0$ shows that $f^*$ is nonzero on reduced integral cohomology in degree $2$.
:::

:::

::: {.pf-step #homology}
$f_*=0$ on every reduced integral homology group.

::: pf-proof
$\widetilde H_i(\RP^\infty;\ZZ)\cong\ZZ/2$ for $i$ odd and $0$ for $i$ even, by the cellular chain complex of $\RP^\infty$ with one cell in each degree and boundary multiplication by $2$; $\widetilde H_i(\CP^\infty;\ZZ)$ is $\ZZ$ for $i$ even and positive and $0$ for $i$ odd. Every homomorphism from $\ZZ/2$ to a free abelian group is zero, and every homomorphism from $0$ is zero, so $f_*=0$ in every reduced degree.
:::

:::

::: {.pf-step #uct}
The universal coefficient sequence in degree $2$ splits as $H^2(X;\ZZ)\cong\operatorname{Hom}(H_2(X),\ZZ)\oplus\operatorname{Ext}(H_1(X),\ZZ)$, and the two groups in question occupy different summands.

::: pf-proof
For $X=\RP^\infty$ one has $H_2=0$ and $H_1=\ZZ/2$, so $H^2\cong\operatorname{Ext}(\ZZ/2,\ZZ)\cong\ZZ/2$, carried by the Ext summand. For $X=\CP^\infty$ one has $H_2=\ZZ$ and odd homology zero, so $H^2\cong\operatorname{Hom}(\ZZ,\ZZ)\cong\ZZ$, carried by the Hom summand.
:::

:::

::: {.pf-step}
$\boxed{f_*=0\text{ on reduced homology while }f^*\ne0\text{ on reduced cohomology, consistently with the UCT}}$.

::: pf-proof
Steps [](#map){.pf-ref}, [](#homology){.pf-ref} and [](#uct){.pf-ref} give the two assertions and the degree-wise computation. There is no contradiction: the universal coefficient theorem's short exact sequence is natural but its splitting is not, so a map that is zero on homology can still act nontrivially on the Ext summand of cohomology; concretely $f^*$ carries $c$, which lies in the Hom summand for $\CP^\infty$, to $\nu$, which lies in the Ext summand for $\RP^\infty$, and the two summands are not matched by any natural splitting.
:::

:::

:::
:::
