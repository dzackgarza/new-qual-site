---
schema: qual/card@1
id: P-KUNLD
kind: problem
title: "Tangent from polynomial long division"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Tangent from polynomial long division"}
Find a Laurent expansion about $z_0=0$ for $f(z) = \tan(z)$ by using polynomial long division on the series expansions for $\sin(z)$ and $\cos(z)$.
:::

:::{.solution}
Computing the Laurent series for $\tan(z)$ at $z=0$:

\[
{\sin(z) \over \cos(z)} 
&= {z - {1\over 3!}z^3 + {1\over 5!} z^5 + \bigo(z^7) \over 1 - {1\over 2!} z^2 + {1\over 4!}z^4 + \bigo(z^6) } 
\\ \\
z - {1\over 3!}z^3 + {1\over 5!}z^5 
&= \qty{1 - {1\over 2!}z^2 + {1\over 4!}z^4}(z)
\ +\qty{ \qty{{1\over 2!} - {1\over 3!}}z^3 + \qty{-{1\over 4!} + {1\over 5!} }z^5 } \\
&= \qty{1 - {1\over 2!}z^2 + {1\over 4!}z^4}(z)
\ +\qty{ {1\over 3}z^3 -{1\over 30}z^5 } 
\\ \\
{1\over 3}z^3 -{1\over 30}z^5 
&= \qty{1 - {1\over 2!}z^2 + {1\over 4!}z^4}\qty{{1\over 3} z^3}
\ +\qty{ \qty{ {1\over 6} - {1\over 30} } z^5 + \qty{ -{1\over 3\cdot 24} }z^7 } 
\\
&= \qty{1 - {1\over 2!}z^2 + {1\over 4!}z^4}\qty{{1\over 3} z^3}
\ + \qty{ {2\over 15}z^5 - {1\over 72}z^7 }
\\ \\
{ {2\over 15}z^5 - {1\over 72}z^7 }
&= \qty{1 - {1\over 2!}z^2 + {1\over 4!}z^4}\qty{{2\over 15} z^5} + \cdot
\\ \\
\implies \tan(z) &= z + {1\over 3}z^3 + {2\over 15 }z^5 + \bigo(z^7)
.\]

:::
