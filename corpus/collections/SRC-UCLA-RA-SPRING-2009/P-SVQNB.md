---
schema: qual/card@1
id: P-SVQNB
kind: problem
title: A nonconstant entire function with $f(1-z)=1-f(z)$ is surjective
classification:
  areas:
  - real-analysis
  topics:
  - Entire Functions
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f$ be an entire non-constant function that satisfies the functional equation $$f(1-z) = 1-f(z)$$ for all $z\in\mathbb{C}$.
Show that $f(\mathbb{C})=\mathbb{C}$.
:::

::: {.solution}
The functional equation implies that $w\in\text{Im}(f)$ if and only if $1-w\in\text{Im}(f)$.
Thus suppose that there were some $w\notin \text{Im}(f)$, then $1-w\notin\text{Im}(f)$ either, so $f$ misses two points (if $w\ne 1/2$). But Picard's little theorem says that an entire function that misses two points is constant, a contradiction.
Thus $f$ hits everything except possibly $1/2$.
But putting $z=1/2$ into the functional equation gives $f(1/2)=1-f(1/2)$, so $f(1/2)=1/2$.
Thus $f$ is surjective.
$\square$
:::
