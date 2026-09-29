---
schema: qual/card@1
id: P-AGH4416HASSEBOUNDRIEMANNHYPOTHESIS
kind: problem
title: Hasse's bound $\abs{a} \leq 2\sqrt{q}$ for $N = \size X(\FF_q)$
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
    Read Hartshorne IV.4.16 together with Exercise IV.4.7 on dual isogenies,
    Exercise IV.4.15 on the dual Frobenius, and the definition of the
    k-linear Frobenius. Cross-checked the degree-quadratic-form proof of
    Hasse's bound against standard elliptic-curve lecture notes.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
  note: >-
    Rechecked the completed trace identity, Frobenius degree quadratic form,
    Hasse bound, and the q=p separability criterion after finishing parts
    (c)--(e).
---

::: {.problem}
Again let $X$ be an elliptic curve over $k$ of characteristic $p$, and suppose $X$ is defined over the field $\FF_q$ of $q=p^r$ elements, i.e., $X \subseteq \PP^2$ can be defined by an equation with coefficients in $\FF_q$.
Assume also that $X$ has a rational point over $\FF_q$.
Let $F': X_q \to X$ be the $k$-linear Frobenius with respect to $q$.

a. Show that $X_q \cong X$ as schemes over $k$, and that under this identification, $F': X \to X$ is the map obtained by the $q$-th power map on the coordinates of points of $X$, embedded in $\PP^2$.

b. Show that $1_X-F'$ is a separable morphism and its kernel is just the set $X(\FF_q)$ of points of $X$ with coordinates in $\FF_q$.

c. Using (Ex.
4.7), show that $F'+\hat{F}'=a_X$ for some integer $a$, and that $N=q-a+1$, where $N=\size X(\FF_q)$.

d. Use the fact that $\deg(m+n F')>0$ for all $m, n \in \ZZ$ to show that $\abs{a} \leq 2 \sqrt{q}$.
This is Hasse's proof of the analogue of the Riemann hypothesis for elliptic curves (App.
C, Ex.
5.6).

e. Now assume $q=p$, and show that the Hasse invariant of $X$ is 0 if and only if $a \equiv 0 \pmod p$.
Conclude for $p \geq 5$ that $X$ has Hasse invariant 0 if and only if $N=p+1$.
:::

::: {.solution}
Let $\pi=F'$ denote the $q$-power Frobenius after the identification in part (a), and write $O$ for the given $\FF_q$-rational origin.

::: pf

::: {.pf-step #s1}

The Frobenius twist $X_q$ is isomorphic to $X$ over $k$, and under this identification
$$
\boxed{\pi(x:y:z)=(x^q:y^q:z^q).}
$$

::: pf-proof

Choose a homogeneous equation
$$
G(x,y,z)=0
$$
for $X$ whose coefficients lie in $\FF_q$.
The $q$-Frobenius twist is obtained by applying the $q$-power automorphism of $k$ to the coefficients.
Every coefficient of $G$ is fixed, so the twisted equation is again $G=0$.
Thus $X_q\cong X$ over $k$.

The $k$-linear Frobenius is the coordinate $q$-power map.
Since
$$
G(x^q,y^q,z^q)=G(x,y,z)^q,
$$
it preserves $X$ and has the displayed form.
This proves part (a).

:::

:::

::: {.pf-step #s2}

The endomorphism
$$
1_X-\pi:X\longrightarrow X
$$
is separable.

::: pf-proof

The differential of the $q$-power Frobenius is zero.
Hence
$$
d(1_X-\pi)_O
=
d(1_X)_O-d\pi_O
=
\id_{T_OX},
$$
which is nonzero.
A homomorphism of elliptic curves is separable exactly when its differential at the origin is nonzero, so $1_X-\pi$ is separable.

:::

:::

::: {.pf-step #s3}

Its kernel is exactly
$$
\boxed{\ker(1_X-\pi)=X(\FF_q).}
$$

::: pf-proof

A geometric point $P=(x:y:z)$ lies in the kernel exactly when
$$
\pi(P)=P.
$$
By step [](#s1){.pf-ref} this is equivalent to $P$ being fixed by the $q$-power Frobenius, hence to $P$ being defined over $\FF_q$.
This proves part (b).

:::

:::

::: {.pf-step #s4}

If $N=\#X(\FF_q)$, then
$$
\deg(1_X-\pi)=N.
$$

::: pf-proof

By step [](#s2){.pf-ref} the endomorphism is separable, so its degree equals the number of geometric kernel points.
Step [](#s3){.pf-ref} identifies these with $X(\FF_q)$.

:::

:::

::: {.pf-step #s5}

There is an integer
$$
a=q+1-N
$$
such that
$$
\boxed{\pi+\widehat\pi=[a]_X.}
$$

::: pf-proof

By additivity of dualization from [[P-AGH447DUALOFAMORPHISM|Exercise IV.4.7(d),(e)]],
$$
\widehat{(1_X-\pi)}=1_X-\widehat\pi.
$$
Exercise IV.4.7(c) applied first to $1_X-\pi$ and then to $\pi$ gives
$$
\widehat{(1_X-\pi)}\circ(1_X-\pi)=[N]_X
$$
and
$$
\widehat\pi\circ\pi=[q]_X.
$$
Therefore
$$
\begin{aligned}
[N]_X
&=(1_X-\widehat\pi)\circ(1_X-\pi)\\
&=[q+1]_X-(\pi+\widehat\pi).
\end{aligned}
$$
Hence
$$
\pi+\widehat\pi=[q+1-N]_X.
$$
Taking $a=q+1-N$ proves part (c), including $N=q-a+1$.

:::

:::

::: {.pf-step #s6}

For all $m,n\in\ZZ$,
$$
\boxed{
\deg([m]_X+[n]_X\circ\pi)
=
m^2+amn+qn^2.
}
$$

::: pf-proof

Put
$$
\phi=[m]_X+[n]_X\circ\pi.
$$
By Exercise IV.4.7(d),(e),
$$
\widehat\phi=[m]_X+[n]_X\circ\widehat\pi.
$$
Using step [](#s5){.pf-ref} and $\widehat\pi\circ\pi=[q]_X$, we obtain
$$
\begin{aligned}
\widehat\phi\circ\phi
&=[m^2]_X+[mn]_X\circ(\pi+\widehat\pi)
  +[n^2]_X\circ\widehat\pi\circ\pi\\
&=[m^2+amn+qn^2]_X.
\end{aligned}
$$
Exercise IV.4.7(c) also gives
$$
\widehat\phi\circ\phi=[\deg\phi]_X.
$$
Since $\ZZ\to\Endo(X,O)$ is injective, the two integers are equal.

:::

:::

::: {.pf-step #s7}

One has Hasse's bound
$$
\boxed{\abs a\le2\sqrt q.}
$$

::: pf-proof

Step [](#s6){.pf-ref} gives
$$
Q(m,n)=m^2+amn+qn^2\ge0
$$
for all $m,n\in\ZZ$, because $Q(m,n)$ is a degree.
The strict positivity in the exercise applies when the corresponding endomorphism is nonzero; nonnegativity is sufficient for the argument.

For $n\ne0$, division by $n^2$ gives
$$
\left(\frac mn\right)^2+a\frac mn+q\ge0.
$$
The rational numbers are dense in $\RR$, so continuity implies
$$
x^2+ax+q\ge0
$$
for every real $x$.
Hence the discriminant is nonpositive:
$$
a^2-4q\le0.
$$
Thus $\abs a\le2\sqrt q$, proving part (d).

:::

:::

::: {.pf-step #s8}

Now assume $q=p$.
The Hasse invariant of $X$ is zero if and only if
$$
\boxed{a\equiv0\pmod p.}
$$

::: pf-proof

Let
$$
V=\widehat\pi.
$$
Step [](#s5){.pf-ref} gives
$$
V=[a]_X-\pi.
$$
The differential of $\pi$ is zero, while the differential of multiplication by $a$ on the one-dimensional tangent space at the origin is multiplication by the image of $a$ in $k$.
Hence
$$
dV_O=a\cdot\id_{T_OX}.
$$
By [[P-AGH4415PTORSIONANDHASSE|Exercise IV.4.15]], the Hasse invariant is zero exactly when the dual Frobenius $V$ is inseparable.
An isogeny of elliptic curves is inseparable exactly when its differential at the origin vanishes.
Therefore
$$
\operatorname{Hasse}(X)=0
\iff
dV_O=0
\iff
a\equiv0\pmod p.
$$

:::

:::

::: {.pf-step #s9}

If $p\ge5$, then the Hasse invariant of $X$ is zero if and only if
$$
\boxed{N=p+1.}
$$

::: pf-proof

When $q=p$, step [](#s7){.pf-ref} gives
$$
\abs a\le2\sqrt p.
$$
For $p\ge5$,
$$
2\sqrt p<p.
$$
Thus an integer $a$ in this range is divisible by $p$ exactly when $a=0$.
By step [](#s8){.pf-ref},
$$
\operatorname{Hasse}(X)=0
\iff
a=0.
$$
Finally step [](#s5){.pf-ref} gives
$$
N=p-a+1,
$$
so $a=0$ is equivalent to $N=p+1$.
This proves part (e).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (b), steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (c), steps [](#s6){.pf-ref} and [](#s7){.pf-ref} prove part (d), and steps [](#s8){.pf-ref} and [](#s9){.pf-ref} prove part (e).

:::

:::

:::
