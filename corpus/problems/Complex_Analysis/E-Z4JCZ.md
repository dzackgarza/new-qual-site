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

::: {.exercise}
\[
\int_{0}^{2 \pi} \frac{d \theta}{1+a^{2}-2 a \cos (\theta)}
= \begin{cases}\frac{2 \pi}{a^{2}-1} & \text { if }|a|>1 \\ \frac{2 \pi}{1-a^{2}} & \text { if }|a|<1\end{cases}
.\]

:::

::: {.solution}
The usual substitution: $z=e^{i\theta}, \dz = (iz)\dtheta$.
\[
I\da \int_{[0, 2\pi]} \inverseof{\qty{a^2 - 2a\cos(\theta) + 1}} \dtheta
&= \oint \inverseof{\qty{a^2-2(z+\inverseof{z}) + 1}} \inverseof{(iz)} \dz \\
&= -i\oint \inverseof{\qty{za^2 - a(z^2+1) +z}} \dz \\
&= -i \oint\inverseof{\qty{-az^2 + (a^2+1)z - a}}\dz \\
&= {i\over a}\oint \inverseof{\qty{z^2 - \qty{a^2+a\over a}z + 1}} \dz \\
&= {i\over a}\oint \inverseof{(z-a)} \inverseof{(z-\inverseof{a})} \dz
,\]
noting that ${a^2+a\over a} = a+\inverseof{a}$.
Now there are two cases:

- $\abs{a} < 1$: then $a\in \DD,\inverseof{a}\in \DD^c$, so there is a simple pole at $a$.
  Then 
  \[
  I 
  &= {i\over a}\, 2\pi i \Res_{z=a} \inverseof{(z-a)}\inverseof{(z-\inverseof{a})} \\
  &=  -{2\pi \over a} \inverseof{(z-\inverseof{a})} \evalfrom_{z=a} \\
  &= -{2\pi \over a(a-\inverseof{a})} \\
  &= {2\pi \over 1 - a^2}
  .\]

- $\abs{a}> 1$: then $\inverseof{a} \in \DD, a\in \DD^c$ so there is a simple pole at $\inverseof{a}$.
  Then 
  \[
  I 
  &= {i\over a}\, 2\pi i \Res_{z=\inverseof{a} } \inverseof{(z-a)}\inverseof{(z-\inverseof{a})} \\
  &=  -{2\pi \over a} \inverseof{(z-a)} \evalfrom_{z=\inverseof{a}} \\
  &= -{2\pi \over a(\inverseof{a} - a)} \\
  &= {2\pi \over a^2 - 1}
  .\]

:::
