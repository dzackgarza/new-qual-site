---
schema: qual/card@1
id: P-AGH4420ENDOMORPHISMRINGCHARP
kind: problem
title: The endomorphism ring in characteristic $p$ and the field of definition of $j$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.20 together with IV.2.4.1, Proposition IV.2.5,
    Exercise IV.4.7, and Exercise IV.4.15. Cross-checked the degree-p
    Frobenius factorization against Milne, Elliptic Curves, Proposition 7.3,
    and the naturality of absolute Frobenius against the Stacks Project,
    Lemma 33.36.2.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
  note: >-
    Rechecked the Frobenius-twist direction, both degree-p factorization
    implications, the associates criterion, the p^2 field-of-definition
    argument, and the semilinear cohomology calculation in part (d).
---

::: {.problem}
Let $X$ be an elliptic curve over a field $k$ of characteristic $p>0$, and let $R=\operatorname{End}(X, P_0)$ be its ring of endomorphisms.

a. Let $X_p$ be the curve over $k$ defined by changing the $k$-structure of $X$ (2.4.1). Show that $j(X_p)=j(X)^{1/p}$.
Thus $X \cong X_p$ over $k$ if and only if $j \in \FF_p$.

b. Show that $p_X$ in $R$ factors into a product $\pi \hat{\pi}$ of two elements of degree $p$ if and only if $X \cong X_p$.
In this case, the Hasse invariant of $X$ is 0 if and only if $\pi$ and $\hat{\pi}$ are associates in $R$ (i.e., differ by a unit).
(Use (2.5).)

c. If $\Hasse(X)=0$ show in any case $j \in \FF_{p^2}$.

d. For any $f \in R$, there is an induced map $f^*: H^1(\OO_X) \to H^1(\OO_X)$.
This must be multiplication by an element $\lambda_f \in k$.
So we obtain a ring homomorphism $\varphi: R \to k$ by sending $f$ to $\lambda_f$.
Show that any $f \in R$ commutes with the (nonlinear) Frobenius morphism $F: X \to X$, and conclude that if $\Hasse(X) \neq 0$, then the image of $\varphi$ is $\FF_p$.
Therefore, $R$ contains a prime ideal $\mfp$ with $R/\mfp \cong \FF_p$.
:::

::: {.solution}
We use the standing convention of Chapter IV that $k$ is algebraically
closed.  Let
$$
F':X_p\longrightarrow X
$$
be Hartshorne's $k$-linear Frobenius, and put
$$
V=\widehat{F'}:X\longrightarrow X_p.
$$
By [[P-AGH4415PTORSIONANDHASSE|Exercise IV.4.15]],
$$
F'\circ V=[p]_X,
\qquad
\deg F'=\deg V=p.
$$

::: pf

::: {.pf-step #s1}

One has
$$
\boxed{j(X_p)=j(X)^{1/p}.}
$$

::: pf-proof

Choose a Weierstrass equation for $X$.  The twist $X_p$ of IV.2.4.1 is
obtained by applying the inverse Frobenius automorphism of the algebraically
closed field $k$ to its coefficients, that is, by replacing each coefficient
$a$ by its unique $p$th root $a^{1/p}$.

The $j$-invariant is a rational expression in the Weierstrass coefficients
with coefficients in the prime field.  Applying inverse Frobenius to all
coefficients therefore applies inverse Frobenius to $j$ itself.  Hence
$$
j(X_p)=j(X)^{1/p}.
$$

:::

:::

::: {.pf-step #s2}

The curves $X$ and $X_p$ are isomorphic over $k$ if and only if
$$
\boxed{j(X)\in\FF_p.}
$$

::: pf-proof

Over the algebraically closed field $k$, elliptic curves are isomorphic if
and only if they have the same $j$-invariant.  By step [](#s1){.pf-ref},
$$
X\cong X_p
\iff
j(X)=j(X)^{1/p}
\iff
j(X)^p=j(X).
$$
The roots in $k$ of $t^p-t$ are exactly the elements of $\FF_p$.  This
proves part (a).

:::

:::

::: {.pf-step #s3}

If $X\cong X_p$, then $[p]_X$ factors in $R$ as
$$
\boxed{[p]_X=\pi\circ\widehat\pi}
$$
with
$$
\deg\pi=\deg\widehat\pi=p.
$$

::: pf-proof

Choose an origin-preserving isomorphism
$$
\alpha:X\overset\sim\longrightarrow X_p
$$
which exists because any isomorphism of the underlying genus-one curves can
be followed by a translation on $X_p$ to send the chosen origin to the
chosen origin.  Define
$$
\pi=F'\circ\alpha:X\longrightarrow X.
$$
Then $\pi\in R$ and $\deg\pi=p$.  By contravariance of the dual and
[[P-AGH447DUALOFAMORPHISM|Exercise IV.4.7]],
$$
\widehat\pi
=
\widehat\alpha\circ V.
$$
The dual of an isomorphism is its inverse, so
$$
\widehat\alpha=\alpha^{-1}.
$$
Consequently
$$
\pi\circ\widehat\pi
=
F'\circ\alpha\circ\alpha^{-1}\circ V
=
F'\circ V
=
[p]_X.
$$
Exercise IV.4.7(f) gives
$$
\deg\widehat\pi=\deg\pi=p.
$$

:::

:::

::: {.pf-step #s4}

Conversely, if
$$
[p]_X=\pi\circ\widehat\pi
$$
with $\pi,\widehat\pi\in R$ both of degree $p$, then
$$
\boxed{X\cong X_p.}
$$

::: pf-proof

The differential of $[p]_X$ is multiplication by $p$, hence is zero in
characteristic $p$.  Thus $[p]_X$ is inseparable.  If both $\pi$ and
$\widehat\pi$ were separable, their composition would be separable.
Therefore at least one of them is inseparable.

An inseparable morphism of degree $p$ between nonsingular curves is purely
inseparable of degree $p$.  Proposition IV.2.5 says that any such morphism
$$
f:X\longrightarrow X
$$
is the $k$-linear Frobenius
$$
X_p\longrightarrow X
$$
after an isomorphism of its source with $X_p$.  Hence $X\cong X_p$.
Together with step [](#s3){.pf-ref} this proves the first assertion of part (b).

:::

:::

::: {.pf-step #s5}

Assume $X\cong X_p$ and choose $\pi$ as in step [](#s3){.pf-ref}.  Then
$$
\boxed{
\Hasse(X)=0
\iff
\pi\text{ and }\widehat\pi\text{ are associates in }R.
}
$$

::: pf-proof

The morphism
$$
\pi=F'\circ\alpha
$$
is purely inseparable of degree $p$.  Moreover step [](#s3){.pf-ref} gives
$$
\widehat\pi=\alpha^{-1}\circ V.
$$
Thus $\widehat\pi$ is inseparable exactly when $V$ is inseparable.
By [[P-AGH4415PTORSIONANDHASSE|Exercise IV.4.15]], this is equivalent to
$\Hasse(X)=0$.

Suppose first that $\Hasse(X)=0$.  Then both $\pi$ and $\widehat\pi$ are
purely inseparable of degree $p$.  Proposition IV.2.5 therefore gives
isomorphisms
$$
\alpha,\beta:X\overset\sim\longrightarrow X_p
$$
such that
$$
\pi=F'\circ\alpha,
\qquad
\widehat\pi=F'\circ\beta.
$$
These isomorphisms preserve the origins: both endomorphisms and $F'$ send
origin to origin, while $F'$ is radicial and hence has only one point over
the origin.  Thus
$$
\alpha(P_0)=\beta(P_0)=P_{0,p}.
$$
Put
$$
u=\beta^{-1}\circ\alpha\in R.
$$
Then $u$ is a unit and
$$
\pi
=F'\circ\beta\circ u
=\widehat\pi\circ u.
$$
Hence $\pi$ and $\widehat\pi$ are associates.

Conversely, suppose that they are associates.  Composition with a unit
preserves separability.  Since $\pi$ is purely inseparable,
$\widehat\pi$ is inseparable as well.  Hence
$$
V=\alpha\circ\widehat\pi
$$
is inseparable, and Exercise IV.4.15 gives $\Hasse(X)=0$.  This completes
part (b).

:::

:::

::: {.pf-step #s6}

If $\Hasse(X)=0$, then
$$
\boxed{j(X)\in\FF_{p^2}.}
$$

::: pf-proof

By Exercise IV.4.15, $\Hasse(X)=0$ means that
$$
V:X\longrightarrow X_p
$$
is inseparable.  Since $\deg V=p$, it is purely inseparable of degree $p$.
Apply Proposition IV.2.5 to $V$.  Its target is $X_p$, so its source is
isomorphic to the Frobenius twist of $X_p$:
$$
X\cong (X_p)_p=X_{p^2}.
$$
Applying step [](#s1){.pf-ref} twice gives
$$
j(X_{p^2})=j(X)^{1/p^2}.
$$
Isomorphic elliptic curves have the same $j$-invariant, hence
$$
j(X)=j(X)^{1/p^2}.
$$
Equivalently,
$$
j(X)^{p^2}=j(X),
$$
whose solutions in $k$ are exactly $\FF_{p^2}$.  This proves part (c).

:::

:::

::: {.pf-step #s7}

Every $f\in R$ commutes with the nonlinear Frobenius
$$
F:X\longrightarrow X.
$$

::: pf-proof

The nonlinear Frobenius here is the absolute Frobenius: on the structure
sheaf it sends a local function $a$ to $a^p$.  For every morphism of schemes
$f:X\to X$ in characteristic $p$,
$$
f^\sharp(a^p)=f^\sharp(a)^p.
$$
Therefore the square
$$
\begin{CD}
X @>{F}>> X\\
@V{f}VV @VV{f}V\\
X @>{F}>> X
\end{CD}
$$
commutes, so
$$
f\circ F=F\circ f.
$$

:::

:::

::: {.pf-step #s8}

If $\Hasse(X)\ne0$, then for every $f\in R$ the scalar
$\lambda_f$ defined by
$$
f^*:H^1(X,\OO_X)\longrightarrow H^1(X,\OO_X)
$$
satisfies
$$
\boxed{\lambda_f\in\FF_p.}
$$

::: pf-proof

The vector space $H^1(X,\OO_X)$ is one-dimensional over $k$, while the
absolute Frobenius induces a $p$-semilinear map
$$
F^*:H^1(X,\OO_X)\longrightarrow H^1(X,\OO_X),
\qquad
F^*(a\xi)=a^pF^*(\xi).
$$
The condition $\Hasse(X)\ne0$ says that $F^*$ is nonzero.  Choose
$\xi$ with
$$
F^*(\xi)\ne0.
$$

Step [](#s7){.pf-ref} and contravariance of pullback give
$$
F^*\circ f^*=f^*\circ F^*.
$$
Since $f^*$ is multiplication by $\lambda_f$,
$$
\lambda_f^pF^*(\xi)
=
F^*(\lambda_f\xi)
=
F^*f^*(\xi)
=
f^*F^*(\xi)
=
\lambda_fF^*(\xi).
$$
Because $F^*(\xi)\ne0$,
$$
\lambda_f^p=\lambda_f.
$$
Thus $\lambda_f$ is a root of $t^p-t$, so
$\lambda_f\in\FF_p$.

:::

:::

::: {.pf-step #s9}

If $\Hasse(X)\ne0$, the image of
$$
\varphi:R\longrightarrow k,
\qquad
f\longmapsto\lambda_f,
$$
is
$$
\boxed{\operatorname{im}\varphi=\FF_p.}
$$

::: pf-proof

Step [](#s8){.pf-ref} gives
$$
\operatorname{im}\varphi\subseteq\FF_p.
$$
For every integer $m$, the endomorphism $[m]_X$ belongs to $R$.  Under the
identification
$$
T_0\Pic^0(X)\cong H^1(X,\OO_X),
$$
the pullback $[m]_X^*$ is the tangent map of the dual endomorphism
$\widehat{[m]_X}$.  Exercise IV.4.7(e) gives
$$
\widehat{[m]_X}=[m]_X,
$$
whose tangent map is multiplication by $m$.  Therefore
$$
\varphi([m]_X)=m\pmod p.
$$
As $m$ varies, these elements exhaust $\FF_p$.  Hence the inclusion is an
equality.

:::

:::

::: {.pf-step #s10}

If $\Hasse(X)\ne0$, the ideal
$$
\mfp=\ker\varphi
$$
is prime and
$$
\boxed{R/\mfp\cong\FF_p.}
$$

::: pf-proof

By step [](#s9){.pf-ref}, $\varphi$ is a surjective ring homomorphism onto the field
$\FF_p$.  The first isomorphism theorem gives
$$
R/\ker\varphi\cong\FF_p.
$$
Moreover, if $ab\in\ker\varphi$, then
$$
0=\varphi(ab)=\varphi(a)\varphi(b)
$$
in the field $\FF_p$, so $\varphi(a)=0$ or $\varphi(b)=0$.  Hence
$\ker\varphi$ is prime.  This proves part (d).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove part (a), steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (b), step
[](#s6){.pf-ref} proves part (c), and steps [](#s7){.pf-ref}, [](#s8){.pf-ref}, [](#s9){.pf-ref} and [](#s10){.pf-ref} prove part (d).

:::

:::

:::
