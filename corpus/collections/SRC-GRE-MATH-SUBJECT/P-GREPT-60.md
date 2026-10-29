---
schema: qual/card@1
id: P-GREPT-60
kind: problem
title: "Eigenvectors of $A$ shared by $2A$, $A^2$ and $A^{-1}$"
classification:
  areas: [applied-algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 60 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $\mathbf{v}$ is an eigenvector of an invertible matrix $A$, then which of the following is/are necessarily true?

I. $\mathbf{v}$ is also an eigenvector of $2A$.

II. $\mathbf{v}$ is also an eigenvector of $A^2$.

III. $\mathbf{v}$ is also an eigenvector of $A^{-1}$.

(A) I only
(B) II only
(C) III only
(D) I and III only
(E) I, II, and III
:::

::: {.solution}

Let $\lambda$ be the eigenvalue such that $A\mathbf v=\lambda\mathbf v$.

::: pf

::: {.pf-step #s1-1}

$\lambda\neq 0$.


::: pf-proof

If $\lambda=0$, then $A\mathbf v=0$. Since $A$ is invertible,
$\mathbf v=A^{-1}A\mathbf v=0$, contradicting the definition of an
eigenvector.

:::

:::

::: {.pf-step #s1-2}

Statement I is true.


::: pf-proof

Multiplying $A\mathbf v=\lambda\mathbf v$ by the scalar $2$ gives
$$
(2A)\mathbf v=(2\lambda)\mathbf v.
$$
Since $\mathbf v\neq 0$, it is an eigenvector of $2A$.

:::

:::

::: {.pf-step #s1-3}

Statement II is true.


::: pf-proof

Applying $A$ to the equation $A\mathbf v=\lambda\mathbf v$ gives
$$
A^2\mathbf v=A(\lambda\mathbf v)=\lambda A\mathbf v
=\lambda^2\mathbf v.
$$
Thus $\mathbf v$ is an eigenvector of $A^2$.

:::

:::

::: {.pf-step #s1-4}

Statement III is true.


::: pf-proof

Multiplying $A\mathbf v=\lambda\mathbf v$ by $A^{-1}$ gives
$$
\mathbf v=\lambda A^{-1}\mathbf v.
$$
By step [](#s1-1){.pf-ref}, $\lambda$ is nonzero, so
$A^{-1}\mathbf v=\lambda^{-1}\mathbf v$. Hence $\mathbf v$ is an
eigenvector of $A^{-1}$.

:::

:::

::: {.pf-step #s1-5}

Therefore the correct answer is $\boxed{\text{(E) I, II, and III}}$.


::: pf-proof

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-4){.pf-ref} prove statements I, II, and III, respectively.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the required choice.

:::

:::

:::
