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

::: pf

::: {.pf-step #block-product-identity}
One has
$$
XY=YX=
\begin{pmatrix}
\Delta&0\\
0&\Delta
\end{pmatrix}.
$$

::: pf-proof
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

:::

::: {.pf-step #delta-invertible-implies-x}
If $\Delta$ is invertible, then $X$ is invertible.

::: pf-proof
Let
$$
Z=\begin{pmatrix}\Delta^{-1}&0\\0&\Delta^{-1}\end{pmatrix}.
$$
By step [](#block-product-identity){.pf-ref},
$$
X(YZ)=(XY)Z=I_{2n}.
$$
Since $X$ is a square matrix, the existence of this right inverse implies
that $X$ is invertible.
:::

:::

::: {.pf-step #delta-singular-implies-x}
If $\Delta$ is singular, then $X$ is singular.

::: pf-proof
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

:::

::: {.pf-step #equivalence}
The matrix $X$ is invertible if and only if $AD-BC$ is invertible.

::: pf-proof
Step [](#delta-invertible-implies-x){.pf-ref} proves that invertibility of $AD-BC=\Delta$ implies invertibility
of $X$. The contrapositive of step [](#delta-singular-implies-x){.pf-ref} proves that invertibility of $X$
implies invertibility of $\Delta$.
:::

:::

::: pf-qed
Step [](#equivalence){.pf-ref} is the required equivalence.
:::

:::
:::
