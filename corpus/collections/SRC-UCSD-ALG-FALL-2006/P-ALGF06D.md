---
schema: qual/card@1
id: P-ALGF06D
kind: problem
title: "Finiteness conditions for a group defined by generators and relations"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 2.2 of the official UCSD Algebra Qualifying Examination, Fall 2006; both parts and the presentation of G_n agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the exceptional case n=1 and proved the exact finite order by matching the normal-form upper bound with an explicit semidirect-product quotient.
---

::: {.problem}
Let $n$ be an integer.
Let $G_n$ be the group given by generators and relations as follows.
$$G_n = \langle x, y \mid x^3 = 1,\; xyx^{-1} = y^n \rangle.$$

(a) Provide (with proof) necessary and sufficient conditions on the integer $n$ for the group $G_n$ to be finite.

(b) Assuming that $G_n$ is finite, compute its order as a function of $n$.
:::


::: {.solution}
The group $G_n$ is finite exactly when $n\neq1$.
For $n\neq1$ its order is
\[
|G_n|=3|n^3-1|.
\]

<1>1. If $n=1$, then $G_n\cong C_3\times\mathbb Z$, so $G_n$ is infinite.
::: {.proof}
When $n=1$, the defining relation becomes
\[
xyx^{-1}=y,
\]
which is equivalent to $xy=yx$.
Thus
\[
G_1=\langle x,y\mid x^3=1,\ [x,y]=1\rangle.
\]
The assignments
\[
x\longmapsto (\bar1,0),
\qquad
y\longmapsto(\bar0,1)
\]
define a homomorphism
\[
G_1\longrightarrow C_3\times\mathbb Z,
\]
and the assignments
\[
(\bar a,b)\longmapsto x^a y^b
\]
define a homomorphism in the opposite direction.
These maps are inverse on the generators, hence
\[
G_1\cong C_3\times\mathbb Z.
\]
Therefore $G_1$ is infinite.
:::

<1>2. Suppose $n\neq1$ and set
\[
m:=|n^3-1|.
\]
Then every element of $G_n$ has one of the forms
\[
y^a,
\qquad
y^a x,
\qquad
y^a x^2,
\qquad 0\le a<m.
\]
In particular, $|G_n|\le3m$.
::: {.proof}
Conjugating $y$ three times by $x$ gives
\[
x^3 y x^{-3}=y^{n^3}.
\]
Since $x^3=1$, the left-hand side is $y$, so
\[
y^{n^3-1}=1.
\]
Because $n\neq1$, we have $m>0$, and therefore
\[
y^m=1.
\]

The defining conjugation relation also gives, for every integer $a$,
\[
xy^a=y^{na}x.
\]
Hence every word in $x^{\pm1}$ and $y^{\pm1}$ can be rewritten by moving all powers of $x$ to the right.
Using $x^3=1$, its $x$-exponent may be reduced modulo $3$, and using $y^m=1$, its $y$-exponent may be reduced modulo $m$.
Thus every element has one of the stated $3m$ normal forms.
:::

<1>3. There is a group of order $3m$ satisfying the defining relations of $G_n$.
::: {.proof}
Since
\[
\gcd(n,n^3-1)=1,
\]
we also have
\[
\gcd(n,m)=1.
\]
Thus multiplication by $n$ modulo $m$ defines an automorphism
\[
\alpha:C_m\longrightarrow C_m,
\qquad
\alpha(\bar a)=\overline{na}.
\]
Moreover,
\[
n^3\equiv1\pmod m,
\]
so
\[
\alpha^3=\operatorname{id}_{C_m}.
\]
Therefore the assignment sending a generator of $C_3$ to $\alpha$ defines an action of $C_3$ on $C_m$.
Form the semidirect product
\[
H:=C_m\rtimes_{\alpha} C_3.
\]
It has order
\[
|H|=3m.
\]

Let $\bar y$ generate $C_m$ and let $\bar x$ generate the $C_3$ factor.
Then
\[
\bar x^3=1
\]
and, by construction of the action,
\[
\bar x\bar y\bar x^{-1}=\bar y^n.
\]
Hence the defining relations of $G_n$ hold in $H$.
Because $\bar x$ and $\bar y$ generate $H$, the presentation of $G_n$ induces a surjective homomorphism
\[
G_n\twoheadrightarrow H.
\]
Consequently
\[
|G_n|\ge |H|=3m.
\]
:::

<1>4. For $n\neq1$, one has
\[
G_n\cong C_{|n^3-1|}\rtimes C_3
\]
and
\[
|G_n|=3|n^3-1|.
\]
::: {.proof}
By <1>2,
\[
|G_n|\le3m,
\]
while <1>3 gives a quotient of $G_n$ of order $3m$, so
\[
|G_n|\ge3m.
\]
Thus
\[
|G_n|=3m=3|n^3-1|.
\]
The surjection in <1>3 is therefore an isomorphism.
Together with <1>1, this also proves that $G_n$ is finite if and only if $n\neq1$.
:::
:::
