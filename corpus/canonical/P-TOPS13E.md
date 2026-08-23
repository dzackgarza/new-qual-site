---
schema: qual/card@1
id: P-TOPS13E
kind: problem
title: "No antipodal-preserving map from R^3 minus origin to R^2"
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
  - Fundamental Group
relations: []
review: draft
solved: false
---

::: problem
Prove by contradiction that there does not exist a continuous map $f : \mathbb{R}^3 \setminus \{0\} \to \mathbb{R}^2$ with the property that $f(x) \neq f(-x)$ for all $x \in \mathbb{R}^3 \setminus \{0\}$.

Hint: Define $g : \mathbb{R}^3 \setminus \{0\} \to S^1$ by
$$
g(x) = \frac{f(x) - f(-x)}{|f(x) - f(-x)|},
$$
which satisfies $g(-x) = -g(x)$. Define the loop $\eta : I \to \mathbb{R}^3 \setminus \{0\}$ by $\eta(s) = (\cos(2\pi s), \sin(2\pi s), 0)$ and consider the loop $h = g \circ \eta$ in $S^1$.
:::