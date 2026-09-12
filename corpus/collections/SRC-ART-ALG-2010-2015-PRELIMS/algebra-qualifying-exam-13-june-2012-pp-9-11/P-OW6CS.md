---
schema: qual/card@1
id: P-OW6CS
kind: problem
title: Examples and non-examples in Galois theory
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked all six parts of June 2012 Fields 2 on PDF page 11. The source reverses the extension directions in (a) and (b), as did the card, while the former solution silently treated the reversed variants."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the explicit extension-direction correction, the unrestricted algebraic Galois argument in (b), and every existence or impossibility claim; replaced the unsupported solvability assertion by an explicit radical tower."
---

::: {.problem}
Give an example of each of the following or explain why no such examples exist.
One or two sentence answers will suffice; you don't need to give formal proofs.

a. A Galois extension $K/F$ and an intermediate field $E$ ($F \subset E \subset K$) such that $E/F$ is not Galois.

b. A Galois extension $K/F$ and an intermediate field $E$ ($F \subset E \subset K$) such that $K/E$ is not Galois.

c. A finite field of size 8.

d. A subfield $E$ of the splitting field of $x^5 + x - 1$ with $[E:\mathbb{Q}] = 7$.

e. A field extension $K/F$ which is finite dimensional but not separable.

f. An irreducible fifth degree polynomial over $\mathbb{Q}$ which is solvable by radicals.
:::

::: remark
With the prescribed inclusions $F\subset E\subset K$,
the expressions $F/E$ and $E/K$ reverse the field-extension
directions and do not define extensions via these inclusions.
Parts (a) and (b) use the meaningful directions $E/F$ and
$K/E$, respectively. No finiteness assumption on $K/F$
is needed in part (b).
:::

::: solution
<1>1. In part (a), take $F=\mathbb Q$,
$E=\mathbb Q(a)$, and $K=\mathbb Q(a,\zeta)$, where
$a=\sqrt[3]{2}>0$ and $\zeta=e^{2\pi i/3}$.

::: proof
The polynomial $T^3-2$ is Eisenstein at two and therefore
irreducible over $\mathbb Q$ [@DF04]. Thus $[E:F]=3>1$.
The field $E$ is real, whereas $\zeta$ is nonreal, so
$E\subset K$ is also strict.
The roots $a,\zeta a,\zeta^2a$ generate $K$, because
their ratio recovers $\zeta$. Hence $K$ is a splitting
field in characteristic zero and $K/F$ is Galois [@DF04].
But $E$ contains only the real root of the irreducible
polynomial $T^3-2$, so $E/F$ is not normal and is not Galois.
:::

<1>2. No example exists in part (b): $K/E$ is always Galois.

::: proof
For $a\in K$, let $p_a(T)\in F[T]$ and $q_a(T)\in E[T]$
be its monic minimal polynomials over $F$ and $E$.
The extension $K/F$ is algebraic, so both exist.
Since $p_a(a)=0$, division by the minimal polynomial
over $E$ gives $q_a\mid p_a$ in $E[T]$.
Normality and separability of $K/F$ imply that $p_a$
splits into distinct linear factors in $K[T]$.
Its divisor $q_a$ therefore does the same.
Thus every element of $K$ is separable over $E$, and
every irreducible polynomial over $E$ with a root in
$K$ splits over $K$. This proves that $K/E$ is algebraic,
normal, and separable, hence Galois, without assuming
that its degree is finite.
:::

<1>3. In part (c), take $\mathbb F_2[T]/(T^3+T+1)$.

::: proof
The polynomial is nonzero at both $0$ and $1$.
A reducible cubic over a field has a linear factor,
so this polynomial is irreducible over $\mathbb F_2$.
The quotient is consequently a field [@DF04]. Polynomial
division gives the basis $1,[T],[T^2]$ over $\mathbb F_2$,
so it has exactly $2^3=8$ elements.
:::

<1>4. No example exists in part (d).

::: proof
Let $L$ be the splitting field of $T^5+T-1$ over $\mathbb Q$.
This is a finite Galois extension, since the base field
has characteristic zero [@DF04]. Its automorphisms act
faithfully on the distinct roots, because those roots
generate $L$. There are at most five such roots, so
this action embeds $\operatorname{Gal}(L/\mathbb Q)$
into $S_5$, adding fixed letters if necessary.
Lagrange's theorem gives
$[L:\mathbb Q]=|\operatorname{Gal}(L/\mathbb Q)|\mid120$.
For an intermediate field $E$, the tower law makes
$[E:\mathbb Q]$ a divisor of $[L:\mathbb Q]$ and hence
of $120$. Since $7\nmid120$, degree seven is impossible.
:::

<1>5. In part (e), take $F=\mathbb F_2(t)$ and $K=F(u)$
with $u^2=t$, where $t$ is transcendental.

::: proof
The polynomial $T^2-t$ has no root in $F$: an equality
$(A(t)/B(t))^2=t$, with nonzero polynomials $A,B$, would
give $2\deg A=1+2\deg B$, impossible by parity.
It is therefore irreducible, giving $[K:F]=2$.
In $K[T]$ it equals $(T-u)^2$, so the minimal polynomial
of $u$ has a repeated root. Hence $K/F$ is not separable.
:::

<1>6. In part (f), take $f(T)=T^5-2$.

::: proof
Eisenstein's criterion at two proves irreducibility over
$\mathbb Q$ [@DF04]. Let $b=\sqrt[5]{2}$ and choose a
primitive fifth root of unity $\xi$. The roots of $f$
are precisely $\xi^j b$, $0\leq j<5$.
They all lie in the radical tower
$$
\mathbb Q\subset\mathbb Q(\xi)
\subset\mathbb Q(\xi,b):
\qquad \xi^5=1\in\mathbb Q,\quad b^5=2\in\mathbb Q(\xi).
$$
Each step adjoins an element having a positive integral
power in the preceding field. Thus every root of the
irreducible fifth-degree polynomial lies in a radical
extension, which is exactly solvability by radicals.
:::
:::
