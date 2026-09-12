---
schema: qual/card@1
id: P-ALGS17C
kind: problem
title: "Irreducible non-prime element and non-principal maximal ideal in Z[sqrt(-6)]"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Number Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $R = \mathbb{Z}[\sqrt{-6}]$.

(a) Prove that 3 is an irreducible element of $R$ which is not prime.

(b) Find an element $r \in R$ such that the ideal $I = \langle 3, r \rangle$ is a maximal ideal in $R$.
Prove that $I$ is not a principal ideal.
:::

::: {.solution}
<1>1. For $z=a+b\sqrt{-6}\in R$, define
\[
N(z)=(a+b\sqrt{-6})(a-b\sqrt{-6})=a^2+6b^2.
\]
Then $N(zw)=N(z)N(w)$, and the only units of $R$ are $\pm1$.
::: {.proof}
The norm is multiplicative by direct multiplication.
If $z$ is a unit, then $N(z)$ is a positive integer unit, hence $N(z)=1$; the equation $a^2+6b^2=1$ gives $b=0$ and $a=\pm1$.
Conversely, $\pm1$ are units.
:::

<1>2. The element $3$ is irreducible in $R$.
::: {.proof}
Suppose $3=xy$ with neither $x$ nor $y$ a unit.
Taking norms gives
\[
9=N(3)=N(x)N(y).
\]
Since nonunits have norm at least $2$, the only possible nontrivial factorization of $9$ is $3\cdot3$.
But the equation
\[
a^2+6b^2=3
\]
has no integer solution: if $b=0$, then $a^2=3$, while if $b\ne0$, then $a^2+6b^2\ge6$.
Thus no element of $R$ has norm $3$, contradiction.
Hence one of $x,y$ is a unit.
:::

<1>3. The element $3$ is not prime in $R$.
::: {.proof}
We have
\[
(\sqrt{-6})^2=-6=3(-2),
\]
so $3$ divides $(\sqrt{-6})^2$.
But $3$ does not divide $\sqrt{-6}$ in $R$: if $\sqrt{-6}=3(a+b\sqrt{-6})$, then comparison of coefficients gives $3b=1$, impossible for $b\in\mathbb Z$.
Thus $3$ is irreducible but not prime.
:::

<1>4. Take $r=\sqrt{-6}$ and
\[
I=(3,\sqrt{-6}).
\]
Then $I$ is maximal.
::: {.proof}
Define
\[
\pi:R\longrightarrow \mathbb F_3,\qquad a+b\sqrt{-6}\longmapsto \overline a.
\]
This is a surjective ring homomorphism because $-6\equiv0\pmod3$.
Its kernel consists exactly of elements with $3\mid a$, namely
\[
\ker\pi=(3,\sqrt{-6})=I.
\]
Hence $R/I\cong\mathbb F_3$ is a field, so $I$ is maximal.
:::

<1>5. The ideal $I$ is not principal.
::: {.proof}
The quotient $R/I\cong\mathbb F_3$ has three elements, so $[R:I]=3$ as additive groups.
If $I=(\alpha)$ for some nonzero $\alpha=a+b\sqrt{-6}$, multiplication by $\alpha$ on the free abelian group $R=\mathbb Z\oplus\mathbb Z\sqrt{-6}$ has matrix
\[
\begin{pmatrix}a&-6b\\ b&a\end{pmatrix},
\]
whose determinant is $a^2+6b^2=N(\alpha)$.
Therefore
\[
[R:(\alpha)]=|N(\alpha)|.
\]
Thus principality of $I$ would force $N(\alpha)=3$, but <1>2 showed that no such element exists.
Hence $I$ is not principal.
:::
:::
