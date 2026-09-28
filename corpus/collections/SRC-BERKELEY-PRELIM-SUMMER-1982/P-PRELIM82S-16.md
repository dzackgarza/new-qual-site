---
schema: qual/card@1
id: P-PRELIM82S-16
kind: problem
title: Sums of nilpotent matrices and invertibility of $I-A$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For part (a), the two standard square-zero off-diagonal 2-by-2
    matrices are nilpotent, while their sum squares to the identity and
    is not nilpotent. For part (b), if A^k=0 then
    I+A+...+A^{k-1} is a two-sided inverse of I-A by the finite
    geometric-series identity.
---

::: {.problem}
A square matrix $A$ is nilpotent if $A^k=0$ for some positive integer $k$.

(a) If $A$ and $B$ are nilpotent, must $A+B$ be nilpotent?
Give a proof or counterexample.

(b) Prove that if $A$ is nilpotent, then $I-A$ is invertible.
:::

::: {.solution}
<1>1. (a) The sum of two nilpotent matrices need not be nilpotent.

::: {.proof}
Take
$$
A=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
$$
Then
$$
A^2=0,
\qquad
B^2=0,
$$
so both $A$ and $B$ are nilpotent. However,
$$
A+B=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
$$
and
$$
(A+B)^2=I.
$$
Hence
$$
(A+B)^{2m}=I
$$
for every $m\geq1$. If $(A+B)^r=0$ for some $r\geq1$, then
$(A+B)^{2r}=0$, contradicting the displayed identity with $m=r$.
Thus $A+B$ is not nilpotent.
:::

<1>2. (b) Suppose $A^k=0$ for some $k\geq1$, and define
$$
S=I+A+A^2+\cdots+A^{k-1}.
$$
Then
$$
(I-A)S=I.
$$

::: {.proof}
Expanding and cancelling consecutive powers gives
$$
\begin{aligned}
(I-A)S
&=
(I+A+\cdots+A^{k-1})
-
(A+A^2+\cdots+A^k)\\
&=
I-A^k\\
&=
I.
\end{aligned}
$$
:::

<1>3. Under the same hypotheses,
$$
S(I-A)=I.
$$

::: {.proof}
Since every term of $S$ is a power of $A$, it commutes with $A$. Thus
the same finite geometric-series computation gives
$$
S(I-A)=I-A^k=I.
$$
:::

<1>4. Therefore
$$
\boxed{(I-A)^{-1}=I+A+A^2+\cdots+A^{k-1}}.
$$

::: {.proof}
Steps <1>2 and <1>3 show that the displayed matrix is both a left and
right inverse of $I-A$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 answers part (a), and step <1>4 proves part (b).
:::
:::
