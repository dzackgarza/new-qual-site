---
schema: qual/card@1
id: P-B2P3P
kind: problem
title: Jordan and rational forms from characteristic and minimal polynomials;
  nilpotents with a unique two-dimensional invariant subspace
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Rational Canonical Form
  - Nilpotence
relations: []
review: draft
---

::: {.problem}
Let $V$ be a 5-dimensional vector space over a field $F$.

a. Let $T: V \to V$ be a linear transformation with characteristic polynomial $(x-1)^3(x-2)^2$ and minimal polynomial $(x-1)^2(x-2)$.
    i. Write down a matrix which represents $T$ in Jordan normal form.
    ii. Write down the matrix which represents $T$ in rational normal form.
b. Instead, let $T: V \to V$ be a *nilpotent* linear transformation which has exactly one 2-dimensional invariant subspace.
    i. How many similarity classes of such linear maps $T$ are there?
    ii. Assuming finally that $F$ is the finite field $\mathbb{F}_q$ with $q$ elements, find an explicit formula for the number of such linear maps $T$.
:::

::: {.solution}
<1>1. In part (a), the Jordan canonical form is
$$
\boxed{
J_2(1)\oplus[1]\oplus[2]\oplus[2]
}
=
\begin{pmatrix}
1&1&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&2&0\\
0&0&0&0&2
\end{pmatrix}.
$$
::: {.proof}
The characteristic polynomial has algebraic multiplicities $3$ at $1$ and $2$ at $2$. The exponent $2$ of $x-1$ in the minimal polynomial forces the largest Jordan block at eigenvalue $1$ to have size $2$, so the partition of $3$ is $2+1$. The exponent $1$ of $x-2$ forces all Jordan blocks at eigenvalue $2$ to have size $1$, so the partition of $2$ is $1+1$.
:::

<1>2. In part (a), the invariant factors are
$$
d_1=(x-1)(x-2),
\qquad
d_2=(x-1)^2(x-2),
$$
and the rational canonical form is
$$
\boxed{
\begin{pmatrix}
0&-2&0&0&0\\
1&3&0&0&0\\
0&0&0&0&2\\
0&0&1&0&-5\\
0&0&0&1&4
\end{pmatrix}
}.
$$
::: {.proof}
The elementary divisors are
$$
(x-1),\quad (x-1)^2,\quad (x-2),\quad (x-2).
$$
Aligning the prime-power factors by divisibility gives the two invariant factors $d_1\mid d_2$ displayed above. Their companion matrices are
$$
C(d_1)=
\begin{pmatrix}0&-2\\1&3\end{pmatrix},
\qquad
C(d_2)=
\begin{pmatrix}
0&0&2\\
1&0&-5\\
0&1&4
\end{pmatrix},
$$
whose block diagonal sum is the displayed rational canonical form.
:::

<1>3. In part (b), there is exactly one similarity class: the regular nilpotent class
$$
\boxed{J_5(0)}.
$$
::: {.proof}
For a single nilpotent Jordan block $J_5(0)$, the corresponding $F[x]$-module is
$$
F[x]/(x^5).
$$
Its submodules are exactly $(x^j)/(x^5)$, so there is exactly one submodule of dimension $2$, namely $(x^3)/(x^5)$.

Conversely, suppose the nilpotent Jordan form has at least two blocks. Let $u$ and $v$ be nonzero vectors at the bottoms of two distinct Jordan chains. Then
$$
W_1=\Span\{u,v\}
$$
is a $2$-dimensional invariant subspace. If some Jordan block has size at least $2$, choose a predecessor $u'$ with $Tu'=u$; then
$$
W_2=\Span\{u,u'\}
$$
is another invariant $2$-plane, distinct from $W_1$. If every block has size $1$, then $T=0$ and every $2$-plane is invariant, so uniqueness again fails. Hence exactly one invariant $2$-plane occurs precisely for the single block $J_5(0)$.
:::

<1>4. If $F=\FF_q$, the number of such linear maps is
$$
\boxed{q^6(q^5-1)(q^4-1)(q^3-1)(q^2-1)}.
$$
::: {.proof}
By step <1>3, these maps form the conjugacy class of the regular nilpotent $J_5(0)$ in $\GL_5(\FF_q)$. Its invertible centralizer consists of the units in
$$
\FF_q[J_5(0)]\cong \FF_q[t]/(t^5),
$$
namely the polynomials
$$
a_0+a_1J_5(0)+\cdots+a_4J_5(0)
$$
with $a_0\ne0$. Thus the centralizer has order
$$
(q-1)q^4.
$$
Since
$$
|\GL_5(\FF_q)|
=q^{10}(q^5-1)(q^4-1)(q^3-1)(q^2-1)(q-1),
$$
orbit-stabilizer gives
$$
\frac{|\GL_5(\FF_q)|}{(q-1)q^4}
=q^6(q^5-1)(q^4-1)(q^3-1)(q^2-1).
$$
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>1 and step <1>2 answer part (a), while step <1>3 and step <1>4 answer part (b).
:::
:::
