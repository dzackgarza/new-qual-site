---
schema: qual/card@1
id: S-4S7BD
kind: solution
title: Solution to P-SVQNB
classification:
  areas:
  - real-analysis
  topics:
  - entire-functions
  - holomorphic-functions
relations:
- kind: solves
  target: P-SVQNB
review: draft
---

:::{.solution}
The functional equation implies that $w\in\text{Im}(f)$ if and only if $1-w\in\text{Im}(f)$. Thus suppose that there were some $w\notin \text{Im}(f)$, then $1-w\notin\text{Im}(f)$ either, so $f$ misses two points (if $w\ne 1/2$). But Picard's little theorem says that an entire function that misses two points is constant, a contradiction. Thus $f$ hits everything except possibly $1/2$. But putting $z=1/2$ into the functional equation gives $f(1/2)=1-f(1/2)$, so $f(1/2)=1/2$. Thus $f$ is surjective. $\square$
:::
