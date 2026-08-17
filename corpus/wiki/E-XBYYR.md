---
schema: qual/card@1
id: E-XBYYR
kind: exercise
title: "State the standard Schwarz reflection principle involving\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-reflection
  - fractional-linear-transformations
  - maximum-modulus-principle
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
a. 
State the standard Schwarz reflection principle involving reflection across the real axis.

b. 
Give a linear fractional transformation $T$ mapping $\DD$ to $\HH$.
Let $g(z) = \bar z$, and show
\[  
(T^{-1} \circ g \circ T)(z) = 1/\bar z
.\]

c.
Suppose that $f$ is holomorphic on $\DD$, continuous on $\bar \DD$, and real on $S^1$.
Show that $f$ must be constant.

:::

:::{.solution}
**Part 1**:
Let $\Omega = \Omega^+ \union I \union \Omega^-$ be a region symmetric about $\RR$.
If $f$ is holomorphic on $\Omega^+$ extending continuously to $I$ and real valued on $I$, then $f$ extends to a holomorphic function $F$ on all of $\Omega$ defined on $\Omega^-$ by $F(z) = \bar{f(\bar{z})}$.

**Part 2**:
The map is $T(z) = -i\qty{z+1\over z-1}$ with $T\inv(z) = {z-i\over z+i}$, so
\[
(T\inv \circ g \circ T)(z)
&= T\inv\bar{\qty{-i {z+1\over z-1} }} \\
&= T\inv\qty{i{\bar z + 1 \over \bar z - 1}} \\
&= {i\qty{\bar z + 1 \over \bar z - 1} - i \over i\qty{\bar z + 1 \over \bar z - 1} + i } \\
&= {(\bar z + 1) - (\bar z - 1) \over (\bar z + 1) + (\bar z - 1)} \\
&= {1\over \bar{z}}
.\]


**Part 3**:
Define $h: \HH\to \bar{\HH}$ by $h(z) = (T\circ f\circ T\inv)(z)$.
Under $T\inv: \DD\to \HH$, we have $T(S^1) = \RR$, so $h$ is a holomorphic function on $\HH$ that is continuous and real-valued on $\RR$.
By the reflection principle, defining $H(z) \da \bar{h(\bar z)}$ for $\Im(z) < 0$ yields an entire function $H: \CC\to \CC$
Noting that for $g(z) \da \bar{z}$, $g=g\inv$, we can write
\[
H \da g\inv \circ h \circ = h\inv \circ (T\inv \circ f \circ T)\circ g
.\]
We can then conjugate $H$ by $T$ to get a direct formula in terms of $f$, and unwinding this yields the extension $F:\CC\to \CC$ defined by
\[
F(z) = 
\begin{cases}
f(z) & z\in \DD 
\\
f_-(z) \da {1\over \bar{f\bar{z}}} & z\in \DD^c \\
f(z) = f_i(z) & z\in S^1
\end{cases}
.\]
In particular, $H$ is an entire bounded function and thus constant, making $F$ constant as well and consequently $f$ is constant.
:::

