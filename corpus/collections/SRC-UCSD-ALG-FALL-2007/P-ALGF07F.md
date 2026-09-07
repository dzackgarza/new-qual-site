---
schema: qual/card@1
id: P-ALGF07F
kind: problem
title: "Quadratic extensions and Galois behavior in characteristic 2"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 6 of the official UCSD Algebra Qualifying Examination, Fall 2007. The local card omitted source part (c), which asks for a degree-2 characteristic-2 extension that is not Galois; that part has been restored.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified separability and normality of quadratic extensions outside characteristic 2, the Galois extension F_4/F_2, and the purely inseparable quadratic extension F_2(t^{1/2})/F_2(t).
---

::: {.problem}
Let $F \geq K$ be an extension field of degree 2.

(a) If $K$ has characteristic not 2, show $F$ is Galois over $K$.

(b) Give an example where $F$ is Galois over $K$ even though $\operatorname{char} K = 2$.

(c) Give an example where $F$ is not Galois over $K$.
:::

::: {.solution}
<1>1. If $\operatorname{char}K\neq2$, every degree-$2$ extension $F/K$ is Galois.
::: {.proof}
Choose
\[
\alpha\in F\setminus K.
\]
Since $[F:K]=2$, one has
\[
F=K(\alpha),
\]
and the minimal polynomial of $\alpha$ over $K$ has degree $2$.
Write it as
\[
m(T)=T^2+bT+c\in K[T].
\]
Because $m$ is irreducible, $\alpha\notin K$.

The other root of $m$ is
\[
\beta=-b-\alpha,
\]
which also belongs to $F$.
Thus $m$ splits completely over $F$.
Moreover $m$ has distinct roots.
Indeed, if it had a repeated root, that root would be
\[
-\frac b2\in K
\]
because $2$ is invertible in $K$, contradicting irreducibility of $m$.
Hence $m$ is separable.

Therefore $F$ is the splitting field over $K$ of the separable polynomial $m$.
So $F/K$ is normal and separable, hence Galois.
:::

<1>2. There are quadratic Galois extensions in characteristic $2$.
::: {.proof}
Take
\[
K=\mathbb F_2
\]
and
\[
F=\mathbb F_4
=\mathbb F_2[\alpha],
\]
where $\alpha$ satisfies
\[
\alpha^2+\alpha+1=0.
\]
The polynomial
\[
T^2+T+1
\]
has no root in $\mathbb F_2$, so it is irreducible and
\[
[F:K]=2.
\]
Its derivative is $1$, so it is separable, and its two roots are
\[
\alpha
\qquad\text{and}\qquad
\alpha+1,
\]
both of which lie in $F$.
Thus $F$ is its splitting field over $K$, so
\[
\mathbb F_4/\mathbb F_2
\]
is Galois.
Its nontrivial automorphism is the Frobenius map
\[
x\longmapsto x^2.
\]
:::

<1>3. There are quadratic extensions in characteristic $2$ which are not Galois.
::: {.proof}
Let $t$ be transcendental over $\mathbb F_2$, set
\[
K=\mathbb F_2(t),
\]
and let
\[
F=K(u),
\qquad
u^2=t.
\]
First, $t$ is not a square in $K$.
Indeed, if
\[
t=\left(\frac{a(t)}{b(t)}\right)^2
\]
for nonzero coprime polynomials $a,b\in\mathbb F_2[t]$, then
\[
a(t)^2=t\,b(t)^2.
\]
The exponent of the irreducible factor $t$ on the left is even, whereas on the right it is odd, a contradiction.
Thus
\[
T^2-t
\]
has no root in $K$ and is irreducible, so
\[
[F:K]=2.
\]

In characteristic $2$,
\[
\frac{d}{dT}(T^2-t)=0.
\]
In an algebraic closure, if $u^2=t$, then
\[
T^2-t=(T-u)^2.
\]
Hence the minimal polynomial of $u$ is inseparable.
Therefore $F/K$ is not separable and consequently is not Galois.
:::
:::
