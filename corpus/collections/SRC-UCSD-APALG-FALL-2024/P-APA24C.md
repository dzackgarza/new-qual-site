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

<1>3. The desired inequality follows from the codimension form of the Courant--Fischer theorem:
\[
\lambda_j(M)=\min_{\operatorname{codim}S=j-1}\ \max_{0\ne x\in S}R_M(x).
\]
::: {.proof}
Choose a subspace $S_A$ of codimension $k-1$ such that
\[
\max_{0\ne x\in S_A}R_A(x)=\lambda_k(A).
\]
Set
\[
S_0=S_A\cap K.
\]
Since $K$ has codimension $2$,
\[
\operatorname{codim}S_0\le (k-1)+2=k+1.
\]
Hence $\dim S_0\ge n-k-1$. Choose a subspace
\[
S\subseteq S_0
\]
of dimension exactly $n-k-1$, equivalently of codimension exactly $k+1$.
For every nonzero $x\in S$, we have $x\in K$ and $x\in S_A$, so
\[
R_C(x)=R_A(x)\le \lambda_k(A).
\]
Applying Courant--Fischer to $C$ gives
\[
\lambda_{k+2}(C)
\le \max_{0\ne x\in S}R_C(x)
\le \lambda_k(A).
\]
Therefore
\[
\boxed{\lambda_{k+2}(C)\le \lambda_k(A)}
\qquad(1\le k\le n-2).
\]
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

::: {.solution}
Let
\[
R_M(x)=\frac{x^HMx}{x^Hx}
\]
denote the Rayleigh quotient of a Hermitian matrix $M$.

<1>1. The kernel of $B^H$ has codimension $2$.
::: {.proof}
Since $\operatorname{rank}B=2$, also $\operatorname{rank}B^H=2$. Hence by rank-nullity,
\[
\dim\ker B^H=n-2.
\]
:::

<1>2. On $\ker B^H$, the quadratic forms of $A$ and $C$ agree.
::: {.proof}
If $x\in\ker B^H$, then
\[
BB^Hx=0,
\]
so
\[
Cx=(A+BB^H)x=Ax.
\]
Therefore
\[
R_C(x)=R_A(x)
\]
for every nonzero $x\in\ker B^H$.
:::

<1>3. For every $1\le k\le n-2$,
\[
\lambda_{k+2}(C)\le \lambda_k(A).
\]
::: {.proof}
By the Courant--Fischer min-max principle,
\[
\lambda_{k+2}(C)
=
\min_{\substack{L\subseteq\mathbb C^n\\ \dim L=n-k-1}}
\max_{0\ne x\in L}R_C(x).
\]
Let $E_k\subseteq\mathbb C^n$ be the span of eigenvectors of $A$ corresponding to
\[
\lambda_k(A),\lambda_{k+1}(A),\ldots,\lambda_n(A).
\]
Then
\[
\dim E_k=n-k+1,
\]
and every nonzero $x\in E_k$ satisfies
\[
R_A(x)\le \lambda_k(A).
\]
Now set
\[
L=E_k\cap\ker B^H.
\]
Using <1>1,
\[
\dim L
\ge \dim E_k+\dim\ker B^H-n
=(n-k+1)+(n-2)-n
=n-k-1.
\]
Choose an $(n-k-1)$-dimensional subspace $L_0\subseteq L$.
For every nonzero $x\in L_0$, <1>2 gives
\[
R_C(x)=R_A(x)\le \lambda_k(A).
\]
Hence
\[
\max_{0\ne x\in L_0}R_C(x)\le \lambda_k(A).
\]
Applying Courant--Fischer to the particular admissible subspace $L_0$ yields
\[
\lambda_{k+2}(C)
\le
\max_{0\ne x\in L_0}R_C(x)
\le \lambda_k(A).
\]
This is the desired two-step interlacing inequality.
:::
:::

::: {.solution}
Let
\[
K=\ker B^H.
\]
Since \(\operatorname{rank} B=2\), we have \(\operatorname{rank} B^H=2\), hence
\[
\dim K=n-2.
\]
Moreover, for every \(x\in K\),
\[
x^HCx=x^HAx+x^HBB^Hx=x^HAx+\|B^Hx\|^2=x^HAx.
\]

<1>1. For every \(1\le k\le n-2\),
\[
\lambda_{k+2}(C)
=\min_{\substack{L\subseteq\mathbb C^n\\ \dim L=n-k-1}}
\ \max_{0\ne x\in L}\frac{x^HCx}{x^Hx}.
\]
::: {.proof}
This is the Courant--Fischer min--max theorem applied to the \((k+2)\)-nd largest eigenvalue of the Hermitian matrix \(C\).
:::

<1>2. Let \(E\) be the span of eigenvectors of \(A\) corresponding to
\[
\lambda_k(A),\lambda_{k+1}(A),\ldots,\lambda_n(A).
\]
Then
\[
\dim E=n-k+1
\]
and, for every nonzero \(x\in E\),
\[
\frac{x^HAx}{x^Hx}\le \lambda_k(A).
\]
::: {.proof}
Choose an orthonormal eigenbasis \(u_1,\ldots,u_n\) of \(A\) with
\[
Au_j=\lambda_j(A)u_j.
\]
Then
\[
E=\operatorname{span}\{u_k,\ldots,u_n\}.
\]
For \(x=\sum_{j=k}^n c_ju_j\neq0\),
\[
\frac{x^HAx}{x^Hx}
=\frac{\sum_{j=k}^n |c_j|^2\lambda_j(A)}{\sum_{j=k}^n |c_j|^2}
\le \lambda_k(A).
\]
:::

<1>3. The subspace
\[
L:=E\cap K
\]
has dimension at least \(n-k-1\).
::: {.proof}
Using \(\dim(E\cap K)\ge \dim E+\dim K-n\),
\[
\dim(E\cap K)
\ge (n-k+1)+(n-2)-n
=n-k-1.
\]
Thus \(L\) contains a subspace \(L_0\) of dimension exactly \(n-k-1\).
:::

<1>4. For every nonzero \(x\in L_0\),
\[
\frac{x^HCx}{x^Hx}
=\frac{x^HAx}{x^Hx}
\le \lambda_k(A).
\]
::: {.proof}
Because \(L_0\subseteq K=\ker B^H\), we have \(x^HCx=x^HAx\). Because \(L_0\subseteq E\), <1>2 gives the inequality.
:::

<1>5. Therefore
\[
\lambda_{k+2}(C)\le \lambda_k(A)
\qquad(1\le k\le n-2).
\]
::: {.proof}
By <1>1, \(\lambda_{k+2}(C)\) is the minimum, over all subspaces of dimension \(n-k-1\), of the maximal Rayleigh quotient of \(C\) on that subspace. Choosing the particular subspace \(L_0\) from <1>3 and using <1>4 gives
\[
\lambda_{k+2}(C)
\le \max_{0\ne x\in L_0}\frac{x^HCx}{x^Hx}
\le \lambda_k(A).
\]
:::
:::

::: {.solution}
Let
\[
R_M(x)=\frac{x^HMx}{x^Hx}
\]
be the Rayleigh quotient of a Hermitian matrix $M$.

<1>1. Since $\operatorname{rank}B=2$, the subspace
\[
K:=\ker B^H\subseteq\mathbb C^n
\]
has codimension $2$.
Moreover, for every $x\in K$,
\[
R_C(x)=R_A(x).
\]
::: {.proof}
By rank-nullity applied to $B^H$, whose rank is also $2$,
\[
\dim K=n-2.
\]
If $x\in K$, then $B^Hx=0$, and therefore
\[
x^HCx=x^HAx+x^HBB^Hx=x^HAx+\|B^Hx\|^2=x^HAx.
\]
Dividing by $x^Hx$ gives the equality of Rayleigh quotients.
:::

<1>2. For a Hermitian matrix $M$ with eigenvalues
\[
\lambda_1(M)\ge\cdots\ge\lambda_n(M),
\]
the Courant--Fischer min--max formula is
\[
\lambda_j(M)
=
\min_{\substack{L\subseteq\mathbb C^n\\ \dim L=n-j+1}}
\ \max_{0\ne x\in L} R_M(x).
\]
:::

<1>3. Fix $1\le k\le n-2$ and let $L\subseteq\mathbb C^n$ be any subspace of dimension
\[
\dim L=n-k+1.
\]
Then
\[
\dim(L\cap K)\ge n-k-1.
\]
::: {.proof}
Using
\[
\dim(L\cap K)\ge \dim L+\dim K-n,
\]
we obtain
\[
\dim(L\cap K)
\ge (n-k+1)+(n-2)-n
=n-k-1.
\]
:::

<1>4. We have
\[
\lambda_{k+2}(C)\le\lambda_k(A).
\]
::: {.proof}
Let $L$ be an arbitrary $(n-k+1)$-dimensional subspace. By <1>3, choose a subspace
\[
L'\subseteq L\cap K
\]
of dimension exactly $n-k-1$. Then <1>1 gives
\[
\max_{0\ne x\in L'}R_C(x)
=
\max_{0\ne x\in L'}R_A(x)
\le
\max_{0\ne x\in L}R_A(x).
\]
By Courant--Fischer applied to $C$ at index $k+2$,
\[
\lambda_{k+2}(C)
\le
\max_{0\ne x\in L'}R_C(x).
\]
Hence
\[
\lambda_{k+2}(C)
\le
\max_{0\ne x\in L}R_A(x).
\]
Since this holds for every $(n-k+1)$-dimensional subspace $L$, taking the minimum over all such $L$ and applying Courant--Fischer to $A$ at index $k$ gives
\[
\lambda_{k+2}(C)
\le
\lambda_k(A).
\]
This is exactly the desired interlacing inequality.
:::
:::
