---
schema: qual/card@1
id: PR-KGHJ2
kind: proposition
title: Stabilizers of points in the same orbit are conjugate
slogan: 'Points in one orbit have conjugate stabilizers.'
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Conjugacy
  - Group Actions
relations: []
review: draft
---

::: {.proposition}
Let a group $G$ [[D-WYC7C|act]] on a set $X$, and let $x_0, x_1 \in X$ lie in the same orbit, say $x_1 = g \cdot x_0$ with $g \in G$.
Then the stabilizers satisfy $G_{x_1} = g\, G_{x_0}\, \inverseof{g}$.
In particular, if $G$ acts transitively on $X$, all stabilizers are conjugate.
:::

::: {.proof}
For $h\in G$,
$$
\begin{aligned}
h\in G_{x_0} &\iff h\cdot x_0 = x_0 \\
&\iff h\inverseof{g}\cdot x_1 = \inverseof{g}\cdot x_1 \\
&\iff gh\inverseof{g}\cdot x_1 = x_1 \\
&\iff gh\inverseof{g} \in G_{x_1},
\end{aligned}
$$
so $g\,G_{x_0}\,\inverseof{g} \subseteq G_{x_1}$, and the same equivalences read backwards give $\inverseof{g}\,G_{x_1}\,g\subseteq G_{x_0}$.
Hence $G_{x_1} = g\, G_{x_0}\, \inverseof{g}$.
If the action is transitive, any two points lie in one orbit, so all stabilizers are conjugate.
:::
