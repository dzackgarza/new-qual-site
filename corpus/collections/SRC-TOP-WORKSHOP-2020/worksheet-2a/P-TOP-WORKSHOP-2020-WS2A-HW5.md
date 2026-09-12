---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2A-HW5
kind: problem
title: Analyze the topologist’s sine wave (warm-up)
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Optional: Explain why the “topologist’s sine wave” $$X=\{(0,0)\}\cup\{(x,\sin(1/x)):x>0\}$$ is an example of a space which is connected but not path connected.
:::

::: {.solution}
Let
\[
G=\{(x,\sin(1/x)):x>0\}.
\]
The map
\[
(0,\infty)\to G,
\qquad x\mapsto(x,\sin(1/x))
\]
is a homeomorphism, with inverse given by first-coordinate projection. Hence \(G\) is path connected, in particular connected.

The point \((0,0)\) lies in \(\overline G\): for example,
\[
x_n=\frac1{n\pi}\longrightarrow0,
\qquad
(x_n,\sin(1/x_n))=(x_n,0)\longrightarrow(0,0).
\]
A connected set together with any one of its closure points is connected, so
\[
X=G\cup\{(0,0)\}
\]
is connected.

It is not path connected. Suppose there were a path
\[
\gamma(t)=(x(t),y(t)):[0,1]\to X
\]
from \((0,0)\) to a point of \(G\). Let
\[
t_0=\sup\{t:x(t)=0\}.
\]
Then \(x(t_0)=0\), while for \(t>t_0\) sufficiently close to \(t_0\) we have \(x(t)>0\) and hence
\[
y(t)=\sin(1/x(t)).
\]
Continuity of \(x\) and \(x(t_0)=0\) force \(1/x(t)\) to become arbitrarily large as \(t\downarrow t_0\). Since \(x([t_0,t_0+\varepsilon])\) is an interval containing \(0\) and some positive number, it contains values \(1/(\pi/2+2\pi n)\) and \(1/(3\pi/2+2\pi n)\) for arbitrarily large \(n\). Along corresponding sequences \(t_n,s_n\downarrow t_0\), one has
\[
y(t_n)=1,
\qquad
y(s_n)=-1,
\]
contradicting continuity of \(y\) at \(t_0\). Thus no such path exists, and \(X\) is connected but not path connected.
:::
