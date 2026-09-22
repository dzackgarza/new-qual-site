---
schema: qual/card@1
id: P-BERK85S-10
kind: problem
title: Minimal polynomial of a three-by-three companion matrix
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
    Used the cyclic vector e_1: e_1, Ae_1, A^2e_1 are the standard basis.
    The relation A^3e_1=a e_1+bAe_1+cA^2e_1 gives the cubic annihilator,
    while cyclicity excludes every annihilator of smaller degree.
---

::: {.problem}
For arbitrary $a,b,c$ in a field $F$, compute the minimal polynomial of
\[
\begin{pmatrix}
0&0&a\\
1&0&b\\
0&1&c
\end{pmatrix}.
\]
:::

::: {.solution}
Let
$$
A
\coloneqq
\begin{pmatrix}
0&0&a\\
1&0&b\\
0&1&c
\end{pmatrix},
$$
and let $e_1,e_2,e_3$ be the standard basis of $F^3$.

<1>1. The vector $e_1$ is cyclic for $A$:
$$
e_1,
\qquad
Ae_1=e_2,
\qquad
A^2e_1=e_3
$$
form a basis of $F^3$.

::: {.proof}
The first column of $A$ is $e_2$, so $Ae_1=e_2$. The second column of
$A$ is $e_3$, so
$$
A^2e_1=Ae_2=e_3.
$$
Thus the three displayed vectors are exactly the standard basis.
:::

<1>2. One has
$$
A^3e_1
=
a e_1+bAe_1+cA^2e_1.
$$

::: {.proof}
By step <1>1,
$$
A^3e_1=Ae_3.
$$
The third column of $A$ is
$$
a e_1+b e_2+c e_3.
$$
Substitute $e_2=Ae_1$ and $e_3=A^2e_1$.
:::

<1>3. The polynomial
$$
q(t)\coloneqq t^3-ct^2-bt-a
$$
annihilates $A$.

::: {.proof}
Step <1>2 says
$$
q(A)e_1=0.
$$
Since $q(A)$ commutes with $A$,
$$
q(A)Ae_1=Aq(A)e_1=0
$$
and
$$
q(A)A^2e_1=A^2q(A)e_1=0.
$$
By step <1>1, the vectors $e_1,Ae_1,A^2e_1$ form a basis. Hence
$q(A)$ vanishes on a basis and therefore
$$
q(A)=0.
$$
:::

<1>4. No nonzero polynomial of degree at most $2$ annihilates $A$.

::: {.proof}
Suppose
$$
p(t)=u+vt+wt^2
$$
satisfies $p(A)=0$. Applying this operator to $e_1$ gives
$$
u e_1+vAe_1+wA^2e_1=0.
$$
The three vectors are linearly independent by step <1>1, so
$$
u=v=w=0.
$$
Thus $p=0$.
:::

<1>5. The minimal polynomial of $A$ is
$$
\boxed{
m_A(t)=t^3-ct^2-bt-a
}.
$$

::: {.proof}
Step <1>3 gives a monic degree-$3$ annihilating polynomial. Step <1>4
shows that no nonzero annihilating polynomial has smaller degree. By the
definition of the minimal polynomial, it must therefore equal $q(t)$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 computes the requested minimal polynomial for arbitrary
$a,b,c\in F$.
:::
:::
