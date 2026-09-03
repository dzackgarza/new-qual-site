---
schema: qual/card@1
id: E-MUN-2-2
kind: problem
title: Preimage preserves all set operations; image preserves unions only
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
---

::: {.exercise}

Let $f: A \to B$ and let $A_i \subset A$ and $B_i \subset B$ for $i = 0$ and $i = 1$ . Show that $f^-$

preserves inclusions, unions, intersections, and differences of sets:

(a) $B_0 \subset B_1 \Rightarrow f^{-1}(B_0) \subset f^{-1}(B_1)$ .

(b) $f^{-1}(B_{0} \cup B_{1}) = f^{-1}(B_{0}) \cup f^{-1}(B_{1}).$

(c) $f^{-1}(B_{0} \cap B_{1}) = f^{-1}(B_{0}) \cap f^{-1}(B_{1}).$

(d) $f^{-1}(B_0 - B_1) = f^{-1}(B_0) - f^{-1}(B_1)$ .

Show that $f$ preserves inclusions and unions only:

(e) $A_0 \subset A_1 \Rightarrow f(A_0) \subset f(A_1)$ .

(f) $f(A_{0} \cup A_{1}) = f(A_{0}) \cup f(A_{1}).$

(g) $f(A_0 \cap A_1) \subset f(A_0) \cap f(A_1)$ ; show that equality holds if $f$ is injective.

(h) $f(A_0 - A_1) \supset f(A_0) - f(A_1)$ ; show that equality holds if $f$ is injective.
:::
