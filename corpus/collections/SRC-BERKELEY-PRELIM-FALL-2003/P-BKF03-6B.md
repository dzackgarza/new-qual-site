---
schema: qual/card@1
id: P-BKF03-6B
kind: problem
title: Berkeley Fall 2003 prelim problem 6B
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
\n\n::: {.solution}\n<1>1. The hypothesis implies\n\[\n\int_\Gamma q(z)f(z)\,dz=0\n\]\nfor every polynomial $q\in\mathbb C[z]$ and every closed contour $\Gamma$ avoiding the poles of $f$.\n::: {.proof}\nFix a polynomial $p$.
Applying the hypothesis first to $p+1$ and then to $p$, and subtracting, gives\n\[\n0=\int_\Gamma\bigl((p+1)^2-p^2\bigr)f(z)\,dz\n=\int_\Gamma(2p+1)f(z)\,dz.\n\]\nNow let $q$ be arbitrary and choose\n\[\np=\frac{q-1}{2},\n\]\nwhich is again a polynomial over $\mathbb C$.
Then $2p+1=q$, giving the desired identity.\n:::\n\n<1>2. The function $f$ has no poles.\n::: {.proof}\nSuppose, for contradiction, that $f$ has a pole of order $m\ge1$ at $a$.
Its Laurent expansion near $a$ has the form\n\[\nf(z)=\frac{c_{-m}}{(z-a)^m}+\frac{c_{-(m-1)}}{(z-a)^{m-1}}+\cdots,\n\qquad c_{-m}\ne0.\n\]\nTake the polynomial\n\[\nq(z)=(z-a)^{m-1}.\n\]\nThen $q(z)f(z)$ has a simple pole at $a$ with residue $c_{-m}\ne0$.
Choose a sufficiently small positively oriented circle $\Gamma$ about $a$ containing no other pole of $f$.
By the residue theorem,\n\[\n\int_\Gamma q(z)f(z)\,dz=2\pi i\,c_{-m}\ne0,\n\]\ncontradicting <1>1. Thus $f$ has no poles.\n:::\n\n<1>3. Therefore $f$ is entire.\n::: {.proof}\nA meromorphic function on $\mathbb C$ is holomorphic away from its poles.
By <1>2 there are no poles, so $f$ is holomorphic on all of $\mathbb C$.\n:::\n:::\n
