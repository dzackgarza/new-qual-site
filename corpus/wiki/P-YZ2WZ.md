---
schema: qual/card@1
id: P-YZ2WZ
kind: problem
title: "This problem may be much harder than expected."
classification:
  areas:
  - real-analysis
  topics: []
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




