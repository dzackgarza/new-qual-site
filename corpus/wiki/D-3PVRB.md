---
schema: qual/card@1
id: D-3PVRB
kind: definition
title: "The Infinity Norm / Essential supremum / Essentially bounded"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.definition title="The Infinity Norm / Essential supremum / Essentially bounded"}
\[
\norm{f}_\infty &\definedas \inf_{\alpha \geq 0} \theset{\alpha \suchthat \mu\qty{\theset{\abs{f} \geq \alpha}} = 0}
.\]
In words, this is the smallest upper bound that holds almost everywhere, so $\abs{f(x)} \leq \norm{f}_\infty$ holds for almost every $x$.
A function $f:X \to \CC$ is **essentially bounded** iff there exists a real number $c$ such that $\mu(\theset{\abs{f} > x}) = 0$, i.e. $\norm{f}_\infty < \infty$.
:::
