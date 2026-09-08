---
schema: qual/card@1
id: P-RAF16H
kind: problem
title: "Minimum distance equals maximum projection onto orthogonal complement"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 8 of the official UCSD Fall 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $H$ be a real Hilbert space and $M$ a nonempty, closed subspace of $H$.
Suppose $x_0 \in H \setminus M$.
Prove that
$$
\min\{\|x - x_0\| : x \in M\} = \max\{\langle x_0, y \rangle : y \in M^\perp,\; \|y\| = 1\}.
$$
:::

::: solution
<1>1. Decompose $x_0$ orthogonally relative to $M$.
::: proof
Since $M$ is a closed subspace of the Hilbert space $H$, the projection theorem gives unique vectors
\[
m_0\in M,
\qquad
z\in M^\perp
\]
such that
\[
x_0=m_0+z.
\]
Because $x_0\notin M$, we have $z\ne0$.
:::

<1>2. Compute the minimum distance to $M$.
::: proof
For any $x\in M$,
\[
x_0-x=(m_0-x)+z,
\]
where $m_0-x\in M$ and $z\in M^\perp$. Hence, by Pythagoras,
\[
\|x_0-x\|^2
=\|m_0-x\|^2+\|z\|^2
\ge\|z\|^2.
\]
Equality holds at $x=m_0$. Therefore
\[
\min_{x\in M}\|x-x_0\|=\|z\|.
\]
:::

<1>3. Compute the maximum over the unit sphere of $M^\perp$.
::: proof
If $y\in M^\perp$ and $\|y\|=1$, then
\[
\langle x_0,y\rangle
=\langle m_0+z,y\rangle
=\langle z,y\rangle
\le\|z\|
\]
by Cauchy--Schwarz. Taking
\[
y_0=\frac{z}{\|z\|}\in M^\perp
\]
gives $\|y_0\|=1$ and
\[
\langle x_0,y_0\rangle=\|z\|.
\]
Thus
\[
\max_{\substack{y\in M^\perp\\\|y\|=1}}\langle x_0,y\rangle
=\|z\|
=\min_{x\in M}\|x-x_0\|.
\]
:::
:::
