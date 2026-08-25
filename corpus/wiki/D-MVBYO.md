---
schema: qual/card@1
id: D-MVBYO
kind: definition
title: Comparability of topologies
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Continuity
relations: []
review: draft
---

::: {.definition title="Comparability of topologies"}
Given two topologies $\tau_1, \tau_2$,

- $\tau_1$ is **finer/stronger/larger** than $\tau_2$ iff $\tau_1 \contains \tau_2$ (idea: finer resolutions).

- $\tau_1$ is **coarser/weaker/smaller** than $\tau_2$ iff $\tau_1 \iscontainedin \tau_2$.

Two topologies are **comparable** if either $\tau_1 \subseteq \tau_2$ or $\tau_2 \subseteq \tau_1$.

::: {.remark}
The set of all topologies on a given set $X$ forms a complete lattice bounded under inclusion:

- $\sup(\tau_1, \tau_2) = \tau_1 \union \tau_2$

  - The finest topology is the discrete topology $\tau_{\terminal} \da 2^X$, where every set is open.

- $\inf(\tau_1, \tau_2) = \gens{\tau_1 \intersect \tau_2}$, the topology *generated* by the intersection.

  - The coarsest topology is the indiscrete topology $\tau_{\initial} \da \ts{\emptyset, X}$.

If $f:X\to Y$, then

- Increasing $\tau(X)$ or decreasing $\tau(Y)$ makes it *easier* for $f$ to be continuous, i.e. every map continuous with respect to $\tau_1(X)$ will remain continuous with respect to $\tau_2(X)$.
  Writing $\tau_1(X) \to \tau_2(X) \iff \tau_1(X) \leq \tau_2(X)$,

\begin{tikzcd}
	{\tau_2(X)} && {\Hom_\Top(\tau_2(X), \tau(Y))} \\
	\\
	{\tau_1(X)} && {\Hom_\Top(\tau_1(X), \tau(Y))}
	\arrow[""{name=0, anchor=center, inner sep=0}, from=3-1, to=1-1]
	\arrow[""{name=1, anchor=center, inner sep=0}, from=3-3, to=1-3]
	\arrow["{\Hom_\Top(\wait, Y)}", shorten <=19pt, shorten >=19pt, Rightarrow, from=0, to=1]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNCxbMCwyLCJcXHRhdV8xKFgpIl0sWzAsMCwiXFx0YXVfMihYKSJdLFsyLDAsIlxcSG9tX1xcVG9wKFxcdGF1XzIoWCksIFxcdGF1KFkpKSJdLFsyLDIsIlxcSG9tX1xcVG9wKFxcdGF1XzEoWCksIFxcdGF1KFkpKSJdLFswLDFdLFszLDJdLFs0LDUsIlxcSG9tX1xcVG9wKFxcd2FpdCwgWSkiLDAseyJzaG9ydGVuIjp7InNvdXJjZSI6MjAsInRhcmdldCI6MjB9fV1d)

\begin{tikzcd}
	{\tau_2(Y)} && {\Hom_\Top(\tau(X), \tau_2(Y))} \\
	\\
	{\tau_1(Y)} && {\Hom_\Top(\tau(X), \tau_2(Y))}
	\arrow[""{name=0, anchor=center, inner sep=0}, from=3-1, to=1-1]
	\arrow[""{name=1, anchor=center, inner sep=0}, from=1-3, to=3-3]
	\arrow["{\Hom_\Top(X, \wait)}", shorten <=19pt, shorten >=19pt, Rightarrow, from=0, to=1]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNCxbMCwyLCJcXHRhdV8xKFkpIl0sWzAsMCwiXFx0YXVfMihZKSJdLFsyLDAsIlxcSG9tX1xcVG9wKFxcdGF1KFgpLCBcXHRhdV8yKFkpKSJdLFsyLDIsIlxcSG9tX1xcVG9wKFxcdGF1KFgpLCBcXHRhdV8yKFkpKSJdLFswLDFdLFsyLDNdLFs0LDUsIlxcSG9tX1xcVG9wKFgsIFxcd2FpdCkiLDAseyJzaG9ydGVuIjp7InNvdXJjZSI6MjAsInRhcmdldCI6MjB9fV1d)

- Decreasing $\tau(X)$ or increasing $\tau(Y)$ makes it *easier* for $f$ to be an open map.

- For a fixed $X$, decreasing $\tau(X)$ makes it *easier* for sequences to converge in $X$.
:::

::: {.example}
Write $\tau_\zar(X)$ for the Zariski topology on a space and $\tau_{\an}(X)$ for the classical/Euclidean topology.
Then $\tau_\zar(\CC^n) < \tau_{\an}(\CC^n)$, i.e. the Zariski topology is strictly weaker than the Euclidean topology and has fewer open sets.
:::
:::
