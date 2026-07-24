---
schema: qual/card@1
id: E-XQW4K
kind: exercise
title: "Showing singularities are removable"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Showing singularities are removable"}
Consider
\[
f(z) \da {1\over \sin(z)} - {1\over z} + {2z\over z^2-\pi^2}
.\]
Show that on $\abs{z} < 2\pi$, all singularities are removable, and find a Laurent expansion about $z=0$.

:::

:::{.solution title="Using L'Hopital and boundedness"}
Note that the singularities are
\[
z = 0, \pi, -\pi
.\]

That $z=0$ is removable:
\[
\lim_{z\to 0} f(z) 
&= \lim_{z\to 0} {z-\sin(z) \over z\sin(z)} \\
&\equalsbecause{\text{LH}} \lim_{z\to 0} {1 - \cos(z) \over \sin(z) + z\cos(z)} \\
&\equalsbecause{\text{LH}} \lim_{z\to 0} {\sin(z) \over \cos(z) + \cos(z) -z\sin(z) } \\
&= 0 < \infty
,\]
so in particular $f$ is bounded in a neighborhood of $z=0$, making it removable.

That $z=\pi$ is removable:
\[
\lim_{z\to \pi} f(z) 
&= \lim_{z\to \pi} {1\over \sin(z)} - {1\over z} + {1\over z-\pi} + {1\over z+\pi}\\
&= c_1 + \lim_{z\to \pi} {1\over \sin(z)} + {1\over z-\pi} \\
&= c_1 + \lim_{z\to \pi} { (z-\pi) -\sin(z) \over (z-\pi) \sin(z) }\\
&= c_1 + \lim_{w\to 0} { w -\sin(w + \pi) \over w \sin(w+\pi) } \qquad w\da z-\pi \\
&= c_1 - \lim_{w\to 0} { w + \sin(w) \over w \sin(w) } \\
&\equalsbecause{\text{LH}} c_1 + 0 < \infty
,\]
using the same L'Hopital argument as above. 
So this limit is bounded.

That $z=-\pi$ is removable:
\[
\lim_{z\to \pi} f(z) 
&= \lim_{z\to -\pi} {1\over \sin(z)} - {1\over z} + {1\over z-\pi} + {1\over z+\pi}\\
&= c_2 + \lim_{z\to -\pi} {1\over \sin(z)} + {1\over z+\pi}\\
&= c_2 + \lim_{z\to -\pi} {(z+\pi) - \sin(z) \over (z+\pi) \sin(z) } \\
&= c_2 - \lim_{z\to -\pi} {w + \sin(w) \over w \sin(w) } \qquad w \da z+\pi \\
&= c_2 + 0 < \infty
,\]
again by the same argument.

For a Laurent expansion about $z=0$, note
\[
{1\over \sin(z) } 
&= {1\over z + c_3 z^3 + c_5 z^5 + \bigo(z^7)} \\
&= z\inv( 1 + c_3z^2 + (c_3^2-c_5)z^4 + \bigo(z^6)) \\
&= z\inv + {1\over 3!} z + \qty{ \qty{1\over 3!}^2 - {1\over 5!} }z^3 + \bigo(z^5) \\
&= z\inv + {1\over 6}z + {7\over 360}z^3 + \bigo(z^5)
.\]
and
\[
{2z\over z^2-\pi^2} 
&= - {2z\over \pi^2} {1\over 1 - \qty{z\over \pi}^2 } \\
&= -{2z\over \pi^2}\sum_{k\geq 0}\qty{z\over \pi}^{2k} \\
&= -{2z\over \pi^2}\qty{1 + {1\over \pi^2} z^2 + {1\over \pi^4}z^4 + \bigo(z^6) } \\
&= -{2\over \pi^2}z -{2\over \pi^4}z^3 - {2\over \pi^6} z^5 - \bigo(z^7)
,\]
so
\[
f(z) &= 
\qty{z\inv + {1\over 6}z + {7\over 360}z^3 + \bigo(z^5)}
+
\qty{-{2\over \pi^2}z -{2\over \pi^4}z^3 - {2\over \pi^6} z^5 - \bigo(z^7)}
- z\inv \\
&= \qty{ {1\over 6} - {2\over \pi^2}}z + \qty{{7\over 360} - {2\over \pi^4} }z^3 + \bigo(z^5)
.\]
:::

:::{.solution title="Comparing orders of vanishing"}
Write
\[
f(z) = {z-\sin(z) \over z\sin(z)} - {2z\over z^2-\pi^2}
,\]

For $z=0$, the 2nd term doesn't contribute to zero/pole order.
For the first, take an expansion:
\[
f_1(z) 
&= {z - \qty{ z + c_3z^3 + \bigo(z^5)} \over z \qty{z + c_3z^3 + \bigo(z^5)} } \\ \\
&= { -c_3z^3 + \bigo(z^5)\over z^2 + \bigo(z^4) }
,\]
so there is a zero of order 3 in the numerator and of order 2 in the denominator, making the singularity removable.
A similar argument works at $z=\pm \pi$.
:::
