---
schema: qual/card@1
id: P-ULHPN
kind: problem
title: $\operatorname{Ext}(\ZZ\oplus\ZZ/2\oplus\ZZ/3,\ZZ\oplus\ZZ/4\oplus\ZZ/5)$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and structured. The card's solution was extraction residue: it carried \envlist,
    the undefined \wait, three tikzcd diagrams and their uiver.app links, and a footnote marker
    whose definition sat inside the solution. The mathematics is kept exactly — the answer Z/2 +
    Z/2 + Z/3, isomorphic to Z/2 + Z/6 — and the facts it listed (Ext of a free module vanishes,
    Ext(Z/n, B) = B/nB from the resolution 0 -> Z -> Z -> Z/n -> 0, and Ext's additivity) are
    now steps with their resolutions written out and the nine entries computed one by one; the
    card's identification of Ext with Ext^1 is stated. The acknowledgement of Oskar Henriksson
    recorded in the removed footnote is dropped with the diagram apparatus. Not claimed: a
    retained solution set; the collection's provenance is the UCSD qualifying examination
    compilation.
---

::: {.problem}
Compute $\Ext(\ZZ \oplus \ZZ_2 \oplus \ZZ_3, \ZZ \oplus \ZZ_4 \oplus \ZZ_5)$.
:::

::: {.solution}
Throughout $\Ext$ means $\Ext^{1}_{\ZZ}$ for $\ZZ$-modules, so that $\Ext^{0}_{\ZZ} = \Hom_{\ZZ}$, and $A \coloneqq \ZZ \oplus \ZZ/2 \oplus \ZZ/3$ with $A_{1} = \ZZ$, $A_{2} = \ZZ/2$, $A_{3} = \ZZ/3$, while $B \coloneqq \ZZ \oplus \ZZ/4 \oplus \ZZ/5$ with $B_{1} = \ZZ$, $B_{2} = \ZZ/4$, $B_{3} = \ZZ/5$.

::: pf

::: {.pf-step #free}
$\\Ext(\\ZZ, B) = 0$ for every $\\ZZ$-module $B$.

::: pf-proof
$\\ZZ$ is a free, hence projective, $\\ZZ$-module, and the first Ext group of a projective module vanishes.

:::

:::

::: {.pf-step #cyclic}
For every $\\ZZ$-module $B$ and every $n \\ge 1$ there is a natural isomorphism $\\Ext(\\ZZ/n, B) \\cong B/nB$.

::: pf-proof
Apply $\\Hom_{\\ZZ}(-, B)$ to the free resolution $0 \\to \\ZZ \\xrightarrow{\\cdot n} \\ZZ \\to \\ZZ/n \\to 0$. This gives the exact sequence $0 \\to \\Hom(\\ZZ/n,B) \\to \\Hom(\\ZZ,B) \\xrightarrow{\\cdot n} \\Hom(\\ZZ,B) \\to \\Ext(\\ZZ/n,B) \\to \\Ext(\\ZZ,B) = 0$, using step [](#free){.pf-ref} for the last term. The middle map is multiplication by $n$ on $B$, identifying $\\Hom(\\ZZ,B) \\cong B$, so $\\Ext(\\ZZ/n,B) \\cong B/nB$.

:::

:::

::: {.pf-step #additivity}
$\\Ext\\bigl(\\bigoplus_{i}A_{i}, \\bigoplus_{k}B_{k}\\bigr) \\cong \\bigoplus_{i,k}\\Ext(A_{i}, B_{k})$, the sums finite.

::: pf-proof
$\\Hom_{\\ZZ}$ is additive in each variable, and a finite direct sum is also a finite direct product; $\\Ext$ is computed from $\\Hom$ by a projective resolution in the first variable and an injective resolution in the second, so it carries finite direct sums in the first variable and finite direct products in the second to direct products of the Ext groups, which for finitely many summands is the direct sum.

:::

:::

::: {.pf-step #matrices}
The nine groups $\\Ext(A_{i}, B_{k})$ are: $0$ in the row $i = 1$; $\\ZZ/2$, $\\ZZ/2$, $0$ in the row $i = 2$; and $\\ZZ/3$, $0$, $0$ in the row $i = 3$.

::: pf-proof
Row $i = 1$: step [](#free){.pf-ref}. Row $i = 2$: $\\Ext(\\ZZ/2, \\ZZ) \\cong \\ZZ/2\\ZZ = \\ZZ/2$, $\\Ext(\\ZZ/2, \\ZZ/4) \\cong \\ZZ/4/2\\ZZ/4 \\cong \\ZZ/2$, and $\\Ext(\\ZZ/2, \\ZZ/5) \\cong \\ZZ/5/2\\ZZ/5 = 0$ because multiplication by $2$ is surjective on $\\ZZ/5$. Row $i = 3$: $\\Ext(\\ZZ/3,\\ZZ) \\cong \\ZZ/3\\ZZ = \\ZZ/3$, $\\Ext(\\ZZ/3,\\ZZ/4) \\cong \\ZZ/4/3\\ZZ/4 = 0$ because multiplication by $3$ is surjective on $\\ZZ/4$, and $\\Ext(\\ZZ/3,\\ZZ/5) \\cong \\ZZ/5/3\\ZZ/5 = 0$. All nine values are by step [](#cyclic){.pf-ref}.

:::

:::

::: pf-step
$\\Ext\\bigl(\\ZZ \\oplus \\ZZ_{2} \\oplus \\ZZ_{3},\\ \\ZZ \\oplus \\ZZ_{4} \\oplus \\ZZ_{5}\\bigr) \\cong \\ZZ/2 \\oplus \\ZZ/2 \\oplus \\ZZ/3 \\cong \\boxed{\\ZZ/2 \\oplus \\ZZ/6}$.

::: pf-proof
By step [](#additivity){.pf-ref} the answer is the direct sum of the nine groups of step [](#matrices){.pf-ref}, in which only $\\ZZ/2$, $\\ZZ/2$ and $\\ZZ/3$ are nonzero: their sum is $\\ZZ/2 \\oplus \\ZZ/2 \\oplus \\ZZ/3$. The Chinese remainder theorem, applicable because $2$ and $3$ are coprime, identifies $\\ZZ/2 \\oplus \\ZZ/3$ with $\\ZZ/6$, giving the second form.

:::

:::

:::
:::
