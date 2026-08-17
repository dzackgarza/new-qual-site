---
schema: qual/card@1
id: E-JKROF
kind: exercise
title: "$1/a+b\\cos(\\theta)$"
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - integrals
  - trigonometry
relations: []
review: draft
solved: true
---
:::{.exercise title="$1/a+b\cos(\theta)$"}
\[
\int_{0}^{2 \pi} \frac{d \theta}{a+b \cos \theta}=\frac{2 \pi}{\sqrt{a^{2}-b^{2}}}
.\]

:::

:::{.solution}
The usual substitution: $z=e^{i\theta}, \dtheta = (iz)\inv \dz$.
\[
\int_{[0, 2\pi]} (a +b\cos(\theta))\inv \dtheta 
&= \oint \qty{ a + {b\over 2}(z+z\inv)}\inv (iz)\inv \dz \\
&= -i\oint \qty{ za + {b\over 2}(z^2 + 1)} \inv \dz \\
&= -i \oint \qty{{b\over 2}z^2 + az + {b\over 2} }\inv \dz \\
&= -{2i\over b} \oint \qty{z^2 + {2a\over b}z + 1}\inv \dz \\
&= -{2i\over b}\oint (z-r_1)\inv (z-r_2)\inv \dz
,\]
where the roots can just be found using the quadratic formula
\[
z_k 
&= {1\over 2} \qty{-{2a\over b} \pm \sqrt{\qty{2a\over b}^2 - 4}} \\
&= -{a\over b}\pm {1\over 2}\sqrt{{4a^2 \over b^2} - 4} \\
&= -{a\over b}\pm \sqrt{{a^2 \over b^2} - 1} \\
&= -{a\over b}\pm \sqrt{{a^2 - b^2 \over b^2}} \\
&= -{a\over b}\pm {1\over b } \sqrt{{a^2 - b^2}} 
.\]
Thus
\[
r_1 &\da b\inv\qty{-a + \sqrt{a^2-b^2}} \\
r_2 &\da b\inv\qty{-a - \sqrt{a^2-b^2}} 
.\]

Since $r_1 r_2 = 1$ and thus $\abs{r_1 r_2} = 1$, only one root is in $\DD$ and this yields one simple pole.
Assume $a>b$.
Note that for $r_2$, $\abs{a/b} > 1$ and $\abs{a^2-b^2}>0$, so $r_2 \approx -1 - \eps < -1$, so $r_1\in \DD$.
Computing the residue here:
\[
\Res_{z=r_1} (z-r_1)\inv (z-r_2)\inv 
&= (z-r_2)\inv \evalfrom_{z=r_1} \\
&= (r_1 - r_2)\inv \\
&= \qty{2b\inv \sqrt{a^2-b^2} }\inv
,\]
so 
\[
I &= 2\pi i \cdot -{2 i \over b}{b\over 2\sqrt{a^2-b^2}} \\
&= {2\pi \over \sqrt{a^2-b^2} }
.\]

:::

