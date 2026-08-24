---
schema: qual/card@1
id: E-HAT-3.B-2
kind: exercise
title: "Chain homotopy as a chain map on the cone"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
---

Let $C$ and $C'$ be chain complexes, and let $I$ be the chain complex consisting of $\mathbb{Z}$ in dimension 1 and $\mathbb{Z} \times \mathbb{Z}$ in dimension 0, with the boundary map taking a generator $e$ in dimension 1 to the difference $v_1 - v_0$ of generators $v_i$ of the two $\mathbb{Z}$'s in dimension 0. Show that a chain map $f: I \otimes C \to C'$ is precisely the same as a chain homotopy between the two chain maps $f_i: C \to C'$, $c \mapsto f(v_i \otimes c)$, $i = 0, 1$.
[The chain homotopy is $h(c) = f(e \otimes c)$.]
