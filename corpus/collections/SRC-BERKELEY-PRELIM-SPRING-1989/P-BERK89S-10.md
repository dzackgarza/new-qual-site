---
schema: qual/card@1
id: P-BERK89S-10
kind: problem
title: Invertibility of a $2\times2$ block matrix with commuting blocks
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used the commuting-block adjugate identity and, for the converse, produced
    a nonzero kernel vector for the block matrix from a kernel vector of
    $AD-BC$.
---

::: {.problem}
Let
\[
X=\begin{pmatrix}A&B\\C&D\end{pmatrix}
\]
be a real $2n\times2n$ matrix, where $A,B,C,D$ are $n\times n$ matrices that commute pairwise. Prove that $X$ is invertible if and only if
\[
AD-BC
\]
is invertible.
:::

::: {.solution}
Set
$$
\Delta=AD-BC,
\qquad
Y=\begin{pmatrix}D&-B\\-C&A\end{pmatrix}.
$$

<1>1. One has
$$
XY=YX=
\begin{pmatrix}
\Delta&0\\
0&\Delta
\end{pmatrix}.
$$

::: {.proof}
Direct block multiplication gives
$$
XY=
\begin{pmatrix}
AD-BC&-AB+BA\\
CD-DC&-CB+DA
\end{pmatrix}.
$$
Because $A,B,C,D$ commute pairwise, the off-diagonal blocks vanish and the
lower-right block equals $AD-BC=\Delta$. Thus
$$
XY=\begin{pmatrix}\Delta&0\\0&\Delta\end{pmatrix}.
$$
Similarly,
$$
YX=
\begin{pmatrix}
DA-BC&DB-BD\\
-CA+AC&-CB+AD
\end{pmatrix}
=\begin{pmatrix}\Delta&0\\0&\Delta\end{pmatrix}.
$$
:::

<1>2. If $\Delta$ is invertible, then $X$ is invertible.

::: {.proof}
Let
$$
Z=\begin{pmatrix}\Delta^{-1}&0\\0&\Delta^{-1}\end{pmatrix}.
$$
By step <1>1,
$$
X(YZ)=(XY)Z=I_{2n}.
$$
Since $X$ is a square matrix, the existence of this right inverse implies
that $X$ is invertible.
:::

<1>3. If $\Delta$ is singular, then $X$ is singular.

::: {.proof}
Choose $0\neq v\in\RR^n$ with $\Delta v=0$. Consider first
$$
u_1=\binom{Dv}{-Cv}.
$$
Using pairwise commutativity,
$$
Xu_1
=\binom{ADv-BCv}{CDv-DCv}
=\binom{\Delta v}{0}
=0.
$$
If $u_1\neq0$, then $X$ has a nonzero kernel vector and is singular.

Suppose $u_1=0$, so $Cv=Dv=0$, and set
$$
u_2=\binom{-Bv}{Av}.
$$
Then
$$
Xu_2
=\binom{-ABv+BAv}{-CBv+DAv}
=\binom{0}{\Delta v}
=0.
$$
If $u_2\neq0$, again $X$ is singular. Finally, if $u_2=0$ as well, then
$Av=Bv=Cv=Dv=0$. The nonzero vector
$$
u_3=\binom{v}{0}
$$
satisfies
$$
Xu_3=\binom{Av}{Cv}=0.
$$
Thus $X$ is singular in every case.
:::

<1>4. The matrix $X$ is invertible if and only if $AD-BC$ is invertible.

::: {.proof}
Step <1>2 proves that invertibility of $AD-BC=\Delta$ implies invertibility
of $X$. The contrapositive of step <1>3 proves that invertibility of $X$
implies invertibility of $\Delta$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required equivalence.
:::
:::
