---
schema: qual/card@1
id: P-PGDPX
kind: problem
title: A measurable set with a gap between any two points and no isolated points
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - counterexamples
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Does there exist a nonempty measurable set $E \subset \mathbb{R}$ satisfying the following two properties:

a. given $x,y \in E$, there exists $z \notin E$ that lies between $x$ and $y$;
b. $E$ has no isolated points?
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Yes; take $E = \mathbb{R}\setminus\mathbb{Q}$, the set of irrational numbers.
<1>2. (a) holds for $E$.
    Proof: given $x, y \in E$ with $x < y$, the rationals are dense in $\mathbb{R}$, so there is a rational $z \in (x, y)$; then $z \notin E$ and $z$ lies between $x$ and $y$.
<1>3. (b) holds for $E$.
    Proof: $E$ has no isolated points. Indeed, given $x \in E$ (irrational) and $\epsilon > 0$, the interval $(x-\epsilon, x+\epsilon)$ is uncountable while $\mathbb{Q}$ is countable, so it contains an irrational $x' \ne x$; every punctured neighborhood of $x$ meets $E$.
<1>4. Q.E.D.
:::
