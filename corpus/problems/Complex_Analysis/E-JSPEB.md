---
schema: qual/card@1
id: E-JSPEB
kind: problem
title: Using the estimates
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
---

:::{.exercise}
Suppose $f: \DD\to \DD$ with $f(0) = 0$ and $\abs{f(z)} \leq \abs{e^z}$ when $\abs{z} = 1$.
Find an upper bound for $f\qty{1+i\over 2}$.

:::

:::{.solution}
Consider $g(z) \da f(z)/e^z$ -- since $g(0) = 0$ and $g: \DD\to \DD$, Schwarz applies and 
\[
\abs{g(z)}\leq \abs{z} \implies \abs{f(z)} \leq \abs{ze^z} \leq e\abs{z}
.\]
So
\[
\abs{f\qty{1+i\over 2}} \leq e\abs{1+i\over 2}= {e\sqrt{2} \over 2}
.\]
:::
