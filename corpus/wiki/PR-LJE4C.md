---
schema: qual/card@1
id: PR-LJE4C
kind: proposition
title: "Correspondence Theorem for Ideals"
classification:
  areas:
  - algebra
  topics:
  - isomorphism-theorems
  - ideals
  - rings
relations: []
review: draft
---
:::{.proposition title="Correspondence Theorem for Ideals"}
For $I\in \Id(R)$, the canonical quotient map $\phi: R \to R/I$ induces a bijective correspondence:
\[
\correspond{
  J \in \Id(R) \st J\contains I
}
&\mapstofrom
  \Id(R/I) \\
J \da \phi\inv(\bar J) &\mapsfrom \bar{J} \\
J &\mapsto \bar{J} \da \phi(J) 
,\]
where $\phi: R\to R/I$ is the canonical quotient morphism.

More traditionally:

- If $S, I \in \Id(R)$ with $S$ containing $I$ then
\[
S/I \leq R/I
.\]

- Every ideal in $\Id(R/I)$ is of the form $\bar{S} \da S/I$ for some $S\in \Id(R)$ containing $I$.

- The **third isomorphism theorem** is the last bullet only: if $I, J \in \Id(R)$ with $I \subseteq J \subseteq R$ then there is an isomorphism
\[
{R/I \over J/I} \mveq {R\over J}
.\]

Moreover, $A\leq R$ is a subring containing $I$ iff $A/I$ is a subring of $R/I$.
The correspondence carries subrings to subrings and ideals to ideals; a subring of $R$ containing $I$ need not be an ideal.
:::
