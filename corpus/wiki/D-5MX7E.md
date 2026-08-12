---
schema: qual/card@1
id: D-5MX7E
kind: definition
title: "Colimit"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
:::{.definition title="Colimit"}
For a directed system $(X_{i}, f_{ij})$, the **colimit** is an object $X$ with a sequence of projections $\pi_{i}:X\to X_{i}$ such that for any $Y$ mapping into the system, the following diagram commutes:

\begin{tikzcd}
                 &                            &  & Y \arrow[lldddd, "\psi_{j}"] \arrow[rrdddd, "\psi_{i}"] \arrow[dd, "\exists!", dashed] &  &               &        \\
                 &                            &  &                                                                                    &  &               &        \\
                 &                            &  & X \arrow[lldd, "\pi_{j}"] \arrow[rrdd, "\pi_{i}"]                                      &  &               &        \\
                 &                            &  &                                                                                    &  &               &        \\
\cdots \arrow[r] & X_{j} \arrow[rrrr, "f_{ij}"] &  &                                                                                    &  & X_{i} \arrow[r] & \cdots
\end{tikzcd}

:::{.example title="of colimits"}
\envlist

- Products
- Pullbacks
- Inverse / projective limits
- The \( p\dash \)adic integers \( \ZZ_{p} \).
:::

:::
