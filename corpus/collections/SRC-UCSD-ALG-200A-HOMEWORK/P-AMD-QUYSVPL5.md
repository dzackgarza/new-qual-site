---
schema: qual/card@1
id: P-AMD-QUYSVPL5
kind: problem
title: Nilpotence passes to subgroups and quotients
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Subgroups
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 6, Exercise 1(a). Restored
    the source's explicit statement that G need not be finite, corrected the
    quotient assertion to normal subgroups, and restored the
    lower-central-series hint.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    The lower central series of a subgroup lies termwise in that of G, while
    the lower central series of a quotient is the image of the series of G.
---

::: {.problem}
Let $G$ be a group; do not assume that $G$ is finite.

Prove that if $G$ is nilpotent, then every subgroup of $G$ and every quotient group of $G$ is nilpotent.

Hint: use the lower central series.
:::

::: {.solution}
<1>1. Write the lower central series of a group $K$ as
\[
\gamma_1(K)=K,
\qquad
\gamma_{i+1}(K)=[K,\gamma_i(K)].
\]
A group $K$ is nilpotent precisely when $\gamma_{c+1}(K)=1$ for some $c\ge0$.
::: {.proof}
This is the lower-central-series characterization of nilpotence used in the problem hint.
:::

<1>2. If $H\le G$, then for every $i\ge1$,
\[
\gamma_i(H)\le\gamma_i(G).
\]
::: {.proof}
We induct on $i$.
For $i=1$,
\[
\gamma_1(H)=H\le G=\gamma_1(G).
\]
If $\gamma_i(H)\le\gamma_i(G)$, then
\[
\gamma_{i+1}(H)
  =[H,\gamma_i(H)]
  \le [G,\gamma_i(G)]
  =\gamma_{i+1}(G).
\]
Thus the containment holds for every $i$.
:::

<1>3. Every subgroup of a nilpotent group is nilpotent.
::: {.proof}
Suppose $G$ is nilpotent, so
\[
\gamma_{c+1}(G)=1
\]
for some $c$.
If $H\le G$, then <1>2 gives
\[
\gamma_{c+1}(H)\le\gamma_{c+1}(G)=1.
\]
Hence $H$ is nilpotent.
:::

<1>4. If $N\trianglelefteq G$ and $\pi:G\to G/N$ is the quotient map, then for every $i\ge1$,
\[
\gamma_i(G/N)=\pi(\gamma_i(G))
                 =\gamma_i(G)N/N.
\]
::: {.proof}
Again use induction on $i$.
For $i=1$ the equality is
\[
G/N=\pi(G).
\]
If it holds for $i$, then surjectivity of $\pi$ and preservation of commutators give
\[
\begin{aligned}
\gamma_{i+1}(G/N)
  &=[G/N,\gamma_i(G/N)]\\
  &=[\pi(G),\pi(\gamma_i(G))]\\
  &=\pi([G,\gamma_i(G)])\\
  &=\pi(\gamma_{i+1}(G)).
\end{aligned}
\]
:::

<1>5. Every quotient of a nilpotent group is nilpotent.
::: {.proof}
Let $N\trianglelefteq G$, and suppose
\[
\gamma_{c+1}(G)=1.
\]
By <1>4,
\[
\gamma_{c+1}(G/N)
  =\pi(\gamma_{c+1}(G))
  =1.
\]
Therefore $G/N$ is nilpotent.
Together with <1>3, this proves the claim.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
