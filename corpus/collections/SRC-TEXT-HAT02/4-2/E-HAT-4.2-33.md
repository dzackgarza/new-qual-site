---
schema: qual/card@1
id: E-HAT-4.2-33
kind: problem
title: "Homotopy groups if all Hopf-like bundles existed"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 33; the stored statement matches.
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
    Rewritten as a Lamport structured proof, with one repair. The prose justified the
    splitting isomorphism $\pi_i(S^n)\cong\pi_i(S^{2n-1})\oplus\pi_{i-1}(S^{n-1})$ by
    "the fiber inclusion is nullhomotopic since $\pi_{n-1}(S^{2n-1})=0$", which controls one
    degree only; the card now names the hypothesis of Exercise 31 (nullity of the inclusion
    in every degree), records that it is an extra hypothesis not implied by that vanishing,
    notes where it is available ($n=2$, and the two Hopf bundles the exercise names), and
    proves from the long exact sequence alone the unconditional isomorphism for
    $i\le 2n-2$. The conclusion is unchanged and is stated as the counterfactual it is.
    Cited: Corollary 4.12 printed p. 349, Hurewicz printed p. 366, the bundle sequence printed
    p. 376, Exercises 31 and 33 printed p. 392. Not claimed: a retained solution set, so the
    argument is the card's own.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Two corrections to this date's earlier note, both from work done after the proof was
    written. (1) The card said no retained solution set covers the exercise; Steven V.
    Sam's set does, at Exercise 4.2.33, PDF p. 25, with the double induction on $i-n$ and
    $n$ that the card now follows and cites. (2) That note called the previous prose's
    justification of the splitting wrong, on the ground that vanishing of
    $\pi_{n-1}(S^{2n-1})$ "controls one degree only". That complaint is itself wrong and is
    withdrawn: the fiber inclusion is a *map* $S^{n-1}\to S^{2n-1}$ whose homotopy class is
    an element of $\pi_{n-1}(S^{2n-1})=0$, so the map is nullhomotopic, and a nullhomotopic
    map vanishes on every $\pi_j$ because its induced maps factor through the homotopy
    groups of a point. Exercise 31's hypothesis therefore does hold, the card's step now
    proves it that way, and the only thing the card adds to the set is the unconditional
    statement for $i\le 2n-2$ and that verification. Mathematics re-read; the exercise is
    on printed p. 392.
---

::: {.problem}
Show that if there were fiber bundles $S^{n-1} \to S^{2n-1} \to S^n$ for all $n$, then the groups $\pi_i(S^n)$ would be finitely generated free abelian groups computable by induction, and nonzero for $i \geq n \geq 2$.
:::

::: {.solution}
The published solution is **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), Exercise 4.2.33, PDF p. 25**, whose double induction on $i-n$ and $n$ this proof follows: the base cases $\pi_i(S^n)=0$ for $i<n$ and $\pi_n(S^n)=\ZZ$, and the step through Exercise 4.2.31. The card adds the verification of Exercise 31's hypothesis (below) and the part of the computation that does not need it. The statement is Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 33, printed p. 392; it is a counterfactual, and the hypothesis is not known to hold — such bundles exist only for $n=2,4,8$.

Throughout, assume fiber bundles $S^{n-1}\to S^{2n-1}\xrightarrow{p}S^n$ exist for every $n\ge2$, and let $\partial$ denote the boundary map of the long exact homotopy sequence of such a bundle.

::: pf

::: {.pf-step #exact}
For every $n\ge2$ and every $i$ the sequence
$$
\pi_i(S^{n-1})\longrightarrow\pi_i(S^{2n-1})\longrightarrow\pi_i(S^n)\xrightarrow{\ \partial\ }\pi_{i-1}(S^{n-1})\longrightarrow\pi_{i-1}(S^{2n-1})
$$
is exact.

::: pf-proof
The homotopy groups of a fiber bundle form the long exact sequence of the fibration (printed p. 376), with fibre $S^{n-1}$, total space $S^{2n-1}$ and base $S^n$.

:::

:::

::: {.pf-step #low}
For $i\le 2n-2$ the boundary map gives an isomorphism $\pi_i(S^n)\cong\pi_{i-1}(S^{n-1})$.

::: pf-proof
In the sequence of step [](#exact){.pf-ref}, $\pi_i(S^{2n-1})=0$ because $i<2n-1=\dim S^{2n-1}$ (Corollary 4.12, printed p. 349), and $\pi_{i-1}(S^{2n-1})=0$ because $i-1<2n-1$. Exactness then makes both the incoming and the outgoing map around $\pi_i(S^n)$ zero, so $\partial$ is injective and surjective.

:::

:::

::: {.pf-step #split}
If the inclusion $S^{n-1}\hookrightarrow S^{2n-1}$ is nullhomotopic, then $\pi_i(S^n)\cong\pi_i(S^{2n-1})\oplus\pi_{i-1}(S^{n-1})$ for all $i$.

::: pf-proof
This is Exercise 31 of §4.2, printed p. 392: for a fiber bundle $F\to E\to B$ whose fiber inclusion is homotopic to a constant map, the long exact sequence breaks into split short exact sequences, giving $\pi_i(B)\cong\pi_i(E)\oplus\pi_{i-1}(F)$. Its hypothesis holds here: the inclusion is a map $S^{n-1}\to S^{2n-1}$ whose homotopy class lies in $\pi_{n-1}(S^{2n-1})=0$, because $n-1<2n-1=\dim S^{2n-1}$ (Corollary 4.12, printed p. 349), so the inclusion is nullhomotopic as a map; and a nullhomotopic map induces the zero map on every $\pi_j$, its induced maps factoring through the homotopy groups of a point. So the short exact sequences split and the isomorphism holds in every degree. The two Hopf bundles $S^3\to S^7\to S^4$ and $S^7\to S^{15}\to S^8$ are the cases where the bundles are known to exist.

:::

:::

::: {.pf-step #finitely-generated}
Granting step [](#split){.pf-ref}, every $\pi_i(S^n)$ with $i\ge n\ge2$ is a finitely generated free abelian group, and its rank is computable by induction.

::: pf-proof
Induct on $i$; for fixed $i$ descend on $n$ from $i$ to $2$. The group $\pi_i(S^n)$ is $0$ for $n>i$, by Corollary 4.12 again. For $n\le i$, step [](#split){.pf-ref} writes $\pi_i(S^n)$ as a direct sum of $\pi_i(S^{2n-1})$ and $\pi_{i-1}(S^{n-1})$: the second has index $i-1<i$ and so is already known, and the first has sphere dimension $2n-1>n$, so it is already known in the descending induction on $n$ — it is $0$ when $2n-1>i$. A direct sum of finitely generated free abelian groups is finitely generated and free, and the rank of a free abelian group determines it, so the recursion computes the group, with base $\pi_n(S^n)\cong\ZZ$ by the Hurewicz theorem (printed p. 366).

:::

:::

::: {.pf-step #nonzero}
Granting step [](#split){.pf-ref}, $\pi_i(S^n)\ne0$ for $i\ge n\ge2$.

::: pf-proof
First, $\pi_j(S^2)\ne0$ for every $j\ge2$. For $j=2$ this is $\pi_2(S^2)\cong\ZZ$. For $j\ge3$, step [](#split){.pf-ref} for $n=2$ gives $\pi_j(S^2)\cong\pi_j(S^3)\oplus\pi_{j-1}(S^1)=\pi_j(S^3)$ because $\pi_{j-1}(S^1)=0$, and step [](#split){.pf-ref} for $n=3$ gives a surjection $\pi_j(S^3)\to\pi_{j-1}(S^2)$. Composing, a nonzero $\pi_{j-1}(S^2)$ forces $\pi_j(S^2)\ne0$, which is the induction on $j$.
For general $n$, step [](#split){.pf-ref} applied for $n,n-1,\ldots,3$ exhibits $\pi_i(S^n)$ as a direct sum containing a copy of $\pi_{i-n+2}(S^2)$, by $n-2$ applications of the second summand; that group is nonzero by the previous paragraph because $i-n+2\ge2$. A direct sum with a nonzero summand is nonzero.

:::

:::

::: {.pf-step #conclusion}
If such bundles existed for all $n$, the groups $\pi_i(S^n)$ would be finitely generated free abelian, computable by induction, and nonzero for $i\ge n\ge2$.

::: pf-proof
Steps [](#finitely-generated){.pf-ref} and [](#nonzero){.pf-ref} give the three assertions; the phrase "computable by induction" refers to the recursion of step [](#finitely-generated){.pf-ref}, which terminates because at each stage either a sphere dimension increases past $i$ or $i$ decreases. Step [](#low){.pf-ref} records the part of the computation that does not need the hypothesis of Exercise 31 at all.

:::

:::

:::
:::
