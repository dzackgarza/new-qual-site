---
schema: qual/card@1
id: P-UCLARA16S-09
kind: problem
title: Entire functions with $|f|=1$ on the unit circle are monomials
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f:\CC\to\CC$ be entire and assume that $|f(z)|=1$ when $|z|=1$. Show that
\[
f(z)=Cz^m
\]
for some integer $m\ge0$ and $C\in\CC$ with $|C|=1$.
:::

::: {.solution}

Let $a_1,\dots,a_N$ be the zeros of $f$ in $\mathbb D$, listed with multiplicity, and define
\[
B(z)
\coloneqq
\prod_{j=1}^N
\frac{z-a_j}{1-\overline{a_j}z}.
\]
If $f$ has no zeros in $\mathbb D$, take $N=0$ and $B\equiv1$.

::: pf

::: {.pf-step #s1-1}

The function $B$ is holomorphic on a neighborhood of $\overline{\mathbb D}$, has exactly the same zeros as $f$ in $\mathbb D$ with the same multiplicities, and satisfies
\[
|B(z)|=1
\qquad
(|z|=1).
\]


::: pf-proof

Because $|f|=1$ on the unit circle, $f$ has no zeros there. Zeros of a nonzero holomorphic function are isolated, so compactness of $\overline{\mathbb D}$ implies that there are only finitely many zeros in $\mathbb D$.

For $|a_j|<1$, the denominator $1-\overline{a_j}z$ has its only zero at $1/\overline{a_j}$, whose modulus is greater than $1$. Thus every factor is holomorphic on a neighborhood of $\overline{\mathbb D}$. For $|z|=1$,
\[
|z-a_j|
=
|z|\,|1-\overline{z}a_j|
=
|1-\overline{a_j}z|,
\]
so each factor has modulus $1$ on the unit circle. The assertion about zeros is immediate from the numerators.

:::

:::

::: pf-step

The quotient
\[
h\coloneqq\frac{f}{B}
\]
extends to a holomorphic nonvanishing function on $\mathbb D$ and satisfies
\[
|h(z)|=1
\qquad
(|z|=1).
\]


::: pf-proof

By step [](#s1-1){.pf-ref}, $f$ and $B$ have the same zeros in $\mathbb D$ with the same multiplicities, so all apparent singularities of $f/B$ are removable and the extension has no zeros. On the unit circle, step [](#s1-1){.pf-ref} and the hypothesis give
\[
|h(z)|
=
\frac{|f(z)|}{|B(z)|}
=1.
\]

:::

:::

::: {.pf-step #s1-3}

There is a constant $C\in\CC$ with $|C|=1$ such that
\[
f(z)=C B(z)
\qquad
(z\in\mathbb D).
\]


::: pf-proof

By the maximum-modulus principle applied to $h$,
\[
|h(z)|\le1
\qquad
(z\in\mathbb D).
\]
Since $h$ is nonvanishing, $1/h$ is holomorphic on $\mathbb D$ and also has boundary modulus $1$. Applying the maximum-modulus principle to $1/h$ gives
\[
|h(z)|\ge1.
\]
Hence $|h|\equiv1$ on $\mathbb D$. By the open mapping theorem, a nonconstant holomorphic function has open image, whereas the unit circle has empty interior. Thus $h$ is constant, say $h\equiv C$, with $|C|=1$.

:::

:::

::: {.pf-step #s1-4}

Every zero $a_j$ equals $0$.


::: pf-proof

Suppose that some $a_j\ne0$. Then the corresponding Blaschke factor has a pole at
\[
p_j
\coloneqq
\frac1{\overline{a_j}},
\qquad
|p_j|>1.
\]
No numerator factor vanishes at $p_j$, because every numerator zero $a_k$ lies in $\mathbb D$ while $|p_j|>1$. Hence $B$ has a genuine pole at $p_j$.

On the connected domain obtained from $\CC$ by deleting the finitely many poles of $B$, both $f$ and $CB$ are holomorphic and agree on the nonempty open set $\mathbb D$ by step [](#s1-3){.pf-ref}. The identity theorem therefore gives
\[
f=CB
\]
throughout that domain. But $f$ is holomorphic at $p_j$, whereas $CB$ has a genuine pole there, a contradiction. Thus every $a_j=0$.

:::

:::

::: {.pf-step #s1-5}

There is an integer $m\ge0$ such that
\[
\boxed{f(z)=Cz^m}
\qquad
(z\in\CC),
\]
with $|C|=1$.


::: pf-proof

By step [](#s1-4){.pf-ref}, all $N$ zeros of $f$ in $\mathbb D$ are at $0$. Therefore
\[
B(z)=z^N.
\]
Step [](#s1-3){.pf-ref} gives
\[
f(z)=Cz^N
\qquad
(z\in\mathbb D).
\]
Both sides are entire, so the identity theorem extends the equality to all of $\CC$. Taking $m=N$ gives the claimed form, including $m=0$ when $f$ has no zeros in $\mathbb D$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the required classification.

:::

:::

:::
