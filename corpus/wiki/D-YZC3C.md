---
schema: qual/card@1
id: D-YZC3C
kind: definition
title: Uniform Convergence
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
relations: []
review: draft
---

:::{.definition title="Uniform Convergence"}
\[
(\forall \varepsilon>0)\left(\exists n_{0} = n_0(\eps) \right)(\forall x \in S)\left(\forall n>n_{0}\right)\left(\left|f_{n}(x)-f(x)\right|<\varepsilon\right)
.\]
Negated:[^Negated_uniform_convergence]
\[  
(\exists \varepsilon>0)\left(\forall n_{0} = n_0 (\eps) \right)(\exists x = x(n_0) \in S)\left(\exists n>n_{0}\right)\left(\left|f_{n}(x)-f(x)\right| \geq \varepsilon\right)
.\]

:::

[^Negated_uniform_convergence]: Slogan: to negate, find a bad $x$ depending on $n_0$ that are larger than some $\eps$.
