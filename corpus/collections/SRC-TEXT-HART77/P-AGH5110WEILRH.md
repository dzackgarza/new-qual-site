---
schema: qual/card@1
id: P-AGH5110WEILRH
kind: problem
title: Weil's proof of the Riemann hypothesis for curves over finite fields
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.10, the retained Egbert companion argument, the local
    Frobenius-degree card, and Exercises V.1.6 and V.1.9. The companion has the
    correct intersection calculation but reverses the optimization language:
    qx+1/x is minimized on x>0, not maximized. The proof below derives the
    quadratic intersection inequality and takes the infimum over positive
    rational ratios and the supremum over negative rational ratios, giving
    both sides of the Weil bound.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $C$ be a curve of genus $g$ defined over the finite field $\FF_q$, and let $N$ be the number of points of $C$ rational over $\FF_q$.
Then $N=1-a+q$, with $|a| \leqslant 2 g \sqrt{q}$.

To prove this, we consider $C$ as a curve over the algebraic closure $k$ of $\FF_q$.
Let $f: C \rightarrow C$ be the $k$-linear Frobenius morphism obtained by taking $q$ th powers, which makes sense since $C$ is defined over $\FF_q$, so $X_q \cong X$ (See $V, 2.4.1$).

Let $\Gamma \subseteq C \times C$ be the graph of $f$, and let $\Delta \subseteq C \times C$ be the diagonal.

Show that $\Gamma^2=q(2-2 g)$, and $\Gamma . \Delta=N$.
Then apply (Ex.
1.9) to $D=r \Gamma+s \Delta$ for all $r$ and $s$ to obtain the result.

See (App.
C, Ex.
5.7) for another interpretation of this result.
:::

::: {.solution}
Let
$$
F=(f,\id_C):C\times C\longrightarrow C\times C.
$$

::: pf

::: {.pf-step #s1}

The $q$-power Frobenius $f:C\to C$ is finite of degree $q$.

::: pf-proof

Write $q=p^r$. The $k$-linear $p$-power Frobenius on a smooth curve over the
perfect field $k$ has degree $p$; this is recorded in [[D-IV2FROBTWIST]]. The
$q$-power Frobenius is its $r$-fold iterate, with the intervening Frobenius
twists identified with $C$ because the curve is defined over $\FF_q$.
Multiplicativity of degree under composition therefore gives
$$
\deg f=p^r=q.
$$

:::

:::

::: {.pf-step #s2}

Scheme-theoretically,
$$
\Gamma=F^*\Delta,
$$
and
$$
\boxed{\Gamma^2=q(2-2g)}.
$$

::: pf-proof

The inverse image of the diagonal under $F$ consists of pairs $(P,Q)$ with
$$
f(P)=Q,
$$
which is exactly the graph of $f$; the same equality holds scheme-theoretically
because both are defined by pulling back the diagonal ideal.

The morphism $F$ is finite of degree $q$ by step [](#s1){.pf-ref}. The projection formula
for intersection numbers therefore gives
$$
(F^*\Delta)^2
=
q\Delta^2.
$$
Exercise V.1.6, proved on [[P-AGH516DIAGONAL]], gives
$$
\Delta^2=2-2g.
$$
Substitution yields
$$
\Gamma^2=q(2-2g).
$$

:::

:::

::: {.pf-step #s3}

The closed points of $\Gamma\cap\Delta$ are exactly the
$\FF_q$-rational points of $C$.

::: pf-proof

A geometric point $(P,P)$ of the diagonal lies on the graph exactly when
$$
f(P)=P.
$$
The fixed geometric points of the $q$-power Frobenius are precisely the points
defined over $\FF_q$. Thus the underlying set of $\Gamma\cap\Delta$ is in
bijection with $C(\FF_q)$.

:::

:::

::: {.pf-step #s4}

Every point of $\Gamma\cap\Delta$ has intersection multiplicity one, so
$$
\boxed{\Gamma\cdot\Delta=N}.
$$

::: pf-proof

The differential of Frobenius is zero. At a fixed point $P$, under
$$
T_{(P,P)}(C\times C)=T_PC\oplus T_PC,
$$
the tangent line to the graph is
$$
T_{(P,P)}\Gamma=\{(v,0):v\in T_PC\},
$$
while the tangent line to the diagonal is
$$
T_{(P,P)}\Delta=\{(v,v):v\in T_PC\}.
$$
These two one-dimensional subspaces meet only at zero and span the tangent
space of the surface. Hence the two smooth curves meet transversally at every
fixed point, so every local intersection multiplicity is one. Step [](#s3){.pf-ref} now
gives
$$
\Gamma\cdot\Delta=\#C(\FF_q)=N.
$$

:::

:::

::: {.pf-step #s5}

With
$$
l=C\times\{Q\},
\qquad
m=\{Q\}\times C
$$
for a geometric point $Q\in C$, the divisors $\Gamma$ and $\Delta$ have types
$$
\Gamma:(q,1),
\qquad
\Delta:(1,1)
$$
in the notation of Exercise V.1.9.

::: pf-proof

The intersection $\Gamma\cap m$ is obtained by fixing the first coordinate
$P=Q$, leaving the single point $(Q,f(Q))$ with multiplicity one. Thus
$$
\Gamma\cdot m=1.
$$
The intersection with $l$ is the fibre $f^{-1}(Q)$, whose scheme-theoretic
length is $\deg f=q$ by step [](#s1){.pf-ref}. Hence
$$
\Gamma\cdot l=q.
$$
The diagonal meets each ruling transversally in one point, so
$$
\Delta\cdot l=\Delta\cdot m=1.
$$
This gives the stated types.

:::

:::

::: {.pf-step #s6}

For integers $r,s$, put
$$
D=r\Gamma+s\Delta.
$$
Then
$$
D^2
=(2-2g)(qr^2+s^2)+2rsN
$$
and $D$ has type
$$
(rq+s,r+s).
$$

::: pf-proof

The square formula follows from steps [](#s2){.pf-ref} and [](#s4){.pf-ref} together with
$\Delta^2=2-2g$:
$$
\begin{aligned}
D^2
&=r^2\Gamma^2+2rs(\Gamma\cdot\Delta)+s^2\Delta^2\\
&=(2-2g)(qr^2+s^2)+2rsN.
\end{aligned}
$$
The type is additive, so step [](#s5){.pf-ref} gives
$$
D\cdot l=rq+s,
\qquad
D\cdot m=r+s.
$$

:::

:::

::: {.pf-step #s7}

For every pair of integers $r,s$,
$$
rs(N-q-1)\leq g(qr^2+s^2).
$$

::: pf-proof

Apply the Castelnuovo--Severi inequality from Exercise V.1.9,
[[P-AGH519HODGEINDEX]], to the divisor $D$ of step [](#s6){.pf-ref}:
$$
D^2\leq2(D\cdot l)(D\cdot m).
$$
Substituting the formulas from step [](#s6){.pf-ref} gives
$$
(2-2g)(qr^2+s^2)+2rsN
\leq
2(rq+s)(r+s).
$$
Dividing by two and collecting terms yields
$$
rs(N-q-1)\leq g(qr^2+s^2).
$$

:::

:::

::: {.pf-step #s8}

One has
$$
N-q-1\leq2g\sqrt q.
$$

::: pf-proof

Take $r,s>0$ in step [](#s7){.pf-ref} and divide by $rs$:
$$
N-q-1
\leq
g\left(q\frac rs+\frac sr\right).
$$
As $r/s$ ranges over the positive rational numbers, these ratios are dense in
$\RR_{>0}$. For $x>0$, the arithmetic--geometric mean inequality gives
$$
qx+\frac1x\geq2\sqrt q,
$$
with equality at $x=1/\sqrt q$. Hence the infimum over positive rational $x$
is $2\sqrt q$. Taking the infimum in the displayed family of upper bounds
gives
$$
N-q-1\leq2g\sqrt q.
$$

:::

:::

::: {.pf-step #s9}

One has
$$
N-q-1\geq-2g\sqrt q.
$$

::: pf-proof

Take $r>0$ and $s<0$ in step [](#s7){.pf-ref}. Dividing by the negative number $rs$
reverses the inequality:
$$
N-q-1
\geq
g\left(q\frac rs+\frac sr\right).
$$
Writing $x=r/s<0$ and $t=-x>0$ gives
$$
qx+\frac1x
=
-\left(qt+\frac1t\right)
\leq
-2\sqrt q.
$$
The negative rational numbers are dense in $\RR_{<0}$, so the supremum of the
right-hand side over such rational $x$ is $-2g\sqrt q$. Taking this supremum
gives the asserted lower bound.

:::

:::

::: {.pf-step #s10}

Setting
$$
a=q+1-N,
$$
one has
$$
\boxed{N=1-a+q}
\qquad\text{and}\qquad
\boxed{|a|\leq2g\sqrt q}.
$$

::: pf-proof

Steps [](#s8){.pf-ref} and [](#s9){.pf-ref} give
$$
|N-q-1|\leq2g\sqrt q.
$$
Since $a=-(N-q-1)$, the same bound holds for $|a|$, and the defining equation
for $a$ rearranges to $N=1-a+q$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove the two requested intersection identities, and steps
[](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref}, [](#s8){.pf-ref}, [](#s9){.pf-ref} and [](#s10){.pf-ref} apply Exercise V.1.9 to obtain the stated Riemann-hypothesis bound.

:::

:::

:::
