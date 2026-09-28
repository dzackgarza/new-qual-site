---
schema: qual/card@1
id: P-AGH445DEGREETWOENDOMORPHISM
kind: problem
title: Exactly three values of $j$ admit an endomorphism of degree $2$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Riemann-Hurwitz
  - Jacobians
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.5 together with Lemma IV.4.4, Theorem IV.4.1, and
    the group-law results preceding the exercise. The ramification calculation
    and the six S_3 possibilities for the Legendre parameter were solved
    explicitly; the resulting three parameter orbits give the three j-values
    printed in Hartshorne.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X, P_0$ be an elliptic curve having an endomorphism $f: X \to X$ of degree 2.

a. If we represent $X$ as a 2-1 covering of $\PP^1$ by a morphism $\pi: X \to \PP^1$ ramified at $P_0$, then as in (4.4), show that there is another morphism $\pi': X \to \PP^1$ and a morphism $g: \PP^1 \to \PP^1$, also of degree 2, such that $\pi \circ f=g \circ \pi'$.

b. For suitable choices of coordinates in the two copies of $\PP^1$, show that $g$ can be taken to be the morphism $x \mapsto x^2$.

c. Now show that $g$ is branched over two of the branch points of $\pi$, and that $g^{-1}$ of the other two branch points of $\pi$ consists of the four branch points of $\pi'$.
Deduce a relation involving the invariant $\lambda$ of $X$.

d. Solving the above, show that there are just three values of $j$ corresponding to elliptic curves with an endomorphism of degree 2, and find the corresponding values of $\lambda$ and $j$.
Answers: $j=2^6 \cdot 3^3$; $j=2^6 \cdot 5^3$; $j=-3^3 \cdot 5^3$.
:::

::: {.solution}
Hartshorne is assuming $\characteristic k\ne2$ in this section.

<1>1. The degree-$2$ endomorphism $f$ is unramified, and
$$
\ker f=\{P_0,T\}
$$
for a nonzero point $T$ of order $2$.

::: {.proof}
Since $\deg f=2$ and $\characteristic k\ne2$, the morphism $f$ is separable.
Riemann--Hurwitz for $f:X\to X$ gives
$$
0=2g(X)-2=2(2g(X)-2)+\deg R_f=\deg R_f,
$$
so $f$ is unramified.

An endomorphism of an elliptic curve is a group homomorphism, so its kernel
has two points.  Write it as $\{P_0,T\}$.  Being a two-element subgroup, it
has $2T=P_0$.
:::

<1>2. There are degree-$2$ morphisms
$$
\pi':X\longrightarrow\PP^1,
\qquad
g:\PP^1\longrightarrow\PP^1
$$
such that
$$
\pi\circ f=g\circ\pi'.
$$

::: {.proof}
Let $\pi'$ be the morphism associated to
$$
\abs{P_0+T}.
$$
Riemann--Roch gives $h^0(P_0+T)=2$.  It has no base point: if $Q$ were a
base point, then
$$
h^0(P_0+T-Q)=h^0(P_0+T)=2,
$$
whereas a degree-$1$ divisor on a genus-one curve has at most one independent
section.  Thus this degree-$2$ divisor gives a base-point-free $g^1_2$.
Its deck
involution is
$$
\iota_T(R)=T-R,
$$
because $R+(T-R)\sim P_0+T$.

The morphism $\pi$, defined by $\abs{2P_0}$, has deck involution
$[-1](R)=-R$.  Since $f(T)=P_0$ and $f$ is a homomorphism,
$$
f(T-R)=-f(R).
$$
Hence
$$
(\pi\circ f)(T-R)=\pi(-f(R))=\pi(f(R)).
$$
Thus $\pi\circ f$ is constant on the fibres of $\pi'$ and factors through a
morphism $g:\PP^1\to\PP^1$.  Comparing degrees gives
$$
4=\deg(\pi\circ f)=\deg g\cdot2,
$$
so $\deg g=2$.
:::

<1>3. After suitable choices of coordinates on the two copies of $\PP^1$,
$$
g(t)=t^2.
$$

::: {.proof}
The degree-$2$ map $g$ is separable.  Riemann--Hurwitz gives exactly two
simple ramification points.  Send them to $0,\infty$ in the source and send
their branch values to $0,\infty$ in the target.  Then $g$ has a double zero
at $0$ and a double pole at $\infty$, so $g(t)=ct^2$.  Rescaling the target
coordinate makes $c=1$.
:::

<1>4. The branch values of $g$ are two of the four branch values of $\pi$,
and the branch values of $\pi'$ are exactly the inverse images under $g$ of
the other two.

::: {.proof}
Because $f$ is unramified, the branch values of $\pi\circ f$ are exactly the
branch values of $\pi$, and every ramification index of the composite is
$2$.

Using
$$
\pi\circ f=g\circ\pi',
$$
every branch value of $g$ is therefore a branch value of $\pi$.  No branch
value of $\pi'$ can be a ramification point of $g$: otherwise the
corresponding point of $X$ would have ramification index $4$ for the
composite.  Thus the four branch values of $\pi'$ lie over the two branch
values of $\pi$ that are not branch values of $g$.  Each of those two target
points has two distinct inverse images under $g$, giving exactly the four
branch values of $\pi'$.
:::

<1>5. Write the branch set of $\pi$ as
$$
\{0,\infty,1,\lambda\}
$$
so that the two branch values of $g$ are $0,\infty$, and choose
$\mu\in k$ with
$$
\mu^2=\lambda.
$$
Then the Legendre parameter arising from $\pi'$ can be taken to be
$$
\lambda'
=
\left(\frac{\mu-1}{\mu+1}\right)^2,
$$
and $\lambda'$ must belong to the $\Sigma_3$-orbit of $\lambda$.

::: {.proof}
By step <1>3, $g(t)=t^2$.  Step <1>4 therefore says that the branch set of
$\pi'$ is
$$
\{1,-1,\mu,-\mu\}.
$$
The fractional linear transformation
$$
s
=
\frac{\mu-1}{\mu+1}\frac{t+1}{t-1}
$$
sends
$$
-1\longmapsto0,
\qquad
1\longmapsto\infty,
\qquad
\mu\longmapsto1,
$$
and sends $-\mu$ to
$$
\left(\frac{\mu-1}{\mu+1}\right)^2.
$$
Hence this last number is a Legendre parameter for the same elliptic curve
$X$.  By Theorem IV.4.1 and Lemma IV.4.5, two Legendre parameters define
isomorphic elliptic curves exactly when they differ by the $\Sigma_3$ action.
Thus
$$
\lambda'
\in
\left\{
\lambda,
1-\lambda,
\lambda^{-1},
1-\lambda^{-1},
(1-\lambda)^{-1},
\lambda(\lambda-1)^{-1}
\right\}.
$$
This is the required relation involving $\lambda$.
:::

<1>6. Up to the $\Sigma_3$-action, the relation in step <1>5 has exactly
three classes of solutions:
$$
\lambda=-1,
\qquad
\lambda^2-6\lambda+1=0,
\qquad
\lambda^2-\lambda+16=0.
$$

::: {.proof}
Substitute $\lambda=\mu^2$ and
$$
\lambda'=\left(\frac{\mu-1}{\mu+1}\right)^2
$$
into the six possibilities of step <1>5.  Since
$\lambda\ne0,1$, we have $\mu\ne0,\pm1$.  Clearing denominators and removing
the excluded factors gives the equations
$$
\begin{gathered}
\mu^2+1=0,\\
\mu^2+2\mu-1=0,
\qquad
\mu^2-2\mu-1=0,\\
\mu^2+3\mu+4=0,
\qquad
\mu^2-3\mu+4=0,\\
4\mu^2+3\mu+1=0,
\qquad
4\mu^2-3\mu+1=0.
\end{gathered}
$$
These are precisely the nonexcluded factors from the six equalities
$$
\lambda'=\lambda,
\ 1-\lambda,
\ \lambda^{-1},
\ 1-\lambda^{-1},
\ (1-\lambda)^{-1},
\ \lambda(\lambda-1)^{-1}.
$$

The first equation gives $\lambda=-1$.  Either of the next two gives
$$
\lambda^2-6\lambda+1=0.
$$
The next two give
$$
\lambda^2-\lambda+16=0.
$$
The last two give
$$
16\lambda^2-\lambda+1=0,
$$
whose reciprocal $\lambda^{-1}$ satisfies
$$
(\lambda^{-1})^2-\lambda^{-1}+16=0.
$$
Thus the last two lie in the same $\Sigma_3$-orbit as the preceding class.
No other parameter classes occur.
:::

<1>7. The corresponding $j$-invariants are
$$
\boxed{
2^6\cdot3^3,
\qquad
2^6\cdot5^3,
\qquad
-3^3\cdot5^3
}.
$$

::: {.proof}
Use Hartshorne's formula
$$
j(\lambda)
=
256\frac{(\lambda^2-\lambda+1)^3}
{\lambda^2(\lambda-1)^2}.
$$

For $\lambda=-1$,
$$
j=1728=2^6\cdot3^3.
$$

If $\lambda^2-6\lambda+1=0$, then
$$
\lambda^2-\lambda+1=5\lambda,
\qquad
(\lambda-1)^2=4\lambda.
$$
Therefore
$$
j
=
256\frac{(5\lambda)^3}{4\lambda^3}
=
8000
=
2^6\cdot5^3.
$$

If $\lambda^2-\lambda+16=0$, then
$$
\lambda^2-\lambda+1=-15,
\qquad
\lambda(\lambda-1)=-16.
$$
Hence
$$
j
=
256\frac{(-15)^3}{(-16)^2}
=
-3375
=
-3^3\cdot5^3.
$$

Over the algebraically closed field one may choose representatives
$$
\lambda=-1,
\qquad
\lambda=3\pm2\sqrt2,
\qquad
\lambda=\frac{1\pm3\sqrt{-7}}2,
$$
respectively.  In small positive characteristic some of the three displayed
integer $j$-values may coincide after reduction; the calculation above shows
that no additional $j$-values occur.
:::

<1>8. Each of the three parameter classes is realized by a degree-$2$
endomorphism.

::: {.proof}
Choose $\mu$ satisfying one of the equations in step <1>6 and set
$\lambda=\mu^2$.  Consider the smooth genus-one curves
$$
X_\lambda:
\qquad
y^2=x(x-1)(x-\lambda)
$$
and
$$
X_\mu':
\qquad
Y^2=(t^2-1)(t^2-\mu^2).
$$
The formulas
$$
x=t^2,
\qquad
y=tY
$$
give a degree-$2$ morphism
$$
F:X_\mu'\longrightarrow X_\lambda,
$$
since
$$
(tY)^2=t^2(t^2-1)(t^2-\mu^2).
$$

By step <1>5, the Legendre parameter of $X_\mu'$ is
$$
\lambda'
=
\left(\frac{\mu-1}{\mu+1}\right)^2.
$$
For the solutions retained in step <1>6, $\lambda'$ lies in the
$\Sigma_3$-orbit of $\lambda$.  Hence Theorem IV.4.1 gives
$$
X_\mu'\cong X_\lambda.
$$
Choose an isomorphism carrying the origin of $X_\lambda$ to either point of
$X_\mu'$ lying above the origin of $X_\lambda$ under $F$; this is possible by
composing any isomorphism with a translation on $X_\mu'$.  Its composition
with $F$ is then an endomorphism of $X_\lambda$ of degree $2$.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove parts (a)--(b), steps <1>4--<1>5 prove part (c),
and steps <1>6--<1>8 give the three parameter classes and the three
$j$-values of part (d), together with their realization.
:::
:::
