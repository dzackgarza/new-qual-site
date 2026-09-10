---
schema: qual/card@1
id: P-MVETM
kind: problem
title: If every irreducible in $F[x]$ is separable then every element of $F$ is a $p$-th power
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Characteristic
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $F$ be a field of characteristic $p>0$. Suppose every irreducible polynomial in $F[x]$ is separable. Show that every $a\in F$ is a $p$-th power in $F$.
:::

::: {.solution}
Let $a\in F$. If $a=0$, take $\beta=0$. Assume $a\ne0$ and consider
\[
f(x)=x^p-a.
\]
In an algebraic closure choose its unique root $\beta$, so
\[
\beta^p=a
\qquad\text{and}\qquad
f(x)=(x-\beta)^p.
\]

The derivative is $f'(x)=0$, so $f$ is inseparable. By hypothesis no irreducible polynomial over $F$ is inseparable; therefore $f$ cannot be irreducible. Choose a monic irreducible proper factor
\[
g(x)\mid f(x),
\qquad
1\le \ell:=\deg g<p.
\]
Over the algebraic closure, every root of $g$ is the unique root $\beta$ of $f$, hence
\[
g(x)=(x-\beta)^\ell.
\]
Since $g\in F[x]$, its constant coefficient gives
\[
(-\beta)^\ell\in F,
\]
so $\beta^\ell\in F$.

Because $1\le\ell<p$ and $p$ is prime,
\[
\gcd(\ell,p)=1.
\]
Choose integers $u,v$ with
\[
u\ell+vp=1.
\]
Since $\beta\ne0$,
\[
\beta
=\beta^{u\ell+vp}
=(\beta^\ell)^u(\beta^p)^v
\in F.
\]
Therefore
\[
a=\beta^p
\]
with $\beta\in F$. Thus Frobenius $x\mapsto x^p$ is surjective on $F$.
:::
