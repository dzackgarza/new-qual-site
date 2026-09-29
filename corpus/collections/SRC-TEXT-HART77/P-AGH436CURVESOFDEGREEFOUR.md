---
schema: qual/card@1
id: P-AGH436CURVESOFDEGREEFOUR
kind: problem
title: Classification of curves of degree $4$ in projective space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Embeddings
  - Elliptic Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.6 together with IV.3.4--3.5 and the rational quartic
    example II.7.8.6. The classification uses the linear span, the
    minimal-degree theorem, and the strict projection genus bound. In the
    elliptic case the proof computes at least two containing quadrics and
    identifies their complete intersection with X by comparing Hilbert
    polynomials, avoiding an unsupported set-theoretic Bezout shortcut.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Curves of Degree 4.

a. If $X$ is a curve of degree 4 in some $\PP^n$, show that either
    (1) $g=0$, in which case $X$ is either the rational normal quartic in $\PP^4$ (Ex. 3.4) or the rational quartic curve in $\PP^3$ (II, 7.8.6), or
    (2) $X \subseteq \PP^2$, in which case $g=3$, or
    (3) $X \subseteq \PP^3$ and $g=1$.

b. In the case $g=1$, show that $X$ is a complete intersection of two irreducible quadric surfaces in $\PP^3$ (I, Ex. 5.11). Hint: Use the exact sequence $0 \to \mci_X \to \OO_{\PP^3} \to \OO_X \to 0$ to compute $\dim H^0(\PP^3, \mci_X(2))$, and thus conclude that $X$ is contained in at least two irreducible quadric surfaces.
:::

::: {.solution}
Let
$$
\PP^r=\langle X\rangle
$$
be the linear span of $X$. Then $X$ is nondegenerate in $\PP^r$, and its
degree in the span is still $4$.

::: pf

::: {.pf-step #s1}

One has
$$
2\le r\le4.
$$

::: pf-proof

The case $r=1$ is impossible: an integral one-dimensional closed subscheme
of $\PP^1$ is $\PP^1$ itself and has degree $1$.

If $r\ge4$, then
$$
\deg X=4\le r.
$$
By [[P-AGH434RATIONALNORMALCURVE|Exercise IV.3.4(b)]], a nondegenerate curve
of degree at most its ambient dimension must have degree equal to that
dimension. Hence $r=4$.
Thus $2\le r\le4$.

:::

:::

::: {.pf-step #s2}

If $r=4$, then
$$
g(X)=0
$$
and $X$ is the rational normal quartic in $\PP^4$ up to projective
automorphism.

::: pf-proof

This is exactly
[[P-AGH434RATIONALNORMALCURVE|Exercise IV.3.4(b)]] with
$$
d=r=4.
$$

:::

:::

::: {.pf-step #s3}

If $r=2$, then
$$
g(X)=3.
$$

::: pf-proof

In this case $X$ is a nonsingular plane curve of degree $4$. The plane-curve
genus formula gives
$$
g(X)
=
\frac{(4-1)(4-2)}2
=3.
$$

:::

:::

::: {.pf-step #s4}

If $r=3$, then
$$
g(X)\in\{0,1\}.
$$

::: pf-proof

Since $X\subseteq\PP^3$ is nondegenerate,
[[P-AGH435PROJECTIONFROMSPACECURVE|Exercise IV.3.5(b)]] gives
$$
g(X)
<
\frac12(4-1)(4-2)
=3.
$$
Thus
$$
g(X)\in\{0,1,2\}.
$$

Suppose $g(X)=2$. Put
$$
\mcl=\mco_X(1).
$$
Then
$$
\deg\mcl=4.
$$
For a canonical divisor $K$ on a genus-$2$ curve,
$$
\deg(K-\mcl)=-2,
$$
so Riemann--Roch gives
$$
h^0(X,\mcl)
=
4+1-2
=3.
$$
But nondegeneracy in $\PP^3$ makes the restriction map
$$
H^0(\PP^3,\mco(1))
\hookrightarrow
H^0(X,\mcl)
$$
injective, so the right side has dimension at least $4$. This contradiction
excludes genus $2$.

:::

:::

::: {.pf-step #s5}

The alternatives in part (a) are exactly:

1. $g=0$, with $X$ a rational normal quartic in $\PP^4$ or a nonsingular
   rational quartic in $\PP^3$;
2. $X\subseteq\PP^2$, in which case $g=3$;
3. $X\subseteq\PP^3$ and $g=1$.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} leave only the stated cases.

If $r=4$, step [](#s2){.pf-ref} gives the rational normal quartic.
If $r=3$ and $g=0$, then $X\cong\PP^1$ and the given degree-$4$ embedding
is precisely a nonsingular rational quartic in $\PP^3$ in the sense of
Hartshorne II.7.8.6.
The remaining $r=3$ possibility is $g=1$, and step [](#s3){.pf-ref} handles $r=2$.
This proves (a).

:::

:::

::: {.pf-step #s6}

Assume now that $g(X)=1$. Then
$$
h^0(X,\mco_X(2))=8.
$$

::: pf-proof

Part (a) puts $X$ nondegenerately in $\PP^3$. Let
$$
H=\mco_X(1).
$$
Then
$$
\deg(2H)=8.
$$
On a genus-$1$ curve the canonical divisor has degree $0$, so
$$
\deg(K_X-2H)=-8
$$
and hence
$$
h^0(K_X-2H)=0.
$$
Riemann--Roch therefore gives
$$
h^0(X,\mco_X(2))
=
8+1-1
=8.
$$

:::

:::

::: {.pf-step #s7}

The vector space of quadrics containing $X$ has dimension at least
$2$:
$$
h^0(\PP^3,\mci_X(2))\ge2.
$$

::: pf-proof

Twist
$$
0
\longrightarrow
\mci_X
\longrightarrow
\mco_{\PP^3}
\longrightarrow
\mco_X
\longrightarrow0
$$
by $\mco_{\PP^3}(2)$ and take global sections. Exactness gives
$$
0
\longrightarrow
H^0(\PP^3,\mci_X(2))
\longrightarrow
H^0(\PP^3,\mco(2))
\longrightarrow
H^0(X,\mco_X(2)).
$$
The middle space has dimension
$$
\binom{3+2}{2}=10,
$$
whereas step [](#s6){.pf-ref} gives dimension $8$ for the target. Therefore the kernel
has dimension at least
$$
10-8=2.
$$

:::

:::

::: {.pf-step #s8}

Every nonzero quadric surface containing $X$ is irreducible.

::: pf-proof

A reducible quadric surface in $\PP^3$ is a union of two planes, allowing the
two planes to coincide. If such a quadric contained the irreducible curve
$X$, irreducibility of $X$ would force $X$ to lie in one of those planes.
This contradicts part (a), which places the genus-$1$ case nondegenerately
in $\PP^3$. Hence every containing quadric is irreducible.

:::

:::

::: {.pf-step #s9}

Choose two linearly independent quadrics
$$
Q_1,Q_2\in H^0(\PP^3,\mci_X(2)).
$$
Then
$$
Z=V(Q_1,Q_2)
$$
is a complete-intersection curve with Hilbert polynomial
$$
P_Z(m)=4m.
$$

::: pf-proof

Step [](#s7){.pf-ref} supplies the independent quadrics, and step [](#s8){.pf-ref} makes them
irreducible. Since they are distinct irreducible polynomials, they have no
common factor. Thus they form a regular sequence in
$$
k[x_0,x_1,x_2,x_3],
$$
so $Z$ is the complete intersection of two quadrics.

Its Koszul resolution is
$$
0
\longrightarrow
\mco_{\PP^3}(-4)
\longrightarrow
\mco_{\PP^3}(-2)^{\oplus2}
\longrightarrow
\mco_{\PP^3}
\longrightarrow
\mco_Z
\longrightarrow0.
$$
Hence
$$
\begin{aligned}
P_Z(m)
&=
\binom{m+3}{3}
-2\binom{m+1}{3}
+\binom{m-1}{3}\\
&=4m.
\end{aligned}
$$

:::

:::

::: {.pf-step #s10}

One has
$$
X=Z
$$
scheme-theoretically.

::: pf-proof

Because both quadrics contain $X$, there is a closed immersion
$$
X\hookrightarrow Z.
$$
The Hilbert polynomial of the degree-$4$, genus-$1$ curve $X$ is
$$
P_X(m)
=
4m+1-g
=4m.
$$
Step [](#s9){.pf-ref} gives the same polynomial for $Z$.

Let $\mathcal K$ be the kernel of the induced surjection
$$
\mco_Z\twoheadrightarrow\mco_X.
$$
Additivity of Hilbert polynomials gives
$$
P_{\mathcal K}=P_Z-P_X=0.
$$
A nonzero coherent sheaf on a projective scheme has a nonzero Hilbert
polynomial, so
$$
\mathcal K=0.
$$
Therefore $X=Z$ as schemes.

:::

:::

::: {.pf-step #s11}

The genus-$1$ quartic is a complete intersection of two irreducible
quadric surfaces in $\PP^3$.

::: pf-proof

Steps [](#s8){.pf-ref}, [](#s9){.pf-ref} and [](#s10){.pf-ref} produce irreducible quadric surfaces $V(Q_1)$ and
$V(Q_2)$ and prove
$$
\boxed{X=V(Q_1)\cap V(Q_2)}
$$
scheme-theoretically. This proves (b).

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves (a), and step [](#s11){.pf-ref} proves (b).

:::

:::

:::
