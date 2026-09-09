---
schema: qual/card@1
id: P-3MHHW
kind: problem
title: Local rings via localization and units; primes are primary and irreducible
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Localization
  - Prime Ideals
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
- Show that localizing a ring at a prime ideal produces a local ring.

- Show that $R$ is a local ring iff for every $x\in R$, either $x$ or $1-x$ is a unit.

- Show that if $R$ is a local ring then $R\setminus R^\times$ is a proper ideal that is contained in the Jacobson radical $J(R)$ (and equals it).

- Show that if $R\neq 0$ is a ring in which every non-unit is nilpotent then $R$ is local.

- Show that every prime ideal is primary.

- Show that every prime ideal is irreducible.
:::

::: solution
Let all rings here be commutative with identity.

1. If $\mathfrak p\in\operatorname{Spec}R$, then in $R_{\mathfrak p}$ every fraction $a/s$ with $a\notin\mathfrak p$ is a unit, with inverse $s/a$. Thus the nonunits are exactly
\[
\mathfrak pR_{\mathfrak p},
\]
so this is the unique maximal ideal and $R_{\mathfrak p}$ is local.

2. Suppose first that $(R,\mathfrak m)$ is local. If both $x$ and $1-x$ were nonunits, both would lie in $\mathfrak m$, forcing $1\in\mathfrak m$, impossible. Hence one of $x,1-x$ is a unit.

Conversely, assume that for every $x$, one of $x,1-x$ is a unit. Let $\mathfrak m$ be the set of nonunits. If $x\in\mathfrak m$ and $r\in R$, then $rx$ is a nonunit. If $x,y\in\mathfrak m$ but $u=x+y$ were a unit, then
\[
1=u^{-1}x+u^{-1}y.
\]
Since $u^{-1}x$ is a nonunit, the hypothesis makes $u^{-1}y=1-u^{-1}x$ a unit, hence $y$ a unit, contradiction. Thus $\mathfrak m$ is an ideal. Every proper ideal consists of nonunits, so every proper ideal is contained in $\mathfrak m$; hence $\mathfrak m$ is the unique maximal ideal.

3. Therefore, in a local ring,
\[
R\setminus R^\times=\mathfrak m=J(R).
\]

4. Suppose $R\ne0$ and every nonunit is nilpotent. A nilpotent element cannot be a unit, so the set of nonunits is exactly the nilradical $\sqrt{(0)}$, which is an ideal. By part 2, $R$ is local.

5. If $\mathfrak p$ is prime and $xy\in\mathfrak p$ with $x\notin\mathfrak p$, then $y\in\mathfrak p$, so $\mathfrak p$ is primary (with exponent $1$).

6. If $\mathfrak p=I\cap J$ and both $I,J$ strictly contain $\mathfrak p$, choose $a\in I\setminus\mathfrak p$ and $b\in J\setminus\mathfrak p$. Then $ab\in IJ\subseteq I\cap J=\mathfrak p$, contradicting primality. Hence $I=\mathfrak p$ or $J=\mathfrak p$, so every prime ideal is irreducible.
:::
