---
schema: qual/card@1
id: P-BKF03-6B
kind: problem
title: Meromorphic $f$ with $\int_\Gamma p^2f\,dz=0$ for all polynomials $p$ is entire
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 6B of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified polarization from square-polynomial weights to arbitrary polynomial weights and the residue contradiction for any pole.
---

::: {.problem}
Let $f ( z )$ be a meromorphic function on the complex plane.
Suppose that for every polynomial $p ( z ) \in \mathbb { C } [ z ]$ and every closed contour Γ avoiding the poles of $f ,$ we have

$$
\int _ { \Gamma } p ( z ) ^ { 2 } f ( z ) d z = 0 .
$$

Prove that f (z) is entire.
:::


::: {.solution}
<1>1. The hypothesis implies
\[
\int_\Gamma q(z)f(z)\,dz=0
\]
for every polynomial $q\in\mathbb C[z]$ and every closed contour $\Gamma$ avoiding the poles of $f$.
::: {.proof}
Fix a polynomial $p$.
Applying the hypothesis first to $p+1$ and then to $p$, and subtracting, gives
\[
0=\int_\Gamma\bigl((p+1)^2-p^2\bigr)f(z)\,dz
=\int_\Gamma(2p+1)f(z)\,dz.
\]
Now let $q$ be arbitrary and choose
\[
p=\frac{q-1}{2},
\]
which is again a polynomial over $\mathbb C$.
Then $2p+1=q$, giving the desired identity.
:::

<1>2. The function $f$ has no poles.
::: {.proof}
Suppose, for contradiction, that $f$ has a pole of order $m\ge1$ at $a$.
Its Laurent expansion near $a$ has the form
\[
f(z)=\frac{c_{-m}}{(z-a)^m}+\frac{c_{-(m-1)}}{(z-a)^{m-1}}+\cdots,
\qquad c_{-m}\ne0.
\]
Take the polynomial
\[
q(z)=(z-a)^{m-1}.
\]
Then $q(z)f(z)$ has a simple pole at $a$ with residue $c_{-m}\ne0$.
Choose a sufficiently small positively oriented circle $\Gamma$ about $a$ containing no other pole of $f$.
By the residue theorem,
\[
\int_\Gamma q(z)f(z)\,dz=2\pi i\,c_{-m}\ne0,
\]
contradicting <1>1. Thus $f$ has no poles.
:::

<1>3. Therefore $f$ is entire.
::: {.proof}
A meromorphic function on $\mathbb C$ is holomorphic away from its poles.
By <1>2 there are no poles, so $f$ is holomorphic on all of $\mathbb C$.
:::
:::

