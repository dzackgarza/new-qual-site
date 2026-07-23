---
schema: qual/card@1
id: P-R3DSM
kind: problem
title: "Prove the following inequality, and explain when equality holds:"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Prove the following inequality, and explain when equality holds:
\[
\abs{z-w} \geq \abs{ \abs{z} - \abs{w} }
.\]

:::

:::{.solution}
\[
\abs{z-w}^2 
&= (z-w)(\bar z - \bar w) \\
&= \abs{z}^2 + \abs{w}^2 - z\bar{w} - \bar{z} w \\
&= \abs{z}^2 + \abs{w}^2 - 2\Re(\bar w z) \\
&\geq \abs{z}^2 + \abs{w}^2 - 2\abs{\bar w }\abs{z} \\
&\geq \qty{ \abs{z} - \abs{w} }^2
,\]
and taking square roots introduces an absolute value on the final term.
Here we've used the basic estimate 
\[
\Re(z) \leq \abs{z} \implies -\Re(z) \geq -\abs{z}
.\]



:::

