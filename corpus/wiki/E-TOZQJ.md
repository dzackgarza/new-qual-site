---
schema: qual/card@1
id: E-TOZQJ
kind: exercise
title: "Residue from Laurent expansion: $1/(z - \\sin(z))$"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Residue from Laurent expansion: $1/(z - \sin(z))$"}
Use a direct Laurent expansion to show
\[
\Res_{z=0} {1\over z-\sin(z)} = {3! \over 5\cdot 4}
.\]

> Note the necessity: one doesn't know the order of the pole at zero, so it's unclear how many derivatives to take.

:::

:::{.solution}
Expand:
\[
{1\over z - \sin(z)}
&= z\inv \qty{1 - z\inv \sin(z) }\inv \\
&= z\inv \qty{1 - z\inv\qty{ z - {1\over 3!}z^3 + {1\over 5!} z^5 - \cdots}}\inv\\
&= z\inv \qty{1 - \qty{ 1 - {1\over 3!}z^2 + {1\over 5!} z^4 - \cdots}}\inv \\
&= z\inv \qty{{1\over 3!}z^2 - {1\over 5!}z^4 + \cdots}\inv \\
&= z\inv \cdot 3! z^{-2} \qty{1 - {1\over 5!/3!}z^2 + \cdots}\inv \\
&= {3!\over z^3} \qty{1 \over 1 - \qty{ {1\over 5\cdot 4}z^2 + \cdots}} \\
&= {3!\over z^3}\qty{1 + \qty{{1\over 5\cdot 4}z^2} + \qty{{1\over 5\cdot 4}z^2}^2 + \cdots} \\
&= 3! z^{-3} + {3!\over 5\cdot 4}z\inv + O(z) \\
.\]

:::

