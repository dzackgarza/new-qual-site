---
schema: qual/card@1
id: P-OUQ2Q
kind: problem
title: $\QQ[x]$-modules from order-$6$ matrices in $M_4(\QQ)$, and groups
  of order $24$
classification:
  areas:
  - prelim
  topics:
  - Rational Canonical Form
  - Modules
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---
::: {.problem}
Suppose $A \in M_4(\QQ)$ is a 4-by-4 matrix of multiplicative order 6. We use $A$ to give $\QQ^4$ the structure of a $\QQ[x]$-module in the usual way, by setting $x \cdot v = Av$ for $v \in \QQ^4$.

a. What are all of the isomorphism classes of $\QQ[x]$-modules that can arise this way?

b. For each of your answers above, write down the rational canonical form of the corresponding matrix $A$.

c. What are all the of the abelian groups of size 24 (up to isomorphism)?
:::

::: {.solution}
Write
$$
\Phi_1=x-1,
\qquad
\Phi_2=x+1,
\qquad
\Phi_3=x^2+x+1,
\qquad
\Phi_6=x^2-x+1.
$$
For $j\in\{1,2,3,6\}$, put
$$
M_j=\QQ[x]/(\Phi_j).
$$

::: pf

::: {.pf-step #s1}

The $\QQ[x]$-module $\QQ^4$ is a direct sum of copies of
$M_1,M_2,M_3,M_6$, and the multiplicities
$(a,b,c,d)$ satisfy
$$
a+b+2c+2d=4.
$$

::: pf-proof

Since $A$ has multiplicative order $6$, one has $A^6=I$, so the minimal
polynomial of $A$ divides
$$
x^6-1
=\Phi_1\Phi_2\Phi_3\Phi_6.
$$
These four factors are distinct irreducibles in $\QQ[x]$, so
$x^6-1$ is square-free. Hence the corresponding
$\QQ[x]$-module is semisimple and decomposes as
$$
M_1^{\oplus a}\oplus
M_2^{\oplus b}\oplus
M_3^{\oplus c}\oplus
M_6^{\oplus d}.
$$
The dimensions over $\QQ$ of these four simple modules are
$1,1,2,2$, respectively, which gives the displayed dimension equation.

:::

:::

::: {.pf-step #s2}

The matrix $A$ has order exactly $6$ if and only if
$$
d>0
\qquad\text{or}\qquad
(b>0\text{ and }c>0).
$$

::: pf-proof

The roots of $\Phi_j$ are primitive $j$th roots of unity. Because the
minimal polynomial is square-free, the order of $A$ is the least common
multiple of the orders $j$ for which $M_j$ occurs. Thus the least common
multiple is $6$ exactly when a primitive sixth root occurs, or when both
orders $2$ and $3$ occur.

:::

:::

::: {.pf-step #s3}

The seven possible module isomorphism classes in part (a) are
$$
\boxed{
\begin{aligned}
&M_6\oplus M_6,\\
&M_3\oplus M_6,\\
&M_2\oplus M_2\oplus M_6,\\
&M_2\oplus M_2\oplus M_3,\\
&M_1\oplus M_2\oplus M_6,\\
&M_1\oplus M_2\oplus M_3,\\
&M_1\oplus M_1\oplus M_6.
\end{aligned}}
$$

::: pf-proof

By step [](#s1){.pf-ref}, the multiplicity quadruples satisfy
$a+b+2c+2d=4$, and step [](#s2){.pf-ref} imposes the order-$6$ condition.

If $d=2$, the only solution is $(0,0,0,2)$.
If $d=1$, the remaining dimension is $2$, giving
$$
(0,0,1,1),\quad
(2,0,0,1),\quad
(1,1,0,1),\quad
(0,2,0,1).
$$
If $d=0$, step [](#s2){.pf-ref} requires $b,c>0$. Then necessarily $c=1$ and
$a+b=2$, giving
$$
(1,1,1,0),\quad(0,2,1,0).
$$
These seven possibilities are pairwise nonisomorphic by uniqueness of
the primary decomposition over the PID $\QQ[x]$.

:::

:::

::: {.pf-step #s4}

For a monic polynomial
$$
p(x)=x^r+c_{r-1}x^{r-1}+\cdots+c_0,
$$
write
$$
C(p)=
\begin{pmatrix}
0&0&\cdots&0&-c_0\\
1&0&\cdots&0&-c_1\\
0&1&\cdots&0&-c_2\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
0&0&\cdots&1&-c_{r-1}
\end{pmatrix}.
$$
The seven rational canonical forms corresponding to step [](#s3){.pf-ref} are
$$
\boxed{
\begin{aligned}
&\operatorname{diag}(C(\Phi_6),C(\Phi_6)),\\
&C(\Phi_3\Phi_6),\\
&\operatorname{diag}(C(\Phi_2),C(\Phi_2\Phi_6)),\\
&\operatorname{diag}(C(\Phi_2),C(\Phi_2\Phi_3)),\\
&C(\Phi_1\Phi_2\Phi_6),\\
&C(\Phi_1\Phi_2\Phi_3),\\
&\operatorname{diag}(C(\Phi_1),C(\Phi_1\Phi_6)).
\end{aligned}}
$$

::: pf-proof

The invariant factors are obtained by placing each irreducible factor
$\Phi_j$ into the last as many invariant factors as its multiplicity.
Thus the seven invariant-factor lists are
$$
\begin{aligned}
&(\Phi_6,\Phi_6),\\
&(\Phi_3\Phi_6),\\
&(\Phi_2,\Phi_2\Phi_6),\\
&(\Phi_2,\Phi_2\Phi_3),\\
&(\Phi_1\Phi_2\Phi_6),\\
&(\Phi_1\Phi_2\Phi_3),\\
&(\Phi_1,\Phi_1\Phi_6).
\end{aligned}
$$
Each list satisfies the required divisibility chain, and its companion
blocks give the displayed rational canonical form. Explicitly,
$$
\begin{aligned}
\Phi_3\Phi_6&=x^4+x^2+1,\\
\Phi_2\Phi_6&=x^3+1,\\
\Phi_2\Phi_3&=x^3+2x^2+2x+1,\\
\Phi_1\Phi_2\Phi_6&=x^4-x^3+x-1,\\
\Phi_1\Phi_2\Phi_3&=x^4+x^3-x-1,\\
\Phi_1\Phi_6&=x^3-2x^2+2x-1.
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

The abelian groups of order $24$ are
$$
\boxed{
\ZZ/24,\qquad
\ZZ/2\times\ZZ/12,\qquad
(\ZZ/2)^2\times\ZZ/6}.
$$

::: pf-proof

Since $24=2^3\cdot3$, the classification theorem for finite abelian
groups gives three possibilities for the Sylow $2$-subgroup,
$$
\ZZ/8,
\qquad
\ZZ/4\times\ZZ/2,
\qquad
(\ZZ/2)^3,
$$
and the unique Sylow $3$-part $\ZZ/3$. Combining relatively prime cyclic
factors gives exactly the three displayed groups.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} answers part (a), step [](#s4){.pf-ref} answers part (b), and step [](#s5){.pf-ref}
answers part (c).

:::

:::

:::
