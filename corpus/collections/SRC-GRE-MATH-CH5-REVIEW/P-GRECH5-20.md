---
schema: qual/card@1
id: P-GRECH5-20
kind: problem
title: Eigenvalue of a Hermitian $2\times2$ matrix
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 20 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
The complex matrix

$$
A = \begin{pmatrix} 2 & 2 + i \\ 2 - i & 6 \end{pmatrix}
$$

has which one of the following as an eigenvalue?

(A) $-1$
(B) $3$
(C) $7$
(D) $i$
(E) $1 + i$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The characteristic polynomial of $A$ is
$$
p(\lambda)=\lambda^2-8\lambda+7.
$$


::: pf-proof

One has
$$
\operatorname{tr}(A)=2+6=8
$$
and
$$
\det A
=2\cdot6-(2+i)(2-i)
=12-(4-i^2)
=12-5
=7.
$$
For a $2\times2$ matrix, the characteristic polynomial is
$$
\lambda^2-\operatorname{tr}(A)\lambda+\det A,
$$
which gives the displayed polynomial.

:::

:::

::: {.pf-step #s1-2}

The eigenvalues of $A$ are $1$ and $7$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
p(\lambda)=\lambda^2-8\lambda+7=(\lambda-1)(\lambda-7).
$$
The eigenvalues are precisely the roots of the characteristic polynomial.

:::

:::

::: {.pf-step #s1-3}

Thus the listed eigenvalue is
$$
\boxed{7},
$$
so the answer is (C).


::: pf-proof

Step [](#s1-2){.pf-ref} gives the complete set of eigenvalues, and among the listed choices only $7$ occurs.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} identifies the required choice.

:::

:::

:::
