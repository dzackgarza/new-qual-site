---
schema: qual/card@1
id: P-AGH463DEGREEFIVEGENUSTWO
kind: problem
title: A curve of degree $5$ and genus $2$ in $\PP^3$ lies on a unique quadric
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Genus
  - Very Ample Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.6.3 and the retained Lomont and Egbert companion
    solutions. The source statement needs no correction. Lomont stops after
    the uniqueness argument, while Egbert only sketches the ruling
    distinction. The proof below independently proves the sharper criterion:
    for a degree-five line bundle L on a genus-two curve, the unique containing
    quadric is smooth exactly when L-2K is non-effective, and is a quadric cone
    when L-2K is effective.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
A curve of degree 5 and genus 2 in $\PP^3$ is contained in a unique quadric surface $Q$.
Show that for any abstract curve $X$ of genus 2, there exist embeddings of degree 5 in $\PP^3$ for which $Q$ is nonsingular, and there exist other embeddings of degree 5 for which $Q$ is singular.
:::

::: {.solution}
Write line-bundle classes additively, and let $K$ denote a canonical divisor.
For an embedding $X\subseteq\PP^3$, put $H=\OO_X(1)$.

<1>1. Every curve of degree $5$ and genus $2$ in $\PP^3$ is contained in a
quadric surface.

::: {.proof}
Since $\deg H=5$,
$$
\deg(2H)=10.
$$
Riemann--Roch gives
$$
h^0(X,2H)-h^0(X,K-2H)=10+1-2=9.
$$
Now
$$
\deg(K-2H)=2-10=-8,
$$
so $h^0(X,K-2H)=0$ and therefore
$$
h^0(X,2H)=9.
$$
On the other hand,
$$
h^0(\PP^3,\OO_{\PP^3}(2))=10.
$$
Thus the restriction map
$$
H^0(\PP^3,\OO_{\PP^3}(2))
\longrightarrow
H^0(X,2H)
$$
has nonzero kernel.  A nonzero element of that kernel is the equation of a
quadric containing $X$.
:::

<1>2. The containing quadric is unique.

::: {.proof}
First, $X$ is not contained in a plane.  Otherwise its image would be a
nonsingular plane quintic, whose genus is
$$
\frac{(5-1)(5-2)}2=6,
$$
contrary to $g(X)=2$.

Suppose that two linearly independent quadrics $Q_1,Q_2$ contain $X$.  If
they had a common surface component, that component would have to be a plane.
Writing their equations as
$$
q_1=\ell m_1,
\qquad
q_2=\ell m_2,
$$
the integrality of $X$ and the fact that $X\not\subseteq V(\ell)$ would force
both $m_1$ and $m_2$ to vanish on $X$.  Since $q_1,q_2$ are independent,
$m_1,m_2$ are independent, so $X$ would lie on the line
$V(m_1,m_2)$, impossible.

Hence $Q_1$ and $Q_2$ have no common surface component.  Their intersection
is then a complete-intersection curve of degree
$$
2\cdot2=4.
$$
Every irreducible curve component of that intersection has degree at most
$4$, so it cannot contain the degree-$5$ curve $X$.  This contradiction proves
uniqueness.
:::

<1>3. Every line bundle $L$ of degree $5$ on an abstract genus-$2$ curve
defines a degree-$5$ embedding
$$
\varphi_L:X\hookrightarrow\PP^3.
$$

::: {.proof}
By [[P-AGH431GENUSTWOVERYAMPLE|Exercise IV.3.1]], every divisor of degree
$5$ on a genus-$2$ curve is very ample.  Moreover,
$$
\deg(K-L)=2-5=-3,
$$
so Riemann--Roch gives
$$
h^0(X,L)=5+1-2=4.
$$
Thus the complete linear system $\abs{L}$ embeds $X$ in $\PP^3$.  Its
hyperplane bundle is $L$, so the image has degree $5$.
:::

<1>4. Let $L$ have degree $5$, and put
$$
M=L-2K,
\qquad
D=L-K.
$$
If $M$ is non-effective, then the unique quadric containing
$\varphi_L(X)$ is nonsingular.

::: {.proof}
Here
$$
\deg M=1,
\qquad
\deg D=3.
$$
Since $\deg(K-D)=-1$, Riemann--Roch gives
$$
h^0(X,D)=2.
$$
We claim that $\abs{D}$ is base-point free.  If $P$ were a base point, then
$$
h^0(X,D-P)=h^0(X,D)=2.
$$
The divisor $E=D-P$ has degree $2$, and Riemann--Roch gives
$$
h^0(X,E)-h^0(X,K-E)=1.
$$
Hence $h^0(X,K-E)\ge1$.  But $K-E$ has degree $0$, so it must be linearly
equivalent to $0$.  Thus
$$
D-P\sim K,
$$
and therefore
$$
M=D-K\sim P,
$$
contradicting the assumption that $M$ is non-effective.  Hence $D$ is a
base-point-free pencil.

By [[P-AGH417HYPERELLIPTIC|Exercise IV.1.7]], $\abs{K}$ is also a
base-point-free pencil.  Its evaluation sequence, tensored by $\OO_X(D)$,
is
$$
0
\longrightarrow
\OO_X(D-K)
\longrightarrow
H^0(X,K)\otimes\OO_X(D)
\longrightarrow
\OO_X(K+D)
\longrightarrow0.
$$
On global sections, the kernel of multiplication
$$
H^0(X,K)\otimes H^0(X,D)
\longrightarrow
H^0(X,L)
$$
is therefore $H^0(X,D-K)=H^0(X,M)=0$.  Both source and target have
dimension $4$, so multiplication is an isomorphism.

Consequently the complete map $\varphi_L$ is the composite
$$
X
\xrightarrow{(\varphi_K,\varphi_D)}
\PP^1\times\PP^1
\xrightarrow{\text{Segre}}
\PP^3.
$$
Its image is therefore contained in the smooth Segre quadric.  By step
<1>2, this is the unique quadric containing $\varphi_L(X)$.
:::

<1>5. If $M=L-2K$ is effective, then the unique quadric containing
$\varphi_L(X)$ is singular.

::: {.proof}
Since $\deg M=1$, effectivity gives
$$
M\sim P
$$
for some point $P\in X$.  Let $s$ be a nonzero section of $\OO_X(P)$, and
let $u,v$ be a basis of $H^0(X,K)$.

The canonical system defines the degree-two surjection
$$
\varphi_K:X\longrightarrow\PP^1
$$
from [[P-AGH417HYPERELLIPTIC|Exercise IV.1.7]].  Pullback therefore injects
$$
H^0(\PP^1,\OO_{\PP^1}(2))
\hookrightarrow
H^0(X,2K).
$$
Both spaces have dimension $3$, since Riemann--Roch gives
$$
h^0(X,2K)=4+1-2=3.
$$
Hence
$$
u^2,\quad uv,\quad v^2
$$
form a basis of $H^0(X,2K)$.

Multiplication by $s$ embeds this space in
$$
H^0(X,2K+P)=H^0(X,L),
$$
so
$$
su^2,\quad suv,\quad sv^2
$$
are linearly independent.  Extend them by a section $w$ to a basis of
$H^0(X,L)$.  In the corresponding coordinates
$[x_0:x_1:x_2:x_3]$ on $\PP^3$, every point of $\varphi_L(X)$ satisfies
$$
x_0x_2-x_1^2=0.
$$
Thus $\varphi_L(X)$ lies on the quadric cone
$$
Q_0=V_+(x_0x_2-x_1^2),
$$
which is singular at $[0:0:0:1]$.  Step <1>2 says that there is only one
containing quadric, so that quadric is $Q_0$ and is singular.
:::

<1>6. For every abstract genus-$2$ curve, both kinds of degree-$5$ embedding
exist.

::: {.proof}
For a singular containing quadric, choose any point $P\in X$ and set
$$
L_{\mathrm{sing}}=2K+P.
$$
This has degree $5$, so step <1>3 gives an embedding, while
$$
L_{\mathrm{sing}}-2K\sim P
$$
is effective.  Step <1>5 makes its unique containing quadric singular.

For a nonsingular containing quadric, fix $P_0\in X$.  By
[[T-CRVJACFUN]], the Jacobian $\Jac(X)$ has dimension $2$, while the
Abel--Jacobi image
$$
X\longrightarrow\Jac(X),
\qquad
P\longmapsto\OO_X(P-P_0)
$$
has dimension at most $1$.  Choose
$$
A\in\Pic^0(X)
$$
outside that image, and put
$$
M=A\otimes\OO_X(P_0).
$$
Then $\deg M=1$.  It is not effective: otherwise $M\cong\OO_X(P)$ for some
$P$, which would give
$$
A\cong\OO_X(P-P_0),
$$
contrary to the choice of $A$.  Now set
$$
L_{\mathrm{sm}}=\OO_X(2K)\otimes M.
$$
Again $\deg L_{\mathrm{sm}}=5$, so step <1>3 gives an embedding, and
$L_{\mathrm{sm}}-2K=M$ is non-effective.  Step <1>4 makes its unique
containing quadric nonsingular.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove existence and uniqueness of the containing quadric.
Step <1>3 realizes every degree-$5$ line bundle as an embedding, steps
<1>4--<1>5 determine the quadric from $L-2K$, and step <1>6 constructs both
possibilities on every abstract genus-$2$ curve.
:::
:::
