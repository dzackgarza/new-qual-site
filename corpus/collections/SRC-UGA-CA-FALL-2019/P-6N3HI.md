---
schema: qual/card@1
id: P-6N3HI
kind: problem
title: "Conformal map from a lune to the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

:::{.problem}
Find a conformal map from 
\[
D=\ts{ z\in \CC\st |z|<1 \text{ and } \abs{ z-{1\over 2}}>{1\over 2}}
\]
to the unit disk $\Delta=\{z:|z|<1\}$.
:::

:::{.solution}
This is a lune-type region:

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-30_02-25-54.png)

The usual strategy is to blow up the tangency, so send $1\to\infty$ with
\[
f(z) \da {1\over z-1}
.\]

:::{.claim}
$f$ has the following effect:

![](../../assets/Complex_Analysis/999_Quals/figures/2021-12-30_03-27-22.png)

:::

:::{.proof title="of claim"}
Write $C_1$ for $S^1$ and $C_2$ for the smaller circle.
Computing the image of $C_1$: parameterize as $\gamma_1(t) = e^{it}$ for $t\in [-\pi, \pi]$, then
\[
f(\gamma_1(t)) 
&= {1\over e^{it} - 1} \\
&= {e^{-it/2} \over e^{it/2} - e^{-it/2}} \\
&= {e^{-it/2} \over 2i\sin(t/2) } \\
&= -{i\over 2}\csc(t/2)\qty{\cos(t/2) - i\sin(t/2)} \\
&= -{i\over 2}\qty{\cot(t/2) - i } \\
&= {1\over 2}\qty{-1-i\cot(t/2)} \\
&= -{1\over 2} - i\cdot {1\over 2}\cot(t/2)
.\]

Some analysis on $\cot(t/2)$:

- $-\pi\increasesto 0 \leadsto 0\decreasesto -\infty$ 
- $0\increasesto \pi \leadsto \infty\decreasesto 0$ 

Thus for $-\cot(t/2)$,

- $-\pi\increasesto 0 \leadsto 0\increasesto \infty$ 
- $0\increasesto \pi \leadsto -\infty\increasesto 0$ 

So the image is a vertical line through $\Re(z) = -{1\over 2}$ oriented from $-\infty\to\infty$.

For the image of $C_2$: parameterize as $\gamma_2(t) = {1\over 2}\qty{1 + e^{it}}$, then
\[
f(\gamma_2(t))
&= {1\over {1\over 2}\qty{1+e^{it}} - 1 } \\
&= {1\over -{1\over 2} + {1\over 2}e^{it} } \\
&= {1\over {1\over 2}\qty{e^{it} - 1}} \\
&= {2e^{-it/2} \over e^{it/2} - e^{-it/2} } \\
&= {2e^{-it/2} \over 2i\sin(t/2) } \\
&= -i\csc(t/2) \qty{\cos(-t/2) + i\sin(-t/2) } \\
&= -i\csc(t/2) \qty{\cos(t/2) - i\sin(t/2) } \\
&= -i \qty{\cot(t/2) - i } \\
&= -1 - i\cot(t/2)
.\]
By the same argument as above, this traces out a vertical line at $\Re(z) = -1$.

By handedness, since the original region is on the left with respect to $C_1$ and the right with respect to $C_2$, the new region is to the left of $\Re(z) = -{1\over 2}$ and the right of $\Re(z) = -1$ (since both are oriented from $-\infty$ to $\infty$).

:::

From here, it's a standard exercise.
In steps:

- Map $R$ to the vertical strip $-1< \Re(z) < -{1\over 2}$ using $z\mapsto {1\over z-1}$.
- Shift using $z\mapsto z+{1\over 2}$ to send this to $-{1\over 2}< \Re(z) < 0$.
- Rotate using $z\mapsto -iz$ to get $0<\Im(z) < {i\over 2}$, a horizontal strip.
- Dilate using $z\mapsto 2\pi z$, which sends ${i\over 2}\to \pi i$, so the resulting region is $0 < \Im(z) < \pi$.
- Apply $z\mapsto e^z$ to map the horizontal strip to $\HH$.
- Apply the Cayley map $z\mapsto {z-i\over z+i}$ to map $\HH\to\DD$.

:::




