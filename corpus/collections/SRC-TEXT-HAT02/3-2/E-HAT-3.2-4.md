---
schema: qual/card@1
id: E-HAT-3.2-4
kind: problem
title: Fixed points of self-maps of $\CP^n$
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 4. The printed bracketed pointer "[See Exercise 3 in §2.C for an example of a map without fixed points in this exceptional case.]" was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the Lefschetz computation: $f^*$ is a ring map, so $f^*(\alpha^j)=d^j\alpha^j$, the odd
    cohomology vanishes, and $L(f)=1+d+\cdots+d^n$. For even $n$ this is $(r^{n+1}+1)/(r+1)>0$ when
    $d=-r<0$ and positive for $d\ge0$; for odd $n$ it factors as $(1-r)(1+r^2+\cdots+r^{n-1})$,
    vanishing exactly at $d=-1$.
---

::: {.problem}
Apply the Lefschetz fixed point theorem to show that every map $f: \CP^n \to \CP^n$ has a fixed point if $n$ is even, using the fact that $f^*: H^*(\CP^n; \ZZ) \to H^*(\CP^n; \ZZ)$ is a ring homomorphism.
When $n$ is odd show there is a fixed point unless $f^*(\alpha) = -\alpha$, for $\alpha$ a generator of $H^2(\CP^n; \ZZ)$.
[See Exercise 3 in §2.C for an example of a map without fixed points in this exceptional case.]
:::

::: {.solution}
Let $\alpha\in H^2(\CP^n;\ZZ)$ be the standard generator. Since $f^*$ is a ring map, there is an integer $d$ such that
$$
f^*(\alpha)=d\alpha,
\qquad
f^*(\alpha^j)=d^j\alpha^j.
$$
Each even-dimensional cohomology group is infinite cyclic and the odd groups vanish. Hence the Lefschetz number is
$$
L(f)=1+d+d^2+\cdots+d^n.
$$
If $n$ is even, this integer is never zero. Indeed for $d\ge0$ it is positive; for $d<0$, writing $d=-r$ with $r\ge1$, one gets
$$
1-r+r^2-\cdots+r^n=\frac{r^{n+1}+1}{r+1}>0.
$$
Thus $L(f)\ne0$, so the Lefschetz fixed point theorem gives a fixed point.

If $n$ is odd, then
$$
1+d+\cdots+d^n=0
$$
can occur only for $d=-1$: for $d\ge0$ the sum is positive, and for $d=-r<0$,
$$
1-r+r^2-\cdots-r^n=(1-r)(1+r^2+\cdots+r^{n-1}),
$$
which vanishes exactly when $r=1$. Therefore every map has a fixed point unless
$$
f^*(\alpha)=-\alpha.
$$
:::
