---
schema: qual/card@1
id: P-ALGS09B
kind: problem
title: "Normal Sylow subgroups and non-abelian group of order 105"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $G$ be a group of order $105 = 3 \cdot 5 \cdot 7$.

(a) Suppose that $G$ does not have a normal Sylow 7-subgroup.
Show in this case that $G$ has a normal Sylow 3-subgroup and a normal Sylow 5-subgroup.
Prove then that $G$ is abelian, a contradiction.

(b) Show that there is a non-abelian group $G$ of order 105. Explain why your group $G$ is solvable, but not nilpotent.
:::

::: {.solution}
**Part (a).**

<1>1. $n_7 \equiv 1 \pmod 7$ and $n_7 \mid 15$, so $n_7 \in \{1, 15\}$.
::: {.proof}
Sylow's third theorem.
:::

<1>2. Since $G$ has no normal Sylow $7$-subgroup, $n_7 = 15$.
::: {.proof}
<1>1 and the hypothesis (a Sylow subgroup is normal iff unique).
:::

<1>3. $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 35$, so $n_3 \in \{1, 7\}$.
::: {.proof}
Sylow's third theorem.
:::

<1>4. $n_3 = 1$, so the Sylow $3$-subgroup is normal.
<2>1. If $n_3 = 7$, then $G$ has $7 \cdot 2 = 14$ elements of order $3$.
::: {.proof}
each Sylow $3$-subgroup has $2$ non-identity elements, and distinct Sylow $3$-subgroups intersect trivially.
:::
<2>2. The $15$ Sylow $7$-subgroups contribute $15 \cdot 6 = 90$ elements of order $7$.
::: {.proof}
each has $6$ non-identity elements, pairwise disjoint.
:::
<2>3. $14 + 90 = 104 > 105 - 1$, impossible (there are only $105$ elements total, and the identity plus these already exceed $105$).
::: {.proof}
counting elements.
:::
<2>4. Hence $n_3 \neq 7$, so $n_3 = 1$.
::: {.proof}
<2>3 contradicts $n_3 = 7$.
:::

<1>5. $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 21$, so $n_5 \in \{1, 21\}$.
::: {.proof}
Sylow's third theorem.
:::

<1>6. $n_5 = 1$, so the Sylow $5$-subgroup is normal.
<2>1. If $n_5 = 21$, then $G$ has $21 \cdot 4 = 84$ elements of order $5$.
::: {.proof}
each Sylow $5$-subgroup has $4$ non-identity elements, pairwise disjoint.
:::
<2>2. Combined with the $90$ elements of order $7$ (<1>2), this gives $84 + 90 = 174 > 105$, impossible.
::: {.proof}
counting elements.
:::
<2>3. Hence $n_5 = 1$.
::: {.proof}
<2>2.
:::

<1>7. Hence $G$ has normal Sylow $3$- and $5$-subgroups $P_3 \cong \ZZ/3$ and $P_5 \cong \ZZ/5$.
::: {.proof}
<1>4 and <1>6.
:::

<1>8. $P_3 P_5 \cong \ZZ/3 \times \ZZ/5 \cong \ZZ/15$ is a normal subgroup of $G$.
::: {.proof}
both are normal and intersect trivially, so their product is a direct product; a product of normal subgroups is normal.
:::

<1>9. $G$ is abelian.
<2>1. $G/P_3P_5$ has order $7$, hence is cyclic.
::: {.proof}
$|G|/|P_3P_5| = 105/15 = 7$.
:::
<2>2. $P_3P_5 \cong \ZZ/15$ is cyclic.
::: {.proof}
<1>8.
:::
<2>3. A group with a cyclic normal subgroup whose quotient is cyclic is abelian.
::: {.proof}
if $N \trianglelefteq G$ is cyclic and $G/N$ is cyclic, then $G$ is abelian (standard result).
:::
<2>4. Hence $G$ is abelian.
::: {.proof}
<2>1–<2>3.
:::

<1>10. Contradiction: an abelian group has all Sylow subgroups normal, in particular a normal Sylow $7$-subgroup, contradicting the hypothesis.
::: {.proof}
<1>9 and the hypothesis.
:::

<1>11. Q.E.D. (part (a)).
::: {.proof}
<1>10.
:::

**Part (b).**

<1>1. The non-abelian group of order $21$ is $\ZZ/7 \rtimes \ZZ/3$ (the Frobenius group of order $21$).
::: {.proof}
$\operatorname{Aut}(\ZZ/7) \cong \ZZ/6$ has a unique subgroup of order $3$, giving a nontrivial action of $\ZZ/3$ on $\ZZ/7$.
:::

<1>2. $G = (\ZZ/7 \rtimes \ZZ/3) \times \ZZ/5$ is a non-abelian group of order $105$.
::: {.proof}
the direct product with $\ZZ/5$ preserves non-abelianness and has order $21 \cdot 5 = 105$.
:::

<1>3. $G$ is solvable.
::: {.proof}
$G$ has a normal series $1 \trianglelefteq \ZZ/7 \trianglelefteq \ZZ/7 \rtimes \ZZ/3 \trianglelefteq G$ with abelian quotients $\ZZ/7$, $\ZZ/3$, $\ZZ/5$.
:::

<1>4. $G$ is not nilpotent.
::: {.proof}
a nilpotent group is the direct product of its Sylow subgroups, hence has all Sylow subgroups normal; but $G$ has a non-normal Sylow $7$-subgroup (the $\ZZ/7$ factor is not normal in the $\ZZ/7 \rtimes \ZZ/3$ factor), so $G$ is not nilpotent.
:::

<1>5. Q.E.D. (part (b)).
::: {.proof}
<1>2–<1>4.
:::
:::
