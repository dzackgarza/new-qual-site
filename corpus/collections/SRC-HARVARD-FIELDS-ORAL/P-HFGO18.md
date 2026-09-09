---
schema: qual/card@1
id: P-HFGO18
kind: problem
title: A real polynomial of odd degree has a real root
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Prove that every real polynomial of odd degree has a real root.
:::

::: solution
Let
\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0
\]
with $a_n\ne0$ and $n$ odd.

<1>1. The values of $f(x)$ have opposite signs for sufficiently large positive
and negative $x$.
::: proof
Divide by the leading term:
\[
\frac{f(x)}{a_nx^n}
=1+\frac{a_{n-1}}{a_nx}+\cdots+\frac{a_0}{a_nx^n}
\longrightarrow1
\]
as $|x|\to\infty$. Hence for sufficiently large $R>0$, $f(R)$ has the sign of
$a_n$, while, because $n$ is odd, $f(-R)$ has the opposite sign.
:::

<1>2. The polynomial $f$ has a real zero.
::: proof
Polynomials are continuous. By <1>1, for sufficiently large $R$ the numbers
$f(-R)$ and $f(R)$ have opposite signs. The intermediate value theorem therefore
gives some $c\in[-R,R]$ such that
\[
f(c)=0.
\]
:::
:::
