---
schema: qual/card@1
id: E-B4ZSQ
kind: exercise
title: "Finding harmonic conjugates"
classification:
  areas:
  - complex-analysis
  topics:
  - harmonic-functions
  - cauchy-riemann
relations: []
review: draft
---
:::{.exercise title="Finding harmonic conjugates"}
Find a harmonic conjugate for
\[
u(x, y) = x^3 - 3xy^2 -x -y
.\]

:::

:::{.concept}
The standard procedure for harmonic conjugates:

- Start with $u$
- Take $\dd{}{x}$ to get $u_x$
- Apply CR to get $u_x = v_y$
- Take $\int \dy$ to get $v$, which is essentially the solution up to an unknown $f(x)$.
- Take $\dd{}{x}$ to get $v_x$ which involves $f_x$
- Apply CR to set $v_x = -u_y$ and solve for $f_x$
- Compute $\int f_x \dx$ to obtain $f(x)$.

My quick mnemonic:

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

> [Link to Diagram](https://q.uiver.app/?q=WzAsOCxbMCwwLCJ1Il0sWzAsMywidV94Il0sWzQsMywidl95Il0sWzQsMSwidiwgZih4KSJdLFszLDIsInZfeCwgZl94Il0sWzEsMiwidV95LCBmX3giXSxbMSwwLCJmIl0sWzQsMCwidiwgZiIsWzEyMCw2MCw2MCwxXV0sWzAsMSwiXFxkZHt9e3h9Il0sWzEsMiwiQ1IiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMyw0LCJcXGRke317eH0iLDJdLFs0LDUsIkNSIiwwLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzUsNiwiXFxpbnQgXFxkeCIsMl0sWzYsNywiIiwwLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoic3F1aWdnbHkifX19XSxbMiwzLCJcXGludCBcXGR5IiwyXV0=)

:::

:::{.solution}
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

