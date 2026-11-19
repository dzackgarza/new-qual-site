---
schema: qual/card@1
id: P-ALGS13G
kind: problem
title: Finite separable degrees are $p$-powers when all finite degrees are divisible by $p$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 7 of the Spring 2013 UCSD Algebra Qualifying Examination, printed p. 1
    of the single-page paper retained at assets/attachments/SP13_200_Algebra_Qual.pdf, is the statement
    the card answers, and the paragraph at the head of the solution records that the paper prints no
    solutions, so the argument is the card's own. Checked: the statement against the paper's text layer
    at the page named; the solution read for the normal closure, the Sylow $p$-subgroup, and the fixed
    field $N^P$ used to force $G$ to be a $p$-group; `qualc.authoring check` on the card, and
    `tmp/lam.sh` for the numbering and the QED. The card's statement writes the hypothesis for
    extensions with $E\ne F$; the printed wording does not, and at $E=F$ the printed hypothesis would
    fail since $1$ is not divisible by $p$, so the qualification is a clarification of the printed
    sentence and not a weakening of the claim. Not checked: no retained solution set exists for this
    paper to compare the argument with, and no other card of the collection in this pass.
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: The exam hypothesis "the degree of any finite extension E/F is divisible by p" fails
    for E = F and so is never satisfied; the statement now requires it for E different from
    F, as the solution uses it.
---

::: {.problem}
Let $F$ be a field and $p$ be a prime.
Suppose that the degree of any finite field extension $E/F$ with $E \neq F$ is divisible by $p$.
Prove that the degree of any finite separable extension $E/F$ is a power of $p$.
:::

::: {.solution}

The problem is Problem 7 of the Spring 2013 UCSD Algebra Qualifying Examination, printed p. 1 of the single-page paper retained at `assets/attachments/SP13_200_Algebra_Qual.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own, and what it supplies is the normal closure $N$ of $E$ and $G=\operatorname{Gal}(N/F)$: the hypothesis gives $p\mid\cardinality{G}$, a proper Sylow $p$-subgroup $P$ would make $N^P/F$ a proper extension of degree $[G:P]$ prime to $p$, so $G$ is a $p$-group and $[E:F]=[G:H]$ is a power of $p$


::: pf

::: pf-step

Let $E/F$ be a finite separable extension, let $N$ be its normal closure over $F$, and set $G=\operatorname{Gal}(N/F)$.

::: pf-proof

Because $E/F$ is finite separable, its normal closure $N/F$ is finite Galois.

:::

:::

::: pf-step

The hypothesis implies that $p\mid \cardinality{G}$.

::: pf-proof

Take the finite extension $N/F$.
Since $N\ne F$ unless the claim is trivial, the hypothesis gives $p\mid [N:F]=\cardinality{G}$.

:::

:::

::: {.pf-step #s3}

Let $P$ be a Sylow $p$-subgroup of $G$.
Then $P=G$.

::: pf-proof

Suppose $P<G$.
By the Galois correspondence, the fixed field $N^P$ is a proper finite extension of $F$ and
$$
[N^P:F]=[G:P].
$$
The hypothesis therefore gives $p\mid [G:P]$.
But $P$ is a Sylow $p$-subgroup, so $[G:P]$ is relatively prime to $p$.
This contradiction shows $P=G$.

:::

:::

::: pf-step

Hence $G$ is a $p$-group.

::: pf-proof

By step [](#s3){.pf-ref}, $G=P$, and $P$ has order a power of $p$.

:::

:::

::: {.pf-step #s5}

Let $H=\operatorname{Gal}(N/E)$.
Then
$$
[E:F]=[G:H],
$$
so $[E:F]$ is a power of $p$.

::: pf-proof

The Galois correspondence gives $[E:F]=[G:H]$.
Since $G$ is a finite $p$-group, every subgroup index is a power of $p$.

:::

:::

::: pf-step

Therefore every finite separable extension of $F$ has degree a power of $p$.

::: pf-proof

This is exactly step [](#s5){.pf-ref}.

:::

:::

:::

:::
