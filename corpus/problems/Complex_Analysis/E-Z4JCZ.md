---
schema: qual/card@1
id: E-Z4JCZ
kind: problem
title: $1/1+a^2+2a\cos(\theta)$, Poisson kernels
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
  - Harmonic Functions
relations: []
review: draft
---

:::{.exercise}
\[
\int_{0}^{2 \pi} \frac{d \theta}{1+a^{2}-2 a \cos (\theta)}
= \begin{cases}\frac{2 \pi}{a^{2}-1} & \text { if }|a|>1 \\ \frac{2 \pi}{1-a^{2}} & \text { if }|a|<1\end{cases}
.\]

:::

:::{.solution}
The usual substitution: $z=e^{i\theta}, \dz = (iz)\dtheta$.
\[
I\da \int_{[0, 2\pi]} \qty{a^2 - 2a\cos(\theta) + 1}\inv \dtheta
&= \oint \qty{a^2-2(z+z\inv) + 1}\inv (iz)\inv \dz \\
&= -i\oint \qty{za^2 - a(z^2+1) +z}\inv \dz \\
&= -i \oint\qty{-az^2 + (a^2+1)z - a}\inv\dz \\
&= {i\over a}\oint \qty{z^2 - \qty{a^2+a\over a}z + 1}\inv \dz \\
&= {i\over a}\oint (z-a)\inv (z-a\inv)\inv \dz
,\]
noting that ${a^2+a\over a} = a+a\inv$.
Now there are two cases:

- $\abs{a} < 1$: then $a\in \DD,a\inv\in \DD^c$, so there is a simple pole at $a$.
  Then 
  \[
  I 
  &= {i\over a}\, 2\pi i \Res_{z=a} (z-a)\inv(z-a\inv)\inv \\
  &=  -{2\pi \over a} (z-a\inv)\inv \evalfrom_{z=a} \\
  &= -{2\pi \over a(a-a\inv)} \\
  &= {2\pi \over 1 - a^2}
  .\]

- $\abs{a}> 1$: then $a\inv \in \DD, a\in \DD^c$ so there is a simple pole at $a\inv$.
  Then 
  \[
  I 
  &= {i\over a}\, 2\pi i \Res_{z=a\inv } (z-a)\inv(z-a\inv)\inv \\
  &=  -{2\pi \over a} (z-a)\inv \evalfrom_{z=a\inv} \\
  &= -{2\pi \over a(a\inv - a)} \\
  &= {2\pi \over a^2 - 1}
  .\]

:::

