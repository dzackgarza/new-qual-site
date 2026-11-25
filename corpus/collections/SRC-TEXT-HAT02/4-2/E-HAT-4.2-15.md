---
schema: qual/card@1
id: E-HAT-4.2-15
kind: problem
title: "Simply-connected closed 3-manifolds are $S^3$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §4.2. Read against Hatcher, Exercise 15 of §4.2, printed p. 390 with
    its bracketed hint — §4.2's exercises are 1--12 on p. 389, 13--23 on p. 390, 24--29 on p. 391
    and 30--39 on p. 392, checked at PDF pages 398--401 of the held book — and the printed page is
    added, the card having had none. Checked: $H_1=0$ by simple connectivity, $H_2\cong H^1=0$ by
    Poincaré duality and the universal coefficient theorem, and $H_0=H_3=\ZZ$, so $M$ is a homology
    3-sphere; then $\pi_2=0$ by Hurewicz (otherwise it would be the first nonzero higher group and
    would map isomorphically to $H_2=0$), $\pi_3\cong H_3=\ZZ$ by Hurewicz applied to the
    2-connected $M$, and a map $S^3\to M$ carrying a generator is an isomorphism on $H_3$ and hence
    on all homology groups, so homology Whitehead applies — both spaces having CW type, which is the
    hint's Corollary A.12. No defect.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 15. One repair in step `homology`: Poincaré duality was applied
    as $H_i\cong H_{3-i}$ and then the universal coefficient theorem with $H^2$; but
    $H^2\cong\operatorname{Hom}(H_2,\ZZ)\oplus\operatorname{Ext}(H_1,\ZZ)=0$ with $H_1=0$ gives
    only that $H_2$ has no free part, not that it vanishes. The step now pairs the correct degrees:
    $H_2\cong H^1$, $H^1\cong\operatorname{Hom}(H_1,\ZZ)\oplus\operatorname{Ext}(H_0,\ZZ)=0$
    because $H_1=0$ and $H_0$ is free, so $H_2=0$. The rest of the proof reads correct. The provenance
    sentence is corrected: Sam's §4.2 Exercise 15 is retained and covers the exercise, so the claim
    that no retained set does is false; the card's own argument is kept.
---

::: {.problem}
Show that a closed simply-connected 3-manifold is homotopy equivalent to $S^3$. [Use Poincaré duality, and also the fact that closed manifolds are homotopy equivalent to CW complexes, from Corollary A.12 in the Appendix. The stronger statement that a closed simply-connected 3-manifold is homeomorphic to $S^3$ is the Poincaré conjecture, finally proved by Perelman. The higher-dimensional analog, that a closed $n$-manifold homotopy equivalent to $S^n$ is homeomorphic to $S^n$, had been proved earlier for all $n \geq 4$.]
:::

::: {.solution}
A retained solution covers this exercise: **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.2 Exercise 15** (`tmp/sources/hatcher-solutions-sam-2008.md`), whose §4.2 numbering is Hatcher's. Guanyu Li's set ends with §3.3, DeMason's M382C problem set has §4.2 Exercises 1, 2, 14 and 27 only (recorded from an earlier reading of the retained PDF), and the Stanford 215C sets cover §3.B and §3.3. The card's argument is its own, from Poincaré duality (Theorem 3.30), Corollary A.12, the Hurewicz theorem (Theorem 4.32) and Corollary 4.33, and it is kept because it is correct.

::: pf

::: {.pf-step #homology}
$H_0(M;\ZZ)\cong H_3(M;\ZZ)\cong\ZZ$ and $H_1(M;\ZZ)=H_2(M;\ZZ)=0$.

::: pf-proof
$M$ is a closed connected orientable $3$-manifold, so Poincaré duality, Theorem 3.30, gives $H_i(M;\ZZ)\cong H^{3-i}(M;\ZZ)$; in particular $H_0\cong H^3$, $H_1\cong H^2$ and $H_2\cong H^1$. Since $M$ is simply connected, $H_1(M;\ZZ)=0$ by the Hurewicz theorem, so $H^2=0$ and $H_1=0$; and the universal coefficient theorem, Theorem 3.2, gives $H^1\cong\operatorname{Hom}(H_1,\ZZ)\oplus\operatorname{Ext}(H_0,\ZZ)=0$ because $H_1=0$ and $H_0$ is free. Hence $H_2\cong H^1=0$. (The vanishing of $H^2$ alone would give only that $H_2$ has no free part.)
:::
:::

::: {.pf-step #pi-two}
$\pi_2(M)=0$.

::: pf-proof
$M$ is simply connected, so the Hurewicz theorem in the form of Theorem 4.32 identifies $\pi_2(M)$ with $H_2(M;\ZZ)$, which vanishes by step [](#homology){.pf-ref}.
:::
:::

::: {.pf-step #pi-three}
$\pi_3(M)\cong H_3(M;\ZZ)\cong\ZZ$.

::: pf-proof
By steps [](#homology){.pf-ref} and [](#pi-two){.pf-ref} the space $M$ is $2$-connected, so Theorem 4.32 applies in degree $3$ and gives $\pi_3(M)\cong H_3(M;\ZZ)\cong\ZZ$.
:::
:::

::: {.pf-step #map}
There is a map $f:S^3\to M$ inducing an isomorphism on $H_3$ and hence on every homology group.

::: pf-proof
Choose $f$ representing a generator of $\pi_3(M)\cong\ZZ$; under the Hurewicz isomorphism of step [](#pi-three){.pf-ref} this class corresponds to a generator of $H_3(M;\ZZ)$, so $f_*:H_3(S^3)\to H_3(M)$ is an isomorphism. In the remaining degrees $H_0$ is $\ZZ$ for both and $H_1,H_2$ vanish for both by step [](#homology){.pf-ref}, so $f_*$ is an isomorphism in every degree.
:::
:::

::: {.pf-step #whitehead}
$M\simeq S^3$.

::: pf-proof
$M$ is homotopy equivalent to a CW complex by Corollary A.12, and $S^3$ is one; both are simply connected, so Corollary 4.33 applies to $f$ and gives a homotopy equivalence.
:::
:::

:::
:::
