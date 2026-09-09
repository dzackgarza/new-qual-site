---
schema: qual/card@1
id: P-HCAO49
kind: problem
title: The $p$-adic integers form a discrete valuation ring
classification:
  areas:
  - algebra
  topics:
  - Discrete Valuation Rings
  - Valuation Rings
  - Local Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Show that the ring $\mathbb Z_p$ of $p$-adic integers is a discrete valuation ring.
:::

::: solution
Every nonzero $x\in\mathbb Z_p$ has a unique $p$-adic valuation
\[
v_p(x)=n\in\mathbb Z_{\ge0}
\]
and can be written
\[
x=p^n u
\]
with $u\in\mathbb Z_p^\times$.

<1>1. The nonunits of $\mathbb Z_p$ are exactly $p\mathbb Z_p$.
::: proof
An element is a unit precisely when its reduction modulo $p$ is nonzero,
equivalently precisely when $v_p(x)=0$. Thus the unique maximal ideal is
$(p)$.
:::

<1>2. Every nonzero ideal of $\mathbb Z_p$ is a power of $(p)$.
::: proof
Let $0\ne I\subseteq\mathbb Z_p$. The set
$\{v_p(x):0\ne x\in I\}\subseteq\mathbb Z_{\ge0}$ has a least element $n$.
Choose $x\in I$ with $v_p(x)=n$ and write $x=p^n u$ with $u$ a unit. Then
$p^n=xu^{-1}\in I$, so $(p^n)\subseteq I$. Every $y\in I$ has
$v_p(y)\ge n$, hence $y\in(p^n)$. Thus $I=(p^n)$.
:::

<1>3. Hence $\mathbb Z_p$ is a DVR with uniformizer $p$.
::: proof
It is a domain, is local with nonzero principal maximal ideal $(p)$, and every
nonzero ideal is a power of that maximal ideal. This is the ideal-theoretic
characterization of a discrete valuation ring.
:::
:::
