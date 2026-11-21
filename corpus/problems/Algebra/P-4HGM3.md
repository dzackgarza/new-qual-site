---
schema: qual/card@1
id: P-4HGM3
kind: problem
title: Groups of order 8
classification:
  areas:
  - algebra
  topics:
  - Classification
  - p-Groups
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the classification already on the card, whose argument
    (an order-4 element, the index-two subgroup, conjugation inverting r, and s^2 in {1, r^2})
    is correct. Added: the justification that a nonabelian group of order 8 must contain an
    element of order 4, since an element of order 8 would make the group cyclic; normality of
    the index-two subgroup by an order count rather than by assertion; the normal-form argument
    that each presented group has order 8, so that the surjection onto G is an isomorphism; and
    a step separating the five groups by invariants, which the card had left implicit.
---

::: {.problem}
Classify all groups of order 8.
:::

::: {.solution}
Let $G$ be a group of order $8$, and write $C_{n}$ for the cyclic group of order $n$, so that $D_{8}$ is the dihedral group of order $8$ and $Q_{8}$ the quaternion group.

::: pf

::: {.pf-step #abelian}
If $G$ is abelian then $G$ is one of $C_{8}$, $C_{4} \times C_{2}$, $(C_{2})^{3}$.

::: pf-proof
By the fundamental theorem of finite abelian groups $G$ is the direct product of cyclic groups of prime-power order, and $8 = 2^{3}$ admits the partitions $3$, $2+1$ and $1+1+1$, giving $C_{8}$, $C_{4}\times C_{2}$ and $C_{2}\times C_{2}\times C_{2}$.

:::

:::

::: {.pf-step #exponent-two}
If every nonidentity element of $G$ has order $2$ then $G$ is abelian.

::: pf-proof
For $x, y \in G$ one has $(xy)^{-1} = xy$ by the hypothesis applied to $xy$, and also $(xy)^{-1} = y^{-1}x^{-1} = yx$ because $x$ and $y$ are their own inverses; hence $xy = yx$.

:::

:::

::: {.pf-step #order-four}
If $G$ is nonabelian then $G$ contains an element $r$ of order $4$.

::: pf-proof
By Lagrange's theorem every element has order $1$, $2$, $4$ or $8$. An element of order $8$ generates $G$, making $G$ cyclic and hence abelian, which is excluded; and if no element had order $4$ then every nonidentity element would have order $2$, which step [](#exponent-two){.pf-ref} rules out.

:::

:::

::: {.pf-step #index-two}
$H \coloneqq \generators{r}$ has order $4$ and index $2$, so it is normal in $G$, and for $s \notin H$ one has $G = H \sqcup sH$.

::: pf-proof
$r$ has order $4$, so $\cardinality{H} = 4$ and its index is $8/4 = 2$. A subgroup of index $2$ is normal: for $g \in G$ with $g \notin H$ the two left cosets are $H$ and $gH$, so $gH = G \setminus H$, and the two right cosets are $H$ and $Hg$, so $Hg = G \setminus H$ as well; hence $gH = Hg$ and $gHg^{-1} = H$, while $g \in H$ gives $gHg^{-1} = H$ directly. Choosing $s \notin H$ gives the disjoint decomposition $G = H \cup sH$.

:::

:::

::: {.pf-step #conjugation}
Conjugation by $s$ sends $r$ to $r^{-1}$, and $s^{2} \in \theset{1, r^{2}}$.

::: pf-proof
Since $H$ is normal, $srs^{-1} \in H$, and $h \mapsto shs^{-1}$ is an automorphism of $H$; it sends the generator $r$ of $H \cong C_{4}$ to a generator, that is to $r$ or to $r^{3} = r^{-1}$. Were the image $r$, then $s$ would commute with $r$ and hence with every element of $H$, and since every element of $G$ is $r^{i}$ or $sr^{i}$ by step [](#index-two){.pf-ref}, $s$ would commute with every element of $G$, contradicting that $G$ is nonabelian. So $srs^{-1} = r^{-1}$. Also $s^{2} \in H = \theset{1, r, r^{2}, r^{3}}$ by step [](#index-two){.pf-ref}. If $s^{2}$ were $r$ or $r^{3}$, then $s^{2}$ would generate $H$, since $r$ and $r^{3}$ are both generators of a cyclic group of order $4$; then $r \in \generators{s^{2}} \subseteq \generators{s}$ would commute with $s$, contradicting $srs^{-1} = r^{-1} \ne r$. Hence $s^{2} \in \theset{1, r^{2}}$.

:::

:::

::: {.pf-step #dihedral}
If $s^{2} = 1$ then $G \cong D_{8}$, the group with presentation $\generators{r, s \mid r^{4} = s^{2} = 1,\ srs^{-1} = r^{-1}}$.

::: pf-proof
The eight elements $r^{i}$ and $sr^{i}$, $0 \le i \le 3$, are exactly the elements of $G$ by step [](#index-two){.pf-ref}, and the relations $r^{4} = 1$, $s^{2} = 1$ and $srs^{-1} = r^{-1}$ hold by the choice of $r$ and $s$ and by step [](#conjugation){.pf-ref}. The presented group has at most eight elements, since $s^{2} = 1$ and $sr = r^{-1}s$ reduce every word to a normal form $r^{i}s^{j}$ with $0 \le i \le 3$ and $0 \le j \le 1$, and it has exactly eight because the symmetries of the square realise it with $r$ a quarter turn and $s$ a reflection. The assignments $r \mapsto r$, $s \mapsto s$ define a surjective homomorphism from the presented group onto $G$, which is therefore an isomorphism between groups of order $8$.

:::

:::

::: {.pf-step #quaternion}
If $s^{2} = r^{2}$ then $G \cong Q_{8}$, the group with presentation $\generators{r, s \mid r^{4} = 1,\ s^{2} = r^{2},\ srs^{-1} = r^{-1}}$.

::: pf-proof
Writing $i \coloneqq r$ and $j \coloneqq s$ gives $i^{4} = 1$, $j^{2} = i^{2}$, $jij^{-1} = i^{-1}$ and $i^{2} \ne 1$, the defining relations of $Q_{8}$; the group they present has the eight elements $i^{k}$ and $i^{k}j$ and is realised by $\theset{\pm1, \pm i, \pm j, \pm k}$ inside the quaternions. As in step [](#dihedral){.pf-ref} the resulting surjection $Q_{8} \to G$ between groups of order $8$ is an isomorphism.

:::

:::

::: {.pf-step #distinct}
The five groups listed are pairwise non-isomorphic.

::: pf-proof
$C_{8}$ is the only one with an element of order $8$. $C_{4}\times C_{2}$ and $C_{2}^{3}$ are abelian, of exponent $4$ and $2$ respectively, so they differ from each other and from $C_{8}$; $D_{8}$ and $Q_{8}$ are nonabelian, so neither is isomorphic to an abelian group. Between the two nonabelian groups, $Q_{8}$ has exactly one element of order $2$, namely $r^{2}$, whereas $D_{8}$ has five: $s$, $r^{2}$, $sr$, $sr^{2}$ and $sr^{3}$.

:::

:::

::: pf-step
The groups of order $8$ are $\boxed{C_{8},\ C_{4}\times C_{2},\ (C_{2})^{3},\ D_{8},\ Q_{8}}$.

::: pf-proof
Step [](#abelian){.pf-ref} covers the abelian case. In the nonabelian case step [](#order-four){.pf-ref} produces an element $r$ of order $4$, steps [](#index-two){.pf-ref} and [](#conjugation){.pf-ref} produce $s$ with $s^{2} \in \theset{1, r^{2}}$ and $srs^{-1} = r^{-1}$, and steps [](#dihedral){.pf-ref} and [](#quaternion){.pf-ref} identify the two resulting groups as $D_{8}$ and $Q_{8}$; step [](#distinct){.pf-ref} shows no two of the five coincide.

:::

:::

:::
:::
