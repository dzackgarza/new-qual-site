---
schema: qual/card@1
id: P-CAS24G
kind: problem
title: Polynomial of an isolated singularity preserves singularity type
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Holomorphic Functions
relations: []
review: draft
solved: false
---

::: problem
Let $U \subset \mathbb{C}$ be an open set.
Let $f : U \setminus \{a\} \to \mathbb{C}$ be a holomorphic function with an isolated singularity at $a \in U$.

Let $P$ be a non-constant polynomial.
Let $g : U \setminus \{a\} \to \mathbb{C}$ be given by
\[
g(z) = P(f(z)).
\]

Show that:

(i) If $f$ has a removable singularity at $a$, then $g$ has a removable singularity at $a$.

(ii) If $f$ has a pole at $a$, then $g$ has a pole at $a$.

(iii) If $f$ has an essential singularity at $a$, then $g$ has an essential singularity at $a$.
:::
