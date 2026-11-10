---
schema: qual/card@1
id: E-1QGID
kind: problem
title: Compactness, connectedness, and path connectedness of the K-topology line
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §27 Exercise 3, printed p. 178, with Exercise
    26.1(b) and Theorem 23.3; the three parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 27.3, PDF pp. 16-17. [0,1] is compact in the
    coarser usual topology; if it were compact in the K-topology the two would coincide by
    Exercise 26.1(b), which they do not. R_K minus 0 is two rays with the usual topology, so
    R_K is connected; and a path from 0 to 1 would make [0,1] compact in R_K.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Recall that $\RR_K$ denotes $\RR$ in the $K$-topology.

(a) Show that $[0, 1]$ is not compact as a subspace of $\RR_K$.

(b) Show that $\RR_K$ is connected.
[Hint: $(-\infty, 0)$ and $(0, \infty)$ inherit their usual topologies as subspaces of $\RR_K$.]

(c) Show that $\RR_K$ is not path connected.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 27.3, PDF pp. 16--17** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the three parts are theirs, with the citation in (b) repaired: $\overline K$ there means the closure of $K$ in the usual topology.

(a) $[0,1]$ is compact in the usual topology, hence in the coarser of the two topologies; if it were compact in the strictly finer $K$-topology, then by Exercise 26.1(b) the two topologies on $[0,1]$ would coincide, which they do not (the set $[0,1]-K$ is open in the $K$-topology and not in the usual one). So $[0,1]$ is not compact as a subspace of $\RR_{K}$.

(b) $\RR_{K}-\{0\}=(-\infty,0)\cup(0,\infty)$. The first piece inherits the usual topology. For the second, a $K$-basis element intersected with $(0,\infty)$ is $(a,b)\cap(0,\infty)$ or $((a,b)-K)\cap(0,\infty)=(a,b)\cap(0,\infty)-K$, a set open in the usual topology of $(0,\infty)$ (here $K\subset(0,\infty)$ and $K$ is closed in the usual topology). So $(0,\infty)$ inherits the usual topology, hence is connected; so are its closure $[0,\infty)$ and $(-\infty,0]$, and these two meet at $0$, so $\RR_{K}$ is connected by Theorem 23.3.

(c) If there were a path $f:[0,1]\to\RR_{K}$ from $0$ to $1$, then $f$ would be continuous as a map into $\RR$ (the usual topology being coarser), so by the intermediate value theorem $[0,1]\subset f([0,1])$; as $f([0,1])$ is compact in $\RR_{K}$ (continuous image of a compact space) and $[0,1]$ is closed in it, $[0,1]$ would be compact in $\RR_{K}$, contradicting (a). So $\RR_{K}$ is connected but not path connected.
:::
