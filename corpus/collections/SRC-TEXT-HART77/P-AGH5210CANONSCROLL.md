---
schema: qual/card@1
id: P-AGH5210CANONSCROLL
kind: problem
title: Canonical curves on a rational scroll and nonhyperelliptic curves with a $g^1_3$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Canonical Divisor
relations: []
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
For any $n>e \geqslant 0$, let $X$ be the rational scroll of degree $d=2 n-e$ in $\PP^{d+1}$ given by (2.19). If $n \geqslant 2 e-2$, show that $X$ contains a nonsingular curve $Y$ of genus $g=d+2$ which is a canonical curve in this embedding.

Conclude that for every $g \geqslant 4$, there exists a nonhyperelliptic curve of genus $g$ which has a $g_3^1$.
Cf.
(V, §5).
:::

::: {.solution}
Write $X=\FF_e$, let $C_0$ be its negative section, and let $f$ be a
fibre of the ruling
$$
\pi:X\longrightarrow\PP^1.
$$
Thus
$$
C_0^2=-e,
\qquad
C_0\cdot f=1,
\qquad
f^2=0,
$$
and
$$
K_X\sim-2C_0-(e+2)f
$$
[[FE-TORHIRZ]].  In the embedding of (2.19), the hyperplane class is
$$
H\sim C_0+nf,
$$
so $H^2=2n-e=d$.

<1>1. The divisor
$$
D\coloneqq H-K_X
\sim
3C_0+(n+e+2)f
$$
has a base-point-free complete linear system.

::: {.proof}
Put
$$
b=n+e+2.
$$
For a divisor $aC_0+bf$ with $a\ge0$, the ruled-surface projection gives
$$
\pi_*\OO_X(aC_0+bf)
\cong
\bigoplus_{i=0}^{a}\OO_{\PP^1}(b-ie).
$$
Hence $\OO_X(aC_0+bf)$ is globally generated whenever $b\ge ae$: every
summand on the right is then globally generated, and the relative
$\OO_X(a)$ evaluation map is surjective.

For $D$ one has $a=3$, and the hypothesis $n\ge2e-2$ gives
$$
b-3e
=
n-2e+2
\ge0.
$$
Thus $|D|$ is base-point-free.
:::

<1>2. The system $|D|$ contains a nonsingular member $Y$.

::: {.proof}
Set
$$
q=n-2e+2\ge0.
$$
Then
$$
D
\sim
3(C_0+ef)+qf.
$$
If $q>0$, then
$$
D
\sim
\bigl(C_0+(e+q)f\bigr)+2(C_0+ef).
$$
The first summand is very ample by the rational-scroll construction (2.19),
because $e+q>e$, while step <1>1 with $a=1$ shows that $C_0+ef$ is
base-point-free.  The tensor product of a very ample invertible sheaf with
globally generated invertible sheaves is very ample.  Hence $D$ is very
ample, so a general member of $|D|$ is nonsingular by Bertini's theorem.

Suppose $q=0$.  The base-point-free system $|C_0+ef|$ defines the usual
morphism from $\FF_e$ to the rational normal scroll cone: it contracts
exactly $C_0$ and is an immersion on $X\setminus C_0$.  The system

$$
|D|=|3(C_0+ef)|
$$

has the same property away from $C_0$.  Moreover,
$$
D\cdot C_0=0.
$$
Since $|D|$ is base-point-free, a general member does not contain the
contracted section $C_0$, and hence is disjoint from it.  Bertini applied
on $X\setminus C_0$, where the associated morphism is an immersion, then
shows that a general member is nonsingular.  Choose such a member and call
it $Y$.
:::

<1>3. The curve $Y$ is connected, hence irreducible.

::: {.proof}
From
$$
0\longrightarrow\OO_X(-D)
\longrightarrow\OO_X
\longrightarrow\OO_Y
\longrightarrow0
$$
it is enough to prove
$$
H^0(X,\OO_X(-D))=0,
\qquad
H^1(X,\OO_X(-D))=0.
$$
For the first vanishing, choose a fibre that is not a component of an
effective divisor.  Its intersection with that divisor is nonnegative, while
$$
(-D)\cdot f=-3,
$$
so $-D$ cannot be effective.

For the second, Serre duality and $D=H-K_X$ give
$$
H^1(X,\OO_X(-D))^\vee
\cong
H^1(X,\OO_X(K_X+D))
=
H^1(X,\OO_X(H)).
$$
Since
$$
\pi_*\OO_X(H)
\cong
\OO_{\PP^1}(n)\oplus\OO_{\PP^1}(n-e)
$$
and $R^1\pi_*\OO_X(H)=0$, while $n>e\ge0$, one obtains
$$
H^1(X,\OO_X(H))=0.
$$
Therefore $H^0(Y,\OO_Y)=k$, so $Y$ is connected.  By step <1>2 it is
nonsingular; a connected nonsingular curve is irreducible.
:::

<1>4. The canonical bundle of $Y$ is the restriction of the hyperplane
bundle:
$$
\boxed{K_Y\cong\OO_Y(H)}.
$$

::: {.proof}
Adjunction and the definition $D=H-K_X$ give
$$
K_Y
\cong
(K_X+Y)|_Y
\cong
(K_X+D)|_Y
\cong
\OO_Y(H).
$$
:::

<1>5. The genus of $Y$ is
$$
\boxed{g(Y)=d+2}.
$$

::: {.proof}
By step <1>4,
$$
2g(Y)-2
=
\deg K_Y
=
H\cdot D.
$$
Using $H=C_0+nf$ and
$D=3C_0+(n+e+2)f$,
$$
\begin{aligned}
H\cdot D
&=(C_0+nf)\cdot\bigl(3C_0+(n+e+2)f\bigr)\\
&=-3e+(n+e+2)+3n\\
&=4n-2e+2\\
&=2(2n-e)+2\\
&=2d+2.
\end{aligned}
$$
Thus $2g(Y)-2=2d+2$, whence $g(Y)=d+2$.
:::

<1>6. The restriction map
$$
H^0(X,\OO_X(H))
\longrightarrow
H^0(Y,K_Y)
$$
is an isomorphism.  Consequently the given embedding of $Y$ is its
complete canonical embedding.

::: {.proof}
Since $Y\sim D=H-K_X$, restriction gives
$$
0
\longrightarrow
\OO_X(K_X)
\longrightarrow
\OO_X(H)
\longrightarrow
\OO_Y(H)
\longrightarrow0.
$$
Now $H^0(X,\OO_X(K_X))=0$: an effective canonical divisor would have
nonnegative intersection with a general fibre, whereas $K_X\cdot f=-2$.
Also
$$
H^1(X,\OO_X(K_X))
\cong
H^1(X,\OO_X)^\vee
=0
$$
by Serre duality, because $X$ is ruled over $\PP^1$ and
$H^1(X,\OO_X)=0$.  The cohomology sequence therefore makes the restriction
map an isomorphism.  By step <1>4 its target is $H^0(Y,K_Y)$.

Moreover,
$$
h^0(X,\OO_X(H))
=
h^0(\PP^1,\OO(n))+h^0(\PP^1,\OO(n-e))
=
2n-e+2
=
d+2.
$$
Thus the given embedding $X\hookrightarrow\PP^{d+1}$ uses all sections of
$H$.  Its restriction to $Y$ is therefore defined by the complete canonical
system $|K_Y|$, as claimed.
:::

<1>7. For every integer $g\ge4$, parameters $n>e\ge0$ satisfying the
hypotheses can be chosen with
$$
2n-e=g-2.
$$

::: {.proof}
Put $d=g-2\ge2$.  If $d$ is even, take
$$
e=0,
\qquad
n=\frac d2.
$$
Then $n>e$, $2n-e=d$, and $n\ge2e-2$.

If $d$ is odd, then $d\ge3$; take
$$
e=1,
\qquad
n=\frac{d+1}{2}.
$$
Then $n>1=e$, $2n-e=d$, and $n\ge0=2e-2$.
Thus steps <1>1--<1>6 produce a canonical curve of genus $g=d+2$ in every
genus $g\ge4$.
:::

<1>8. Every curve $Y$ produced above carries a $g^1_3$ and is
nonhyperelliptic.

::: {.proof}
The ruling restricts to a morphism
$$
\pi|_Y:Y\longrightarrow\PP^1
$$
of degree
$$
Y\cdot f
=
D\cdot f
=3.
$$
Therefore the pullback of $|\OO_{\PP^1}(1)|$ is a base-point-free
$g^1_3$ on $Y$.

By step <1>6 the complete canonical map of $Y$ is an embedding.  A
hyperelliptic curve of genus at least $2$ has canonical map of degree $2$
onto a rational normal curve, so $Y$ is not hyperelliptic.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>6 construct the required nonsingular canonical curve of genus
$d+2$.  Steps <1>7--<1>8 give, for every $g\ge4$, a nonhyperelliptic
genus-$g$ curve carrying a $g^1_3$.
:::
:::
