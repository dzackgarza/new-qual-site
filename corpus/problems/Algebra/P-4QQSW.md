---
schema: qual/card@1
id: P-4QQSW
kind: problem
title: A PID with a unique prime ideal
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Prime Ideals
  - Local Rings
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
Give an example of a Principal Ideal Domain (PID) with a unique non-zero prime ideal.
Prove that it is a PID and classify all of its ideals.
:::

::: solution
Fix a prime integer $p$ and let
\[
R=\mathbb Z_{(p)}=\left\{\frac ab\in\mathbb Q:p\nmid b\right\}.
\]
Every nonzero $x\in R$ has a unique form
\[
x=p^n u,
\]
with $n\ge0$ and $u\in R^\times$. Indeed, factor the numerator by its $p$-adic valuation; every fraction whose numerator and denominator are both prime to $p$ is a unit.

Let $0\ne I\trianglelefteq R$. The set
\[
\{v_p(x):0\ne x\in I\}\subseteq\mathbb N
\]
has a minimum $n$. Choose $x=p^n u\in I$ with $u$ a unit. Then $p^n=xu^{-1}\in I$, so $(p^n)\subseteq I$. By minimality of $n$, every nonzero $y\in I$ has valuation at least $n$, hence $y\in(p^n)$. Therefore
\[
I=(p^n).
\]
Together with the zero ideal, this gives the complete ideal list
\[
(0),\quad R=(1),\quad (p),\quad(p^2),\quad(p^3),\ldots.
\]
Thus $R$ is a PID.

Because $R$ is a domain, $(0)$ is prime. The ideal $(p)$ is maximal since
\[
R/(p)\cong\mathbb F_p.
\]
For $n\ge2$, $(p^n)$ is not prime because
\[
p\cdot p^{n-1}\in(p^n),
\qquad p,p^{n-1}\notin(p^n).
\]
Hence $(p)$ is the unique nonzero prime ideal of $R$.
:::
