---
schema: qual/card@1
id: T-NBARV
kind: theorem
title: "Classification of Surfaces"
classification:
  areas:
  - topology
  topics:
  - classification
  - surfaces
  - euler-characteristic
relations: []
review: draft
---
:::{.theorem title="Classification of Surfaces"}
The set of surfaces under connect sum forms a monoid with the presentation
\[  
\gens{ \SS^2, \RP^2, \TT \suchthat \SS^2 = 0, 3\RP^2 = \RP^2 + \TT^2} = \ts{ \Sigma_{g, n} \st g, n \in \ZZ^{\geq 0} } 
.\]
where $\Sigma_{g, n}$ is a surface of genus $g$ with $n$ discs removed to form boundary components.

Surfaces are classified up to homeomorphism by orientability and $\chi$, or equivalently "genus" 

- In orientable case, actual genus, $g$ equals the number of copies of $\TT^2$.
- In nonorientable case, $k$ equals the number of copies of $\RP^2$.

In each case, there is a formula
\[  
\chi(X) = 
\begin{cases}
2-2g - b & \text{orientable} \\
2 - k & \text{non-orientable}.
\end{cases}
\]
:::
