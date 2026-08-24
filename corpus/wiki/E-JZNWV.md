---
schema: qual/card@1
id: E-JZNWV
kind: exercise
title: $x/(x^2+4x+13)^2$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Poles
relations: []
review: draft
---

:::{.exercise title="$x/(x^2+4x+13)^2$"}

\[
I\da \int_\RR {x\over (x^2 + 4x+13)^2}\dx
.\]

:::

:::{.solution}
Write the integrand as $f$.

:::{.claim}
$f\in \bigo\qty{1\over z^{3}} \subseteq \bigo\qty{1\over z^{1+\eps}}$ means that a semicircular contour will work:

![Semicircular contour](../../assets/30_Complex_Analysis/040_Residues/figures/2021-12-23_18-14-14.png)

:::

:::{.proof title="Of integrand decay"}
A quick justification: for $R>1$, if $n>k$ then $\abs{z}^n > \abs{z}^k$, so using the reverse triangle inequality,
\[
\abs{z\over (z^2 + 4z + 13)^2} 
&= \abs{z\over z^4 + 8z^3 + 42z^2 + 104z + 169}\\
&\leq \abs{z\over \abs{z}^4 - 8\abs{z}^3 - 42\abs{z}^2 - 104\abs{z} - 169}\\
&\leq \abs{z\over \abs{z}^4 - 8\abs{z}^4 - 42\abs{z}^4 - 104\abs{z}^4 - 169\abs{z}^4}\\
&= \abs{z\over \abs{z}^4( 1 - 8 - 42 - 104 - 169)}\\
&= 322 {\abs{z} \over \abs{z}^4} \\
&= 322 \abs{z}^{-3} \\
&= 322 R^{-3} \to 0 \text{ as } R\to\infty
.\]

:::

Factor the denominator:
\[
x^2 + 4x + 13 = 0 
&\implies x^2 + 4x + \qty{4\over 2}^2 = -13 + \qty{4\over 2}^2 \\
&\implies (x+2)^2 = -9 \\
&\implies x = -2 \pm 3i
,\]
one of which is in $\HH$.
Write these as 
\[
z_1 \da -2+3i && z_2 \da -2 - 3i
.\]

So let $\Gamma$ be comprised of

- $C_1 = [-R,R]$, 
- $C_2 = \ts{Re^{it} \st t\in [0, \pi]}$, 
- $\Gamma = C_1 + C_2$, then
\[
2\pi i \sum_{z_k\in \HH} \Res_{z=z_k}f(z) = \int_\Gamma f = \qty{\int_{C_1} + \int_{C_2}}f
,\]
where $\int_{C_2} f\to 0$ and $\int_{C_1} f\to I$.
So in the limit, $I = 2\pi i \Res_{z=z_1} f(z)$.
Computing this residue: note $z_1$ is a pole of order 2, so
\[
\Res_{z=z_1} 
&= \lim_{z\to z_1} \dd{}{z} (z-z_1)^2f(z)
&= \lim_{z\to z_1} \dd{}{z} {z \over (z-z_2)^2} \\
&= \lim_{z\to z_1} { (z-z_2)^2 - 2z(z-z_2 ) \over (z-z_2)^4} \\
&= \lim_{z\to z_1} { (z-z_2) - 2z \over (z-z_2)^3} \\
&= \lim_{z\to z_1} -{ z+z_2 \over (z-z_2)^3} \\
&= - {z_1 + z_2 \over (z_1 - z_2)^2}\\
&= - {z_1 + \bar{z_1} \over (z_1 - \bar{z_1} )^2}\\
&= - {2\Re(z_1) \over (2i\Im(z_1))^3} \\
&= - {2\cdot (-2) \over (2i\cdot 3) ^3} \\
&= {4\over 2^3 \cdot 3^3 \cdot i^3} \\
&= {-i \over 2 \cdot 3^3 i^2} \\
&= {i\over 54}
,\]
so 
\[
I = 2\pi i \cdot {i\over 54} = -{\pi \over 27}
.\]

:::

