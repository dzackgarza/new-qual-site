---
schema: qual/card@1
id: P-KRYFQ
kind: problem
title: "Suppose $\\phi\\in L^1(\\RR)$ with"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Suppose $\phi\in L^1(\RR)$ with 
\[  
\int \phi(x) \, dx = \alpha
.\]
For each $\delta > 0$ and $f\in L^1(\RR)$, define
\[  
A_\delta f(x) \da \int f(x-y) \delta^{-1} \phi\qty{\delta^{-1} y}\, dy
.\]

a.
Prove that for all $\delta > 0$,
\[  
\norm{A_\delta f}_1 \leq \norm{\phi}_1 \norm{f}_1
.\]

b.
Prove that 
\[  
A_\delta f \to \alpha f \text{ in } L^1(\RR) \qtext{as} \delta\to 0^+
.\]

> Hint: you may use without proof the fact that for all $f\in L^1(\RR)$,
\[  
\lim_{y\to 0} \int_\RR \abs{f(x-y) - f(x)}\, dx = 0
.\]

