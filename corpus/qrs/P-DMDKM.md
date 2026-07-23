---
schema: qual/card@1
id: P-DMDKM
kind: problem
title: "Let $f\\in L^1(\\RR)$ and let \\( \\mathcal{U}\\da \\ts{(x, y) \\in \\RR^2 \\st\u2026"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $f\in L^1(\RR)$ and let \( \mathcal{U}\da \ts{(x, y) \in \RR^2 \st y > 0}  \) denote the upper half plane.
For $(x, y) \in \mathcal{U}$ define 
\[
u(x, y) \da f \convolve P_y(x) && \text{where } P_y(x) \da {1\over \pi}\qty{y \over t^2 + y^2}
.\]

a. Prove that there exists a constant $C$ independent of $f$ such that for all $x\in \RR$, 
\[
\sup_{y > 0} \abs{ u(x, y) } \leq C\cdot Hf(x)
.\]


    *Hint: write the following and try to estimate each term:*
\[
u(x, y) = \int_{\abs t < y} f(x - t) P_y(t) \dt + \sum_{k=0}^{\infty } \int_{A_k} f(x-t) P_y(t)\dt && A_k \da \ts{2^ky \leq \abs t < 2^{k+1}y}
.\]

b. Following the proof of the Lebesgue differentiation theorem, show that for $f\in L^1(\RR)$ and for almost every $x\in \RR$,
\[
u(x, y) \converges{y\to 0} \to f(x)
.\]

