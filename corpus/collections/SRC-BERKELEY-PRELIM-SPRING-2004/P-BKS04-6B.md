---
schema: qual/card@1
id: P-BKS04-6B
kind: problem
title: UC Berkeley Spring 2004 prelim 6B
classification:
  areas: [prelim]
  topics: []
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
---

::: {.problem}
Let $(u_n(x,y))_{n\geq1}$ be a sequence of functions that are defined and harmonic for $(x,y)$ in an open neighborhood of the upper half plane $\RR\times\RR_{\geq0}$. Suppose that $\frac{\partial u_n}{\partial y}(x,0)=0$ for all $x\in\RR$, and $u_n(x,0)$ converges to $0$ as $n\to\infty$ uniformly for $x\in\RR$. Must $u_n(x,y)\to0$ as $n\to\infty$ for every $(x,y)\in\RR\times\RR_{>0}$?
:::

::: {.solution}
No. Let $u_n=\cosh(ny)\cos(nx)/n$. Since $u_n$ is the real part of the holomorphic function $\cos(nz)/n$, it is harmonic on the entire plane.
Then $\frac{\partial u_n}{\partial y}(x,0)=-\sinh(0)\cos(nx)=0$, and $u_n(x,0)=\cos(nx)/n\to0$ as $n\to\infty$ uniformly for $x\in\RR$. But $u_n(0,1)=\cosh(n)/n$ does not tend to $0$ as $n\to\infty$.
:::
