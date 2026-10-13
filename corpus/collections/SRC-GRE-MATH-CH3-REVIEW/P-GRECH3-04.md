---
schema: qual/card@1
id: P-GRECH3-04
kind: problem
title: Solve a cross-product equation using the vector triple product
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 4 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Given the vector identity $\mathbf{A}\times(\mathbf{B}\times\mathbf{C})=(\mathbf{A}\cdot\mathbf{C})\mathbf{B}-(\mathbf{A}\cdot\mathbf{B})\mathbf{C}$, which of the following vectors $\mathbf{V}$ satisfies the equation $\mathbf{A}\times\mathbf{V}=\mathbf{B}$, where $\mathbf{A}$ is a unit vector and $\mathbf{B}$ is a vector orthogonal to $\mathbf{A}$?

(A) $\mathbf{B}+(\mathbf{A}\times\mathbf{B})$
(B) $\mathbf{B}-(\mathbf{A}\times\mathbf{B})$
(C) $\mathbf{A}\times\mathbf{B}$
(D) $\mathbf{A}+(\mathbf{A}\times\mathbf{B})$
(E) $\mathbf{A}-(\mathbf{A}\times\mathbf{B})$
:::

::: {.solution}
<1>1. The vector triple product gives
$$
\mathbf A\times(\mathbf A\times\mathbf B)=-\mathbf B.
$$

::: {.proof}
Apply the stated identity with the outer vector and the first inner vector both equal to $\mathbf A$:
$$
\mathbf A\times(\mathbf A\times\mathbf B)
=(\mathbf A\cdot\mathbf B)\mathbf A
-(\mathbf A\cdot\mathbf A)\mathbf B.
$$
Because $\mathbf A\perp\mathbf B$, the first scalar product is $0$. Because $\mathbf A$ is a unit vector, $\mathbf A\cdot\mathbf A=1$. Hence the expression equals $-\mathbf B$.
:::

<1>2. For
$$
\mathbf V=\mathbf A-(\mathbf A\times\mathbf B),
$$
one has $\mathbf A\times\mathbf V=\mathbf B$.

::: {.proof}
By bilinearity of the cross product and step <1>1,
$$
\begin{aligned}
\mathbf A\times\mathbf V
&=\mathbf A\times\mathbf A
-\mathbf A\times(\mathbf A\times\mathbf B)\\
&=0-(-\mathbf B)\\
&=\mathbf B.
\end{aligned}
$$
:::

<1>3. Therefore the answer is
$$
\boxed{\text{(E) }\mathbf A-(\mathbf A\times\mathbf B)}.
$$

::: {.proof}
Step <1>2 verifies directly that the vector in choice (E) satisfies the required equation.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested vector and corresponding choice.
:::
:::
