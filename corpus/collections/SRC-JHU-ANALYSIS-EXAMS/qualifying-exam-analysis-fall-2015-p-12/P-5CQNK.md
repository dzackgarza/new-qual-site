---
schema: qual/card@1
id: P-5CQNK
kind: problem
title: "Monotone and absolutely continuous functions: two true-or-false statements"
classification:
  areas:
  - real-analysis
  topics:
  - Monotone Functions
  - Absolute Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the JHU Fall 2015 Analysis Qualifying Exam appearance in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

2. Determine whether the following statements are true and false.
   If true, provide a proof.
   If false, prove a counter example.

(a) If $f ( x )$ is a increasing, continuous function on the interval $[ 0 , 1 ]$ such that $f ( 0 ) = 0$ and $f ( 1 ) = 1$ , then there exists a set $E \subset [ 0 , 1 ]$ of positive measure such that $f ^ { \prime } ( x ) > 0$

(b) If $f ( x )$ is a strictly increasing, absolutely continuous function on the interval [0, 1] with $f ( 0 ) = 0$ and $f ( 1 ) = 1$ , then the set $f ^ { - 1 } ( E ) \cap \{ x \in [ 0 , 1 ] : f ^ { \prime } ( x ) > 0 \}$ is measurable for any measurable set $E \subset [ 0 , 1 ]$

::: solution
<1>1. Part (a) is false.
::: proof
Take $f$ to be the Cantor--Lebesgue function. Then $f:[0,1]\to[0,1]$ is continuous and increasing, with
\[
f(0)=0,
\qquad
f(1)=1.
\]
However,
\[
f'(x)=0
\]
for almost every $x\in[0,1]$. Hence
\[
m\{x:f'(x)>0\}=0.
\]
So there need not exist a positive-measure set on which $f'>0$.
:::

<1>2. Reduce part (b) to the preimage of a null set.
::: proof
Now assume $f$ is strictly increasing and absolutely continuous, with $f(0)=0$ and $f(1)=1$. Then $f$ is a homeomorphism of $[0,1]$ onto itself.

Let
\[
D:=\{x\in[0,1]:f'(x)>0\},
\]
where $f'$ is defined arbitrarily on the null set where the derivative does not exist. Since derivatives of absolutely continuous functions are measurable, $D$ is measurable.

Let $E\subset[0,1]$ be Lebesgue measurable. Write
\[
E=B\cup N,
\]
where $B$ is Borel and $N$ is null. Then
\[
f^{-1}(E)\cap D
=\bigl(f^{-1}(B)\cap D\bigr)
\cup
\bigl(f^{-1}(N)\cap D\bigr).
\]
The first set is measurable because $f$ is continuous. It remains to control the second.
:::

<1>3. Show that the null part has null preimage on $D$.
::: proof
Set
\[
A:=f^{-1}(N)\cap D.
\]
Because $f$ is absolutely continuous and strictly increasing, the change-of-variables formula for monotone absolutely continuous functions gives, for every measurable $A\subset[0,1]$,
\[
m(f(A))=\int_A f'(x)\,dx.
\]
Since
\[
f(A)\subseteq N,
\]
we have $m(f(A))=0$. Therefore
\[
\int_A f'(x)\,dx=0.
\]
But $f'(x)>0$ on $A$. Hence $m(A)=0$.

Thus $f^{-1}(N)\cap D$ is measurable, and therefore so is
\[
\boxed{f^{-1}(E)\cap\{f'>0\}.}
\]
So part (b) is true.
:::
:::
