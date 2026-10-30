---
schema: qual/card@1
id: P-GRECH5-19
kind: problem
title: Recovering a matrix parameter from eigenvalues
classification:
  areas:
  - applied-algebra
  topics:
  - Eigenvalues
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 19 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
The eigenvalues of the matrix

$$
A = \begin{pmatrix} 2 & b \\ 3 & -1 \end{pmatrix}
$$

are $-4$ and $b - 1$. Find $b$.

(A) $2$
(B) $3$
(C) $4$
(D) $5$
(E) $6$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The trace of $A$ is
$$
\operatorname{tr}(A)=1.
$$


::: pf-proof

The diagonal entries of $A$ are $2$ and $-1$, so
$$
\operatorname{tr}(A)=2+(-1)=1.
$$

:::

:::

::: {.pf-step #s1-2}

The sum of the two given eigenvalues is
$$
b-5.
$$


::: pf-proof

The eigenvalues are $-4$ and $b-1$, whose sum is
$$
-4+(b-1)=b-5.
$$

:::

:::

::: {.pf-step #s1-3}

The parameter is
$$
\boxed{b=6},
$$
so the answer is (E).


::: pf-proof

For a $2\times2$ matrix, the sum of the eigenvalues, counted with algebraic multiplicity, equals the trace. By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref},
$$
b-5=1,
$$
and hence $b=6$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
