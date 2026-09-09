---
schema: qual/card@1
id: P-HCAO51
kind: problem
title: Maximal ideals under an integral extension
classification:
  areas:
  - algebra
  topics:
  - Integral Extensions
  - Prime Ideals
  - Maximal Ideals
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
Let $A\subseteq B$ be rings, with $B$ integral over $A$.
Let $\mathfrak q$ be a prime ideal of $B$, and put $\mathfrak p=\mathfrak q\cap A$.
Show that $\mathfrak q$ is maximal in $B$ if and only if $\mathfrak p$ is maximal in $A$.
:::

::: solution
Passing to quotients, $B/\mathfrak q$ is integral over
$A/\mathfrak p$, and both are integral domains. Thus it suffices to prove:
if $D\subseteq E$ is an integral extension of domains, then $E$ is a field if
and only if $D$ is a field.

<1>1. If $D$ is a field, then $E$ is a field.
::: proof
Let $0\ne y\in E$. Since $y$ is integral over $D$, choose a monic equation of
least degree
\[
y^n+a_{n-1}y^{n-1}+\cdots+a_0=0.
\]
Minimality forces $a_0\ne0$. Rearranging gives
\[
y^{-1}=-a_0^{-1}(y^{n-1}+a_{n-1}y^{n-2}+\cdots+a_1)\in E.
\]
Thus every nonzero element of $E$ is invertible.
:::

<1>2. If $E$ is a field, then $D$ is a field.
::: proof
For $0\ne x\in D$, its inverse $x^{-1}$ lies in $E$ and is integral over $D$.
A monic equation for $x^{-1}$, multiplied by a suitable power of $x$, expresses
$x^{-1}$ as an element of $D$. Hence every nonzero $x\in D$ is a unit.
:::

<1>3. Therefore $\mathfrak q$ is maximal if and only if $\mathfrak p$ is
maximal.
::: proof
A prime ideal is maximal exactly when its quotient domain is a field. Apply
<1>1--<1>2 to $A/\mathfrak p\subseteq B/\mathfrak q$.
:::
:::
