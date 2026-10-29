---
schema: qual/card@1
id: P-GRECH5-18
kind: problem
title: Eigenvalue consequences for inverse and square
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
  note: Re-transcribed from Chapter 5 review Question 18 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
If $A$ is an invertible matrix with an eigenvalue of $3$ corresponding to the eigenvector $\mathbf{x}$, which of the following statements must be true?

(A) The matrix $A^{-1}$ has an eigenvalue of $\frac{1}{3}$ corresponding to the eigenvector $\mathbf{x}$.
(B) The matrix $A^{-1}$ has an eigenvalue of $\frac{1}{3}$ corresponding to the eigenvector whose entries are the reciprocals of the entries of $\mathbf{x}$.
(C) The matrix $A^2$ has an eigenvalue of $3$ corresponding to the eigenvector $\mathbf{x}$.
(D) The matrix $A^2$ has an eigenvalue of $6$ corresponding to the eigenvector $2\mathbf{x}$.
(E) The matrix $A^2$ has an eigenvalue of $3$ corresponding to the eigenvector $3\mathbf{x}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The eigenvalue equation is
$$
A\mathbf x=3\mathbf x.
$$


::: pf-proof

This is precisely the meaning of the statement that $3$ is an eigenvalue of $A$ corresponding to the eigenvector $\mathbf x$.

:::

:::

::: {.pf-step #s1-2}

The same vector $\mathbf x$ satisfies
$$
A^{-1}\mathbf x=\frac13\mathbf x.
$$


::: pf-proof

Apply $A^{-1}$ to both sides of step [](#s1-1){.pf-ref}. Since $A$ is invertible,
$$
\mathbf x=3A^{-1}\mathbf x,
$$
and division by $3$ gives the displayed equation.

:::

:::

::: {.pf-step #s1-3}

Therefore the statement that must be true is
$$
\boxed{A^{-1}\mathbf x=\frac13\mathbf x},
$$
so the answer is (A).


::: pf-proof

Step [](#s1-2){.pf-ref} says exactly that $1/3$ is an eigenvalue of $A^{-1}$ corresponding to the same eigenvector $\mathbf x$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} identifies the required statement.

:::

:::

:::
