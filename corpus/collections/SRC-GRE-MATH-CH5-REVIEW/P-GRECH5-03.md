---
schema: qual/card@1
id: P-GRECH5-03
kind: problem
title: Three assertions about real $2\times2$ matrices
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
  note: Re-transcribed from Chapter 5 review Question 3 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
Let $A$, $B$, and $C$ be real $2 \times 2$ matrices, and let $0$ denote the $2 \times 2$ zero matrix. Which of the following statements is/are true?

I. $A^2 = 0 \Rightarrow A = 0$
II. $AB = AC \Rightarrow B = C$
III. $A$ is invertible and $A = A^{-1} \Rightarrow A = I$ or $A = -I$

(A) I only
(B) I and III only
(C) II and III only
(D) III only
(E) None of the above
:::

::: {.solution}
<1>1. Statement I is false.

::: {.proof}
Take
$$
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
$$
Then $A\ne0$, but direct multiplication gives
$$
A^2=
\begin{pmatrix}
0&0\\
0&0
\end{pmatrix}.
$$
Thus $A^2=0$ does not imply $A=0$.
:::

<1>2. Statement II is false.

::: {.proof}
Use the matrix $A$ from step <1>1 and set
$$
B=I,
\qquad
C=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
$$
Then $B\ne C$, while
$$
AB=A
$$
and
$$
AC=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}
=A.
$$
Hence $AB=AC$ need not imply $B=C$.
:::

<1>3. Statement III is false.

::: {.proof}
Take
$$
A=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
$$
Then
$$
A^2=I,
$$
so $A$ is invertible and $A^{-1}=A$. However,
$$
A\ne I
\qquad\text{and}\qquad
A\ne-I.
$$
:::

<1>4. None of statements I--III is true, so the answer is
$$
\boxed{\text{(E)}}.
$$

::: {.proof}
Steps <1>1--<1>3 provide explicit counterexamples to I, II, and III respectively.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 identifies the correct choice.
:::
:::
