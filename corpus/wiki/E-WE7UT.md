---
schema: qual/card@1
id: E-WE7UT
kind: exercise
title: "Residues and classifying singularities"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Residues and classifying singularities"}
Classify the singularities of 
\[
f(z) = {z^3+1\over z^2(z+1)}
.\]

:::

:::{.concept}
Showing a pole $z_0$ of $f$ is order $n$: show that $z_0$ is a zero of order $n$ of $1/f$, i.e. $1/f = (z-z_0)^nh(z)$ with $h$ nonvanishing in a neighborhood of $z_0$.
:::

:::{.solution}
Write $f(z) = p(z)/q(z)$ and factor $p$: a principal root is $\omega = e^{i\pi 3}$, so 
\[
p(z) 
&= (z-\omega\zeta_3^0)(z-\omega\zeta_3^1)(z-\omega\zeta_3^2) \\
&= (z-e^{i\pi\over 3})(z-e^{3i\pi \over 3})(z-e^{5i\pi \over 3}) \\
&= (z+1)(z-\omega)(z-\bar\omega)
,\]
so $z=-1$ is a removable singularity of $f$.
Alternatively, note that ${z^3+1 \over z+1} = z^2-z+1$ and cancel the common term.

Note that $z=0$ is a zero of order $n=2$ of $1/f(z)$, since $1/f(z) = z^2h(z)$ where $h$ is nonvanishing in a neighborhood of $0$.
Thus $z=0$ is a pole of order $n=2$ of $f$.
The residue is computed as
\[
\Res_{z=0} f(z) 
&= {1\over (1-1)!} \lim_{z\to 0} \dd{}{z} (z-0)^2f(z) \\
&= \dd{}{z} {z^3+1\over z+1}\evalfrom_{z=0} \\
&= \qty{ {3z^2\over z+1} - {(z^3+1)\cdot 1\over (z+1)^2} }\evalfrom_{z=0} \\
&= -1
.\]

Alternatively, expand as a Laurent series about $z=0$:
\[
f(z) 
&= z^{-2}(z^3 + 1) {1\over 1+z} \\
&= (z + z^{-2})\sum_{k\geq 0}(-z)^k \\
&= (z-z^2 + z^3 - \cdots) + (z^{-2} - z\inv + 1 - z + \cdots)
,\]
and read off the coefficient of $z\inv$.

:::
