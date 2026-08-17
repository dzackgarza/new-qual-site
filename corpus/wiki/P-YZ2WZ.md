---
schema: qual/card@1
id: P-YZ2WZ
kind: problem
title: "This problem may be much harder than expected."
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - fubini-tonelli
relations: []
review: draft
---
:::{.warnings}
This problem may be much harder than expected.
Recommended skip.
:::


Let $f: \RR \cross \RR \to \RR$ be a measurable function and for $x\in \RR$ define the set
\[
E_x \da \ts{ y\in \RR \st \mu\qty{ z\in \RR \st f(x,z) = f(x, y) } > 0 } 
.\]
Show that the following set is a measurable subset of $\RR \cross \RR$:
\[
E \da \Union_{x\in \RR} \ts{ x } \cross E_x
.\]

> Hint: consider the measurable function $h(x,y,z) \da f(x, y) - f(x, z)$.
::: {.solution}
> **AI-Generated Solution**

<1>1. Reformulate via the hint.
    Proof: let $h(x,y,z) = f(x,y) - f(x,z)$, measurable on $\RR^3$, and let
    \[
    A \da \big\{(x,y,z) \in \RR^3 : h(x,y,z) = 0\big\} = \big\{(x,y,z) : f(x,y) = f(x,z)\big\},
    \]
    which is measurable (preimage of $\{0\}$ under a measurable function).
<1>2. For fixed $x, y$, the vertical section $A_{x,y} = \{z : (x,y,z) \in A\}$ satisfies $\mu(A_{x,y}) = \mu\{z : f(x,z) = f(x,y)\}$.
    Proof: by definition of $A$ in <1>1.
<1>3. The map $(x,y) \mapsto \mu(A_{x,y})$ is measurable.
    Proof: by Tonelli's theorem applied to the measurable non-negative function $\chi_A$ on $\RR^3$,
    \[
    (x,y) \mapsto \int_{\RR} \chi_A(x,y,z)\,dz = \mu(A_{x,y})
    \]
    is measurable (the partial integral of a measurable non-negative function over one variable is a measurable function of the remaining variables).
<1>4. $E$ is measurable.
    Proof: by <1>2 and <1>3,
    \[
    E = \Union_{x\in\RR}\{x\} \times E_x = \big\{(x,y) : \mu(A_{x,y}) > 0\big\},
    \]
    the superlevel set of a measurable function, hence measurable.
<1>5. Q.E.D.
:::
