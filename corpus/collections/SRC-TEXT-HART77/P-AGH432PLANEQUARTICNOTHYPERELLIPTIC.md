---
schema: qual/card@1
id: P-AGH432PLANEQUARTICNOTHYPERELLIPTIC
kind: problem
title: A plane quartic is not hyperelliptic and its canonical divisors are the line sections
classification:
  areas:
  - algebraic-geometry
  topics:
  - Canonical Divisor
  - Hyperelliptic Curves
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.2 and the hyperelliptic criterion in IV.1.7. The
    proof uses adjunction for a smooth plane quartic to identify the canonical
    sheaf with O_X(1), then applies Riemann-Roch to a degree-two divisor and
    the uniqueness of the secant or tangent line containing that divisor.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be a plane curve of degree 4.

a. Show that the effective canonical divisors on $X$ are exactly the divisors $X.L$, where $L$ is a line in $\PP^2$.

b. If $D$ is any effective divisor of degree 2 on $X$, show that $\dim \abs{D}=0$.

c. Conclude that $X$ is not hyperelliptic (Ex.
1.7).
:::

::: {.solution}
By [[P-AGH72ARITHGENUS|Exercise I.7.2]], since $X$ is a nonsingular plane
quartic, its genus is
$$
g(X)=\frac{(4-1)(4-2)}2=3,
$$
and therefore every canonical divisor has degree
$$
2g-2=4.
$$

<1>1. The canonical sheaf of $X$ is
$$
\boxed{\omega_X\cong\OO_X(1)}.
$$

::: {.proof}
Adjunction for a nonsingular plane curve of degree $d$ gives
$$
\omega_X
\cong
\bigl(\omega_{\PP^2}\tensor\OO_{\PP^2}(d)\bigr)|_X.
$$
Here
$$
\omega_{\PP^2}\cong\OO_{\PP^2}(-3)
$$
and $d=4$, so
$$
\omega_X\cong\OO_X(4-3)=\OO_X(1).
$$
:::

<1>2. Restriction of linear forms gives an isomorphism
$$
H^0(\PP^2,\OO_{\PP^2}(1))
\xrightarrow{\sim}
H^0(X,\omega_X).
$$

::: {.proof}
By step <1>1 the target is $H^0(X,\OO_X(1))$.
No nonzero linear form vanishes identically on the quartic $X$, so the
restriction map
$$
H^0(\PP^2,\OO_{\PP^2}(1))
\longrightarrow
H^0(X,\OO_X(1))
$$
is injective.

The source has dimension $3$.  Since $\OO_X(1)\cong\omega_X$ and
$g(X)=3$, the target also has dimension
$$
h^0(X,\omega_X)=g(X)=3.
$$
Thus the restriction map is an isomorphism.
:::

<1>3. The effective canonical divisors on $X$ are exactly the divisors
$$
\boxed{X.L}
$$
where $L\subseteq\PP^2$ is a line.

::: {.proof}
An effective canonical divisor is the zero divisor of a nonzero section of
$\omega_X$.  By step <1>2, every such section is the restriction of a nonzero
linear form on $\PP^2$, whose zero locus is a line $L$.
Its zero divisor on $X$ is precisely the scheme-theoretic intersection
$X.L$.

Conversely, restricting the defining linear form of any line $L$ gives a
nonzero section of $\OO_X(1)\cong\omega_X$, so $X.L$ is an effective
canonical divisor.  This proves part (a).
:::

<1>4. Let $D$ be an effective divisor of degree $2$.  Then
$$
\ell(D)=\ell(K-D)
$$
for any canonical divisor $K$.

::: {.proof}
Riemann-Roch gives
$$
\ell(D)-\ell(K-D)
=\deg D+1-g
=2+1-3
=0.
$$
Hence $\ell(D)=\ell(K-D)$.
:::

<1>5. At most one effective canonical divisor contains $D$.

::: {.proof}
Because the ground field is algebraically closed and $\deg D=2$, either
$$
D=P+Q
$$
with $P\ne Q$, or
$$
D=2P.
$$

Suppose an effective canonical divisor contains $D$.  By step <1>3 it has the
form $X.L$ for a line $L$.

If $D=P+Q$ with $P\ne Q$, then $L$ must contain both $P$ and $Q$, so it is
the unique secant line $\overline{PQ}$.

If $D=2P$, then the intersection multiplicity of $L$ and $X$ at $P$ is at
least $2$.  Since $X$ is nonsingular at $P$, this says exactly that $L$ is
the tangent line $T_PX$, which is unique.

Thus in either case there is at most one effective canonical divisor containing
$D$.
:::

<1>6. Every effective divisor $D$ of degree $2$ satisfies
$$
\boxed{\dim|D|=0}.
$$

::: {.proof}
Since $D$ is effective,
$$
\ell(D)\geq1.
$$
By step <1>4, the same is true of $\ell(K-D)$, so there exists at least one
effective canonical divisor containing $D$.

If $\ell(K-D)\geq2$, two linearly independent sections of
$\mcl(K-D)$ would give two distinct effective divisors in $|K-D|$, and after
adding $D$ they would give two distinct effective canonical divisors containing
$D$.  This contradicts step <1>5.
Hence
$$
\ell(K-D)=1.
$$
Step <1>4 gives $\ell(D)=1$, and therefore
$$
\dim|D|=\ell(D)-1=0.
$$
This proves part (b).
:::

<1>7. The plane quartic $X$ is not hyperelliptic.

::: {.proof}
If $X$ were hyperelliptic, [[P-AGH417HYPERELLIPTIC|Exercise IV.1.7]] would
give a finite morphism
$$
f:X\longrightarrow\PP^1
$$
of degree $2$.  Pulling back the degree-$1$ complete linear system on
$\PP^1$ would give a base-point-free linear system of degree $2$ and dimension
$1$ on $X$.  In particular, some effective degree-$2$ divisor $D$ would satisfy
$$
\dim|D|\geq1,
$$
contradicting step <1>6.  Thus $X$ is not hyperelliptic, proving part (c).
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), step <1>6 proves part (b), and step <1>7 proves
part (c).
:::
:::
