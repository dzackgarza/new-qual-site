---
schema: qual/card@1
id: D-OAFF5
kind: definition
title: del and delbar operators
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

:::{.definition title="del and delbar operators"}
\[
\del \da \del_z \da {1\over 2}\qty{\del_x - i \del_y}
\quad
\text{ and }
\quad
\delbar
\da \del_{\bar z}
={1\over 2}\qty{ \del_x + i\del_y}
.\]
Moreover, the 1-form corresponding to $F$ can be written as 
\[
dF = \del F + \delbar F = \dd{F}{z} \dz + \dd{F}{\zbar}\dzbar
.\]

Written slightly more explicitly:
\[
\dd{F}{z} = {1\over 2}\qty{\dd{F}{x} + {1\over i}\dd{F}{y} } && 
\dd{F}{\zbar} = {1\over 2}\qty{\dd{F}{x} - {1\over i}\dd{F}{y} } 
.\]

:::
