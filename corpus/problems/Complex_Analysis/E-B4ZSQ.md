---
schema: qual/card@1
id: E-B4ZSQ
kind: problem
title: A harmonic conjugate of $x^3-3xy^2-x-y$
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Cauchy-Riemann
relations: []
review: draft
---

::: {.exercise}
Find a harmonic conjugate for
\[
u(x, y) = x^3 - 3xy^2 -x -y
.\]

:::

::: {.concept}
A harmonic conjugate $v$ of $u$ on a simply connected domain is computed as follows:

- Start with $u$
- Take $\dd{}{x}$ to get $u_x$
- Apply CR to get $u_x = v_y$
- Take $\int \dy$ to get $v$ up to an unknown function $f(x)$.
- Take $\dd{}{x}$ to get $v_x$ which involves $f_x$
- Apply CR to set $v_x = -u_y$ and solve for $f_x$
- Compute $\int f_x \dx$ to obtain $f(x)$.

The same steps as a diagram:

\begin{tikzcd}
	u & f &&& \textcolor{rgb,255:red,92;green,214;blue,92}{v, f} \\
	&&&& {v, f(x)} \\
	& {u_y, f_x} && {v_x, f_x} \\
	{u_x} &&&& {v_y}
	\arrow["{\dd{}{x}}", from=1-1, to=4-1]
	\arrow["CR", dashed, from=4-1, to=4-5]
	\arrow["{\dd{}{x}}"', from=2-5, to=3-4]
	\arrow["CR", dashed, from=3-4, to=3-2]
	\arrow["{\int \dx}"', from=3-2, to=1-2]
	\arrow[squiggly, from=1-2, to=1-5]
	\arrow["{\int \dy}"', from=4-5, to=2-5]
\end{tikzcd}

:::

::: {.solution}
First, check that $u$ is actually harmonic: 
\[
\laplacian u = \dd{}{x}(3x^2-3y^2-1) + \dd{}{y}(-6xy - 1) = 6x + (-6x) = 0
.\]

Standard procedure: integrate $v_y=u_x$ with respect to $x$,
\[
v_y = u_x = 3x^2 - 3y^2 - 1 \implies 
v = \int u_x \dy = 3x^2y - y^3 - y + f_1(x)
.\]
Now differentiate $v$ with respect to $x$ and set $v_x = -u_y$:
\[
v_x = 6xy + (f_1)_x = -u_y = 6xy + 1\implies f_1 = x + c_1
.\]
Thus
\[
v(x, y) = 3x^2y - y^3 - y + x + c_1
.\]

:::

