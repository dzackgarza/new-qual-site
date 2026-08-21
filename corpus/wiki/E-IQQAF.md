---
schema: qual/card@1
id: E-IQQAF
kind: exercise
title: ML estimate for a semicircular contour
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
relations: []
review: draft
solved: true
---

:::{.exercise title="ML estimate for a semicircular contour"}
Use a semicircular contour and the residue theorem to evaluate
\[
I = \int_\RR {\cos(x) \over x^2 + 1 }\dx
.\]

:::

:::{.solution}
Write
\[
I = \Im \int_\RR f(z) \dz && f(z) \da {e^{iz} \over z^2 + 1}\dz
.\]
Define contours $C_1 = [-R, R]$, $C_2 = \ts{Re^{it} \st t\in [0, \pi]}$, and $\Gamma = C_1 + C_2$.
Then noting that $z_0 = i$ is the only pole of $f$ in $\HH$, by the residue theorem
\[
\int_\Gamma f(z) \dz = 2\pi i \Res_{z=i} f(z) = \qty{\int_{C_1} + \int_{C_2}} f
.\]
Note also that \[
I = \Re \lim_{R\to\infty} \int_{C_1} f
.\]

By the ML estimate,
\[
\abs{\int_{C_2} f(z)\dz } 
&\leq 2\pi R \sup_{z\in C_2} \abs{f(z)} \\
&\da 2\pi R \sup_{z\in C_2} \abs{e^{iz}\over z^2 + 1} \\
&\leq 2\pi R \sup_{z\in C_2} {1 \over \abs{ z^2 + 1} } \\
&\leq 2\pi R\sup_{z\in C_2} {1 \over \abs{z}^2 - 1 } \text{ by the reverse triangle ineq.}\\
&= {2\pi R\over R^2-1} \\
&= \bigo(R^{-1}) \\
&\convergesto{R\to\infty}0
.\]

For the residue, $z=i$ is at worst an order 1 pole, and remains order 1 since $i$ is not a zero of the numerator.
\[
\Res_{z=i} f(z) 
&= \Res_{z=i} {e^{iz} \over (z+i)(z-i)} \\
&= { e^{iz} \over z+i}\evalfrom_{z=i} \\
&= {1\over 2ei}
.\]
Thus 
\[
\lim_{R\to\infty}\int_{C_1} f = 2\pi i \Res_{z=i} f = {2\pi i \over 2ei} = {\pi \over e} \\
\implies I = \Re\qty{\pi \over e} = {\pi \over e}
.\]

Note that this also shows that
\[
\int_\RR { \sin(z) \over z^2 + 1} \dz = 0
.\]

:::

