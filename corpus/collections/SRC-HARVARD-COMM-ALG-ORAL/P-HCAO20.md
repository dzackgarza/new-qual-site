---
schema: qual/card@1
id: P-HCAO20
kind: problem
title: A Cohen--Macaulay ring which is not Gorenstein
classification:
  areas:
  - algebra
  topics:
  - Cohen–Macaulay Rings
  - Gorenstein Rings
  - Homological Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Give an example of a Cohen--Macaulay ring which is not Gorenstein.
:::

::: solution
Let
\[
R=k[x,y]/(x,y)^2.
\]
Then $R$ is Cohen--Macaulay but not Gorenstein.

<1>1. The ring $R$ is an Artinian local ring with maximal ideal
\[
\mathfrak m=(x,y)/(x,y)^2
\]
and residue field $k$.
::: proof
Every element of $R$ has a unique expression
\[
a+bx+cy,
\qquad a,b,c\in k,
\]
because all quadratic monomials vanish. Hence $R$ is finite-dimensional over
$k$, so it is Artinian. An element with $a\ne0$ is a unit, since its nilpotent
part lies in $\mathfrak m$ and $\mathfrak m^2=0$. Thus the nonunits are exactly
$\mathfrak m$, so $R$ is local.
:::

<1>2. The ring $R$ is Cohen--Macaulay.
::: proof
An Artinian local ring has Krull dimension $0$. Its depth is also $0$ unless it
is the zero ring, because a regular sequence in the maximal ideal cannot have
positive length when every element of the maximal ideal is nilpotent and hence
a zerodivisor. Therefore
\[
\operatorname{depth}R=0=\dim R,
\]
so $R$ is Cohen--Macaulay.
:::

<1>3. The socle of $R$ is
\[
\operatorname{Soc}(R)=0:_R\mathfrak m=\mathfrak m.
\]
::: proof
Since $\mathfrak m^2=0$, we have $\mathfrak m\subseteq0:_R\mathfrak m$.
Conversely, if $r=a+bx+cy$ has $a\ne0$, then
\[
xr=ax\ne0,
\]
so $r\notin0:_R\mathfrak m$. Hence the socle is exactly $\mathfrak m$.
:::

<1>4. The socle has $k$-dimension $2$.
::: proof
The classes of $x$ and $y$ form a $k$-basis of $\mathfrak m$.
:::

<1>5. The ring $R$ is not Gorenstein.
::: proof
For an Artinian local ring with residue field $k$, the Artinian Gorenstein
criterion says that the ring is Gorenstein if and only if its socle is
one-dimensional over $k$. By <1>4 the socle of $R$ has dimension $2$, so $R$
is not Gorenstein.
:::
:::
