---
schema: qual/card@1
id: P-5SC3V
kind: problem
title: A PID that is not Euclidean
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Euclidean Domains
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Do you know a Principal Ideal Domain (PID) that is not a Euclidean Domain?
:::

::: solution
A standard example is
\[
R=\mathbb Z\left[\frac{1+\sqrt{-19}}2\right],
\]
the ring of integers of $\mathbb Q(\sqrt{-19})$.

First, $R$ is a PID. The discriminant is $-19$, so Minkowski's bound for ideal classes in this imaginary quadratic field is
\[
\frac{2}{\pi}\sqrt{19}<3.
\]
Hence every ideal class contains an integral ideal of norm $1$ or $2$. But $2$ is inert: the defining polynomial
\[
x^2-x+5\equiv x^2+x+1\pmod2
\]
has no root in $\mathbb F_2$. Thus there is no ideal of norm $2$. Every ideal class therefore contains an ideal of norm $1$, hence the unit ideal; the class group is trivial, so $R$ is a PID.

It is not Euclidean for any Euclidean function. Indeed, in any Euclidean domain that is not a field, choose a nonzero nonunit $b$ of minimal Euclidean value. For every $a$, Euclidean division gives
\[
a=qb+r,\qquad r=0\text{ or }\delta(r)<\delta(b).
\]
By minimality of $\delta(b)$ among nonzero nonunits, every nonzero remainder $r$ must be a unit. Hence every residue class modulo $(b)$ is represented by $0$ or by a unit.

For the present ring, the norm is
\[
N(a+b\theta)=a^2+ab+5b^2,
\qquad \theta=\frac{1+\sqrt{-19}}2.
\]
The only units are $\pm1$. Therefore such a quotient $R/(b)$ would have at most three residue classes, so $|R/(b)|=|N(b)|$ would have to be $2$ or $3$. But
\[
a^2+ab+5b^2
=\left(a+\frac b2\right)^2+\frac{19}{4}b^2
\]
never equals $2$ or $3$ for integers $a,b$. This contradiction shows that $R$ admits no Euclidean function.
:::
