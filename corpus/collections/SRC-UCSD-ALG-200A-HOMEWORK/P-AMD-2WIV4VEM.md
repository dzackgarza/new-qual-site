---
schema: qual/card@1
id: P-AMD-2WIV4VEM
kind: problem
title: Nilpotence lifts from $G/Z(G)$ to $G$
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Centralizers and Normalizers
  - Subgroup Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 6, Exercise 1(b). The
    source places no finiteness hypothesis on G; retained that generality.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    The quotient lower central series is the image of the lower central series
    of G. If gamma_{c+1}(G/Z(G)) is trivial, then gamma_{c+1}(G) lies in the
    center, so the next lower-central term is trivial.
---

::: {.problem}
Let $G$ be a group.
Prove that if $G/Z(G)$ is nilpotent, then $G$ is nilpotent.
:::

::: {.solution}
<1>1. For a group $K$, write its lower central series as
\[
\gamma_1(K)=K,
\qquad
\gamma_{i+1}(K)=[K,\gamma_i(K)].
\]
If $N\trianglelefteq K$ and $\pi:K\to K/N$ is the quotient map, then for every $i\ge1$,
\[
\gamma_i(K/N)=\pi(\gamma_i(K)).
\]
::: {.proof}
We induct on $i$.
For $i=1$,
\[
\gamma_1(K/N)=K/N=\pi(K)=\pi(\gamma_1(K)).
\]
Suppose the formula holds for $i$.
Since $\pi$ is surjective and homomorphisms preserve commutators,
\[
\begin{aligned}
\gamma_{i+1}(K/N)
  &=[K/N,\gamma_i(K/N)]\\
  &=[\pi(K),\pi(\gamma_i(K))]\\
  &=\pi([K,\gamma_i(K)])\\
  &=\pi(\gamma_{i+1}(K)).
\end{aligned}
\]
Thus the formula holds for all $i$.
:::

<1>2. If $G/Z(G)$ is nilpotent, then some term of the lower central series of $G$ lies in $Z(G)$.
::: {.proof}
Set
\[
Z=Z(G).
\]
Since $G/Z$ is nilpotent, there is some $c\ge0$ such that
\[
\gamma_{c+1}(G/Z)=1.
\]
Applying <1>1 to the quotient map $G\to G/Z$ gives
\[
\gamma_{c+1}(G)Z/Z=1.
\]
Hence
\[
\gamma_{c+1}(G)\le Z(G).
\]
:::

<1>3. The lower central series of $G$ terminates one step later.
::: {.proof}
By <1>2,
\[
\gamma_{c+1}(G)\le Z(G).
\]
Therefore
\[
\gamma_{c+2}(G)
  =[G,\gamma_{c+1}(G)]
  \le [G,Z(G)]
  =1.
\]
Thus $G$ is nilpotent.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3.
:::
:::
