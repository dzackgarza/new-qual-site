---
schema: qual/card@1
id: P-ALGS09C
kind: problem
title: "Conditions for a finite field to embed in another finite field"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 3 of the official UCSD Spring 2009 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Proved necessity by viewing K as a finite-dimensional subspace of L, and sufficiency by identifying the roots of X^(p^m)-X inside F_(p^n) when m divides n.
---

::: problem
Let $p$ be a prime number and let $K$, $L$ be fields of orders $p^m$, $p^n$ respectively, where $m < n$.
When is $K$ isomorphic to a subfield of $L$?
:::

::: {.solution}
<1>1. If $K$ is isomorphic to a subfield of $L$, then $m\mid n$.
::: {.proof}
Suppose $K$ is identified with a subfield of $L$.
Then $L$ is a finite-dimensional vector space over $K$, so the tower law gives
\[
[L:\mathbb F_p]=[L:K][K:\mathbb F_p].
\]
Since
\[
[L:\mathbb F_p]=n,
\qquad
[K:\mathbb F_p]=m,
\]
we obtain
\[
n=[L:K]m.
\]
Hence $m\mid n$.
:::

<1>2. If $m\mid n$, then $K$ is isomorphic to a subfield of $L$.
::: {.proof}
Write
\[
n=rm.
\]
Every element $x\in L=\mathbb F_{p^n}$ satisfies
\[
x^{p^n}=x.
\]
Consider the set
\[
F=\{x\in L:x^{p^m}=x\}.
\]
This is a subfield of $L$: if $x,y\in F$, then in characteristic $p$,
\[
(x+y)^{p^m}=x^{p^m}+y^{p^m}=x+y,
\]
and
\[
(xy)^{p^m}=x^{p^m}y^{p^m}=xy.
\]
Also, if $x\ne0$, then
\[
(x^{-1})^{p^m}=(x^{p^m})^{-1}=x^{-1}.
\]

It remains to show that $F$ has exactly $p^m$ elements.
Since $m\mid n$,
\[
p^m-1\mid p^n-1.
\]
The multiplicative group $L^\times$ is cyclic of order $p^n-1$, so it has exactly $p^m-1$ solutions to
\[
x^{p^m-1}=1.
\]
Together with $x=0$, these are exactly the roots of
\[
x^{p^m}-x.
\]
Hence
\[
|F|=p^m.
\]
There is, up to isomorphism, a unique field with $p^m$ elements, so
\[
F\cong K.
\]
Thus $K$ is isomorphic to a subfield of $L$.
:::

<1>3. Therefore
\[
K\hookrightarrow L
\quad\Longleftrightarrow\quad
m\mid n.
\]
::: {.proof}
Combine <1>1 and <1>2.
:::
:::
