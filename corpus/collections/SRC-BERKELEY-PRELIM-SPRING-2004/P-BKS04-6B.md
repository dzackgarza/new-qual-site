---
schema: qual/card@1
id: P-BKS04-6B
kind: problem
title: Harmonic $u_n$ with $\partial_yu_n(x,0)=0$ and $u_n(x,0)\to0$ uniformly need not tend to $0$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, which is a correct counterexample. Added
    the reason u_n is harmonic (the real part of the entire function cos(nz)/n, with the expansion
    written out), the explicit derivative sinh(ny) cos(nx) and its vanishing at y = 0, the uniform
    bound |u_n(x,0)| <= 1/n, and the divergence at (0,1) from cosh n = (e^n + e^-n)/2. The printed statement
    was read at assets/attachments/s04.pdf, problem 6B, and matches the card's.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the retained paper at assets/attachments/s04.pdf, problem 6B: (u_n) harmonic in an
    open neighbourhood of the upper half plane R x R_{>= 0}, du_n/dy(x,0) = 0 for all x, and
    u_n(x,0) -> 0 uniformly in x; must u_n(x,y) -> 0 for every (x,y) in R x R_{>0}? The card's
    statement is that problem verbatim.
---

::: {.problem}
Let $(u_n(x,y))_{n\geq1}$ be a sequence of functions that are defined and harmonic for $(x,y)$ in an open neighborhood of the upper half plane $\RR\times\RR_{\geq0}$. Suppose that $\frac{\partial u_n}{\partial y}(x,0)=0$ for all $x\in\RR$, and $u_n(x,0)$ converges to $0$ as $n\to\infty$ uniformly for $x\in\RR$. Must $u_n(x,y)\to0$ as $n\to\infty$ for every $(x,y)\in\RR\times\RR_{>0}$?
:::

::: {.solution}
This is a problem of the UC Berkeley preliminary examination of Spring 2004 (`assets/attachments/s04.pdf`, problem 6B of the degree-one paper). No published solution set is transcribed: the counterexample below is the card's own.

::: pf

::: {.pf-step #family}
The functions $u_{n}(x,y)=\frac{1}{n}\cosh(ny)\cos(nx)$, $n\geq1$, are harmonic on $\RR^{2}$.

::: pf-proof
$u_{n}$ is the real part of the entire function $\frac{1}{n}\cos(nz)$: writing $z=x+iy$, $\cos(nz)=\cos(nx)\cosh(ny)-i\sin(nx)\sinh(ny)$. The real part of a holomorphic function is harmonic, so $u_{n}$ is harmonic on the whole plane, in particular on a neighbourhood of the closed upper half plane.
:::
:::

::: {.pf-step #normal}
$\frac{\partial u_{n}}{\partial y}(x,0)=0$ for all $x$, and $u_{n}(x,0)\to0$ uniformly in $x$.

::: pf-proof
$\frac{\partial u_{n}}{\partial y}=\frac{1}{n}\,n\sinh(ny)\cos(nx)=\sinh(ny)\cos(nx)$, which vanishes at $y=0$. And $u_{n}(x,0)=\frac{1}{n}\cos(nx)$, so $\abs{u_{n}(x,0)}\leq\frac1n$ for every $x$, which is a bound independent of $x$ tending to $0$ with $n$.
:::
:::

::: {.pf-step #fails}
$u_{n}(0,1)=\frac{\cosh n}{n}$ does not tend to $0$.

::: pf-proof
At $(x,y)=(0,1)$ one has $\cos(0)=1$ and $\cosh n=\frac{e^{n}+e^{-n}}{2}$, so $u_{n}(0,1)=\frac{e^{n}+e^{-n}}{2n}\geq\frac{e^{n}}{2n}\to\infty$.
:::
:::

::: {.pf-step #answer}
The answer to the question is no: the hypotheses do not force pointwise convergence in the open upper half plane.

::: pf-proof
The family of steps [](#family){.pf-ref} and [](#normal){.pf-ref} satisfies both hypotheses, and step [](#fails){.pf-ref} exhibits a single point $(0,1)$ of $\RR\times\RR_{>0}$ where the values are unbounded, so they certainly do not converge to $0$ there.
:::
:::
:::

:::
