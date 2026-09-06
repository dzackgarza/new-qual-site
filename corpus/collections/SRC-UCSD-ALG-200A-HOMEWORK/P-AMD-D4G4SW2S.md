---
schema: qual/card@1
id: P-AMD-D4G4SW2S
kind: problem
title: Sylow subgroups of subgroups via conjugate intersections
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Conjugacy
  - Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 4, Exercise 4. Restored
    the source hypothesis that G is finite and retained all three parts as the
    single Exercise 4 card.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Part (a) embeds a Sylow p-subgroup Q of H in a conjugate of P and then
    uses maximality inside H to identify the intersection with Q. Parts (b)
    and (c) specialize (a) using normality of H and P respectively; uniqueness
    in (c) follows because every p-subgroup of G lies in the unique Sylow
    p-subgroup P.
---

::: {.problem}
Let $G$ be a finite group, let $P\in\operatorname{Syl}_p(G)$, and let $H\le G$.

(a) Prove that there exists $g\in G$ such that
\[
gPg^{-1}\cap H\in\operatorname{Syl}_p(H).
\]

(b) Suppose that $H\normal G$.
Prove that
\[
P\cap H\in\operatorname{Syl}_p(H).
\]

(c) Suppose that $P\normal G$.
Prove that $P\cap H$ is the unique Sylow $p$-subgroup of $H$.
:::

::: {.solution}
<1>1. Every $p$-subgroup of $G$ is contained in a conjugate of $P$.
::: {.proof}
Let $Q\le G$ be a $p$-subgroup.
By the Sylow containment theorem, $Q$ is contained in some Sylow $p$-subgroup $S$ of $G$.
All Sylow $p$-subgroups of $G$ are conjugate, so there exists $g\in G$ such that
\[
S=gPg^{-1}.
\]
Hence
\[
Q\le gPg^{-1}.
\]
:::

<1>2. There exists $g\in G$ such that
\[
gPg^{-1}\cap H\in\operatorname{Syl}_p(H).
\]
::: {.proof}
Choose
\[
Q\in\operatorname{Syl}_p(H).
\]
Since $Q\le H\le G$, the group $Q$ is a $p$-subgroup of $G$.
By <1>1, there exists $g\in G$ such that
\[
Q\le gPg^{-1}.
\]
Therefore
\[
Q\le gPg^{-1}\cap H.
\]
The intersection $gPg^{-1}\cap H$ is a $p$-subgroup of $H$, because it is a subgroup of the $p$-group $gPg^{-1}$.
Since $Q$ is a Sylow $p$-subgroup of $H$, it is maximal among the $p$-subgroups of $H$.
Thus
\[
gPg^{-1}\cap H=Q,
\]
which proves part (a).
:::

<1>3. If $H\normal G$, then for every $g\in G$,
\[
g(P\cap H)g^{-1}=gPg^{-1}\cap H.
\]
::: {.proof}
Conjugation distributes over intersections, so
\[
g(P\cap H)g^{-1}=gPg^{-1}\cap gHg^{-1}.
\]
Since $H\normal G$,
\[
gHg^{-1}=H.
\]
Substitution gives the claimed equality.
:::

<1>4. If $H\normal G$, then
\[
P\cap H\in\operatorname{Syl}_p(H).
\]
::: {.proof}
By <1>2, choose $g\in G$ such that
\[
gPg^{-1}\cap H\in\operatorname{Syl}_p(H).
\]
By <1>3,
\[
gPg^{-1}\cap H=g(P\cap H)g^{-1}.
\]
Because $H\normal G$, conjugation by $g$ restricts to an automorphism of $H$.
Hence $P\cap H$ and $g(P\cap H)g^{-1}$ are conjugate subgroups of $H$ and have the same order.
The latter is a Sylow $p$-subgroup of $H$, so the former is also a Sylow $p$-subgroup of $H$.
This proves part (b).
:::

<1>5. If $P\normal G$, then $P$ is the unique Sylow $p$-subgroup of $G$.
::: {.proof}
A Sylow subgroup is normal if and only if it is unique among the Sylow subgroups of the same prime.
Since $P\in\operatorname{Syl}_p(G)$ and $P\normal G$, it is therefore the unique Sylow $p$-subgroup of $G$.
:::

<1>6. If $P\normal G$, then
\[
P\cap H\in\operatorname{Syl}_p(H).
\]
::: {.proof}
By <1>2, there exists $g\in G$ such that
\[
gPg^{-1}\cap H\in\operatorname{Syl}_p(H).
\]
Since $P\normal G$,
\[
gPg^{-1}=P.
\]
Hence
\[
P\cap H\in\operatorname{Syl}_p(H).
\]
:::

<1>7. If $P\normal G$, every $p$-subgroup of $H$ is contained in $P\cap H$.
::: {.proof}
Let $Q\le H$ be a $p$-subgroup.
Then $Q$ is also a $p$-subgroup of $G$.
By <1>1, $Q$ is contained in a conjugate of $P$.
Since $P\normal G$, every conjugate of $P$ equals $P$.
Thus
\[
Q\le P.
\]
Together with $Q\le H$, this gives
\[
Q\le P\cap H.
\]
:::

<1>8. If $P\normal G$, then $P\cap H$ is the unique Sylow $p$-subgroup of $H$.
::: {.proof}
By <1>6, $P\cap H$ is a Sylow $p$-subgroup of $H$.
Let $Q\in\operatorname{Syl}_p(H)$.
By <1>7,
\[
Q\le P\cap H.
\]
Both $Q$ and $P\cap H$ are Sylow $p$-subgroups of $H$, so they have the same order.
Therefore
\[
Q=P\cap H.
\]
Thus $P\cap H$ is unique, proving part (c).
:::
:::
