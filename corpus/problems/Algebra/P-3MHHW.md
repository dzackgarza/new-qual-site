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

::: {.problem}
(a) Show that localizing a ring at a prime ideal produces a local ring.

(b) Show that $R$ is a local ring iff for every $x\in R$, either $x$ or $1-x$ is a unit.

(c) Show that if $R$ is a local ring then $R\setminus R^\times$ is a proper ideal that is contained in the Jacobson radical $J(R)$ (and equals it).

(d) Show that if $R\neq 0$ is a ring in which every non-unit is nilpotent then $R$ is local.

(e) Show that every prime ideal is primary.

(f) Show that every prime ideal is irreducible.
:::

::: {.solution}
All rings are commutative with identity.

::: pf

::: {.pf-step #ideal-criterion}

If $R\ne0$ and the set $\mathfrak m=R\setminus R^\times$ of nonunits is an ideal, then $R$ is local with maximal ideal $\mathfrak m$.

::: pf-proof

$\mathfrak m$ is proper since $1\notin\mathfrak m$. Every proper ideal consists of nonunits, so it is contained in $\mathfrak m$. Hence $\mathfrak m$ is the unique maximal ideal.

:::

:::

::: pf-step

(a) For $\mathfrak p\in\Spec R$, the ring $R_{\mathfrak p}$ is local with maximal ideal $\mathfrak pR_{\mathfrak p}$.

::: pf-proof

A fraction $a/s$ with $a\notin\mathfrak p$ is a unit with inverse $s/a$. A fraction $a/s$ with $a\in\mathfrak p$ is not a unit: if $(a/s)(b/t)=1$, then $u(ab-st)=0$ for some $u\notin\mathfrak p$, so $uab=ust\notin\mathfrak p$, contradicting $a\in\mathfrak p$. Hence the nonunits of $R_{\mathfrak p}$ form the ideal $\mathfrak pR_{\mathfrak p}$. Also $R_{\mathfrak p}\ne0$, since $1/1$ is a unit. Step [](#ideal-criterion){.pf-ref} applies.

:::

:::

::: {.pf-step #units}

(b) $R$ is local if and only if, for every $x\in R$, $x$ or $1-x$ is a unit.

::: pf-proof

::: {.pf-step #units-forward}

If $(R,\mathfrak m)$ is local, then $x$ or $1-x$ is a unit.

::: pf-proof

Every nonunit lies in a maximal ideal, hence in $\mathfrak m$. If $x$ and $1-x$ were both nonunits, then $1=x+(1-x)\in\mathfrak m$, which is impossible.

:::

:::

::: pf-step

If, for every $x$, $x$ or $1-x$ is a unit, then $R$ is local.

::: pf-proof

$R\ne0$, since in the zero ring $0$ and $1-0$ are nonunits. Let $\mathfrak m$ be the set of nonunits. If $x\in\mathfrak m$ and $r\in R$, then $rx\in\mathfrak m$, since a multiple of a nonunit is a nonunit. Let $x,y\in\mathfrak m$ and suppose $u=x+y$ is a unit. Then $1=u^{-1}x+u^{-1}y$. Since $u^{-1}x$ is a nonunit, the hypothesis makes $u^{-1}y=1-u^{-1}x$ a unit, so $y$ is a unit, a contradiction. Hence $\mathfrak m$ is an ideal, and step [](#ideal-criterion){.pf-ref} applies.

:::

:::

:::

:::

::: pf-step

(c) If $(R,\mathfrak m)$ is local, then $R\setminus R^\times=\mathfrak m=J(R)$, a proper ideal.

::: pf-proof

Every nonunit lies in some maximal ideal, which is $\mathfrak m$, and no element of $\mathfrak m$ is a unit; so $R\setminus R^\times=\mathfrak m$. The Jacobson radical is the intersection of the maximal ideals, which is $\mathfrak m$.

:::

:::

::: pf-step

(d) If $R\ne0$ and every nonunit is nilpotent, then $R$ is local.

::: pf-proof

A nilpotent element is not a unit, so the set of nonunits equals the nilradical, which is an ideal. Apply step [](#ideal-criterion){.pf-ref}.

:::

:::

::: pf-step

(e) Every prime ideal is primary.

::: pf-proof

Let $\mathfrak p$ be prime and $xy\in\mathfrak p$ with $x\notin\mathfrak p$. Then $y\in\mathfrak p$, so $y^1\in\mathfrak p$; and $\mathfrak p$ is proper.

:::

:::

::: pf-step

(f) Every prime ideal is irreducible.

::: pf-proof

Let $\mathfrak p=I\cap J$ with $I,J$ ideals, and suppose both strictly contain $\mathfrak p$. Choose $a\in I\setminus\mathfrak p$ and $b\in J\setminus\mathfrak p$. Then $ab\in I\cap J=\mathfrak p$, contradicting primality. Hence $I=\mathfrak p$ or $J=\mathfrak p$.

:::

:::

:::

:::
