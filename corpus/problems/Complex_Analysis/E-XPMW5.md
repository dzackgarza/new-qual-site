---
schema: qual/card@1
id: E-XPMW5
kind: problem
title: Classifying singularities
classification:
  areas:
  - complex-analysis
  topics:
  - Singularities
  - Laurent Series
  - Removable Singularities
  - Essential Singularities
  - Poles
relations: []
review: draft
---

:::{.exercise}
Classify the singularities at $z=0$ of the following
\[
f_1(z) &= {\Log(1+z) \sin(z) \over z^2} \\
f_2(z) &= e^{\sin\qty{1\over z}} \\
f_3(z) &= {1+z \over e^z-1}
.\]

:::

:::{.solution}
$f_1$: removable, evident from Laurent expansion at $z=0$:
\[
z^{-2}\Log(1+z)\sin(z) 
&= z\inv \qty{ \sum_{k\geq 1} { (-z)^k \over k} }
\qty{z - { z^3 \over 3!} + { z^5 \over 5!} - \cdots} \\
&= z^{-2}
\qty{ -z+ { z^2 \over 2}  - { z^3 \over 3} + \cdots}
\qty{z - { z^3 \over 3!} + { z^5 \over 5!} - \cdots} \\
&= z^{-2}\qty{ z^2(-1) + z^3\qty{1\over 2} + z^2\qty{ -{ 1 \over 3!} - { 1 \over 3} } + \cdots } \\
&= 1 + {z \over 2} + \cdots
.\]

$f_2$: essential, evident from a sequence like $z_k \da \qty{k\cdot {\pi\over 2} }\inv$ which makes $\sin(z_k)$ oscillate between 0 and 1.

$f_3$: pole of order 1 with residue 1, evident after some slightly clever Laurent manipulations:
\[
{1\over e^z-1} 
&= {1 \over z + {1\over 2}z^2 + \cdots} \\
&= {1 \over z\qty{1 + {1\over 2}z + \cdots} } \\
&\da {1\over z \qty{1 + p(z)}} && p(z) \da {1\over 2} z + {1\over 3!}z^2 + \cdots \\
&= z\inv \sum_{k\geq 0}(-p(z))^k z^k \\
&= z\inv \qty{1 - zp(z) + z^2p(z)^2 - z^3p(z)^3 + \bigo(z^4)} \\
&= z\inv\qty{1- \bigo(z^2) + \bigo(z^4) - \bigo(z^6) } \\
&={1\over z} - \bigo(z) + \bigo(z^3)
.\]

:::
