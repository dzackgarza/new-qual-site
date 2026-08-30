---
schema: qual/card@1
id: P-JHUFA02CAH
kind: problem
title: "Entire functions bounded by the square of the modulus"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

3. (20 points) Determine all entire functions f for which $| f ( z ) | \leq | z | ^ { 2 }$ for all $z \in \mathbb { C }$

::: solution
**Goal:** Find all entire $f$ with $|f(z)|\le |z|^2$ for all $z\in\CC$.

<1> Expand at the origin and truncate high terms.
    *Proof:*
    <2>1. Write $f(z)=\sum_{n=0}^\infty a_n z^n$.
    <2>2. By Cauchy estimates, for any $R>0$,
        $$
        |a_n| \le \frac{\max_{|z|=R}|f(z)|}{R^n}\le \frac{R^2}{R^n}=R^{2-n}.
        $$
    <2>3. For $n\ge3$, let $R\to\infty$, then $|a_n|=0$.
    <2>4. So $f(z)=a_0+a_1z+a_2z^2$.

<1> Force the linear terms to vanish.
    *Proof:*
    <2>1. $|f(0)|\le0$ gives $a_0=0$.
    <2>2. Then
        $$
        f(z)=z(a_1+a_2z).
        $$
    <2>3. Dividing by $|z|$, $|a_1+a_2z|\le |z|$ for $z\ne0$.
    <2>4. Letting $z\to0$ gives $a_1=0$.

<1> Identify the remaining coefficient.
    *Proof:*
    <2>1. Now $f(z)=a_2z^2$.
    <2>2. The bound becomes $|a_2||z|^2\le|z|^2$, so $|a_2|\le1$.

<1> Therefore $f(z)=c z^2$ with $|c|\le1$ and this family is valid.

Authored by **Codex 5.3 Spark Extra High**.
:::
