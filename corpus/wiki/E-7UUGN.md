---
schema: qual/card@1
id: E-7UUGN
kind: exercise
title: "Laurent expanding tricky exponentials"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Laurent expanding tricky exponentials"}
Find a Laurent expansion for
\[
f(z) = {1\over 1 + e^z}
\]
about $z_0 = 0$ and $z_1 = i\pi$.

#complex/exercise/completed

:::

:::{.solution}
At $z=0$, we can use a geometric series approach since $\abs{e^z} = e^{\Re(z)} \leq 1$ near $0$.
However, we still have to get rid of the leading 1 in the expansion of $e^z$ in order to get a constant coefficient.
\[
{1\over 1 + e^z} 
&= {1\over 1 + 1 + z + {1\over 2!}z^2 + {1\over 3!} z^3 + \bigo(z^4)} \\
&= {1\over 2 + z + {1\over 2!}z^2 + {1\over 3!} z^3 + \bigo(z^4) } \\
&= {1\over 2} {1\over 1 + {1\over 2} z + {1\over 2\cdot 2!}z^2 + {1\over 2\cdot 3!} z^3 + \bigo(z^4) } \\
&= {1\over 2}{1\over 1 - (-p(z)) } \qquad p(z) \da {1\over 2}z + {1\over 2\cdot 2!}z^2 + {1\over 2\cdot 3!}z^3 + \bigo(z^4)  \\
&= {1\over 2} \sum_{k\geq 0} (-p(z))^k \\
&= {1\over 2}\Big[ 1 - \qty{{1\over 2}z + {1\over 2\cdot 2!}z^2 + {1\over 2\cdot 3!}z^3 + \bigo\qty{z^4} } \\ 
&\qquad + \qty{ {1\over 2}z + {1\over 2\cdot 2!}z^2 + {1\over 2\cdot 3!}z^3 + \bigo\qty{z^4} }^2 \\ 
&\qquad - \qty{{1\over 2} z + {1\over 2\cdot 2!}z^2 + {1\over 2\cdot 3!}z^3 + \bigo\qty{z^4} }^3 \\
&\qquad - \bigo(z^4) \Big]\\
&= {1\over 2}
\Big[ 
1 + z\qty{- {1\over 2}} + z^2\qty{- {1\over 2\cdot 2!} + \qty{1\over 2}^2}\\
&\qquad + z^3
\Big(
-{1\over 2\cdot 3! } +\left[ \qty{1\over 2}^3 + {1\over 2}{1\over 2\cdot 2!}\right] - \qty{1\over 2}^3 
\Big) \\
&\qquad + \bigo(z^4)
\Big]\\
&= {1\over 2} - {1\over 4}z + 0z^2 + {1\over 48}z^3 + \bigo(z^4)
.\]

Expanding at $z-i\pi$: quite a bit easier.
Let $\omega \da z-i\pi$, then
\[
{1\over 1 + e^z}
&= {1\over 1 + e^{z-i\pi}e^{i\pi}} \\
&= {1\over 1 - e^{\omega} } \\
&= {1 \over -\omega - {1\over 2!}\omega^2 - {1\over 3!}\omega^3 - \bigo(\omega^4) } \\
&= -{1\over \omega} {1 \over 1 + {1\over 2!}\omega + {1\over 3!}\omega^2 + \bigo(\omega^3) } \\
&= -{1\over \omega}{1\over 1-(- p(z) ) } \qquad p(z) \da \sum_{k\geq 2}{\omega^{k-1}\over k!} \\
&= -{1\over \omega} \sum_{k\geq 0} (-p(z))^k \\
&= -{1\over \omega}
\left[
1 -
\qty{{1\over 2!}\omega + {1\over 3!}\omega^2 + \bigo(\omega^3)} + 
\qty{{1\over 2!}\omega + {1\over 3!}\omega^2 + \bigo(\omega^3)}^2 -
\bigo(\omega^3)
\right] \\
&= -{1\over \omega}
\left[
1 + \omega\qty{-{1\over 2!}} + \omega^2\qty{-{1\over 3!} + \qty{1\over 2!}^2} + \bigo(\omega^3)
\right] \\
&= -{1\over w} + {1\over 2} - {1\over 12}\omega + \bigo(\omega^2)
.\]

:::

