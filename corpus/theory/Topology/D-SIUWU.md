---
schema: qual/card@1
id: D-SIUWU
kind: definition
title: Short exact sequence
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring.
A \dfn{short exact sequence} of $R$-modules is an [[D-BJYH3|exact sequence]]
$$
0\to A\mapsvia{i}B\mapsvia{j}C\to0
$$
of $R$-modules and $R$-linear maps; equivalently, $i$ is injective, $j$ is surjective, and $\im i=\ker j$ [@Hat02].
It \dfn{splits} if there is an $R$-linear map $s\colon C\to B$ with $j\circ s=\id_C$.
:::

::: {.remark}
In a short exact sequence, $j$ induces an isomorphism $B/i(A)\cong C$.
:::

::: {.proposition title="Splitting lemma"}
For a short exact sequence $0\to A\mapsvia{i}B\mapsvia{j}C\to0$ of $R$-modules, the following are equivalent:

(a) there is an $R$-linear $s\colon C\to B$ with $j\circ s=\id_C$;

(b) there is an $R$-linear $r\colon B\to A$ with $r\circ i=\id_A$;

(c) there is an isomorphism $B\cong A\oplus C$ under which $i$ becomes $a\mapsto(a,0)$ and $j$ becomes $(a,c)\mapsto c$ [@Hat02].
:::
