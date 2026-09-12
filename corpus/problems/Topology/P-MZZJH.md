---
schema: qual/card@1
id: P-MZZJH
kind: problem
title: Genus of an $n$-sheeted cover of a closed surface
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Prove that if $p: M_g \to M_h$ is an $n$-sheeted covering space between connected, closed, orientable surfaces of genus $g$ and $h$, then:
$$g = n(h - 1) + 1.$$
:::

::: solution
<1>1. For a closed orientable surface of genus $r$,
$$
\chi(M_r)=2-2r.
$$

<1>2. Euler characteristic multiplies by the number of sheets in a finite covering:
$$
\chi(M_g)=n\,\chi(M_h).
$$
::: proof
Give $M_h$ a finite CW structure. Each open cell is evenly covered, and an $n$-sheeted covering has exactly $n$ lifts of each cell. Thus every cell count is multiplied by $n$, hence so is the alternating sum defining Euler characteristic.
:::

<1>3. Therefore
$$
2-2g=n(2-2h).
$$
Dividing by $2$ and rearranging gives
$$
g-1=n(h-1),
$$
so
$$
\boxed{g=n(h-1)+1}.
$$
:::
