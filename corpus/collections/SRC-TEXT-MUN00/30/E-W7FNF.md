---
schema: qual/card@1
id: E-W7FNF
kind: problem
title: The lower limit line and the ordered square are not metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Ana Emilia de Orellana, "Solutions -
    Topology Munkres", Section 30 Exercise 6, printed p. 31
    (tmp/sources/munkres-solutions-anadeore.pdf), checked against Munkres, Topology (2000),
    Section 30 Exercise 6, printed p. 194, and against Example 3 (printed p. 192, R_l is Lindelof)
    and Example 5 (printed p. 193, I_o^2 is compact). Orellana's route is the one on the card:
    R_l is separable and Lindelof and not second countable, so by Exercise 30.5 it is not
    metrizable; and I_o^2 is compact, so a metrization would make it second countable and hence
    separable, which it is not. What was corrected: Orellana writes only "I_o^2 is compact ...
    then it also cannot be metrizable, because it is not separable", leaving the non-separability
    unproved; the card exhibits the uncountably many pairwise disjoint open vertical intervals
    {x} x (0,1) that no countable set can meet. Note that the rational points of I_o^2 are not
    dense: an interval {x} x (0,1) with x irrational meets Q x Q in no point.
---

::: {.exercise}

Show that $\RR_\ell$ and $I_o^2$ are not metrizable.
:::

::: {.solution}
For the lower limit line $\RR_\ell$, the rationals are dense, so the space is separable. If it were metrizable, every separable metric space would be second countable. But $\RR_\ell$ is not second countable: if $\mathcal B$ were a basis, then for each $x\in\RR$ choose $B_x\in\mathcal B$ with
$$
x\in B_x\subset[x,x+1).
$$
If $x<y$, then $x\in B_x$ while $x\notin B_y\subset[y,y+1)$, so $B_x\ne B_y$. Thus $x\mapsto B_x$ injects the uncountable set $\RR$ into $\mathcal B$, contradicting countability. Hence $\RR_\ell$ is not metrizable.

For the ordered square $I_o^2=[0,1]\times[0,1]$ in the dictionary order topology, the open vertical intervals
$$
\{x\}\times(0,1),\qquad x\in[0,1],
$$
form an uncountable family of pairwise disjoint nonempty open sets. Therefore $I_o^2$ is not separable. The ordered square is compact. If it were metrizable, compact metrizability would imply second countability, hence separability, contradiction. Thus $I_o^2$ is not metrizable.
:::
