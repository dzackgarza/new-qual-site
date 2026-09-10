---
schema: qual/card@1
id: P-ALGS11G
kind: problem
title: Torsion, free, and torsionfree modules over an integral domain
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Integral Domains
relations: []
review: draft

audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 7 of the official UCSD Spring 2011 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Supplied explicit counterexamples for (i) and (iii) and a basis argument for (ii).
---

::: problem
Let $R$ be an integral domain.
Prove or give an example to disprove (with justification):

(i) If $M$ is a torsion $R$-module, then $\mathrm{Ann}_R(M) \neq 0$.

(ii) If $M$ is a free $R$-module, then $M$ is torsionfree.

(iii) If $M$ is a torsionfree $R$-module, then $M$ is free.
:::


::: {.solution}
<1>1. Statement (i) is false.
::: {.proof}
Take $R=\mathbb Z$ and
\[
M=\bigoplus_{n\ge2}\mathbb Z/n\mathbb Z.
\]
Every element of $M$ has only finitely many nonzero coordinates, so it is killed by the least common multiple of the corresponding finitely many integers $n$.
Thus $M$ is a torsion $\mathbb Z$-module.

However, if $0\ne a\in\mathbb Z$, choose $n>|a|$ with $n\nmid a$.
The element whose only nonzero coordinate is $1\in\mathbb Z/n\mathbb Z$ is not killed by $a$.
Hence no nonzero integer annihilates all of $M$, so
\[
\operatorname{Ann}_{\mathbb Z}(M)=0.
\]
:::

<1>2. Statement (ii) is true.
::: {.proof}
Let $M$ be a free $R$-module with basis $(e_i)_{i\in I}$.
Suppose $0\ne r\in R$ and $rm=0$.
Write
\[
m=\sum_{i\in I}a_i e_i
\]
with only finitely many nonzero $a_i$.
Then
\[
0=rm=\sum_i (ra_i)e_i.
\]
Linear independence of the basis gives $ra_i=0$ for every $i$.
Since $R$ is an integral domain and $r\ne0$, each $a_i=0$.
Thus $m=0$, so $M$ is torsionfree.
:::

<1>3. Statement (iii) is false.
::: {.proof}
Take $R=\mathbb Z$ and $M=\mathbb Q$.
Since $\mathbb Z$ is a domain, if $0\ne n\in\mathbb Z$ and $nq=0$ in $\mathbb Q$, then $q=0$; hence $\mathbb Q$ is torsionfree as a $\mathbb Z$-module.

It is not free.
Indeed, $\mathbb Q$ is divisible: for every $q\in\mathbb Q$ and every integer $n\ne0$, there is $q/n\in\mathbb Q$ with $n(q/n)=q$.
A nonzero free abelian group is not divisible: if $(e_i)$ is a basis and $e_j$ is one basis element, there is no element $x$ with $2x=e_j$, since comparing the coefficient of $e_j$ would require an integer coefficient $1/2$.
Therefore $\mathbb Q$ is not a free $\mathbb Z$-module.
:::

<1>4. Hence the answers are
\[
\boxed{\text{(i) false,}\qquad\text{(ii) true,}\qquad\text{(iii) false.}}
\]
:::

