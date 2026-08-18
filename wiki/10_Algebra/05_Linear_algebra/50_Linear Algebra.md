---
order: 50
---

# Linear Algebra

:::{.remark}
Algorithm for SNF: D&F page 479.

:::

:::{.remark}
Some definitions:

- $A^t$ is the usual transpose.
- $A^{\dagger}$ is the conjugate transpose.
- A matrix is $A^{\dagger}$ is **adjoint** to $A$ iff $\inner{A\vector x}{\vector y} = \inner{\vector x}{A^{\dagger} \vector y}$.
  - $A$ is **self-adjoint** iff $A$ is an adjoint for itself, so $\inner{A\vector x}{\vector y} = \inner{\vector x}{A \vector y}$.
- $A$ is **symmetric** iff $A = A^t$.
  - $A$ is **orthogonal** iff $A^tA = AA^t = I$
- $A$ is **Hermitian** iff $A^{\dagger} = A$.
  - $A$ is **normal** iff $AA^{\dagger} = A^{\dagger} A$.
  - $A$ is **unitary** iff $A^{\dagger}A = AA^{\dagger} = I$.

:::

:::{.fact title="Undergrad reminders"}
\[
\det M = \prod_{\sigma \in S_n} \eps(\sigma) \prod_{i=1}^n a_{i, \sigma(i)}
.\]

For example,

\[
\operatorname{det}\left(\begin{array}{ccc}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right)=\begin{gathered}
a_{11} a_{22} a_{33}+a_{12} a_{23} a_{31}+a_{13} a_{21} a_{32} \\
-a_{13} a_{22} a_{31}-a_{12} a_{21} a_{33}-a_{11} a_{23} a_{32}
\end{gathered}
.\]

Let $\minor_A(i, j)$ denote $A$ with the $i$th row, $j$th column deleted.

One can expand determinants along rows:
\[
\det(A) = \sum_{j=1}^n (-1)^{i+j} a_{ij} \det \minor_A(i, j)
.\]

Also useful, a matrix can be inverted by computing the adjugate:
\[
A\inv = {1\over \det A} \operatorname{adj}(A) && \adj(A)_{ij} \da (-1)^{i+j} \det \minor_A(j, i)
.\]

The eigenvalues of an upper-triangular matrix are exactly the diagonal entries, and the determinant is their product.
More generally, the determinant is always the product of the eigenvalues, and the trace is the sum of the eigenvalues, so $\tr(A) = \sum \lambda_i$ and $\det(A) = \prod \lambda_i$.

Matrices can be block-multiplied when all dimensions are compatible:
\[
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
\begin{bmatrix}
E & F \\
G & H
\end{bmatrix}
= \matt{AE + BG}{AF + BH}{CE + DG}{ CF + DH}
.\]

> Note that if any of these matrix multiplications don't make sense, the results won't be valid!

If $A$ is upper triangular, some entries of $A^k$ can be computed easily:

\[
A\da\left(\begin{array}{ccc}
a_1 & & * \\
& \ddots & \\
0 & & a_n
\end{array}\right)
\implies
A^k = \left(\begin{array}{ccc}
a_1^k & & * \\
& \ddots & \\
0 & & a_n^k
\end{array}\right)
.\]

Traces of products can be commuted: $\trace(AB) = \trace(BA)$, so similar matrices have identical traces since $\trace(PJP\inv) = \trace{PP\inv J} = \trace{J}$.

The coefficients of the characteristic polynomial are elementary symmetric functions in the eigenvalues:
\[
\chi_A(t) = t^n - \qty{\sum_i \lambda_i }t^{n-1} + \qty{\sum_{i < j} \lambda_i \lambda_j }t^{n-2} + \cdots \pm \qty{\prod_i \lambda_i}
.\]

:::

:::{.example title="of polynomial long division"}
Consider $f(x) \da x^3-6x^2+12x-8$, then any rational root is in $\ts{\pm 8, \pm 4, \pm 2, \pm 1}$.
Testing $f(2) = 0$ works, and dividing by $x-2$ yields

![](../../../../assets/assets/figures/2021-07-24_18-32-38.png)

The rest can be factored by inspection:
\[
f(x) = (x-2)(x^2-4x+4) = (x-2)^3
.\]

:::

## Definitions

:::{.remark}
The main powerhouse: for $T:V\to V$ a linear transformation for $V\in\Vect_k$, map to $V\in \modsleft{k[x]}$ by letting polynomials act via $p(x)\cdot \vector v \da p(T)(\vector v)$.
Using that $k[x]$ is a PID iff $k$ is a field, and we can apply the FTFGMPID to get two decompositions:
\[
V &\cong \bigoplus_{i=1}^n k[x]/ \gens{ q_i(x) } && q_{i}(x) \divides q_{i+1}(x) \divides \cdots  \\
V &\cong \bigoplus _{j=1}^m k[x] / \gens{ p_i(x)^{e_i} } && \text{ with } p_i \text{ not necessarily distinct.}
\]

- The $q_i$ are the **invariant factors** of $T$
  - $q_i$ is the minimal polynomial of $T$ restricted to $V_i \da k[x] / \gens{ q_i(x) }$.
  - The largest invariant factor $q_n$ is the **minimal polynomial** of $T$.
  - The product $\prod_{i=1}^n q_i(x)$ is the **characteristic polynomial** of $T$.
- The $p_i$ are the **elementary divisors** of $T$.
  - Grouping equal primes, the factors $p(x)^e$ are the cyclic summands in the primary decomposition.
  - Over an algebraically closed field (or after splitting), each $p_i(x)=x-\lambda$, and $(x-\lambda)^e$ is a Jordan block of size $e$ for eigenvalue $\lambda$.
  - The characteristic polynomial is the product of all elementary divisors.
  - The minimal polynomial is the lcm of the elementary divisors: for each distinct $p$, take the highest power $p^e$ that occurs.
  - The geometric multiplicity of $\lambda$ is the number of elementary divisors that are powers of $x-\lambda$ (the number of Jordan blocks).
  - The size of the largest Jordan block for $\lambda$ is the largest such exponent $e$.

:::

[[D-O4WWN]]

[[D-NRRIT]]

[[D-H4TDM]]

[[D-BSUV4]]

[[D-B4VTH]]

[[D-HGMOW]]

[[D-23FX7]]

[[PR-24CPI]]

[[PR-WDPF7]]

[[D-JIGMN]]

[[D-JRPTK]]

### Matrix Groups

[[D-LIIHP]]

[[PR-UQ3XJ]]

[[D-P5D3T]]

[[D-BAD4E]]

[[D-GY7ZN]]

[[D-XQ3I5]]

[[D-VXJUY]]

[[D-DQPGU]]

## Minimal / Characteristic Polynomials

[[PR-EDD7U]]

:::{.remark}
Fix some notation:
\[
\min_A(x): \quad & \text{The minimal polynomial of } A \\
\chi_A(x): \quad & \text{The characteristic polynomial of } A
.\]

:::

[[D-GK5SF]]

[[D-QFYAC]]

:::{.fact}
If $A$ is upper triangular, then $\det(A) = \prod_{i} a_{ii}$

:::

[[T-SJCF7]]

:::{.proof title="?"}
By minimality, $\min_A$ divides $\chi_A$.
Every $\lambda_i$ is a root of $\min_A(x)$:
Let $(\vector v_i, \lambda_i)$ be a nontrivial eigenpair.
Then by linearity,
$$
\min_A(\lambda_i)\vector v_i = \min_A(A)\vector v_i = \vector 0
,$$
which forces $\min_A(\lambda_i) = 0$.

:::

## Finding Minimal Polynomials

[[PR-UFVPY]]

## Other Canonical Forms

[[PR-K6MMW]]

### Rational Canonical Form

Corresponds to the **Invariant Factor Decomposition** of $T$.

[[D-HJR7M]]

[[PR-4GQIZ]]

[[PR-GBL6P]]

:::{.proof title="?"}
$\not\implies$:
In general, $\min_A \divides \chi_A$, so suppose they're not equal.
Set $n\da \deg \chi_A$, then if $n' \da \deg \min_A < n$, using that $\min_A(A) = 0$ this exhibits a linear dependence in $\ts{v, Av, \cdots, A^{n'} v}$ for any $v$.
In particular, since $n>n'$, any set $\ts{v, Av,\cdots,A^nv}$ has a linear dependence.

$\implies$:
Apply the structure theorem to write $V\cong \bigoplus_{i=1}^m k[x]/\gens{p_i}$.
Since $\chi_A(x) = \prod p_i(x)$ and $\min_A(x) = p_m(x)$, this forces $m=1$ -- one way to see this is that $\dim_k V = \sum_{i=1}^m \dim_k k[x]/\gens{p_i}$,
where $\deg \chi_A = \dim_k V$ and $\deg \min_A = \dim k[x]/\gens{p_m}$.
For these to be equal, this forces $\dim_k k[x]/\gens{p_i} = 0$ for $1\leq i \leq m-1$, making $V$ a cyclic $k[x]\dash$module.
So $V = k[x]\actson \vector v$ for some $\vector v\in V$, which is the desired cyclic vector, and
\[
V = \ts{f(x).v \st f\in k[x]} = \spanof_k\ts{A^k v \st k\geq 0}
.\]
By Cayley-Hamilton, $\chi_A(A) = 0$ and so $A^n$ is a linear combinations of $A^k$ for $0\leq k \leq n-1$, so $V= \spanof_k \ts{A^k v \st 0\leq k \leq n-1}$.

:::

[[PR-TI6YA]]

:::{.remark}
Thus the blocks of $\RCF(A)$ biject with invariant factors of $A$.
Note that any companion matrix is already in $\RCF$.

:::

:::{.proof title="Derivation of RCF"}
\envlist

- Let $k[x] \actson V$ by $p(x) \actson \vector v \da p(T)(\vector v)$, making $V$ into a finitely generated torsion $k[x]\dash$module.
  - Note that $k[x]\dash$submodules are exactly $T\dash$invariant subspaces.

- $k$ a field implies $k[x]$ a PID, so apply structure theorem to obtain an invariant factor decomposition
\[
V \cong k[x] / \gens{\chi_T(x)} \cong \bigoplus_{i=1}^m k[x] / \gens{ p_i(x) }
&& p_1(x) \divides p_2(x) \divides \cdots p_m(x)
.\]

- Since each factor is submodule, each corresponds to a $T\dash$invariant subspace $V_i$ where $p_i$ is the minimal polynomial of $T$ restricted to $V_i$.

  - The largest invariant factor $p_m$ is the minimal polynomial of $T$, their product is the characteristic polynomial.
  This follows because $p_m(x)\actson V = 0$, since $p_i\divides p_m$ for all $i$, forcing $\min_A \divides p_m$ by minimality.

- Write $V \cong \bigoplus_{i=1}^m V_i$ as a $k[x]\dash$module, where $V_i \da k[x] / \gens{ p_i(x) }$, then $T$ is a block matrix $\bigoplus_{i=1}^m T_i$ where $T_i$ is the restriction of $T$ to $V_i$:
\[
\left(\begin{array}{ccccc}T_{1} & 0 & 0 & \cdots & 0 \\ 0 & T_{2} & 0 & \cdots & 0 \\ \vdots & & \ddots & & \vdots \\ 0 & \cdots & & & T_{n}\end{array}\right)
.\]

- It suffices to determine the form of a single $M_i$, so without loss of generality suppose $m=1$ so $V = V_1 = k[x] / \gens{ p(x) }$ is a cyclic $k[x]\dash$module with $\deg p(x) = n$.

- $\chi_M(x) = \min_M(x) \iff$ there exists a cyclic vector $\vector v$, so the set \( \ts{\vector v_i}_{i=0}^{n-1} \da \ts{ \vector v, T\vector v, T^2\vector v, \cdots, T^{n-1}\vector v } \) is a basis for $V_1$.
  - If there is any linear independence, this gives a polynomial relation $\sum_{i=1}^{n'} a_iT^i\vector v = 0$ for some $n'<n$, but then $q(x) \da \sum_{i=1}^{n'} a_i x^i$ is a polynomial annihilating $T$, contradicting the minimality of $p(x)$.
  - So this yields $n$ linearly independent vectors in $k^n$, so it's a basis.
- What is $M_i$ in this basis?
  Check where basis elements are mapped to by $T$, noting that
  \[
p(T) = \sum_{i=1}^{n}a_i T^i\vector v = T^n + a_{n-1} T^{n-1}\vector v + a_{n-2} T^{n-2} + \cdots + a_1 T\vector v + a_0 \vector v = 0
  ,\]
  using the minimal polynomial we can write
  - $T\vector v_0 = \vector v_1$
  - $T\vector v_2 = T^2 \vector v_0$
  - $T\vector v_3 = T^3 \vector v_0$
  - $\cdots$
  - $T\vector v_{n-2} = T^{n-1}\vector v$
  - $T\vector v_{n-1} = T^n\vector v = -a_{n-1}T^{n-1}\vector v - \cdots - a_1 T\vector v - a_0 \vector v$

- So we have
\[
M_1 =
\begin{bmatrix}
0 &  &  &  & -a_0 \\
1 & 0 &  &  & -a_1 \\
 &  1 &  0&  & -a_2 \\
 &  & \ddots &  0 & \vdots \\
 &  &  & 1 & -a_{n-1}
\end{bmatrix}
.\]

:::

### Smith Normal Form

:::{.fact}
For $A\in \Mat(m\times n; R)$ over $R$ any PID, $\SNF(A)$ is a matrix whose diagonal entries are the invariant factors.
How to compute $\SNF(A)$: take $A = \diag(a_i)$ where $a_i = d_i/d_{i-1}$ and $d_i$ is the $\gcd$ of the determinants of all $i\times i$ minors of $A$.
$A\sim B$ are similar $\iff \SNF(A) = \SNF(B)$.

:::

### Using Canonical Forms

[[L-VDLNM]]

[[L-Y5KNM]]

[[PR-OF7ZW]]

## Diagonalizability

:::{.remark}
*Notation:*
$A^{\dagger}$ denotes the conjugate transpose of $A$.

:::

[[L-C5DDK]]

[[T-WQHMA]]

:::{.remark}
In fact, $A$ is symmetric $\iff \spec A$ forms an orthonormal basis.

:::

:::{.proof title="of spectral theorem"}
\envlist

- Suppose $A$ is Hermitian.
- Since $V$ itself is an invariant subspace, $A$ has an eigenvector $\vector v_1 \in V$.
- Let $W_1 = \spanof_k\theset{\vector v_1}\perp$.
- Then for any $\vector w_1 \in W_1$,
$$
\inner{\vector v_1}{ A \vector w_1} =
\inner{A \vector v_1}{\vector w_1} =
\lambda \inner{\vector v_1}{\vector w_1} = 0,
$$
so $A(W_1) \subseteq W_1$ is an invariant subspace, etc.

- Suppose now that $A$ is symmetric.
- Then there is an eigenvector of norm 1, $\vector v \in V$.
\[
\lambda = \lambda\inner{\vector v}{\vector v} = \inner{A\vector v}{\vector v} = \inner{\vector v}{A\vector v} = \overline{\lambda} \implies \lambda \in \RR
.\]

:::

[[PR-GV5CF]]

:::{.proof title="?"}
By induction on number of operators

- $A_n$ is diagonalizable, so $V = \bigoplus E_i$ a sum of eigenspaces
- Restrict all $n-1$ operators $A$ to $E_n$.
- The commute in $V$ so they commute in $E_n$
- **(Lemma)** They were diagonalizable in $V$, so they're diagonalizable in $E_n$
- So they're simultaneously diagonalizable by I.H.
- But these eigenvectors for the $A_i$ are all in $E_n$, so they're eigenvectors for $A_n$ too.
- Can do this for each eigenspace.

> [Full details here](https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf#page=9)

:::

[[T-6ABNR]]

:::{.proof title="?"}
$\implies$:
If $\min_A$ factors into linear factors, so does each invariant factor, so every elementary divisor is linear and $JCF(A)$ is diagonal.

$\impliedby$:
If $A$ is diagonalizable, every elementary divisor is linear, so every invariant factor factors into linear pieces.
But the minimal polynomial is just the largest invariant factor.

:::

## Matrix Counterexamples

:::{.example title="?"}
A matrix that:

- Is not diagonalizable over $\RR$ but diagonalizable over $\CC$

- Has *no* eigenvalues over $\RR$ but has *distinct* eigenvalues over $\CC$

- $\min_M(x) = \chi_M(x) = x^2 + 1$

\[
M = \left(\begin{array}{rr}
0  & 1 \\
-1 & 0
\end{array}\right) \sim
\left(\begin{array}{r|r}
-1 \sqrt{-1} & 0 \\
\hline
0 & 1 \sqrt{-1}
\end{array}
\right)
.\]

:::

:::{.example title="?"}
A matrix that:

- Is not diagonalizable over $\CC$,

- Has eigenvalues $[1, 1]$ (repeated, multiplicity 2)

- $\min_M(x) = \chi_M(x) = x^2-2x+1$

\[
M = \left(\begin{array}{rr}
1 & 1 \\
0 & 1
\end{array}\right)
\sim
\left(
\begin{array}{rr}
1 & 1 \\
0 & 1
\end{array}
\right)
.\]

:::

:::{.example title="?"}
Non-similar matrices with the same characteristic polynomial
\[
\left(\begin{array}{ll}
{0}  & {0} \\
{0} & {0}
\end{array}\right)
\text { and }
\left(\begin{array}{ll}
{0} & {0} \\
{0} & {0}
\end{array}\right)
\]
Here $\chi_A(x) = \chi_B(x) = x^2$, but they are not conjugate since their JCFs differ (note that they're already in JCF!)

:::

:::{.example title="?"}
A full-rank matrix that is not diagonalizable:
\[
\left(
\begin{array}{ccc}
1 & 1 & 0 \\
0 & 1 & 1 \\
0 & 0 & 1 \\
\end{array}
\right)
.\]

:::

:::{.example title="?"}
Matrix roots of unity, i.e. representations of $i$:
\[
M_1
\da
\matt 0 {-1} 1 0 \quad
M_2
\da
\matt 0 1 {-1} 0
.\]

:::

### Counting

[[PR-OYP6J]]

## Exercises

[[E-LJ7PF]]
[[E-D62SD]]
[[E-NUJ7W]]
[[E-GNYRR]]
