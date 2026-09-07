---
schema: qual/card@1
id: P-ALGF14D
kind: problem
title: Irreducibility and primality of $2$ in $\mathbb{Z}[\sqrt{10}]$
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Integral Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 4 of the official UCSD Algebra Qualifying Exam, Fall 2014; all three parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the norm obstruction to factors of norm 2, the explicit failure of primality, and the resulting failure of unique factorization.
---

::: {.problem}
Let $A = \mathbb{Z}[\sqrt{10}]$.

(i) Prove that $2$ is irreducible in $A$.

(ii) Prove that $2$ is NOT prime in $A$.

(iii) Is $A$ a UFD? Justify your answer.
:::


::: {.solution}
Use the multiplicative norm
\[
N(a+b\sqrt{10})=(a+b\sqrt{10})(a-b\sqrt{10})=a^2-10b^2.
\]
For a nonzero element of \(A\), this norm is a nonzero integer.
Also, if \(u\in A\) is a unit, then
\[
N(u)=\pm1,
\]
because norms multiply and \(N(1)=1\).
Conversely, if \(N(u)=\pm1\), then
\[
u^{-1}=\frac{\bar u}{N(u)}\in A,
\]
so \(u\) is a unit.

<1>1. The element \(2\) is irreducible in \(A\).
::: {.proof}
Suppose
\[
2=\alpha\beta
\]
with nonzero \(\alpha,\beta\in A\).
Taking norms gives
\[
4=N(2)=N(\alpha)N(\beta).
\]
If neither factor were a unit, then
\[
|N(\alpha)|\ge2,
\qquad
|N(\beta)|\ge2.
\]
Since their product has absolute value \(4\), necessarily
\[
|N(\alpha)|=|N(\beta)|=2.
\]
Thus some integers \(a,b\) would satisfy
\[
a^2-10b^2=2
\qquad\text{or}\qquad
a^2-10b^2=-2.
\]
Reducing modulo \(5\) gives
\[
a^2\equiv2\pmod5
\qquad\text{or}\qquad
a^2\equiv3\pmod5.
\]
But the quadratic residues modulo \(5\) are only
\[
0,1,4.
\]
Hence no element of \(A\) has norm \(\pm2\).
Therefore every factorization of \(2\) has a unit factor, so \(2\) is irreducible.
:::

<1>2. The element \(2\) is not prime in \(A\).
::: {.proof}
We have
\[
(\sqrt{10})(\sqrt{10})=10=2\cdot5,
\]
so
\[
2\mid (\sqrt{10})^2.
\]
However,
\[
2\nmid\sqrt{10}.
\]
Indeed, if
\[
\sqrt{10}=2(a+b\sqrt{10})
\]
with \(a,b\in\mathbb Z\), comparison of coefficients of \(1\) and \(\sqrt{10}\) gives
\[
2a=0,
\qquad
2b=1,
\]
which is impossible.
Thus \(2\) divides a product without dividing either factor, so it is not prime.
:::

<1>3. The ring \(A\) is not a UFD.
::: {.proof}
In every unique factorization domain, every irreducible element is prime.
By <1>1, \(2\) is irreducible in \(A\), while by <1>2 it is not prime.
Therefore \(A\) cannot be a unique factorization domain.
:::
:::
