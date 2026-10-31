---
schema: qual/card@1
id: P-UCTOP290-S6-1-TORUS
kind: problem
title: Homology of a torus with an attached disk
classification:
  areas:
  - topology
  topics:
  - Simplicial Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 6, Problem 1 in the PDF page image; the source does not specify the disk attaching circle.
---

::: {.problem}
Give a simplicial or $\Delta$-complex model and compute
the integral homology of “the torus with a disc attached
inside it.” Describe generators.
:::

::: {.solution}

Triangulate $T^2$ so that the attaching circle
$\gamma$ is a subcomplex, then attach a
triangulated disk. If
$[\gamma]=(p,q)\in H_1(T^2;\ZZ)\cong\ZZ^2$,
the cellular boundary of the new two-cell is
$(p,q)$. Consequently
$$
H_1\cong\ZZ^2/\langle(p,q)\rangle,\qquad
H_2\cong
\begin{cases}
\ZZ^2,&(p,q)=(0,0),\\
\ZZ,&(p,q)\ne(0,0),
\end{cases}
$$
and $H_0=\ZZ$. In degree two, the torus
fundamental class always survives; when
$(p,q)=0$, a bounding two-chain for $\gamma$
combined with the new disk gives the second
generator.

The source does not specify the attaching circle.
If “inside” means the boundary of an embedded
disk in the torus, then $(p,q)=0$ and the groups
are $\ZZ,\ZZ^2,\ZZ^2$ in degrees $0,1,2$.
:::
