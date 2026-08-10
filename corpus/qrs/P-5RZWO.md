---
schema: qual/card@1
id: P-5RZWO
kind: problem
title: "1. Lemma: $f$ is injective $\\iff f$ has a left inverse $f\\inv$ satisfy\u2026"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

1. Lemma: $f$ is injective $\iff f$ has a left inverse $f\inv$ satisfying $f\inv f(a) = a$.

   Suppose $f,g: A \to A$ are injective and $x,y \in A$, we want to show that $(f\circ g)(x) = (f\circ g)(y) \implies x = y$.
   So suppose $f(g(x)) = f(g(y))$.
   Since $f$ is injective, $f$ has a left inverse, so $g(x) = g(y)$, and since $g$ is injective $x = y$.
   $\qed$
