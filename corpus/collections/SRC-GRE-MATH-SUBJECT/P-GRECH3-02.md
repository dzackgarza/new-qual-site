---
schema: qual/card@1
id: P-GRECH3-02
kind: problem
title: Vector not orthogonal to a given vector
classification:
  areas:
  - real-analysis
  topics:
  - Vectors
  - Dot Product
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 2 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree. Choice (C), lost in the chapter-3.pdf extraction, is taken from the book extraction."
---

::: {.problem}
If $\hat{\mathbf{i}}=(1,0,0)$, $\hat{\mathbf{j}}=(0,1,0)$, and $\hat{\mathbf{k}}=(0,0,1)$, which one of the following vectors is not orthogonal to $\mathbf{v}=2\hat{\mathbf{i}}-\hat{\mathbf{j}}+3\hat{\mathbf{k}}$?

(A) $\hat{\mathbf{i}}-\hat{\mathbf{j}}-\hat{\mathbf{k}}$
(B) $\hat{\mathbf{i}}+2\hat{\mathbf{j}}$
(C) $3\hat{\mathbf{i}}-2\hat{\mathbf{k}}$
(D) $\hat{\mathbf{i}}+3\hat{\mathbf{j}}-\hat{\mathbf{k}}$
(E) $2\hat{\mathbf{i}}+\hat{\mathbf{j}}-\hat{\mathbf{k}}$
:::

Write
$$
\mathbf v=(2,-1,3).
$$

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The vectors in choices (A), (B), (C), and (E) are orthogonal to $\mathbf v$.


::: pf-proof

Their dot products with $\mathbf v$ are
$$
\begin{aligned}
(2,-1,3)\cdot(1,-1,-1)&=2+1-3=0,\\
(2,-1,3)\cdot(1,2,0)&=2-2=0,\\
(2,-1,3)\cdot(3,0,-2)&=6-6=0,\\
(2,-1,3)\cdot(2,1,-1)&=4-1-3=0.
\end{aligned}
$$
Thus each of these four vectors is orthogonal to $\mathbf v$.

:::

:::

::: {.pf-step #s1-2}

The vector in choice (D) is not orthogonal to $\mathbf v$.


::: pf-proof

For choice (D),
$$
(2,-1,3)\cdot(1,3,-1)
=2-3-3
=-4\ne0.
$$
Hence this vector is not orthogonal to $\mathbf v$.

:::

:::

::: {.pf-step #s1-3}

Therefore the answer is
$$
\boxed{\text{(D) }\hat{\mathbf{i}}+3\hat{\mathbf{j}}-\hat{\mathbf{k}}}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show that (D) is the unique listed vector whose dot product with $\mathbf v$ is nonzero.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested vector and corresponding choice.

:::

:::

:::
