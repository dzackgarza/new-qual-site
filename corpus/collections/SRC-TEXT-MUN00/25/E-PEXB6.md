---
schema: qual/card@1
id: E-PEXB6
kind: exercise
title: The comb space and a nowhere locally connected path-connected set
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Let $X$ denote the rational points of the interval $[0, 1] \times 0$ of $\mathbb{R}^2$.
Let $T$ denote the union of all line segments joining the point $p = 0 \times 1$ to points of $X$.

(a) Show that $T$ is path connected, but is locally connected only at the point $p$.

(b) Find a subset of $\mathbb{R}^2$ that is path connected but is locally connected at none of its points.
:::

::: {.solution}
<1>1. Part (a): Path-connectedness and local connectedness of $T$:
<2>1. $T$ is the union of straight line segments $[p, q]$ for $q \in X = ([0, 1] \cap \mathbb{Q}) \times \{0\}$, where $p = (0, 1)$.
Since every segment $[p, q]$ contains $p$, $T$ is star-shaped with respect to the apex $p$.
Thus for any $z \in T$, the segment $[p, z] \subset T$ connects $z$ to $p$, so $T$ is path connected.
::: {.proof}
star-shaped spaces are path connected.
:::
<2>2. **Local connectedness at $p$:**
For any $\varepsilon > 0$, the open ball $B(p, \varepsilon) \cap T$ is star-shaped with respect to $p$, because for each segment $[p, q]$, the intersection $[p, q] \cap B(p, \varepsilon)$ is a connected line segment containing $p$.
Thus $B(p, \varepsilon) \cap T$ is a connected open neighborhood of $p$ in $T$, so $T$ is locally connected at $p$.
::: {.proof}
star-shaped open balls are connected.
:::
<2>3. **Disconnection at all points $z \neq p$:**
Let $z = (x_0, y_0) \in T$ with $z \neq p$, so $y_0 < 1$.
Choose $0 < \varepsilon < 1 - y_0$, so that the ball $B(z, \varepsilon)$ does not contain $p$.
In $B(z, \varepsilon)$, the intersection $B(z, \varepsilon) \cap T$ consists of disjoint line segments along rays emanating from $p$ through rational points in $X$.
Between any two rational rays, there are uncountably many missing irrational rays, so every connected component of $B(z, \varepsilon) \cap T$ is a single line segment.
Since a single line segment has empty interior in $T$, no connected component of $B(z, \varepsilon) \cap T$ is a neighborhood of $z$.
Thus $T$ has no basis of connected neighborhoods at $z$, so $T$ is not locally connected at $z$.
::: {.proof}
components in $B(z, \varepsilon) \cap T$ are 1-dimensional slices with empty interior.
:::

<1>2. Part (b): A nowhere locally connected path-connected subset of $\mathbb{R}^2$:
<2>1. Define two families of line segments:
\[
A = \bigcup_{q \in [0, 1] \cap \mathbb{Q}} \big[(0, 1), (q, 0)\big], \qquad B = \bigcup_{r \in [0, 1] \cap \mathbb{Q}} \big[(0, 0), (r, 1)\big].
\]
Let $Y = A \cup B \subset [0, 1] \times [0, 1]$.
::: {.proof}
definition of double broom / crossed comb space.
:::
<2>2. **Path-connectedness:**
$A$ is path connected (apex $(0, 1)$), $B$ is path connected (apex $(0, 0)$), and $A \cap B \neq \emptyset$ (for instance, the segments $[(0, 1), (1, 0)] \subset A$ and $[(0, 0), (1, 1)] \subset B$ intersect at $(1/2, 1/2)$).
Thus $Y = A \cup B$ is path connected.
::: {.proof}
union of path-connected spaces with non-empty intersection.
:::
<2>3. **Nowhere locally connected:**
- At any point $z \in Y \setminus \{(0, 0), (0, 1)\}$, small neighborhoods do not contain either apex and are disconnected by the density of missing irrational rays in both families $A$ and $B$.
- At the apex $p_1 = (0, 1)$, any open ball $B(p_1, \varepsilon)$ intersects infinitely many disjoint line segments from family $B$ whose endpoints on $y=1$ are rational points other than $(0, 1)$; these segments cannot connect to $(0, 1)$ inside $B(p_1, \varepsilon)$.
- Symmetrically, at $p_0 = (0, 0)$, $B(p_0, \varepsilon)$ intersects infinitely many disconnected segments of $A$.
Therefore, $Y$ fails to be locally connected at every point $z \in Y$.
::: {.proof}
isolation of transversal rational rays.
:::

<1>3. Conclusion:
$T$ is path connected and locally connected precisely at $p$, and $Y = A \cup B$ is path connected and nowhere locally connected. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
