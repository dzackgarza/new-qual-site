---
schema: qual/card@1
id: P-AMD-G3APBSND
kind: problem
title: Conjugates of a proper subgroup are indexed by $G/N_G(H)$ and do not cover $G$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Centralizers and Normalizers
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 3, Exercise 3. Corrected
    the first part from an ill-typed equality between a set and an integer to
    the source's statement about the number of distinct conjugates.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used orbit-stabilizer for conjugation on subgroups to count the conjugates.
    For the non-covering claim, bounded the union by one common identity plus
    [G:N_G(H)] copies of H\{e}, then used H <= N_G(H) and [G:H] >= 2.
---

::: {.problem}
Let $G$ be a finite group and let $H<G$ be a proper subgroup.

1. Show that the number of distinct conjugates of $H$ is
   \[
   [G:N_G(H)],
   \]
   where
   \[
   N_G(H)=\{g\in G:gHg^{-1}=H\}.
   \]

2. Prove that
   \[
   G\ne\bigcup_{g\in G}gHg^{-1}.
   \]
:::

::: {.solution}
<1>1. Under conjugation, the stabilizer of $H$ in $G$ is $N_G(H)$.
::: {.proof}
Let $G$ act on its set of subgroups by
\[
g\cdot K=gKg^{-1}.
\]
By definition,
\[
\operatorname{Stab}_G(H)
=\{g\in G:gHg^{-1}=H\}
=N_G(H).
\]
:::

<1>2. The number of distinct conjugates of $H$ is $[G:N_G(H)]$.
::: {.proof}
The orbit of $H$ under the conjugation action is exactly
\[
\{gHg^{-1}:g\in G\}.
\]
By <1>1 and orbit-stabilizer, its cardinality is
\[
[G:N_G(H)].
\]
:::

<1>3. If
\[
m=[G:N_G(H)],
\]
then
\[
\left|\bigcup_{g\in G}gHg^{-1}\right|
\le 1+m(|H|-1).
\]
::: {.proof}
By <1>2, there are exactly $m$ distinct conjugates of $H$.
Every conjugate has cardinality $|H|$, and every conjugate contains the identity element $e$.

After counting $e$ once, each of the $m$ conjugates can contribute at most $|H|-1$ further elements.
Hence
\[
\left|\bigcup_{g\in G}gHg^{-1}\right|
\le 1+m(|H|-1).
\]
:::

<1>4. We have
\[
m\le [G:H].
\]
::: {.proof}
Every subgroup normalizes itself, so
\[
H\le N_G(H).
\]
Therefore the index formula gives
\[
[G:H]=[G:N_G(H)]\,[N_G(H):H]
=m[N_G(H):H].
\]
Thus $m$ divides, and in particular is at most, $[G:H]$.
:::

<1>5. The union of the conjugates of $H$ has strictly fewer than $|G|$ elements.
::: {.proof}
By <1>3 and <1>4,
\[
\begin{aligned}
\left|\bigcup_{g\in G}gHg^{-1}\right|
&\le 1+[G:H](|H|-1)\\
&=1+|G|-[G:H].
\end{aligned}
\]
Since $H$ is proper,
\[
[G:H]\ge2.
\]
Hence
\[
1+|G|-[G:H]\le |G|-1<|G|.
\]
Therefore
\[
\left|\bigcup_{g\in G}gHg^{-1}\right|<|G|.
\]
:::

<1>6. Consequently,
\[
G\ne\bigcup_{g\in G}gHg^{-1}.
\]
::: {.proof}
This follows immediately from <1>5, since the right-hand side has strictly smaller cardinality than $G$.
:::
:::
