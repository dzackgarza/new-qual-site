---
schema: qual/card@1
id: P-UMKJ4
kind: problem
title: "The goal is to show that any matrix $A \\in M(m\\times n, R)$ is equivalent to a\u2026"
classification:
  areas:
  - algebra
  topics:
  - smith-normal-form
  - canonical-forms
  - principal-ideal-domains
relations: []
review: draft
---

::: problem
> Proof following http://sierra.nmsu.edu/morandi/notes/SmithNormalForm.pdf

The goal is to show that any matrix $A \in M(m\times n, R)$ is *equivalent* to a matrix $D$ of the described form, so $A = PDQ$ for some matrices $P,Q$.
Since $D$ is by construction the Smith normal form of $A$, it suffices to show that $SNF(A)$ can be obtained by left and right multiplication by invertible matrices.
Row operations are performed by left-multiplication by elementary matrices, and column operations by right-multiplication.

We proceed by induction on $m+n$.

For the base case $m + n = 2$, this can only yield a $1\times 1$ matrix, which is already in the desired form.

For the inductive step, we will proceed by considering the top-left $2\times 2$ block, say $M = \left[ \begin{array}{cc} a & b \\ c & d \end{array}\right]$, and showing it can be reduced to a block of the form $M' = \left[ \begin{array}{cc} d_1 & 0 \\ 0 & d_2 \end{array}\right]$ where $d_1 \divides d_2$. 
Then the sub-matrix obtained by deleting the row and column containing $d_1$ is a strictly smaller matrix, allowing the inductive hypothesis to be applied.

Moreover, note that if we are able to perform this reduction by a series of left and right multiplications, this will yields $A_1 = P_1 A Q_1$, and inductively we will have $A_{r} = (P_r \cdots P_2 P_1) A (Q_1 Q_2 \cdots Q_R)$, so each matrix will remain equivalent at every step.

> Note: since $R$ is a PID, any two elements have a gcd, and Bézout holds: $\gcd(a,c) = sa + tc$ for some $s,t\in R$, because $\gens{a, c} = \gens{\gcd(a,c)}$.
> This does not need $R$ to be Euclidean, and indeed not every PID is: $\ZZ\left[ \frac{1+\sqrt{-19} }{2} \right]$ is a PID that admits no Euclidean function.

We'll first reduce the top-left entry and eliminate the bottom-left entry.

Let $d = \gcd(a, c)$, so we can write $d = sa + tc$ for some $s, t\in R$.
We would like to construct an operation that replaces $a$ in $M$ with $d$.

So let $\ell_1, \ell_2$ be parameters to be determined; we can then compute

\begin{align*}
P_1 A = \left[\begin{array}{cc} s & t \\ \ell_1 & \ell_2 \end{array}\right]
\left[\begin{array}{cc} a & b \\ c & d \end{array}\right] =
\left[\begin{array}{cc} d & sb + td \\ \ell_1 a + \ell_2 c & \ell_1 b + \ell_2 d \end{array}\right]
,\end{align*}

where we now only have to choose $\ell_1, \ell_2$ so that $P_1$ is invertible.


This lets us engineer an inverse matrix

\begin{align*}
P_1\inv \definedas \left[\begin{array}{cc} \ell_2 & -t \\ -\ell_1 & s \end{array}\right] \\
\implies P_1 P_1\inv &=
\left[\begin{array}{cc} s & t \\ \ell_1 & \ell_2 \end{array}\right]
\left[\begin{array}{cc} \ell_2 & -t \\ -\ell_1 & s \end{array}\right] \\
&=
\left[\begin{array}{cc} s\ell_2 - t\ell_1 & -ts + st \\ \ell_1 \ell_2 - \ell_2 \ell_1 & -t\ell_1 + s\ell_2  \end{array}\right]
,\end{align*}

which just says that we need to pick $\ell_1, \ell_2$ such that $s\ell_2 - t\ell_1 = 1$, since the off-diagonal entries vanish because $R$ is commutative.


But this can be done by writing $a = d k_1$ and $c = d k_2$, since $d$ was their gcd, then 
$$
d = sa + tc =  s dk_1 + t d k_2 \implies 1 = s k_1 + t k_2,
$$

so just choose $\ell_1  = -k_2, \ell_2 = k_1$ to get $s\ell_2 - t\ell_1 = sk_1 + tk_2 = 1$, yielding $P_1 P_1\inv = I_2$.

We can observe that in the matrix $P_1 A$, since $d$ divides $a$ and $c$, $d$ also divides $\ell_1a+\ell_2 c$.
So write $kd = \ell_1 a + \ell_2 c$, we can then perform a row operation by left-multiplying:


\begin{align*}
Q_1  P_1 A\definedas \left[\begin{array}{cc} 1 & 0 \\ -k & 1 \end{array}\right]
\left[\begin{array}{cc} d & sb + td \\ \ell_1 a + \ell_2 c & \ell_1 b + \ell_2 d \end{array}\right] =
\left[\begin{array}{cc} d & sb + td \\ 0 & -k(sb + td) + \ell_1 b + \ell_2 d \end{array}\right]
.\end{align*}

We now carry out the same process with the top *row* instead of the first *column*.
This begins by computing $d_1 = \gcd(d, sb + td)$, where we can immediately note that $d_1$ divides $d$.

We then write 
$$
d_1 = d s' + (sb + td)t',
$$

then perform column operations (i.e. right-multiplying by some $R_1$) to obtain a matrix of the form 
$$
Q_1 P_1 A R_1 \definedas 
\left[\begin{array}{cc} d & sb + td \\ 0 & -k(sb + td) + \ell_1 b + \ell_2 d \end{array}\right]
\left[\begin{array}{cc} s' & \ell_3 \\ t' & \ell_4 \end{array}\right] = 
\left[\begin{array}{cc} d_1 &  d\ell_3 + (sb + td)\ell_4 \\ ? & ? \end{array}\right]
$$

where again $\ell_3, \ell_4$ are parameters that can be chosen to make $R_1$ invertible.

We can again observe that $d_1$ divides the top-left and (now) the top-right entry, which means we can find a $k'$ such that 

\begin{align*}
Q_1 P_1 A R_1 S_1 \definedas 
\left[\begin{array}{cc} d_1 &  d\ell_3 + (sb + td)\ell_4 \\ ? & ? \end{array}\right]
\left[\begin{array}{cc} 1 & 0 \\ -k' & 1 \end{array}\right] =
\left[\begin{array}{cc} d_1 & 0 \\ ? & ? \end{array}\right]
,\end{align*}

which puts us back in the original situation.

We can then continue by obtaining a $d_2$ that divides $d_1$, doing row operations, and obtaining a matrix of the form
$$
P_2 Q_1P_1 A R_1 S_1 \definedas \left[\begin{array}{cc} d_2 & ? \\ 0 & ? \end{array}\right],
$$
and so on.

In a PID, "to divide is to contain" for ideals, so this generates a sequence of ideals 
$$
(d) \subseteq (d_1) \subseteq (d_2) \subseteq \cdots
$$ 
and since every PID is Noetherian, this increasing chain of ideals eventually stabilizes.

This means that after finitely many steps, we find $d_{N+1} \definedas \gcd(d_N, \cdots) = d_N$, 

obtain a matrix
$$
N \definedas \left(\prod_i Q_i P_i \right) A \left( \prod_i R_i S_i \right) = 
\left[\begin{array}{cc} d_N & x \\ y & z \end{array}\right]
$$

where either 

- $x=0$ and $y$ divides $d_N$, or
- $y = 0$ and $x$ divides $d_N$.

Without loss of generality, supposing the first case holds, we can write $d_N = \alpha y$; then

\begin{align*}
E N \definedas
\left[\begin{array}{cc} 1 & 0 \\ 1 & -\alpha \end{array}\right]
\left[\begin{array}{cc} d_N & 0 \\ y & z \end{array}\right] = 
\left[\begin{array}{cc} d_N & 0 \\ 0 & z \end{array}\right]
,\end{align*}

where $E$ is again invertible, yielding a diagonal matrix.

> Note: in the general case of an $m\times n$ matrix, this eliminates entries $1,2$ and $2,1$. Eliminating the remaining entries in row 1 and column 1 proceed similarly, and never perturb entries that were made zero in a previous step.

Since it is not necessarily the case that $d_N$ divides $z$ here, a small additional modification is needed. This is accomplished by a series of row operations, as described here:

![Image](../../assets/10_Algebra/500_Exercises/PSets/PSet%209/figures/2019-11-26-22%3A38.png)\

This yields the desired form in the top-left $2\times 2$ block, zeroing out the first column and row, so the inductive hypothesis applies to the remaining block. $\qed$
:::
