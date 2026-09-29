---
schema: qual/card@1
id: P-BERK89S-09
kind: problem
title: A group is not a finite union of cosets of two infinite-index subgroups
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Showed that a finite cover by $H$- and $K$-cosets would force
    $H\cap K$ to have finite index in both subgroups, hence finite index in
    $G$, contradicting the assumed infinite indices.
---

::: {.problem}
Let $H,K$ be subgroups of a group $G$, each of infinite index. Prove that $G$ cannot be written as a finite union of left cosets of $H$ and $K$.
:::

::: {.solution}
Set $L=H\cap K$. Suppose, for a contradiction, that there are finite families
of elements $a_1,\ldots,a_r,b_1,\ldots,b_s\in G$ such that
$$
G=\bigcup_{i=1}^r a_iH\ \cup\ \bigcup_{j=1}^s b_jK.
$$
If $r=0$, then $G$ is a union of finitely many left cosets of $K$, contrary
to $[G:K]=\infty$; similarly, $s=0$ contradicts $[G:H]=\infty$. Hence we may
assume $r,s\geq1$.

::: pf

::: {.pf-step #l-finite-index-in-h}
The subgroup $L$ has finite index in $H$.

::: pf-proof
Since $H$ has infinite index in $G$, there is a left coset $gH$ distinct from
all of the finitely many cosets $a_iH$. Distinct left cosets of $H$ are
disjoint, so the assumed cover gives
$$
gH\subseteq\bigcup_{j=1}^s b_jK.
$$
Multiplying by $g^{-1}$ on the left and intersecting with $H$ yields
$$
H=\bigcup_{j=1}^s\left(H\cap g^{-1}b_jK\right).
$$

Whenever $H\cap cK$ is nonempty, choose $h\in H\cap cK$. Then $cK=hK$ and
$$
H\cap cK
=H\cap hK
=h(H\cap K)
=hL.
$$
Thus every nonempty set in the preceding finite union is a left coset of
$L$ in $H$. Hence $[H:L]<\infty$.
:::

:::

::: {.pf-step #l-finite-index-in-k}
The subgroup $L$ has finite index in $K$.

::: pf-proof
Since $K$ also has infinite index in $G$, choose a left coset $g'K$ distinct
from every listed coset $b_jK$. Then the assumed cover forces
$$
g'K\subseteq\bigcup_{i=1}^r a_iH.
$$
Multiplying by $(g')^{-1}$ and repeating the intersection argument from step
[](#l-finite-index-in-h){.pf-ref}, with $H$ and $K$ interchanged, writes $K$ as a finite union of left
cosets of $K\cap H=L$. Therefore $[K:L]<\infty$.
:::

:::

::: {.pf-step #contradiction}
The assumed finite cover is impossible.

::: pf-proof
By step [](#l-finite-index-in-h){.pf-ref}, every left coset of $H$ is a finite union of left cosets of
$L$. By step [](#l-finite-index-in-k){.pf-ref}, the same is true for every left coset of $K$. Hence the
assumed finite cover of $G$ refines to a finite cover of $G$ by left cosets of
$L$. Thus $[G:L]<\infty$.

Since $L\subseteq H$, every left coset of $H$ is a union of left cosets of
$L$, and therefore
$$
[G:H]\leq [G:L]<\infty.
$$
This contradicts the hypothesis that $H$ has infinite index in $G$.
:::

:::

::: pf-qed
Step [](#contradiction){.pf-ref} contradicts the existence of any finite union of left cosets of
$H$ and $K$ equal to $G$.
:::

:::
:::
