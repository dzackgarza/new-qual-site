---
schema: qual/card@1
id: P-HCAO41
kind: problem
title: A Noetherian valuation ring which is not a field is a discrete valuation ring
classification:
  areas:
  - algebra
  topics:
  - Valuation Rings
  - Noetherian Rings
  - Discrete Valuation Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard commutative-algebra oral extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $A$ be a Noetherian valuation ring which is not a field.
Show that $A$ is a discrete valuation ring.
:::


::: solution
Let \(\mathfrak m\) be the maximal ideal of the valuation ring \(A\). Since \(A\)
is not a field, \(\mathfrak m
e0\).

<1>1. The maximal ideal \(\mathfrak m\) is principal.
::: proof
Because \(A\) is Noetherian, write
\[
\mathfrak m=(a_1,\ldots,a_r).
\]
Ideals in a valuation ring are totally ordered by inclusion, so among the
principal ideals \((a_i)\) there is a largest one, say \((a_j)\). Then every
\(a_i\in(a_j)\), hence
\[
\mathfrak m=(a_j).
\]
Set \(\pi=a_j\).
:::

<1>2. Every nonzero ideal of \(A\) is a power of \(\mathfrak m=(\pi)\).
::: proof
Let \(0
e I\subseteq A\). Since \(A\) is Noetherian, \(I\) is finitely
generated, hence principal by the same total-order argument: \(I=(x)\).
If \(x\) is a unit then \(I=A=\mathfrak m^0\). Otherwise \(x\in\mathfrak m\),
so \(x=\pi x_1\). If \(x_1\) is not a unit, repeat.

This process must terminate. Otherwise \(x\in(\pi^n)\) for every \(n\), so
\[
(x)\subseteq\bigcap_{n\ge1}(\pi^n).
\]
But in the Noetherian local domain \(A\), Krull's intersection theorem gives
\[
\bigcap_{n\ge1}\mathfrak m^n=0,
\]
contradicting \(x\ne0\). Hence \(x=u\pi^n\) for a unit \(u\), and therefore
\[
I=(\pi^n)=\mathfrak m^n.
\]
:::

<1>3. \(A\) is a discrete valuation ring.
::: proof
A Noetherian local domain that is not a field is a DVR precisely when its
nonzero maximal ideal is principal; equivalently, every nonzero ideal is a
power of that maximal ideal. Both conditions were established in <1>1 and
<1>2. Thus \(A\) is a DVR with uniformizer \(\pi\).
:::
:::
