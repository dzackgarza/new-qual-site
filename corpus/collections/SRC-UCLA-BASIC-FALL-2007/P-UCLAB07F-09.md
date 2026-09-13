---
schema: qual/card@1
id: P-UCLAB07F-09
kind: problem
title: Limits and continuous dependence for a bounded scalar ODE
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Fall 2007 PDF.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Part (b) is false as printed on all of R; the solution gives a bounded smooth counterexample and records the compact-interval correction.
---

::: {.problem}
Suppose $u_n:\mathbb R\to\mathbb R$ is differentiable and satisfies
\[u_n'(x)=F(u_n(x),x),\]
where $F$ is continuous and bounded.

(a) If $u_n\to u$ uniformly, show that $u$ is differentiable and satisfies $u'(x)=F(u(x),x)$.

(b) Suppose the initial-value problem
\[u'(x)=F(u(x),x),\qquad u(x_0)=y_0\]
has a unique solution $u:\mathbb R\to\mathbb R$, and $u_n(x_0)\to y_0$. Show that $u_n$ converges uniformly to $u$.
:::

::: {.solution}
Part (a) is valid. Fix $x\in\mathbb R$. Since
\[
u_n(x)-u_n(0)=\int_0^x F(u_n(t),t)\,dt,
\]
uniform convergence $u_n\to u$, continuity of $F$, and boundedness of $F$ allow passage to the limit on the compact interval between $0$ and $x$. Thus
\[
u(x)-u(0)=\int_0^x F(u(t),t)\,dt,
\]
so $u$ is differentiable and $u'(x)=F(u(x),x)$.

Part (b), as printed, is false if "uniformly" means uniformly on all of $\mathbb R$. Take
\[
F(y,x)=\tanh y,
\qquad x_0=0,
\qquad y_0=0.
\]
The initial-value problem has the unique solution $u\equiv0$. For initial values $u_n(0)=1/n$, uniqueness gives positive solutions satisfying
\[
\frac{d}{dx}\log(\sinh u_n(x))=1,
\]
hence
\[
\sinh u_n(x)=e^x\sinh(1/n).
\]
Therefore
\[
u_n(x)=\operatorname{arsinh}\!\bigl(e^x\sinh(1/n)\bigr),
\]
which is unbounded as $x\to+\infty$ for every fixed $n$. Consequently
\[
\sup_{x\in\mathbb R}|u_n(x)-u(x)|=\infty,
\]
so $u_n$ does not converge uniformly to $u$ on $\mathbb R$.

The standard continuous-dependence conclusion is uniform convergence on each compact $x$-interval (under hypotheses ensuring the stated uniqueness/continuous dependence), not uniform convergence on the whole real line.
:::
