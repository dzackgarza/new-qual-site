---
schema: qual/card@1
id: E-SS10.EX-8
kind: problem
title: "SS 10.8: Parametrization of Pythagorean triples"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
8. Consider Pythagorean triples $( a , b , c )$ with $a ^ { 2 } + b ^ { 2 } = c ^ { 2 }$ , and with $a , b , c \in \mathbb { Z }$ Suppose moreover that a and b have no common factors.

(a) Show that either a or b must be odd, and the other even.

(b) Show in this case (assuming a is odd and b even) that there are integers m, n so that $a = { \dot { m } } ^ { 2 } - n ^ { 2 } , \ b = 2 m n ,$ and $c = m ^ { 2 } + n ^ { 2 }$ . [Hint: Note that $b ^ { 2 } = ( c - a ) ( c + a )$ , and prove that $( c - a ) / 2$ and $( c + a ) / 2$ are relatively prime integers.]

(c) Conversely, show that whenever c is a sum of two-squares, then there exist integers a and b such that $a ^ { 2 } + b ^ { 2 } = c ^ { 2 }$
:::

::: solution
Assume \(\gcd(a,b)=1\) and \(a^2+b^2=c^2\).

If both \(a\) and \(b\) were odd, then
\[
a^2+b^2\equiv1+1\equiv2\pmod4,
\]
which cannot be a square modulo \(4\). They cannot both be even because they are coprime. Thus exactly one of \(a,b\) is even.

Assume \(a\) is odd and \(b\) is even. Then \(c\) is odd. Also \(\gcd(a,c)=1\): a common divisor of \(a\) and \(c\) would divide \(b^2=c^2-a^2\), hence would divide \(b\), contradicting \(\gcd(a,b)=1\). Set
\[
u=\frac{c-a}{2},
\qquad
v=\frac{c+a}{2}.
\]
These are positive integers (after changing signs if necessary), and
\[
uv=\frac{c^2-a^2}{4}=\left(\frac b2\right)^2.
\]
Moreover
\[
\gcd(u,v)=1,
\]
because a common divisor divides \(u+v=c\) and \(v-u=a\). A product of two coprime positive integers is a square only when each factor is a square, so
\[
u=n^2,
\qquad v=m^2
\]
for some integers \(m,n\). Hence
\[
a=v-u=m^2-n^2,
\qquad
b=2mn,
\qquad
c=u+v=m^2+n^2.
\]

Conversely, if \(c=m^2+n^2\), define
\[
a=m^2-n^2,
\qquad b=2mn.
\]
Then
\[
a^2+b^2
=(m^2-n^2)^2+4m^2n^2
=(m^2+n^2)^2=c^2.
\]
Thus every sum-of-two-squares value of \(c\) occurs as the hypotenuse of an integral Pythagorean triple.
:::
