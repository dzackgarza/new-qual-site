---
schema: qual/card@1
id: P-BLQCR
kind: problem
title: "a."
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
a.
Let $f: \RR \to \RR$. Prove that
$$
f(x) \leq \liminf_{y\to x} f(y)~ \text{for each}~ x\in {\RR} \iff \{ x\in {\RR} \mid f(x) > a \}~\text{is open for all}~ a\in {\RR}
$$


b.
Recall that a function $f: {\RR} \to {\RR}$ is called *lower semi-continuous* iff it satisfies either condition in part (a) above.

Prove that if $\mathcal{F}$ is any family of lower semi-continuous functions, then 
$$
g(x) = \sup\{ f(x) \mid f\in \mathcal{F}\}
$$
is Borel measurable.

> Note that $\mathcal{F}$ need not be a countable family.


