---
schema: qual/card@1
id: D-XC53X
kind: definition
title: Degree of a map of spheres
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $n\geq 1$ and let $f\colon S^n \to S^n$ be a continuous map.
Since $H^n(S^n;\ZZ) \cong \ZZ$, the induced homomorphism $f^*\colon H^n(S^n;\ZZ) \to H^n(S^n;\ZZ)$ is multiplication by a unique integer $d$, that is, $f^*(u) = d\,u$ for every $u\in H^n(S^n;\ZZ)$.
The \dfn{degree} of $f$ is $\deg f \coloneqq d$.
:::

::: {.proposition}
Let $n\geq 1$ and $f, g\colon S^n\to S^n$ be continuous.

(a) If $f$ and $g$ are [[D-Z7I7F|homotopic]], then $\deg f = \deg g$.

(b) $\deg f$ equals the integer $d'$ with $f_*(v) = d'\,v$ for every $v\in H_n(S^n;\ZZ)$.
:::

::: {.concept}
[@Hat02, §2.2, p. 134].
:::
