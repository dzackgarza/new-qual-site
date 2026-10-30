---
schema: qual/card@1
id: P-GREPT-44
kind: problem
title: "Second eigenvalue of a $2\\times2$ matrix with eigenvalue $1$"
classification:
  areas: [applied-algebra]
  topics:
  - Eigenvalues
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 44 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If the matrix $A = \begin{pmatrix} t & 1-t \\ 1 & 2t \end{pmatrix}$ has $1$ as an eigenvalue, then another eigenvalue of $A$ could be

(A) $-3$
(B) $-2$
(C) $2$
(D) $3$
(E) $4$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since $1$ is an eigenvalue,
$$
\det(A-I)=0.
$$


::: pf-proof

A scalar $\lambda$ is an eigenvalue exactly when $A-\lambda I$ is singular.
Applying this with $\lambda=1$ gives the stated determinant equation.

:::

:::

::: {.pf-step #s1-2}

The condition in step [](#s1-1){.pf-ref} forces
$$
t=0
\qquad\text{or}\qquad
t=1.
$$


::: pf-proof

One has
$$
A-I=
\begin{pmatrix}
t-1&1-t\\
1&2t-1
\end{pmatrix},
$$
so
$$
\begin{aligned}
0&=(t-1)(2t-1)-(1-t)\\
&=(t-1)(2t-1)+(t-1)\\
&=2t(t-1).
\end{aligned}
$$
Thus $t=0$ or $t=1$.

:::

:::

::: {.pf-step #s1-3}

If $t=0$, the other eigenvalue is $-1$; if $t=1$, the other
eigenvalue is $2$.


::: pf-proof

For a $2\times2$ matrix, the sum of the two eigenvalues equals the trace.
Here $\operatorname{tr}(A)=3t$. Since one eigenvalue is $1$, the other is
$3t-1$. Substituting the two values from step [](#s1-2){.pf-ref} gives $-1$ and $2$.

:::

:::

::: {.pf-step #s1-4}

Therefore another eigenvalue could be
$$
\boxed{2},
$$
so the answer is (C).


::: pf-proof

Step [](#s1-3){.pf-ref} lists all possible second eigenvalues, and among the choices only
$2$ occurs.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required choice.

:::

:::

:::
