---
schema: qual/card@1
id: E-ENJAF
kind: problem
title: Laurent series of $e^{1/z}\cos(1/z)$ at its essential singularity $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Essential Singularities
  - Power Series
relations: []
review: draft
---

::: {.exercise}
Find a Laurent expansion at $z=0$ for
\[
f(z) \definedas e^{1\over z}\cos\qty{1\over z}
.\]

:::

::: {.solution}
Let $g(z) \definedas e^z\cos(z)$, an entire function with $g(1/z ) = f(z)$ for $z\ne0$.
The Taylor series of $g$ at $0$, evaluated at $1/z$, is the Laurent series of $f$ on $\abs z>0$:
\[
g(z) 
&= e^{z}\cos(z)\\
&= {1\over 2}e^z\qty{e^{iz} + e^{-iz}} \\
&= {1\over 2}\qty{e^{(1+i)z} + e^{(1-i)z}} \\
&= {1\over 2} \sum_{k\geq 0}\qty{(1+i)^k + (1-i)^k} {z^k\over k!} \\
\implies f(z) 
&= {1\over 2} \sum_{k\geq 0}\qty{(1+i)^k + (1-i)^k} {1 \over k!z^k } \\
.\]

:::

