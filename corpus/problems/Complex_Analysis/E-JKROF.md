---
schema: qual/card@1
id: E-JKROF
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}$
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
---

::: {.exercise}
\[
\int_{0}^{2 \pi} \frac{d \theta}{a+b \cos \theta}=\frac{2 \pi}{\sqrt{a^{2}-b^{2}}}
.\]

:::

::: {.solution}
The usual substitution: $z=e^{i\theta}, \dtheta = (iz)\inv \dz$.
\[
\int_{[0, 2\pi]} (a +b\cos(\theta))\inv \dtheta 
&= \oint \qty{ a + {b\over 2}(z+z\inv)}\inv (iz)\inv \dz \\
&= -i\oint \qty{ za + {b\over 2}(z^2 + 1)} \inv \dz \\
&= -i \oint \qty{{b\over 2}z^2 + az + {b\over 2} }\inv \dz \\
&= -{2i\over b} \oint \qty{z^2 + {2a\over b}z + 1}\inv \dz \\
&= -{2i\over b}\oint (z-r_1)\inv (z-r_2)\inv \dz
,\]
where by the quadratic formula the roots are
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

Assume $a>\abs b>0$, so that the integrand is continuous and the roots are real and distinct (for $b=0$ the integral is $2\pi/a$ directly).
Since $r_1 r_2 = 1$, exactly one root lies in $\DD$, giving one simple pole there.
If $b>0$, then $r_2=-(a+\sqrt{a^2-b^2})/b<-a/b<-1$; if $b<0$, then $r_2>a/\abs b>1$. In either case $\abs{r_2}>1$, so $r_1\in \DD$.
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

