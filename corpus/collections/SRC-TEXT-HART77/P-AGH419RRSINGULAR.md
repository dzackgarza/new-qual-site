---
schema: qual/card@1
id: P-AGH419RRSINGULAR
kind: problem
title: Riemann-Roch for singular curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Canonical Divisor
  - Very Ample Divisors
  - Genus
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.1.9 together with the cited Exercise II.7.5 and the
    duality statement used in part (d). The proof treats arbitrary positive
    and negative coefficients in part (a), and explicitly moves the very ample
    representatives away from the finite singular locus in part (c).
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be an integral projective scheme of dimension 1 over $k$.
Let $X_{\reg}$ be the set of regular points of $X$.

a. Let $D=\sum n_i P_i$ be a divisor with support in $X_{\reg}$, i.e., all $P_i \in X_{\reg}$.
Then define $\deg D=\sum n_i$.
Let $\mcl(D)$ be the associated invertible sheaf on $X$, and show that
$$
\chi(\mcl(D))=\deg D+1-p_a .
$$

b. Show that any Cartier divisor on $X$ is the difference of two very ample Cartier divisors.
Use (II, Ex.
7.5).

c. Conclude that every invertible sheaf $\mcl$ on $X$ is isomorphic to $\mcl(D)$ for some divisor $D$ with support in $X_{\reg}$.

d. Assume furthermore that $X$ is a locally complete intersection in some projective space.
Then by (III, 7.11) the dualizing sheaf $\omega_X$ is an invertible sheaf on $X$, so we can define the canonical divisor $K$ to be a divisor with support in $X_{\reg}$ corresponding to $\omega_X$.
Then the formula of a. becomes
$$
l(D)-l(K-D)=\deg D+1-p_a
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $P\in X_{\reg}$ and $D$ is supported in $X_{\reg}$, then
$$
\chi(\mcl(D+P))
=
\chi(\mcl(D))+1.
$$

::: pf-proof

Because $P$ is regular on the one-dimensional scheme $X$, it is an
effective Cartier divisor. Tensoring
$$
0
\longrightarrow
\mco_X(-P)
\longrightarrow
\mco_X
\longrightarrow
k(P)
\longrightarrow
0
$$
by $\mcl(D+P)$ gives
$$
0
\longrightarrow
\mcl(D)
\longrightarrow
\mcl(D+P)
\longrightarrow
k(P)
\longrightarrow
0.
$$
Since $k$ is algebraically closed,
$$
\chi(k(P))=1.
$$
Additivity of Euler characteristic in a short exact sequence therefore
gives the formula.

:::

:::

::: {.pf-step #s2}

For every divisor
$$
D=\sum_i n_iP_i
$$
supported in $X_{\reg}$,
$$
\boxed{
\chi(\mcl(D))
=
\deg D+1-p_a(X).
}
$$

::: pf-proof

Starting from $D=0$, repeatedly apply step [](#s1){.pf-ref} when increasing one
coefficient by $1$. The same formula read backwards applies when
decreasing a coefficient by $1$. Hence
$$
\chi(\mcl(D))
=
\chi(\mco_X)+\sum_i n_i.
$$
By definition of the arithmetic genus of a projective integral curve,
$$
\chi(\mco_X)=1-p_a(X),
$$
while
$$
\sum_i n_i=\deg D.
$$
This proves part (a).

:::

:::

::: {.pf-step #s3}

Let $C$ be any Cartier divisor on $X$. Then
$$
C=A-B
$$
for two very ample Cartier divisors $A$ and $B$.

::: pf-proof

Choose a very ample Cartier divisor $H$ on the projective curve $X$.
The invertible sheaf
$$
\mco_X(H)
$$
is ample and globally generated.

By
[[P-AGH275AMPLEPROPS|Exercise II.7.5]],
for all sufficiently large $n$ the sheaf
$$
\mco_X(C+(n-1)H)
$$
is globally generated. For such an $n$, part (d) of that exercise says
that
$$
\mco_X(C+nH)
=
\mco_X(H)\tensor\mco_X(C+(n-1)H)
$$
is very ample.

Also
$$
\mco_X(nH)
=
\mco_X(H)\tensor\mco_X((n-1)H)
$$
is very ample, because $\mco_X((n-1)H)$ is globally generated. Thus
$$
A=C+nH,
\qquad
B=nH
$$
are very ample Cartier divisors and
$$
C=A-B.
$$
This proves part (b).

:::

:::

::: {.pf-step #s4}

Every invertible sheaf on $X$ is isomorphic to $\mcl(D)$ for a
divisor $D$ supported in $X_{\reg}$.

::: pf-proof

Let $\mcl$ be invertible. Since $X$ is integral, a nonzero rational
trivialization of $\mcl$ gives a Cartier divisor $C$ with
$$
\mcl\cong\mcl(C).
$$
By step [](#s3){.pf-ref}, write
$$
C=A-B
$$
with $A$ and $B$ very ample.

The singular locus of the integral curve $X$ is finite. The complete
linear systems $\abs{A}$ and $\abs{B}$ are base-point free. Therefore one
may choose effective divisors
$$
A'\sim A,
\qquad
B'\sim B
$$
whose supports avoid every singular point: under the embeddings defined by
$A$ and $B$, choose hyperplanes avoiding the finite images of the singular
points.

Then
$$
D=A'-B'
$$
is supported in $X_{\reg}$ and
$$
\mcl(D)
\cong
\mcl(A-B)
\cong
\mcl(C)
\cong
\mcl.
$$
This proves part (c).

:::

:::

::: {.pf-step #s5}

Assume $X$ is a locally complete intersection in projective space.
Then there is a divisor $K$ supported in $X_{\reg}$ such that
$$
\mcl(K)\cong\omega_X.
$$

::: pf-proof

For a projective locally complete intersection curve, the dualizing sheaf
$\omega_X$ is invertible. Apply part (c), proved in step [](#s4){.pf-ref}, to this
invertible sheaf. It gives a divisor $K$ supported in $X_{\reg}$ with
$$
\mcl(K)\cong\omega_X.
$$
This is the canonical divisor specified in the statement.

:::

:::

::: {.pf-step #s6}

For every divisor $D$ supported in $X_{\reg}$,
$$
H^1(X,\mcl(D))^\vee
\cong
H^0(X,\mcl(K-D)).
$$

::: pf-proof

Serre duality for the projective Cohen--Macaulay curve $X$ gives
$$
H^1(X,\mcl(D))^\vee
\cong
\Hom_X(\mcl(D),\omega_X).
$$
Since $\mcl(D)$ is invertible and step [](#s5){.pf-ref} identifies
$\omega_X\cong\mcl(K)$,
$$
\Hom_X(\mcl(D),\omega_X)
\cong
H^0\bigl(X,\omega_X\tensor\mcl(-D)\bigr)
\cong
H^0(X,\mcl(K-D)).
$$

:::

:::

::: {.pf-step #s7}

The singular-curve Riemann--Roch formula is
$$
\boxed{
\ell(D)-\ell(K-D)
=
\deg D+1-p_a(X).
}
$$

::: pf-proof

By step [](#s6){.pf-ref},
$$
h^1(X,\mcl(D))
=
\ell(K-D).
$$
Therefore
$$
\chi(\mcl(D))
=
\ell(D)-\ell(K-D).
$$
Substitute the Euler-characteristic formula from step [](#s2){.pf-ref}:
$$
\chi(\mcl(D))
=
\deg D+1-p_a(X).
$$
This is exactly the displayed formula in part (d).

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part (a), step [](#s3){.pf-ref} proves part (b), step [](#s4){.pf-ref} proves
part (c), and steps [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove part (d).

:::

:::

:::
