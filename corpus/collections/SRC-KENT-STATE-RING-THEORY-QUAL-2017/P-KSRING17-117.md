---
schema: qual/card@1
id: P-KSRING17-117
kind: problem
title: The Jacobson radical of a corner ring $eRe$
classification:
  areas: [algebra]
  topics:
  - Jacobson Radical
  - Idempotents
  - Corner Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 117 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
If R is any ring with identity, let $J ( R )$ denote the Jacobson radical of R. Show that if e is any idempotent of R, then $J ( e R e ) = e J ( R ) e$
:::

::: {.solution}

Write
$$
J
\coloneqq
J(R),
$$
and note that
$$
eRe
$$
is a ring with identity
$$
e.
$$

::: pf

::: {.pf-step #s1-1}

For any ring $S$ with identity and any $x\in S$,
$$
\boxed{
x\in J(S)
\iff
1-sx\in S^\times
\text{ for every }s\in S.
}
$$


::: pf-proof

First suppose
$$
x\in J(S).
$$
Since $J(S)$ is a two-sided ideal,
$$
sx\in J(S)
$$
for every $s$.
Suppose
$$
1-sx
$$
had no left inverse.
Then the left ideal
$$
S(1-sx)
$$
would be proper and hence contained in a maximal left ideal
$$
L.
$$
The Jacobson radical is contained in every maximal left ideal, so
$$
sx\in L.
$$
Also
$$
1-sx\in L.
$$
Therefore
$$
1
=
(1-sx)+sx
\in
L,
$$
contradiction.
Thus
$$
1-sx
$$
has a left inverse.

Similarly, if
$$
1-sx
$$
had no right inverse, the proper right ideal
$$
(1-sx)S
$$
would lie in a maximal right ideal
$$
M.
$$
The Jacobson radical is contained in every maximal right ideal, so again
$$
sx\in M
$$
and
$$
1-sx\in M,
$$
forcing
$$
1\in M,
$$
contradiction.
Thus
$$
1-sx
$$
has both a left inverse and a right inverse.
These inverses coincide, so
$$
1-sx
$$
is a unit.

Conversely, suppose
$$
1-sx
$$
is a unit for every
$$
s\in S,
$$
but
$$
x\notin J(S).
$$
Since
$$
J(S)
$$
is the intersection of the maximal left ideals of $S$, there is a maximal left ideal
$$
L
$$
with
$$
x\notin L.
$$
Then
$$
L+Sx
$$
is a left ideal properly containing $L$, so maximality gives
$$
L+Sx=S.
$$
Thus
$$
1
=
\ell+sx
$$
for some
$$
\ell\in L,
\qquad
s\in S.
$$
Hence
$$
1-sx
=
\ell
\in
L.
$$
But a proper left ideal cannot contain a unit, contradiction.
Therefore
$$
x\in J(S).
$$

:::

:::

::: pf-step

One has
$$
eJe
\subseteq
eRe.
$$


::: pf-proof

Since
$$
J
\subseteq
R,
$$
every element
$$
eje
$$
with
$$
j\in J
$$
lies in
$$
eRe.
$$

:::

:::

::: {.pf-step #s1-3}

Let
$$
x\in eJe
$$
and
$$
y\in eRe.
$$
Then
$$
yx\in J(R).
$$


::: pf-proof

Because
$$
x\in eJe,
$$
one has
$$
x\in J(R)
$$
since $J(R)$ is a two-sided ideal.
Therefore
$$
yx\in J(R).
$$

:::

:::

::: {.pf-step #s1-4}

The element
$$
yx
$$
commutes with $e$ and satisfies
$$
eyx=yx=yxe.
$$


::: pf-proof

Both
$$
y
\qquad\text{and}\qquad
x
$$
belong to
$$
eRe.
$$
Hence
$$
ey=y=ye
$$
and
$$
ex=x=xe.
$$
Therefore
$$
e(yx)=yx=(yx)e.
$$

:::

:::

::: {.pf-step #s1-5}

The element
$$
e-yx
$$
is a unit of the corner ring
$$
eRe.
$$


::: pf-proof

By step [](#s1-3){.pf-ref} and the criterion from step [](#s1-1){.pf-ref} applied in $R$,
$$
1-yx
$$
is a unit of $R.
By step [](#s1-4){.pf-ref},
$$
e
$$
commutes with
$$
1-yx.
$$
Hence it also commutes with
$$
(1-yx)^{-1}.
$$
Set
$$
v
\coloneqq
e(1-yx)^{-1}e
\in
eRe.
$$
Then
$$
\begin{aligned}
(e-yx)v
&=
e(1-yx)e
e(1-yx)^{-1}e\\
&=
e(1-yx)(1-yx)^{-1}e\\
&=
e.
\end{aligned}
$$
The same computation on the other side gives
$$
v(e-yx)=e.
$$
Thus
$$
e-yx
$$
is invertible in
$$
eRe.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
eJ(R)e
\subseteq
J(eRe).
}
$$


::: pf-proof

Let
$$
x\in eJ(R)e.
$$
For every
$$
y\in eRe,
$$
step [](#s1-5){.pf-ref} shows
$$
e-yx
$$
is a unit in the ring
$$
eRe
$$
whose identity is $e$.
By step [](#s1-1){.pf-ref} applied to
$$
S=eRe,
$$
one has
$$
x\in J(eRe).
$$

:::

:::

::: {.pf-step #s1-7}

Now let
$$
x\in J(eRe).
$$
Then
$$
x=ex=xe.
$$


::: pf-proof

Every element of the corner ring
$$
eRe
$$
has the form
$$
ere.
$$
Hence multiplication by $e$ on either side fixes it.

:::

:::

::: {.pf-step #s1-8}

Fix
$$
r\in R,
$$
and set
$$
a
\coloneqq
e-ere\,x
\in
eRe.
$$
Then $a$ is a unit of $eRe$.


::: pf-proof

The element
$$
ere
$$
lies in
$$
eRe.
$$
Because
$$
x\in J(eRe),
$$
the Jacobson-radical criterion from step [](#s1-1){.pf-ref} gives that
$$
e-(ere)x
$$
is a unit of
$$
eRe.
$$
This is exactly $a$.

:::

:::

::: {.pf-step #s1-9}

Put
$$
f
\coloneqq
1-e
$$
and
$$
b
\coloneqq
frex.
$$
Then
$$
1-rx
=
a+f-b.
$$


::: pf-proof

By step [](#s1-7){.pf-ref},
$$
x=ex.
$$
Hence
$$
rx
=
rex
=
(e+f)rex
=
erex+frex.
$$
Therefore
$$
\begin{aligned}
1-rx
&=
e+f-erex-frex\\
&=
(e-erex)+f-b\\
&=
a+f-b.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-10}

Let
$$
a^{-1}
\in
eRe
$$
denote the inverse of $a$.
Then
$$
v
\coloneqq
a^{-1}+f+ba^{-1}
$$
is an inverse of
$$
1-rx.
$$


::: pf-proof

The Peirce relations give
$$
ef=fe=0,
$$
$$
a,a^{-1}\in eRe,
$$
and
$$
b\in fRe.
$$
Hence
$$
ab=0,
\qquad
a^{-1}b=0,
\qquad
bf=0,
\qquad
b^2=0.
$$
Using step [](#s1-9){.pf-ref},
$$
\begin{aligned}
(1-rx)v
&=
(a+f-b)
(a^{-1}+f+ba^{-1})\\
&=
aa^{-1}
+f^2
+fba^{-1}
-ba^{-1}\\
&=
e+f\\
&=
1.
\end{aligned}
$$
Similarly,
$$
\begin{aligned}
v(1-rx)
&=
(a^{-1}+f+ba^{-1})
(a+f-b)\\
&=
a^{-1}a
+f^2
-fb
+ba^{-1}a\\
&=
e+f-b+b\\
&=
1.
\end{aligned}
$$
Thus $v$ is a two-sided inverse.

:::

:::

::: {.pf-step #s1-11}

For every
$$
r\in R,
$$
the element
$$
1-rx
$$
is a unit of $R$.


::: pf-proof

The element
$$
r
$$
was arbitrary in step [](#s1-8){.pf-ref}, and step [](#s1-10){.pf-ref} constructs an inverse for
$$
1-rx.
$$

:::

:::

::: {.pf-step #s1-12}

Therefore
$$
x\in J(R).
$$


::: pf-proof

Apply the Jacobson-radical criterion from step [](#s1-1){.pf-ref} in the ring $R$ to step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Since
$$
x=exe,
$$
one has
$$
x\in eJ(R)e.
$$


::: pf-proof

Step [](#s1-12){.pf-ref} gives
$$
x\in J(R),
$$
and step [](#s1-7){.pf-ref} gives
$$
x=exe.
$$
Thus
$$
x
\in
eJ(R)e.
$$

:::

:::

::: {.pf-step #s1-14}

Hence
$$
\boxed{
J(eRe)
\subseteq
eJ(R)e.
}
$$


::: pf-proof

The element
$$
x\in J(eRe)
$$
was arbitrary, and step [](#s1-13){.pf-ref} proves the required containment.

:::

:::

::: {.pf-step #s1-15}

Combining both inclusions,
$$
\boxed{
J(eRe)
=
eJ(R)e.
}
$$


::: pf-proof

Step [](#s1-6){.pf-ref} gives
$$
eJ(R)e
\subseteq
J(eRe),
$$
and step [](#s1-14){.pf-ref} gives the reverse inclusion.

:::

:::

::: pf-qed

Step [](#s1-15){.pf-ref} is the required identity.

:::

:::

:::
