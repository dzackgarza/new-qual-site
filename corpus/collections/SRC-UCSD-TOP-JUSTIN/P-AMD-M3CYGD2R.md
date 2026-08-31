---
schema: qual/card@1
id: P-AMD-M3CYGD2R
kind: problem
title: Homology of $\RP^2$, $T^2$, and $S^1 \cup_{z^n} B^2$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
  - Quotient Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Compute the homology of:

1. $\RP^2 = M \union_\del D^2$

2. $T^2 = S^1 \cross S^1 = (S^1\cross I)\union_f (S^1\cross I)$ where $(x,0) \sim (x,1) \sim (\bar x, 0) \in \CC$

3. $S^1 \union_{f} B^2$ attached along $\del B^2$ using $z\mapsto z^n$
:::

::: {.solution}
**Goal.** Compute the homology of $\RP^2$, $T^2$, and $S^1 \cup_{z^n} B^2$.

<1>1. $H_*(\RP^2)$.
<2>1. $\RP^2 = M \cup_\partial D^2$ (Möbius band with a disk attached along its boundary).
::: {.proof}
the standard cell structure of $\RP^2$.
:::
<2>2. $H_0(\RP^2) = \ZZ$, $H_1(\RP^2) = \ZZ/2$, $H_2(\RP^2) = 0$.
::: {.proof}
the cellular chain complex is $\ZZ \xrightarrow{2} \ZZ \xrightarrow{0} \ZZ$ (the attaching map of the $2$-cell has degree $2$), giving $H_0 = \ZZ$, $H_1 = \ZZ/2$, $H_2 = 0$.
:::

<1>2. $H_*(T^2)$.
<2>1. $T^2 = S^1 \times S^1$ has cell structure with one $0$-cell, two $1$-cells, one $2$-cell.
::: {.proof}
standard.
:::
<2>2. $H_0(T^2) = \ZZ$, $H_1(T^2) = \ZZ \oplus \ZZ$, $H_2(T^2) = \ZZ$.
::: {.proof}
the cellular chain complex is $\ZZ \xrightarrow{0} \ZZ^2 \xrightarrow{0} \ZZ$ (all boundary maps zero), giving $H_0 = \ZZ$, $H_1 = \ZZ^2$, $H_2 = \ZZ$.
:::

<1>3. $H_*(S^1 \cup_{z^n} B^2)$.
<2>1. The space is $S^1$ with a $2$-cell attached along the map $z \mapsto z^n$ (degree $n$).
::: {.proof}
the attaching map $\partial B^2 = S^1 \to S^1$ is $z \mapsto z^n$, of degree $n$.
:::
<2>2. The cellular chain complex is $\ZZ \xrightarrow{n} \ZZ \xrightarrow{0} \ZZ$.
::: {.proof}
the $2$-cell attaches with degree $n$, so $\partial_2$ is multiplication by $n$; $\partial_1 = 0$.
:::
<2>3. $H_0 = \ZZ$, $H_1 = \ZZ/n$, $H_2 = 0$.
::: {.proof}
$H_0 = \ZZ$; $H_1 = \ZZ/n\ZZ$ (the cokernel of multiplication by $n$); $H_2 = \ker(n) = 0$ (multiplication by $n$ is injective).
:::

<1>4. Q.E.D.
::: {.proof}
<1>1, <1>2, <1>3 give the three homology computations.
:::
:::
