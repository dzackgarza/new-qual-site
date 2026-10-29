---
schema: qual/card@1
id: P-WESTOP04-05
kind: problem
title: Classify a surface obtained from a labeled hexagon
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: "Direct inspection of page 3 of assets/attachments/topology_2005-2003.pdf confirms that the printed cyclic word is abaca^{-1}c^{-1}. Thus the source itself is inconsistent with its instruction to identify the six edges in pairs: a occurs three times, b once, and c twice."
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source printed the word abaca^{-1}c^{-1}, in which a occurs three times and b once, so it defines no pairing. The statement now uses abacb^{-1}c^{-1}, changing the fifth letter; each one-letter repair that replaces an a by b gives the same surface, the connected sum of three projective planes.
---

::: {.problem}
1. List the compact connected surfaces up to homeomorphism.

2. Form a surface from a hexagon by identifying its boundary edges in pairs according to the cyclic word
   $$
   abac b^{-1}c^{-1},
   $$
   and identify the resulting compact connected surface.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The compact connected surfaces are, up to homeomorphism,
$$
\boxed{
S^2,\qquad
\#^g(S^1\times S^1)\ (g\ge1),\qquad
\#^k\RP^2\ (k\ge1).}
$$


::: pf-proof

This is the classification theorem for compact connected surfaces.
The orientable surfaces are the sphere and the connected sums of
$g$ tori.
The nonorientable surfaces are the connected sums of
$k$ real projective planes.

:::

:::

::: {.pf-step #s1-2}

The quotient $S$ of the hexagon has one vertex, three edges and one face, so $\chi(S)=-1$.

::: pf-proof

Name the hexagon's vertices $v_0,\ldots,v_5$ in order, so the six edges, read as the word $abacb^{-1}c^{-1}$, are
$$
a:v_0\to v_1,\quad
b:v_1\to v_2,\quad
a:v_2\to v_3,\quad
c:v_3\to v_4,\quad
b:v_5\to v_4,\quad
c:v_0\to v_5.
$$
Matching initial and terminal points of equally labeled edges gives
$$
a:\ v_0\sim v_2,\ v_1\sim v_3;\qquad
b:\ v_1\sim v_5,\ v_2\sim v_4;\qquad
c:\ v_3\sim v_0,\ v_4\sim v_5.
$$
These relations join $v_0\sim v_2\sim v_4\sim v_5\sim v_1\sim v_3$, so all six vertices become one point. The quotient CW structure has one $0$-cell, three $1$-cells $a,b,c$ and one $2$-cell, so
$$
\chi(S)=1-3+1=-1.
$$

:::

:::

::: {.pf-step #s1-3}

The surface $S$ is nonorientable.

::: pf-proof

The letter $a$ occurs twice in the word with the same exponent. The two $a$-edges, together with a band in the hexagon joining them, form a Möbius band in $S$, so $S$ is nonorientable.

:::

:::

::: {.pf-step #s1-4}

$$
\boxed{S\cong\RP^2\#\RP^2\#\RP^2.}
$$

::: pf-proof

By step [](#s1-1){.pf-ref} and step [](#s1-3){.pf-ref}, $S\cong\#^k\RP^2$ for some $k\ge1$, and $\chi(\#^k\RP^2)=2-k$. Step [](#s1-2){.pf-ref} gives $2-k=-1$, so $k=3$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (1), and step [](#s1-4){.pf-ref} answers part (2).

:::

:::

:::
