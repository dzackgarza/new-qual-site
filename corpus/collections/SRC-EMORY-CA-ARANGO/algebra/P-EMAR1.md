---
schema: qual/card@1
id: P-EMAR1
kind: problem
title: "Power series ring is Euclidean domain"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
An integral domain $R$ is a Euclidean domain if there is a function $N : R \to \{n \in \mathbf{Z} \mid n \geq 0\}$ such that $N(0) = 0$ and for each $a, b \in R$ with $b \neq 0$, there exist elements $q, r \in R$ with $a = qb + r$ and $r = 0$ or $N(r) < N(b)$.

(a) Prove that the ring $F[[x]]$ of power series over a field $F$ is a Euclidean domain.

(b) Prove that every Euclidean domain is a PID.
:::

::: {.solution}
**Part (a).**

<1>1. Define $N: F[[x]] \to \ZZ_{\ge 0}$ by $N(0) = 0$ and $N(f) = \operatorname{ord}(f)$ (the order of vanishing, i.e. the smallest power of $x$ with nonzero coefficient) for $f \neq 0$.
Proof: definition.

<1>2. For $a, b \in F[[x]]$ with $b \neq 0$, write $b = x^m u$ where $u$ is a unit (a power series with nonzero constant term).
Proof: $b = x^m u$ with $u(0) \neq 0$, so $u$ is a unit in $F[[x]]$.

<1>3. If $N(a) \ge N(b) = m$, then $a = x^m v$ for some $v \in F[[x]]$, so $a = (v u^{-1}) b + 0$, with $q = v u^{-1}$ and $r = 0$.
Proof: $a = x^m v = (v u^{-1})(x^m u) = q b$.

<1>4. If $N(a) < N(b) = m$, then $a = 0 \cdot b + a$, with $q = 0$ and $r = a$, and $N(r) = N(a) < N(b)$.
Proof: division with $q = 0$.

<1>5. Hence $F[[x]]$ is a Euclidean domain.
Proof: <1>2–<1>4.

**Part (b).**

<1>1. Let $I$ be a nonzero ideal of a Euclidean domain $R$.
Proof: take an arbitrary ideal.

<1>2. Choose $b \in I \setminus \{0\}$ with $N(b)$ minimal.
Proof: the set $\{N(a) : a \in I, a \neq 0\}$ has a minimum (well-ordering of $\ZZ_{\ge 0}$).

<1>3. $I = (b)$.
<2>1. For any $a \in I$, write $a = qb + r$ with $r = 0$ or $N(r) < N(b)$.
Proof: Euclidean division.
<2>2. $r = a - qb \in I$.
Proof: $a, b \in I$.
<2>3. Hence $r = 0$ (otherwise $N(r) < N(b)$ contradicts the minimality of $N(b)$).
Proof: <2>2 and <1>2.
<2>4. Therefore $a = qb \in (b)$.
Proof: <2>3.

<1>4. Hence $I = (b)$ is principal, so $R$ is a PID.
Proof: <1>3.

<1>5. Q.E.D.
Proof: <1>5 (a) and <1>4 (b).
:::
