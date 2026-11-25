---
schema: qual/card@1
id: E-HAT-4.2-1
kind: problem
title: "No retraction $\\RP^n \\to \\RP^k$ via homotopy groups"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 1 (AT.txt 19332-19333) and correct as it stands. The
    argument is right in both cases: for k>=2 a retraction would make i_*: pi_k(RP^k) -> pi_k(RP^n)
    injective, but pi_k(RP^k) = pi_k(S^k) = Z and pi_k(RP^n) = pi_k(S^n) = 0 since k<n; for k=1,
    pi_1(RP^1) = Z and pi_1(RP^n) = Z_2 for n>1, and no injection Z -> Z_2 exists. Checked that the
    identifications used are covering-space invariance (S^m -> RP^m is the universal cover for m>=2) and
    need no further hypothesis. Not checked: nothing outside this exercise.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: a retraction gives $r_*i_*=\id$ on
    each homotopy group, so $i_*$ is injective; for $k\ge2$ the universal covers $S^k\to\RP^k$ and
    $S^n\to\RP^n$ give $\pi_k(\RP^k)=\ZZ$ and $\pi_k(\RP^n)=0$ for $k<n$; and for $k=1$ the deck
    group of $S^n\to\RP^n$ gives $\pi_1(\RP^n)=\ZZ_2$, with no injection $\ZZ\to\ZZ_2$. Added: the
    functoriality statement from which injectivity of $i_*$ follows, the covering-space reason for
    each identification, and the remark that $k=0$ is excluded by the hypothesis and is the case in
    which a retraction does exist. The statement is §4.2 Exercise 1, and no retained solution set
    covers it.

- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 1. The proof is correct. Provenance correction: the earlier
    event on this card says that no retained solution set covers the exercise, and that is false —
    Sam's §4.2 Exercise 1 (`tmp/sources/hatcher-solutions-sam-2008.md`) solves it, his §4.2 numbering
    being Hatcher's. The card's own argument is kept, being correct and independent.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 1. The proof reads correct. One provenance correction: the
    solution said that no retained set covers the exercise, and the retained sets' actual coverage is
    now recorded — Sam's §4.2 numbering is Hatcher's and Proudfoot's homework 7 covers 1, 2, 30, 31
    and 32, announcing 39 without a solution of it.
---

::: {.problem}
Use homotopy groups to show there is no retraction $\RP^n \to \RP^k$ if $n > k > 0$.
:::

::: {.solution}
A retained solution covers this exercise: **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.2 Exercise 1** (`tmp/sources/hatcher-solutions-sam-2008.md`), and **Nicholas Proudfoot, *Math 634: Algebraic Topology I*, homework 7, Problem 1** (`tmp/sources/uoregon-proudfoot-634-hw7.md`). The card's own argument is kept; it uses only the homotopy groups of projective spaces and the functoriality of $\pi_*$, and it covers $k=1$ with the others.

::: pf

::: {.pf-step #retraction-injective}
If $r\colon\RP^n\to\RP^k$ retracts the inclusion $i\colon\RP^k\hookrightarrow\RP^n$, then $i_*\colon\pi_j(\RP^k)\to\pi_j(\RP^n)$ is injective for every $j$.

::: pf-proof
A retraction satisfies $r\circ i=\operatorname{id}_{\RP^k}$, so functoriality gives $r_*i_*=\operatorname{id}_{\pi_j(\RP^k)}$ for every $j$; a map with a left inverse is injective.
:::

:::

::: {.pf-step #higher}
If $k\ge2$ there is no retraction $\RP^n\to\RP^k$ with $n>k$.

::: pf-proof
For $k\ge2$ the universal cover $S^k\to\RP^k$ gives $\pi_k(\RP^k)\cong\pi_k(S^k)=\ZZ$ by Proposition 4.1, while for $n>k\ge2$ the covering $S^n\to\RP^n$ gives $\pi_k(\RP^n)\cong\pi_k(S^n)=0$, since $k<n$. So $i_*$ would be a map $\ZZ\to0$, which is not injective, contradicting step [](#retraction-injective){.pf-ref}.
:::

:::

::: {.pf-step #circle}
If $k=1$ there is no retraction $\RP^n\to\RP^1$ with $n>1$.

::: pf-proof
$\RP^1=S^1$, so $\pi_1(\RP^1)=\ZZ$, while $\pi_1(\RP^n)=\ZZ_2$ for $n\ge2$ because $S^n\to\RP^n$ is a universal cover with deck group $\ZZ_2$. There is no injective homomorphism $\ZZ\to\ZZ_2$, so step [](#retraction-injective){.pf-ref} is violated.
:::

:::

::: {.pf-step}
$\boxed{\text{There is no retraction }\RP^n\to\RP^k\text{ for }n>k>0}$.

::: pf-proof
Steps [](#higher){.pf-ref} and [](#circle){.pf-ref} cover the two cases $k\ge2$ and $k=1$; the case $k=0$ is excluded by the hypothesis $k>0$, and in that case a retraction does exist.
:::

:::

:::
:::
