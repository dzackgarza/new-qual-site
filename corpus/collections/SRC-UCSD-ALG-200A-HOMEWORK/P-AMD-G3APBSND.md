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

::: pf

::: {.pf-step #s1}

Under conjugation, the stabilizer of $H$ in $G$ is $N_G(H)$.

::: pf-proof

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

:::

::: {.pf-step #s2}

The number of distinct conjugates of $H$ is $[G:N_G(H)]$.

::: pf-proof

The orbit of $H$ under the conjugation action is exactly
\[
\{gHg^{-1}:g\in G\}.
\]
By step [](#s1){.pf-ref} and orbit-stabilizer, its cardinality is
\[
[G:N_G(H)].
\]

:::

:::

::: {.pf-step #s3}

If
\[
m=[G:N_G(H)],
\]
then
\[
\left|\bigcup_{g\in G}gHg^{-1}\right|
\le 1+m(|H|-1).
\]

::: pf-proof

By step [](#s2){.pf-ref}, there are exactly $m$ distinct conjugates of $H$.
Every conjugate has cardinality $|H|$, and every conjugate contains the identity element $e$.

After counting $e$ once, each of the $m$ conjugates can contribute at most $|H|-1$ further elements.
Hence
\[
\left|\bigcup_{g\in G}gHg^{-1}\right|
\le 1+m(|H|-1).
\]

:::

:::

::: {.pf-step #s4}

We have
\[
m\le [G:H].
\]

::: pf-proof

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

:::

::: {.pf-step #s5}

The union of the conjugates of $H$ has strictly fewer than $|G|$ elements.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref},
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

:::

::: pf-step

Consequently,
\[
G\ne\bigcup_{g\in G}gHg^{-1}.
\]

::: pf-proof

This follows immediately from step [](#s5){.pf-ref}, since the right-hand side has strictly smaller cardinality than $G$.

:::

:::

:::

:::
