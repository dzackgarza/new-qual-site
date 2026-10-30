---
schema: qual/card@1
id: P-GRECH5-15
kind: problem
title: Dimension of the image from nullity
classification:
  areas:
  - applied-algebra
  topics:
  - Rank-Nullity Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 15 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
Let $T\colon \RR^5 \to \RR^3$ be a linear transformation whose kernel is a three-dimensional subspace of $\RR^5$. The set $\{T(\mathbf{x}) : \mathbf{x} \in \RR^5\}$ is

(A) the trivial subspace
(B) a line through the origin
(C) a plane through the origin
(D) all of $\RR^3$
(E) Cannot be determined from the information given
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The image of $T$ has dimension $2$.


::: pf-proof

The rank-nullity theorem gives
$$
\dim\RR^5=\dim\ker T+\dim\operatorname{im}T.
$$
Since $\dim\ker T=3$, one obtains
$$
5=3+\dim\operatorname{im}T,
$$
and therefore $\dim\operatorname{im}T=2$.

:::

:::

::: {.pf-step #s1-2}

The set $\{T(\mathbf x):\mathbf x\in\RR^5\}$ is
$$
\boxed{\text{a plane through the origin}},
$$
so the answer is (C).


::: pf-proof

The displayed set is $\operatorname{im}T$, which is a linear subspace of $\RR^3$. By step [](#s1-1){.pf-ref} it is two-dimensional. A two-dimensional linear subspace of $\RR^3$ is a plane containing the origin.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} identifies the image.

:::

:::

:::
