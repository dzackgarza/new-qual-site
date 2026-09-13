---
schema: qual/card@1
id: P-BKF14-1A
kind: problem
title: Broomstick change-making generating function and asymptotics
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1A and its solution in the vendored UC Berkeley Fall 2014 solution packet; repaired the malformed limit transcription in the prior card.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The pole-order argument isolates the unique cubic pole at z=1; nontrivial 29th roots contribute only O(n), so they do not affect the n^2 limit.
---

::: {.problem}
Let $a(n)$ be the number of ways that Harry Potter can buy a new broomstick valued at $n$ knuts using bronze knuts, silver sickles worth $29$ knuts, and gold galleons worth $17$ sickles. Find
\[
\sum_{n\ge 0} a(n)z^n
\]
and
\[
\lim_{n\to\infty}\frac{a(n)}{n^2}.
\]
:::

::: {.solution}
A purchase is determined by nonnegative integers $(r,s,g)$ satisfying
\[
r+29s+(17\cdot29)g=n.
\]
Hence
\[
\sum_{n\ge0}a(n)z^n
=\left(\sum_{r\ge0}z^r\right)
 \left(\sum_{s\ge0}z^{29s}\right)
 \left(\sum_{g\ge0}z^{493g}\right)
=\frac1{(1-z)(1-z^{29})(1-z^{493})}.
\]

Near $z=1$,
\[
1-z^{29}=29(1-z)+O((1-z)^2),
\qquad
1-z^{493}=493(1-z)+O((1-z)^2),
\]
so
\[
\frac1{(1-z)(1-z^{29})(1-z^{493})}
=\frac1{17\cdot29^2}\frac1{(1-z)^3}
+O\!\left(\frac1{(1-z)^2}\right).
\]
The coefficient of $(1-z)^{-3}$ is
\[
[z^n](1-z)^{-3}=\binom{n+2}{2}=\frac{n^2}{2}+O(n).
\]
Every pole other than $z=1$ has order at most $2$: a nontrivial common root of $z^{29}=1$ and $z^{493}=1$ is a nontrivial $29$th root of unity, where only the last two denominator factors vanish. Therefore all other poles contribute only $O(n)$ to $a(n)$.

Consequently
\[
a(n)=\frac{n^2}{2\cdot17\cdot29^2}+O(n),
\]
and thus
\[
\boxed{\displaystyle
\lim_{n\to\infty}\frac{a(n)}{n^2}
=\frac1{2\cdot17\cdot29^2}.}
\]
:::
