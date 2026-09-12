---
schema: qual/card@1
id: P-BKF81-4
kind: problem
title: Cayley transform between orthogonal and skew-symmetric matrices
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Verified both directions of the Cayley transform using transpose identities, proved I±S invertible for skew-symmetric S, and checked the formulas are mutual inverses."
---

::: problem
Prove the following for real $n\times n$ matrices.

(a) If $A$ is orthogonal and has no eigenvalue $-1$, then $I+A$ is nonsingular and $S=(I-A)(I+A)^{-1}$ is skew-symmetric.

(b) If $S$ is skew-symmetric, then $A=(I-S)(I+S)^{-1}$ is orthogonal and has no eigenvalue $-1$.

(c) The correspondence between $A$ and $S$ is one-to-one.
:::

::: solution
<1>1. Prove part (a).
::: proof
Assume $A$ is orthogonal and has no eigenvalue $-1$. Then
$$
\ker(I+A)=\{0\},
$$
so $I+A$ is nonsingular.

Define
$$
S=(I-A)(I+A)^{-1}.
$$
Since $A^t=A^{-1}$,
$$
\begin{aligned}
S^t
&=(I+A^t)^{-1}(I-A^t)\\
&=(I+A^{-1})^{-1}(I-A^{-1}).
\end{aligned}
$$
Now
$$
I+A^{-1}=A^{-1}(I+A),
$$
and
$$
I-A^{-1}=-A^{-1}(I-A).
$$
Therefore
$$
S^t
=-(I+A)^{-1}(I-A).
$$
The matrices $I-A$ and $I+A$ commute, so they also commute with
$(I+A)^{-1}$. Hence
$$
S^t=-(I-A)(I+A)^{-1}=-S.
$$
Thus $S$ is skew-symmetric.
:::

<1>2. For skew-symmetric $S$, both $I+S$ and $I-S$ are nonsingular.
::: proof
Suppose
$$
(I+S)x=0.
$$
Then $Sx=-x$. Since $S^t=-S$ and the matrices are real,
$$
\langle Sx,x\rangle
=-\langle x,Sx\rangle
=-\langle Sx,x\rangle,
$$
so
$$
\langle Sx,x\rangle=0.
$$
But $Sx=-x$ would give
$$
\langle Sx,x\rangle=-\|x\|^2,
$$
hence $x=0$. Thus $I+S$ is nonsingular. The same argument with $Sx=x$
shows that $I-S$ is nonsingular.
:::

<1>3. Prove that $A=(I-S)(I+S)^{-1}$ is orthogonal and has no eigenvalue $-1$.
::: proof
Let $S^t=-S$ and define
$$
A=(I-S)(I+S)^{-1}.
$$
By step <1>2 this is well-defined. Taking transposes,
$$
\begin{aligned}
A^t
&=(I+S^t)^{-1}(I-S^t)\\
&=(I-S)^{-1}(I+S).
\end{aligned}
$$
Since $I-S$ and $I+S$ commute,
$$
A^{-1}=(I+S)(I-S)^{-1}=(I-S)^{-1}(I+S)=A^t.
$$
Thus $A$ is orthogonal.

Moreover
$$
I+A
=\bigl((I+S)+(I-S)\bigr)(I+S)^{-1}
=2(I+S)^{-1},
$$
which is nonsingular. Therefore $-1$ is not an eigenvalue of $A$.
:::

<1>4. The two formulas are mutual inverses.
::: proof
Starting from
$$
S=(I-A)(I+A)^{-1},
$$
we obtain
$$
I-S=2A(I+A)^{-1},
$$
and
$$
I+S=2(I+A)^{-1}.
$$
Hence
$$
(I-S)(I+S)^{-1}=A.
$$

Conversely, starting from
$$
A=(I-S)(I+S)^{-1},
$$
one similarly gets
$$
I-A=2S(I+S)^{-1},
\qquad
I+A=2(I+S)^{-1},
$$
and therefore
$$
(I-A)(I+A)^{-1}=S.
$$
Thus the two constructions undo each other. In particular the correspondence
between orthogonal matrices without eigenvalue $-1$ and skew-symmetric
matrices is one-to-one.
:::
:::
