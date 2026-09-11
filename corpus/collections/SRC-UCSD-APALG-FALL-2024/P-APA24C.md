---
schema: qual/card@1
id: P-APA24C
kind: problem
title: Eigenvalue interlacing for a Hermitian matrix plus a rank-$2$ update
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-11
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-11
---

::: problem
Let $A, C \in M_n(\mathbb{C}) = \mathbb{C}^{n \times n}$ be Hermitian and suppose the following:

- The $n$ eigenvalues of $A$ are notated and ordered as follows:
  \[
  \lambda_1(A) \geq \lambda_2(A) \geq \cdots \geq \lambda_n(A);
  \]

- The $n$ eigenvalues of $C$ are notated and ordered as follows:
  \[
  \lambda_1(C) \geq \lambda_2(C) \geq \cdots \geq \lambda_n(C);
  \]

- We have $C = A + B B^H$ for some rank $2$ matrix $B \in M_{n,m}(\mathbb{C}) = \mathbb{C}^{n \times m}$ with $m \geq 2$.
  Note: $B^H = \overline{B}^T$.

Prove, for all $1 \leq k \leq n - 2$, that
\[
\lambda_{k+2}(C) \leq \lambda_k(A).
\]
:::

::: {.solution}
Let $u_1,\ldots,u_n$ be an orthonormal eigenbasis of the Hermitian matrix $A$, ordered so that
\[
Au_j=\lambda_j(A)u_j,
\qquad
\lambda_1(A)\ge\cdots\ge\lambda_n(A).
\]
Fix $k$ with $1\le k\le n-2$.

<1>1. Let
\[
E:=\operatorname{span}\{u_k,u_{k+1},\ldots,u_n\}.
\]
Then $\dim E=n-k+1$, and every nonzero $x\in E$ satisfies
\[
\frac{x^HAx}{x^Hx}\le\lambda_k(A).
\]
::: {.proof}
Write
\[
x=\sum_{j=k}^n c_j u_j.
\]
Then
\[
\frac{x^HAx}{x^Hx}
=\frac{\sum_{j=k}^n\lambda_j(A)|c_j|^2}{\sum_{j=k}^n|c_j|^2}.
\]
Every eigenvalue appearing in this convex combination is at most $\lambda_k(A)$, so the quotient is at most $\lambda_k(A)$.
:::

<1>2. Let
\[
K:=\ker B^H.
\]
Since $\operatorname{rank}B=2$, one has $\dim K=n-2$, and
\[
BB^Hx=0
\]
for every $x\in K$.
::: {.proof}
Because $\operatorname{rank}B^H=\operatorname{rank}B=2$, rank-nullity gives
\[
\dim\ker B^H=n-2.
\]
If $x\in K$, then $B^Hx=0$, so $BB^Hx=B(0)=0$.
:::

<1>3. The intersection $E\cap K$ contains a subspace $S$ of dimension $n-k-1$.
::: {.proof}
For subspaces of an $n$-dimensional vector space,
\[
\dim(E\cap K)\ge \dim E+\dim K-n.
\]
Using <1>1 and <1>2,
\[
\dim(E\cap K)
\ge(n-k+1)+(n-2)-n
=n-k-1.
\]
Choose any $(n-k-1)$-dimensional subspace $S\subseteq E\cap K$.
:::

<1>4. Every nonzero $x\in S$ satisfies
\[
\frac{x^HCx}{x^Hx}\le\lambda_k(A).
\]
::: {.proof}
Since $S\subseteq K$, <1>2 gives $BB^Hx=0$. Hence
\[
Cx=(A+BB^H)x=Ax.
\]
Since also $S\subseteq E$, <1>1 gives
\[
\frac{x^HCx}{x^Hx}
=\frac{x^HAx}{x^Hx}
\le\lambda_k(A).
\]
:::

<1>5. For a Hermitian matrix $C$,
\[
\lambda_j(C)
=\min_{\substack{L\subseteq\mathbb C^n\\ \dim L=n-j+1}}
\ \max_{0\ne x\in L}\frac{x^HCx}{x^Hx}.
\]
::: {.proof}
This is the Courant--Fischer min--max formula. For completeness, let $v_1,\ldots,v_n$ be an orthonormal eigenbasis of $C$ with eigenvalues decreasing.
The subspace
\[
L_0=\operatorname{span}\{v_j,\ldots,v_n\}
\]
has dimension $n-j+1$, and every Rayleigh quotient on $L_0$ is at most $\lambda_j(C)$, so the minimum is at most $\lambda_j(C)$.
Conversely, any subspace $L$ of dimension $n-j+1$ meets
\[
\operatorname{span}\{v_1,\ldots,v_j\}
\]
nontrivially, since the dimensions sum to $n+1$. Any nonzero vector in that intersection has Rayleigh quotient at least $\lambda_j(C)$. Hence the maximum over $L$ is at least $\lambda_j(C)$. Combining the two inequalities proves the formula.
:::

<1>6. Therefore, for every $1\le k\le n-2$,
\[
\boxed{\lambda_{k+2}(C)\le\lambda_k(A).}
\]
::: {.proof}
Apply <1>5 with $j=k+2$. Then the competing subspaces have dimension
\[
n-(k+2)+1=n-k-1.
\]
The subspace $S$ from <1>3 has exactly this dimension, so
\[
\lambda_{k+2}(C)
\le \max_{0\ne x\in S}\frac{x^HCx}{x^Hx}
\le\lambda_k(A)
\]
by <1>4.
:::
:::

::: {.solution}
Fix $1\le k\le n-2$.
Let $u_1,\ldots,u_n$ be an orthonormal eigenbasis of the Hermitian matrix $A$, ordered so that
\[
Au_j=\lambda_j(A)u_j,
\qquad
\lambda_1(A)\ge\cdots\ge\lambda_n(A).
\]
Set
\[
E_k:=\operatorname{span}\{u_k,u_{k+1},\ldots,u_n\}.
\]
Then
\[
\dim E_k=n-k+1,
\]
and every nonzero $x\in E_k$ satisfies
\[
\frac{x^HAx}{x^Hx}\le \lambda_k(A).
\]

Since $B$ has rank $2$, so does $B^H$, and therefore
\[
\dim\ker B^H=n-2.
\]
Hence
\[
\dim(E_k\cap\ker B^H)
\ge \dim E_k+\dim\ker B^H-n
=(n-k+1)+(n-2)-n
=n-k-1.
\]
Choose a subspace
\[
L\subseteq E_k\cap\ker B^H
\]
with
\[
\dim L=n-k-1.
\]
For every $x\in L$, one has $B^Hx=0$, and thus
\[
BB^Hx=0.
\]
Therefore on $L$,
\[
Cx=(A+BB^H)x=Ax.
\]
Consequently, for every nonzero $x\in L$,
\[
\frac{x^HCx}{x^Hx}
=
\frac{x^HAx}{x^Hx}
\le \lambda_k(A).
\]

Now apply the Courant--Fischer min--max formula for the $(k+2)$-nd largest eigenvalue of the Hermitian matrix $C$:
\[
\lambda_{k+2}(C)
=
\min_{\substack{M\subseteq\mathbb C^n\\\dim M=n-k-1}}
\max_{0\ne x\in M}
\frac{x^HCx}{x^Hx}.
\]
Using the particular subspace $L$ constructed above gives
\[
\lambda_{k+2}(C)
\le
\max_{0\ne x\in L}
\frac{x^HCx}{x^Hx}
\le
\lambda_k(A).
\]
Thus, for every $1\le k\le n-2$,
\[
\boxed{\lambda_{k+2}(C)\le \lambda_k(A)}.
\]
:::

::: {.solution}
Let
\[
R_M(x)=\frac{x^H Mx}{x^Hx}
\]
be the Rayleigh quotient of a Hermitian matrix $M$.

<1>1. The subspace
\[
K:=\ker B^H
\]
has codimension at most $2$, and $C$ agrees with $A$ on $K$ in the sense that
\[
x^HCx=x^HAx\qquad(x\in K).
\]
::: {.proof}
Since $\operatorname{rank}B=2$, also $\operatorname{rank}B^H=2$, so
\[
\dim K=n-2.
\]
If $x\in K$, then $B^Hx=0$, hence
\[
x^HBB^Hx=\|B^Hx\|^2=0.
\]
Therefore
\[
x^HCx=x^H(A+BB^H)x=x^HAx.
\]
:::

<1>2. For every subspace $S\subseteq\mathbb C^n$ of dimension $k+2$,
\[
\dim(S\cap K)\ge k.
\]
::: {.proof}
Using the dimension inequality,
\[
\dim(S\cap K)
\ge \dim S+\dim K-n
=(k+2)+(n-2)-n=k.
\]
:::

<1>3. By the Courant--Fischer min--max principle,
\[
\lambda_{k+2}(C)
=\min_{\dim S=k+2}\ \max_{0\ne x\in S}R_C(x).
\]
For each such $S$, choose a $k$-dimensional subspace $T\subseteq S\cap K$. Then
\[
\max_{0\ne x\in S}R_C(x)
\ge \max_{0\ne x\in T}R_C(x)
=\max_{0\ne x\in T}R_A(x)
\ge \lambda_k(A).
\]
This inequality is in the wrong direction for the desired conclusion, so instead use the dual Courant--Fischer formula
\[
\lambda_{k+2}(C)
=\max_{\dim L=k+2}\ \min_{0\ne x\in L}R_C(x),
\]
which still does not directly compare with $A$. We therefore use the equivalent codimension form below.
:::

<1>4. The desired inequality follows from the codimension form of Courant--Fischer:
\[
\lambda_j(M)=\min_{\operatorname{codim}S=j-1}\ \max_{0\ne x\in S}R_M(x).
\]
::: {.proof}
Fix a subspace $S_A$ of codimension $k-1$ for which
\[
\max_{0\ne x\in S_A}R_A(x)=\lambda_k(A).
\]
Set
\[
S:=S_A\cap K.
\]
Since $K$ has codimension $2$,
\[
\operatorname{codim}S\le (k-1)+2=k+1.
\]
Enlarge $S$ if necessary to a subspace $\widetilde S$ of codimension exactly $k+1$ contained in $S_A$ and containing $S$; equivalently, choose any codimension-$k+1$ subspace of $S_A$ contained in $K$.
For every nonzero $x\in\widetilde S\subseteq K$,
\[
R_C(x)=R_A(x)\le \lambda_k(A).
\]
Therefore, by Courant--Fischer,
\[
\lambda_{k+2}(C)
\le \max_{0\ne x\in\widetilde S}R_C(x)
\le \lambda_k(A).
\]
Hence
\[
\boxed{\lambda_{k+2}(C)\le \lambda_k(A)}
\qquad(1\le k\le n-2).
\]
:::
:::
