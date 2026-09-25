---
schema: qual/card@1
id: P-BKF86-5
kind: problem
title: Jordan form of $X\mapsto XA-AX$ for a nilpotent $2\times2$ matrix $A$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
---

::: {.problem}
Let $M_{2\times2}$ denote the vector space of complex $2\times2$ matrices.
Let
\[
A=\begin{pmatrix}0&1\\0&0\end{pmatrix}
\]
and let the linear transformation $T:M_{2\times2}\to M_{2\times2}$ be defined by $T(X)=XA-AX$.
Find the Jordan canonical form for $T$.
:::

::: {.solution}
Let $E_{ij}$ denote the standard matrix units in $M_{2\times2}$.

<1>1. The action of $T$ on the standard basis is
$$
\begin{aligned}
T(E_{11})&=E_{12},&
T(E_{12})&=0,\\
T(E_{21})&=E_{22}-E_{11},&
T(E_{22})&=-E_{12}.
\end{aligned}
$$

::: {.proof}
Direct multiplication by
$$
A=\begin{pmatrix}0&1\\0&0\end{pmatrix}
$$
gives
$$
\begin{aligned}
E_{11}A&=E_{12},& AE_{11}&=0,\\
E_{12}A&=0,& AE_{12}&=0,\\
E_{21}A&=E_{22},& AE_{21}&=E_{11},\\
E_{22}A&=0,& AE_{22}&=E_{12}.
\end{aligned}
$$
Subtracting the right products from the left products gives the four displayed formulas.
:::

<1>2. Define
$$
v_1=-2E_{12},\qquad
v_2=E_{22}-E_{11},\qquad
v_3=E_{21},\qquad
v_4=E_{11}+E_{22}.
$$
Then
$$
T(v_1)=0,\qquad
T(v_2)=v_1,\qquad
T(v_3)=v_2,\qquad
T(v_4)=0.
$$

::: {.proof}
By step <1>1,
$$
\begin{aligned}
T(v_1)&=-2T(E_{12})=0,\\
T(v_2)&=T(E_{22})-T(E_{11})=-2E_{12}=v_1,\\
T(v_3)&=T(E_{21})=E_{22}-E_{11}=v_2,\\
T(v_4)&=T(E_{11})+T(E_{22})=0.
\end{aligned}
$$
:::

<1>3. The ordered family $(v_1,v_2,v_3,v_4)$ is a basis of $M_{2\times2}$.

::: {.proof}
Suppose
$$
a v_1+b v_2+c v_3+d v_4=0.
$$
In the basis $(E_{11},E_{12},E_{21},E_{22})$, the left-hand side is
$$
(-b+d)E_{11}-2aE_{12}+cE_{21}+(b+d)E_{22}.
$$
Hence
$$
-b+d=0,\qquad -2a=0,\qquad c=0,\qquad b+d=0.
$$
Thus $a=b=c=d=0$, so the four vectors are linearly independent. Since $M_{2\times2}$ has dimension $4$, they form a basis.
:::

<1>4. The Jordan canonical form of $T$ is
$$
\boxed{
J_3(0)\oplus J_1(0)
=
\begin{pmatrix}
0&1&0&0\\
0&0&1&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}
}.
$$

::: {.proof}
By step <1>3, $(v_1,v_2,v_3,v_4)$ is a basis. Step <1>2 shows that, in this basis, $v_3\mapsto v_2\mapsto v_1\mapsto0$ is one Jordan chain of length $3$, while $v_4\mapsto0$ is a Jordan chain of length $1$. Therefore the matrix of $T$ in this basis is exactly the displayed block diagonal Jordan matrix.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required Jordan canonical form.
:::
:::
