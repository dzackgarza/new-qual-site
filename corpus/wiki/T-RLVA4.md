---
schema: qual/card@1
id: T-RLVA4
kind: theorem
title: The Correspondence Theorem / 4th Isomorphism Theorem
classification:
  areas:
  - algebra
  topics:
  - Isomorphism Theorems
  - Normal Subgroups
  - Subgroups
relations: []
review: draft
---

:::{.theorem}
Suppose $N \normal G$, then there exists a correspondence:

\[  
\left\{
H < G \suchthat N \subseteq H
\right\}
\mapstofrom
\left\{
H \suchthat H < \frac G N
\right\}
\\
\correspond{
  \text{Subgroups of $G$} \\
  \text{containing $N$}
} \mapstofrom
\correspond{
  \text{Subgroups of the } \\
  \text{quotient $G/N$}
}
.\]

In words, subgroups of $G$ containing $N$ correspond to subgroups of the quotient group $G/N$. 
This is given by the map $H \mapsto H/N$.
:::
