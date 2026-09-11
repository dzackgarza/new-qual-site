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
<1>1. Let
\[
K:=\ker B^H.
\]
Then \(\dim K=n-2\), and for every \(x\in K\),
\[
Cx=Ax.
\]
::: {.proof}
Since \(\operatorname{rank}B=2\), we also have \(\operatorname{rank}B^H=2\). By rank-nullity,
\[
\dim K=n-2.
\]
If \(x\in K\), then \(B^Hx=0\), so
\[
Cx=(A+BB^H)x=Ax.
\]
:::

<1>2. For every Hermitian matrix \(H\) and every \(1\le j\le n\), the Courant--Fischer formula gives
\[
\lambda_j(H)
=\min_{\substack{L\subseteq\mathbb C^n\\ \dim L=n-j+1}}
\ \max_{0\ne x\in L}
\frac{x^HHx}{x^Hx}.
\]
::: {.proof}
This is the standard min--max characterization of the ordered eigenvalues of a Hermitian matrix.
:::

<1>3. Fix \(1\le k\le n-2\). There exists a subspace \(L\subseteq\mathbb C^n\) of dimension \(n-k+1\) such that
\[
\max_{0\ne x\in L}\frac{x^HAx}{x^Hx}=\lambda_k(A).
\]
::: {.proof}
Take \(L\) to be the span of orthonormal eigenvectors of \(A\) corresponding to
\[
\lambda_k(A),\lambda_{k+1}(A),\ldots,\lambda_n(A).
\]
Then \(\dim L=n-k+1\), and the Rayleigh quotient of \(A\) on \(L\) is at most \(\lambda_k(A)\), with equality on an eigenvector for \(\lambda_k(A)\).
:::

<1>4. The intersection \(L\cap K\) has dimension at least \(n-k-1\).
::: {.proof}
Using \(\dim(U\cap W)\ge \dim U+\dim W-n\),
\[
\dim(L\cap K)
\ge (n-k+1)+(n-2)-n
=n-k-1.
\]
Since \(k\le n-2\), this number is nonnegative.
:::

<1>5. Therefore
\[
\lambda_{k+2}(C)\le \lambda_k(A).
\]
::: {.proof}
Choose a subspace \(M\subseteq L\cap K\) with
\[
\dim M=n-k-1=n-(k+2)+1.
\]
For every nonzero \(x\in M\subseteq K\), <1>1 gives
\[
\frac{x^HCx}{x^Hx}
=\frac{x^HAx}{x^Hx}.
\]
Because \(M\subseteq L\), <1>3 yields
\[
\max_{0\ne x\in M}\frac{x^HCx}{x^Hx}
\le \lambda_k(A).
\]
Applying Courant--Fischer to \(C\) at index \(k+2\),
\[
\lambda_{k+2}(C)
=\min_{\substack{N\subseteq\mathbb C^n\\ \dim N=n-k-1}}
\max_{0\ne x\in N}
\frac{x^HCx}{x^Hx}
\le
\max_{0\ne x\in M}
\frac{x^HCx}{x^Hx}
\le \lambda_k(A).
\]
Thus the claimed inequality holds for every \(1\le k\le n-2\).
:::
:::

::: {.solution}
Let
\[
K:=\ker(B^H)\subseteq\mathbb C^n.
\]
Since \(\operatorname{rank}B=2\), also \(\operatorname{rank}B^H=2\), so
\[
\dim K=n-2.
\]
Moreover, for every \(x\in K\),
\[
x^H Cx=x^HAx+x^HBB^Hx=x^HAx+\|B^Hx\|^2=x^HAx.
\]

<1>1. Fix \(1\le k\le n-2\). By the Courant--Fischer min--max theorem,
\[
\lambda_k(A)
=
\min_{\substack{S\subseteq\mathbb C^n\\ \dim S=n-k+1}}
\ \max_{0\ne x\in S}\frac{x^HAx}{x^Hx}.
\]
Choose a subspace \(S\) of dimension \(n-k+1\) for which
\[
\max_{0\ne x\in S}\frac{x^HAx}{x^Hx}=\lambda_k(A).
\]
::: {.proof}
Because \(A\) is Hermitian, there is an orthonormal eigenbasis \(u_1,\dots,u_n\) with eigenvalues
\[
\lambda_1(A)\ge\cdots\ge\lambda_n(A).
\]
Taking
\[
S=\operatorname{span}\{u_k,u_{k+1},\ldots,u_n\}
\]
gives \(\dim S=n-k+1\), and every Rayleigh quotient on \(S\) is at most \(\lambda_k(A)\), with equality at \(u_k\).
:::

<1>2. The intersection
\[
T:=S\cap K
\]
has dimension at least \(n-k-1\).
::: {.proof}
For subspaces of an \(n\)-dimensional vector space,
\[
\dim(S\cap K)\ge \dim S+\dim K-n.
\]
Hence
\[
\dim T
\ge (n-k+1)+(n-2)-n
=n-k-1.
\]
:::

<1>3. There exists a subspace \(T_0\subseteq T\) with
\[
\dim T_0=n-(k+2)+1=n-k-1.
\]
For every nonzero \(x\in T_0\),
\[
\frac{x^HCx}{x^Hx}
=
\frac{x^HAx}{x^Hx}
\le \lambda_k(A).
\]
::: {.proof}
Choose any \((n-k-1)\)-dimensional subspace \(T_0\subseteq T\), possible by <1>2.
Because \(T_0\subseteq K\), the quadratic forms of \(A\) and \(C\) agree on \(T_0\). Because \(T_0\subseteq S\), the choice of \(S\) in <1>1 gives
\[
\frac{x^HAx}{x^Hx}\le \lambda_k(A)
\]
for all nonzero \(x\in T_0\).
:::

<1>4. Therefore
\[
\boxed{\lambda_{k+2}(C)\le \lambda_k(A)}
\qquad(1\le k\le n-2).
\]
::: {.proof}
Apply Courant--Fischer to \(C\):
\[
\lambda_{k+2}(C)
=
\min_{\substack{W\subseteq\mathbb C^n\\ \dim W=n-k-1}}
\ \max_{0\ne x\in W}\frac{x^HCx}{x^Hx}.
\]
Using the particular subspace \(T_0\) from <1>3,
\[
\lambda_{k+2}(C)
\le
\max_{0\ne x\in T_0}\frac{x^HCx}{x^Hx}
\le \lambda_k(A).
\]
This is the desired rank-two interlacing inequality.
:::
:::

::: {.solution}
Let
\[
R_M(x)=\frac{x^H Mx}{x^Hx}
\]
denote the Rayleigh quotient of a Hermitian matrix $M$ on a nonzero vector $x$.

<1>1. On the subspace
\[
K:=\ker B^H,
\]
we have $C=A$.
::: {.proof}
If $x\in K$, then $B^Hx=0$, hence
\[
BB^Hx=B(B^Hx)=0.
\]
Therefore
\[
Cx=(A+BB^H)x=Ax.
\]
So $R_C(x)=R_A(x)$ for every nonzero $x\in K$.
:::

<1>2. Since $\operatorname{rank}B=2$, the subspace $K=\ker B^H$ has codimension $2$ in $\mathbb C^n$.
::: {.proof}
Because $\operatorname{rank}(B^H)=\operatorname{rank}(B)=2$, rank--nullity gives
\[
\dim K=n-2.
\]
:::

<1>3. Fix $1\le k\le n-2$, and let $E_k$ be the span of eigenvectors of $A$ corresponding to
\[
\lambda_k(A),\lambda_{k+1}(A),\ldots,\lambda_n(A).
\]
Then
\[
\dim E_k=n-k+1
\]
and
\[
R_A(x)\le \lambda_k(A)
\]
for every nonzero $x\in E_k$.
::: {.proof}
Choose an orthonormal eigenbasis $u_1,\ldots,u_n$ of $A$ with
\[
Au_j=\lambda_j(A)u_j.
\]
Then
\[
E_k=\operatorname{span}\{u_k,\ldots,u_n\}.
\]
For
\[
x=\sum_{j=k}^n c_j u_j\ne0,
\]
we have
\[
R_A(x)
=\frac{\sum_{j=k}^n \lambda_j(A)|c_j|^2}{\sum_{j=k}^n|c_j|^2}
\le \lambda_k(A),
\]
because every $\lambda_j(A)\le\lambda_k(A)$ for $j\ge k$.
:::

<1>4. The intersection $E_k\cap K$ has dimension at least
\[
n-k-1.
\]
::: {.proof}
For subspaces $U,W\subseteq\mathbb C^n$,
\[
\dim(U\cap W)\ge \dim U+\dim W-n.
\]
Using <1>2 and <1>3,
\[
\dim(E_k\cap K)
\ge (n-k+1)+(n-2)-n
=n-k-1.
\]
:::

<1>5. Choose an $(n-k-1)$-dimensional subspace
\[
F\subseteq E_k\cap K.
\]
Then
\[
R_C(x)\le\lambda_k(A)
\]
for every nonzero $x\in F$.
::: {.proof}
Because $F\subseteq K$, <1>1 gives $R_C(x)=R_A(x)$ for $x\in F$. Because $F\subseteq E_k$, <1>3 gives $R_A(x)\le\lambda_k(A)$.
:::

<1>6. Therefore
\[
\lambda_{k+2}(C)\le\lambda_k(A).
\]
::: {.proof}
Use the Courant--Fischer min--max formula in the form
\[
\lambda_j(C)
=
\min_{\substack{S\subseteq\mathbb C^n\\ \dim S=n-j+1}}
\ \max_{0\ne x\in S}R_C(x).
\]
For $j=k+2$, the required dimension is
\[
n-(k+2)+1=n-k-1.
\]
The subspace $F$ from <1>5 has exactly this dimension, so
\[
\lambda_{k+2}(C)
\le \max_{0\ne x\in F}R_C(x)
\le \lambda_k(A).
\]
This proves the required inequality for every $1\le k\le n-2$.
:::
:::

::: {.solution}
Fix $1\le k\le n-2$.

<1>1. Let $E\subseteq\mathbb C^n$ be the direct sum of the eigenspaces of $A$ corresponding to the eigenvalues
\[
\lambda_k(A),\lambda_{k+1}(A),\ldots,\lambda_n(A).
\]
Then
\[
\dim E=n-k+1,
\]
and every nonzero $x\in E$ satisfies
\[
\frac{x^HAx}{x^Hx}\le \lambda_k(A).
\]
::: {.proof}
Because $A$ is Hermitian, it has an orthonormal eigenbasis. The subspace $E$ is spanned by eigenvectors for the $n-k+1$ smallest eigenvalues. If
\[
x=\sum_{j=k}^n c_j u_j,
\]
where $Au_j=\lambda_j(A)u_j$, then
\[
\frac{x^HAx}{x^Hx}
=
\frac{\sum_{j=k}^n |c_j|^2\lambda_j(A)}{\sum_{j=k}^n|c_j|^2}
\le \lambda_k(A).
\]
:::

<1>2. Since $\operatorname{rank}B=2$,
\[
\dim\ker B^H=n-2.
\]
Hence
\[
\dim(E\cap\ker B^H)\ge n-k-1.
\]
::: {.proof}
Rank-nullity gives
\[
\dim\ker B^H=n-\operatorname{rank}B^H=n-2.
\]
For two subspaces $U,W\subseteq\mathbb C^n$,
\[
\dim(U\cap W)\ge \dim U+\dim W-n.
\]
Applying this with $U=E$ and $W=\ker B^H$ gives
\[
\dim(E\cap\ker B^H)
\ge (n-k+1)+(n-2)-n
=n-k-1.
\]
:::

<1>3. Choose a subspace
\[
S\subseteq E\cap\ker B^H
\]
with
\[
\dim S=n-k-1.
\]
For every nonzero $x\in S$,
\[
\frac{x^HCx}{x^Hx}\le \lambda_k(A).
\]
::: {.proof}
Since $x\in\ker B^H$,
\[
BB^Hx=0.
\]
Thus, using $C=A+BB^H$,
\[
x^HCx=x^HAx.
\]
Since $x\in E$, <1>1 gives
\[
\frac{x^HCx}{x^Hx}
=
\frac{x^HAx}{x^Hx}
\le \lambda_k(A).
\]
:::

<1>4. Therefore
\[
\boxed{\lambda_{k+2}(C)\le \lambda_k(A)}.
\]
::: {.proof}
By the Courant--Fischer min--max theorem,
\[
\lambda_{k+2}(C)
=
\min_{\substack{L\subseteq\mathbb C^n\\ \dim L=n-(k+2)+1}}
\ \max_{0\ne x\in L}
\frac{x^HCx}{x^Hx}.
\]
The required dimension is
\[
n-(k+2)+1=n-k-1.
\]
Using the particular subspace $S$ constructed in <1>3,
\[
\lambda_{k+2}(C)
\le
\max_{0\ne x\in S}
\frac{x^HCx}{x^Hx}
\le \lambda_k(A).
\]
This proves the stated interlacing inequality for every $1\le k\le n-2$.
:::
:::
