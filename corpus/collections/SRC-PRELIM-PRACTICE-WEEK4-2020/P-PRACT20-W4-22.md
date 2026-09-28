---
schema: qual/card@1
id: P-PRACT20-W4-22
kind: problem
title: Noninvertibility from $AB-BA=A$ and from $A^3=B^3$, $A^2B=B^2A$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Matrices
  - Invertibility
relations: []
review: draft
---

::: {.problem}
Suppose that matrices A, $B \in \mathbb { R } ^ { n \times n }$ satisfy $A B - B A = A$ . Show that A is not invertible.\
If instead we assume $A \neq B , A ^ { 3 } = B ^ { 3 }$ and $A ^ { 2 } B = B ^ { 2 } A$ , show that $A ^ { 2 } + B ^ { 2 }$ is not invertible.
:::

::: {.solution}
<1>1. If $AB-BA=A$, then $A$ is not invertible.
::: {.proof}
Suppose instead that $A$ were invertible. Right-multiplying the relation by $A^{-1}$ gives
$$
ABA^{-1}-B=I,
$$
so
$$
ABA^{-1}=B+I.
$$
Thus $B$ and $B+I$ would be similar. Similar matrices have the same trace, whereas
$$
\operatorname{tr}(B+I)
=\operatorname{tr}(B)+n
\ne\operatorname{tr}(B).
$$
This contradiction shows that $A$ is not invertible.
:::

<1>2. If $A\ne B$, $A^3=B^3$, and $A^2B=B^2A$, then $A^2+B^2$ is not invertible.
::: {.proof}
Using the two hypotheses,
$$
\begin{aligned}
(A^2+B^2)A
&=A^3+B^2A\\
&=B^3+A^2B\\
&=(A^2+B^2)B.
\end{aligned}
$$
Hence
$$
(A^2+B^2)(A-B)=0.
$$
If $A^2+B^2$ were invertible, multiplying by its inverse would give $A-B=0$, contrary to $A\ne B$. Therefore $A^2+B^2$ is not invertible.
:::

<1>3. Q.E.D.
::: {.proof}
Steps <1>1--<1>2 prove the two requested noninvertibility statements.
:::
:::
