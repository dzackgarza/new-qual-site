---
schema: qual/card@1
id: P-JHUSP07ANH
kind: problem
title: "A function and its Fourier transform cannot both have compact support"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 8 of the JHU Analysis Qualifying Exam, Spring 2007, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f\in L^1(\mathbb R)$ and define
\[
\widehat f(z)=\int_{\mathbb R}e^{-ixz}f(x)\,dx.
\]
Show that, unless $f=0$ almost everywhere, the functions $f$ and $\widehat f$ cannot both have compact support.
:::

::: {.solution}
Assume that $f$ has compact support, say
\[
\operatorname{supp}f\subset[-R,R].
\]
Then for every complex number $z$ the integral
\[
F(z)=\int_{-R}^R e^{-ixz}f(x)\,dx
\]
is absolutely convergent. Moreover, for every integer $k\ge0$,
\[
F^{(k)}(z)=\int_{-R}^R(-ix)^k e^{-ixz}f(x)\,dx,
\]
with differentiation justified by dominated convergence on compact subsets of $\mathbb C$. Hence $F$ is entire, and on the real axis it agrees with the Fourier transform $\widehat f$.

Now suppose also that $\widehat f$ has compact support. Then there exists $M>0$ such that
\[
F(\xi)=\widehat f(\xi)=0
\qquad\text{for all real }|\xi|>M.
\]
Thus the entire function $F$ vanishes on the nonempty open interval $(M,\infty)$ of the real axis. By the identity theorem for holomorphic functions,
\[
F\equiv0\quad\text{on }\mathbb C.
\]
Therefore $\widehat f=0$ on $\mathbb R$. By uniqueness of the Fourier transform on $L^1(\mathbb R)$,
\[
f=0\quad\text{almost everywhere}.
\]
Consequently, a nonzero $L^1$ function and its Fourier transform cannot both have compact support.
:::
