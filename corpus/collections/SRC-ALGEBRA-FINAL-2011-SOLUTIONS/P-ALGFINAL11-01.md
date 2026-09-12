---
schema: qual/card@1
id: P-ALGFINAL11-01
kind: problem
title: Classify groups of order 105
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let G be a group of order 105.

(a) Show that G has a normal subgroup of order 5 or 7. [points]:[4]

(b) Show that G has a cyclic normal subgroup of order 35. [4]

(c) Show that the Sylow 5- and 7-subgroups of G are both normal.
[3]

(d) Classify groups of order 105.
:::

::: {.solution}
(a) If a Sylow 5-subgroup F is not normal, then it has $1 + 5 k$ conjugates where $k \geq 1$ and 1 + 5k divides $1 0 5 / 5 = 2 1$ , whence $1 + 5 k = 2 1$ and there are $2 1 \cdot 4 = 8 4$ elements of order 5. Similarly if a Sylow 7-subgroup S is not normal, then there are $1 5 \cdot 6 = 9 0$ elements of order 7. Since $8 4 + 9 0 > 1 0 5$ , at least one of F and S must be normal.

(b) Since at least one of F and S is normal, and (clearly) $| F \cap S | = 1$ , therefore $F S < G$ is a subgroup of order 35. Since 5 doesn’t divide $7 - 1$ , every group of order 35 is cyclic.

(c) The cyclic group F S has unique subgroups of orders 5 and 7, so it has 31 elements of order $\neq 5 .$ , and 29 elements of order $\neq 7$ . Hence, and since $| G | = 1 0 5 , G$ cannot have 84 elements of order 5 or 90 of order $7 ;$ so by the proof of (a), both F and S are normal.

(d) As in (b), if T is the Sylow 3-subgroup, then, since $S \triangleleft G$ , therefore $T S < G$ is a subgroup of order 21, a complement of $F \triangleleft G$ . Since $\lvert \mathrm { A u t } ( F ) \rvert = 4$ , any homomorphism $T S \to \operatorname { A u t } ( F )$ is trivial; and consequently G is the direct product $T S \times F$ . There are, up to isomorphism, just two groups of order 21, and one of order $5 ;$ correspondingly, there are just two possibilities for G.
:::
