---
schema: qual/card@1
id: P-ALGF07E
kind: problem
title: "Conditions for f(x^p) to be a p-th power in characteristic p"
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
  date: 2026-09-07
  note: Checked against Question 5 of the official UCSD Algebra Qualifying Examination, Fall 2007; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified that f(x^p) is a p-th power exactly when every coefficient of f lies in the image F^p of Frobenius, with necessity obtained by coefficient comparison after the freshman's-dream identity.
---

::: {.problem}
Let $F$ be a field of characteristic $p$ and let $f \in F[x]$ be a polynomial, $f(x) = \sum_i f_i x^i$.
Give necessary and sufficient conditions on the $\{f_i\}$ for $f(x^p)$ itself to be a $p$-th power, i.e.\ $f(x^p) = g(x)^p$ for some $g \in F[x]$.
In particular, prove that your condition is necessary.
:::

::: {.solution}
The necessary and sufficient condition is
\[
f_i\in F^p:=\{a^p:a\in F\}
\qquad\text{for every }i.
\]
Equivalently, every coefficient of $f$ must have a $p$-th root in $F$.

<1>1. In characteristic $p$, taking the $p$-th power of a polynomial applies Frobenius to its coefficients and multiplies every exponent by $p$.
::: {.proof}
Let
\[
g(x)=\sum_j g_jx^j\in F[x].
\]
Since the binomial coefficients
\[
\binom pk
\]
are divisible by $p$ for $0<k<p$, one has
\[
(a+b)^p=a^p+b^p
\]
in every ring of characteristic $p$.
Applying this repeatedly to the finite sum defining $g$ gives
\[
g(x)^p
=\sum_j(g_jx^j)^p
=\sum_j g_j^p x^{jp}.
\]
:::

<1>2. If every $f_i$ is a $p$-th power in $F$, then $f(x^p)$ is a $p$-th power in $F[x]$.
::: {.proof}
For each $i$, choose $g_i\in F$ such that
\[
g_i^p=f_i.
\]
Set
\[
g(x):=\sum_i g_i x^i.
\]
By <1>1,
\[
g(x)^p
=\sum_i g_i^p x^{ip}
=\sum_i f_i x^{ip}
=f(x^p).
\]
Thus the condition is sufficient.
:::

<1>3. If $f(x^p)=g(x)^p$ for some $g\in F[x]$, then every $f_i$ is a $p$-th power in $F$.
::: {.proof}
Write
\[
g(x)=\sum_j g_jx^j.
\]
By <1>1,
\[
g(x)^p=\sum_j g_j^p x^{jp}.
\]
On the other hand,
\[
f(x^p)=\sum_i f_i x^{ip}.
\]
Equality of polynomials implies equality of the coefficient of $x^{ip}$ for every $i$, hence
\[
f_i=g_i^p.
\]
Therefore
\[
f_i\in F^p
\]
for every $i$.
This proves necessity and completes the equivalence.
:::
:::
