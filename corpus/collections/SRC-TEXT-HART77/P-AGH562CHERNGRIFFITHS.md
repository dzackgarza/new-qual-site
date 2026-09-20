---
schema: qual/card@1
id: P-AGH562CHERNGRIFFITHS
kind: problem
title: Chern-Griffiths theorem bounding the geometric genus by the degree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Canonical Divisor
  - Adjunction
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read the current Hartshorne V.6.2 transcription and collection context,
    and the retained Hartshorne V migration ledger, which records that the
    V.6.2 statement and its Clifford/Riemann--Roch/Kodaira hint were compared
    with the source. The retained Hartshorne solution attachment ends in
    Chapter IV, so there is no V.6.2 source solution to incorporate. The
    proof below is an independent argument using a general hyperplane
    section, Clifford's theorem, adjunction, surface Riemann--Roch, and
    Kodaira vanishing.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the complete argument. Checked the hyperplane restriction bound
    h^0(C,O_C(1))>=n+1, the iterative restriction argument that nonspeciality
    forces p_g=0, and the Clifford equality case at d=2n. In the hyperelliptic
    equality case, deg L=2n and h^0(L)=n+1 make all sections pullbacks of
    H^0(P^1,O(n)), contradicting very ampleness. In the canonical equality
    case, K_X.H=0 and a nonzero canonical section force K_X~0; surface
    Riemann--Roch plus Kodaira vanishing then gives
    h^0(O_X(1))=n+2-q, while nondegeneracy gives at least n+2 sections, so
    q=0 and X is K3.
---

::: {.problem}
Prove the following theorem of Chern and Griffiths.
Let $X$ be a nonsingular surface of degree $d$ in $\PP_{\CC}^{n+1}$, which is not contained in any hyperplane.
If $d<2 n$, then $p_g(X)=0$.
If $d=2 n$, then either $p_g(X)=0$, or $p_g(X)=1$ and $X$ is a K3 surface.

Hint: Cut $X$ with a hyperplane and use Clifford's theorem (IV, 5.4). For the last statement, use the Riemann-Roch theorem on $X$ and the Kodaira vanishing theorem (III, 7.15).
:::

::: {.solution}
Put
$$
A=\OO_X(1).
$$
Choose a general hyperplane section
$$
C\in|A|.
$$
By [[T-BERTINI|Bertini's theorem]], $C$ is a smooth irreducible curve.
Write
$$
L=A|_C=\OO_C(1).
$$
Then
$$
\deg L=C^2=A^2=d.
$$

<1>1. The hyperplane line bundle satisfies
$$
\boxed{h^0(C,L)\ge n+1.}
$$

::: {.proof}
Since $X$ is not contained in any hyperplane, restriction of ambient
linear forms gives an injection
$$
H^0(\PP^{n+1},\OO(1))
\hookrightarrow
H^0(X,A).
$$
Thus
$$
h^0(X,A)\ge n+2.
$$

The section defining $C$ gives the exact sequence
$$
0\longrightarrow\OO_X
\longrightarrow A
\longrightarrow L
\longrightarrow0.
$$
Since $X$ is an irreducible projective variety,
$$
h^0(X,\OO_X)=1.
$$
The image of $H^0(X,A)$ in $H^0(C,L)$ therefore has dimension
$$
h^0(X,A)-1\ge n+1.
$$
Hence $h^0(C,L)\ge n+1$.
:::

<1>2. If $d<2n$, then $L$ is nonspecial:
$$
\boxed{H^1(C,L)=0.}
$$

::: {.proof}
Suppose instead that $L$ is special.
Since $L$ has positive degree and has nonzero sections, Clifford's theorem
[[T-CRVCLIFF]] gives
$$
h^0(C,L)
\le
\frac{\deg L}{2}+1
=
\frac d2+1.
$$
If $d<2n$, then
$$
\frac d2+1<n+1,
$$
contradicting step <1>1.
Thus $L$ is nonspecial.
:::

<1>3. Whenever $H^1(C,L)=0$, one has
$$
\boxed{p_g(X)=0.}
$$

::: {.proof}
Adjunction gives
$$
\omega_C
\cong
(\omega_X\otimes A)|_C,
$$
and therefore
$$
\omega_X|_C
\cong
\omega_C\otimes L^{-1}.
$$
Serre duality on $C$ gives
$$
H^0(C,\omega_C\otimes L^{-1})
\cong
H^1(C,L)^\vee
=0.
$$

For every $m\ge0$, tensor the hyperplane-section sequence by
$\omega_X\otimes A^{-m}$:
$$
0
\longrightarrow
\omega_X\otimes A^{-(m+1)}
\longrightarrow
\omega_X\otimes A^{-m}
\longrightarrow
\omega_C\otimes L^{-(m+1)}
\longrightarrow0.
$$
The right-hand sheaf has no nonzero global section. Indeed, if it had a
section, multiplying by any nonzero section of $L^m$ would give a nonzero
section of
$$
\omega_C\otimes L^{-1},
$$
which has none. Hence for every $m\ge0$,
$$
H^0(X,\omega_X\otimes A^{-(m+1)})
\xrightarrow{\sim}
H^0(X,\omega_X\otimes A^{-m}).
$$
Iterating,
$$
h^0(X,\omega_X)
=
h^0(X,\omega_X\otimes A^{-m})
$$
for every $m$.

For $m\gg0$, the latter space is zero. Otherwise an effective divisor
$D_m$ would satisfy
$$
D_m\sim K_X-mA,
$$
so ampleness of $A$ would give
$$
0\le A\cdot D_m
=
A\cdot K_X-mA^2,
$$
which is impossible for sufficiently large $m$ because $A^2=d>0$.
Therefore
$$
p_g(X)=h^0(X,\omega_X)=0.
$$
:::

<1>4. If $d=2n$ and $L$ is special, then
$$
\boxed{L\cong\omega_C.}
$$

::: {.proof}
Clifford's theorem and step <1>1 give
$$
n+1
\le
h^0(C,L)
\le
\frac d2+1
=
n+1.
$$
Thus equality holds in Clifford's theorem.

The divisor class $L$ is nonzero.
If equality came from the hyperelliptic case, then $L$ would be a
multiple of the unique $g^1_2$:
$$
L\cong f^*\OO_{\PP^1}(n)
$$
for the hyperelliptic double cover
$$
f:C\to\PP^1.
$$
Pullback gives an injective map
$$
H^0(\PP^1,\OO_{\PP^1}(n))
\hookrightarrow
H^0(C,L).
$$
Both spaces have dimension $n+1$: the source has that dimension, and
equality in the preceding Clifford estimate gives
$$
h^0(C,L)=n+1.
$$
Thus every section of $L$ is pulled back from $\PP^1$ and takes the same
value on the two points of each fiber of $f$. Hence $L$ could not be very
ample.
But $L=\OO_C(1)$ is very ample because it is the restriction of the
projective embedding.

The only remaining equality case in Clifford's theorem is therefore
$$
L\cong\omega_C.
$$
:::

<1>5. In the special case of step <1>4,
$$
\boxed{K_X\cdot A=0.}
$$

::: {.proof}
Adjunction gives
$$
\omega_X|_C
\cong
\omega_C\otimes L^{-1}.
$$
Step <1>4 identifies the right-hand side with $\OO_C$. Consequently
$$
\deg(\omega_X|_C)=0.
$$
Since $C\sim A$, this degree is
$$
K_X\cdot A.
$$
:::

<1>6. If $d=2n$, $L$ is special, and $p_g(X)>0$, then
$$
\boxed{\omega_X\cong\OO_X}
$$
and
$$
\boxed{p_g(X)=1.}
$$

::: {.proof}
Choose a nonzero canonical section.
Its zero divisor $D$ is effective and satisfies
$$
D\sim K_X.
$$
By step <1>5,
$$
A\cdot D
=
A\cdot K_X
=0.
$$
Since $A$ is ample, every nonzero effective curve has positive
intersection with $A$. Hence $D=0$.

A nowhere-vanishing section of $\omega_X$ trivializes it, so
$$
\omega_X\cong\OO_X.
$$
Because $X$ is an irreducible projective variety over $\CC$,
$$
h^0(X,\OO_X)=1.
$$
Thus
$$
p_g(X)
=
h^0(X,\omega_X)
=1.
$$
:::

<1>7. Under the hypotheses of step <1>6,
$$
\boxed{q(X)=h^1(X,\OO_X)=0.}
$$

::: {.proof}
Put
$$
q=h^1(X,\OO_X).
$$
Step <1>6 gives $p_g=1$, so
$$
\chi(\OO_X)
=
1-q+p_g
=
2-q.
$$

Apply surface Riemann--Roch [[T-SRFRR]] to $A$.
Since $K_X\sim0$ and
$$
A^2=\deg X=d=2n,
$$
one obtains
$$
\chi(A)
=
\chi(\OO_X)+\frac12A\cdot(A-K_X)
=
(2-q)+n
=
n+2-q.
$$

By Kodaira vanishing [[T-KODVAN]], using
$$
A\cong\omega_X\otimes A
$$
and the ampleness of $A$,
$$
H^i(X,A)=0
\qquad
(i>0).
$$
Hence
$$
h^0(X,A)
=
\chi(A)
=
n+2-q.
$$

The given nondegenerate embedding
$$
X\hookrightarrow\PP^{n+1}
$$
supplies $n+2$ linearly independent global sections of $A$. Therefore
$$
n+2
\le
h^0(X,A)
=
n+2-q.
$$
Thus $q\le0$, and hence
$$
q=0.
$$
:::

<1>8. If $d<2n$, then $p_g(X)=0$. If $d=2n$, then either
$p_g(X)=0$, or $p_g(X)=1$ and $X$ is a K3 surface.

::: {.proof}
For $d<2n$, step <1>2 makes $L$ nonspecial, and step <1>3 gives
$$
p_g(X)=0.
$$

Now assume $d=2n$.
If $L$ is nonspecial, step <1>3 again gives $p_g(X)=0$.
If $L$ is special, step <1>4 gives $L\cong\omega_C$.
If in addition $p_g(X)=0$, this is the first alternative in the theorem.
Otherwise steps <1>6--<1>7 give
$$
\omega_X\cong\OO_X,
\qquad
p_g(X)=1,
\qquad
q(X)=0.
$$
A smooth projective surface over $\CC$ with trivial canonical bundle and
$H^1(X,\OO_X)=0$ is a K3 surface. Hence the second alternative is exactly
that $X$ is K3.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove the strict inequality case. Steps <1>4--<1>8
analyze the equality case and give precisely the two alternatives stated
in the theorem.
:::
:::
