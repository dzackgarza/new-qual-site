---
schema: qual/card@1
id: P-CH9S-T10
kind: problem
title: Left cosets of a non-normal subgroup of $A_4$ do not form a group
classification:
  areas:
    - algebra
  topics:
    - Normal Subgroups and Factor Groups
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: '2026-09-14'
    note: Checked against Team Problem Solutions for Ch 9, problem 10, in the deterministic MinerU Flash extraction assets/attachments/Ch9Sltns_extracted.md. Part (b) refers to Table 5.1 on page 111; that multiplication table is not contained in this retained solution PDF.
  - event: source-checked
    by: claude-opus-5
    date: 2026-09-16
    note: Stated the permutations alpha_6, alpha_7, alpha_9, alpha_11 of Table 5.1 as identified by the source's own solution to Team Problem 10 in Ch9Sltns.pdf.
---

::: {.problem}
Let $H=\{(1),(12)(34)\}$ in $A_4$.

(a) Show that $H$ is not normal in $A_4$.

(b) Referring to the multiplication table for $A_4$ in Table 5.1 on page 111, show that, although $\alpha_6H=\alpha_7H$ and $\alpha_9H=\alpha_{11}H$, it is not true that $\alpha_6\alpha_9H=\alpha_7\alpha_{11}H$.
Explain why this proves that the left cosets of $H$ do not form a group under coset multiplication.

In Table 5.1, $\alpha_6 = (243)$, $\alpha_7 = (142)$, $\alpha_9 = (132)$ and $\alpha_{11} = (234)$, as identified in the source's solution.
:::

::: {.solution}

Let
$$
t=(12)(34),
\qquad
H=\{(1),t\}.
$$

::: pf

::: {.pf-step #s1-1}

The subgroup $H$ is not normal in $A_4$.


::: pf-proof

Take $g=(123)$. Direct multiplication gives
$$
gH=\{(123),(134)\},
$$
whereas
$$
Hg=\{(123),(243)\}.
$$
These two cosets are not equal. A subgroup is normal exactly when its
left and right cosets agree for every group element, so
$H\not\trianglelefteq A_4$.

:::

:::

::: {.pf-step #s1-2}

The stated pairs of left cosets are equal:
$$
\alpha_6H=\alpha_7H,
\qquad
\alpha_9H=\alpha_{11}H.
$$


::: pf-proof

Using the permutations specified in the problem,
$$
\alpha_6^{-1}\alpha_7
=(234)(142)
=(12)(34)
=t\in H,
$$
and
$$
\alpha_9^{-1}\alpha_{11}
=(123)(234)
=(12)(34)
=t\in H.
$$
For left cosets, $aH=bH$ exactly when $a^{-1}b\in H$. The two displayed
computations therefore give the required equalities.

:::

:::

::: {.pf-step #s1-3}

The products of the chosen representatives determine different left cosets:
$$
\alpha_6\alpha_9H\neq\alpha_7\alpha_{11}H.
$$


::: pf-proof

Direct multiplication gives
$$
\alpha_6\alpha_9
=(243)(132)
=(12)(34)
=t\in H,
$$
so
$$
\alpha_6\alpha_9H=H.
$$
On the other hand,
$$
\alpha_7\alpha_{11}
=(142)(234)
=(14)(23).
$$
Since $(14)(23)\notin H$, its left coset is not the identity coset:
$$
\alpha_7\alpha_{11}H=(14)(23)H\neq H.
$$
Thus the two product cosets are different.

:::

:::

::: {.pf-step #s1-4}

Coset multiplication is not well-defined on the set of left cosets of $H$.


::: pf-proof

By step [](#s1-2){.pf-ref}, the first factors $\alpha_6H$ and $\alpha_7H$ represent
the same left coset, and the second factors $\alpha_9H$ and
$\alpha_{11}H$ also represent the same left coset. If the rule
$$
(aH)(bH)=(ab)H
$$
were well-defined, replacing either representative by another
representative of the same coset could not change the product coset.
Step [](#s1-3){.pf-ref} shows that it does change. Hence the rule is not well-defined.

:::

:::

::: {.pf-step #s1-5}

The left cosets of $H$ do not form a group under coset multiplication.


::: pf-proof

A group operation must first be a well-defined binary operation on the
underlying set. Step [](#s1-4){.pf-ref} shows that the proposed coset multiplication
is not well-defined, so it cannot make the set of left cosets into a
group.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (a), and steps [](#s1-2){.pf-ref} through [](#s1-5){.pf-ref} prove part (b).

:::

:::

:::
