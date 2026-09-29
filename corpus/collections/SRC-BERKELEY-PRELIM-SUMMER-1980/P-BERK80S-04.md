---
schema: qual/card@1
id: P-BERK80S-04
kind: problem
title: Conjugates of a subgroup in a finite group
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 4 of the vendored Berkeley Preliminary Exam, Summer 1980; restored the garbled conjugation notation $xHx^{-1}$. The source uses $H\subset G$ and part 2 forces the intended meaning to be proper inclusion.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the normalizer orbit count and the strict union bound using the common identity element.
---

::: {.problem}
Let $G$ be a finite group and let $H\subsetneq G$ be a proper subgroup.

1. Show that the number of subgroups of $G$ of the form $xHx^{-1}$, for $x\in G$, is at most the index $[G:H]$.

2. Prove that some element of $G$ is not contained in any subgroup of the form $xHx^{-1}$, $x\in G$.
:::

::: {.solution}
Let
$$
N_G(H)=\{g\in G:gHg^{-1}=H\}
$$
be the normalizer of $H$.

::: pf

::: {.pf-step #s1}

The number of conjugates of $H$ is at most $[G:H]$.

::: pf-proof

The group $G$ acts by conjugation on its set of subgroups. The stabilizer
of $H$ is exactly $N_G(H)$, so the orbit-stabilizer theorem gives
$$
\#\{xHx^{-1}:x\in G\}=[G:N_G(H)].
$$
Since every $h\in H$ normalizes $H$, one has
$$
H\le N_G(H).
$$
Therefore
$$
[G:N_G(H)]\le [G:H].
$$

:::

:::

::: {.pf-step #s2}

The union of all conjugates of $H$ is a proper subset of $G$.

::: pf-proof

Let
$$
m=\#\{xHx^{-1}:x\in G\}.
$$
By step [](#s1){.pf-ref},
$$
m\le [G:H].
$$
Every conjugate $xHx^{-1}$ has exactly $\abs{H}$ elements, and every one
contains the identity element $e$. Each conjugate therefore contributes at
most $\abs{H}-1$ elements other than $e$ to the union, and
$$
\abs{\bigcup_{x\in G}xHx^{-1}}
\le 1+m(\abs{H}-1)
\le 1+[G:H](\abs{H}-1).
$$
Since $H$ is proper, $[G:H]>1$. Using $\abs{G}=[G:H]\abs{H}$,
$$
1+[G:H](\abs{H}-1)
=\abs{G}-[G:H]+1
<\abs{G}.
$$

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part 1. By step [](#s2){.pf-ref}, some element of $G$ lies in no
subgroup $xHx^{-1}$, which proves part 2.

:::

:::

:::
