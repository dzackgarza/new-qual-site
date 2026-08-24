---
schema: qual/card@1
id: P-AMD-D7IX7C4G
kind: problem
title: No map $S^2\to S^1$ commuting with the antipodal map
classification:
  areas:
  - topology
  topics:
  - Degree
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
Show that there is no map $f: S^2 \to S^1$ that commutes with the antipodal map.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Prove that there does not exist any continuous map $f \colon S^2 \to S^1$ such that $f(-x) = -f(x)$ for all $x \in S^2$ (i.e. commuting with the antipodal map).

<1>1. Restrict $f$ to the equatorial circle $S^1 \subset S^2$.
<2>1. Let $i \colon S^1 \hookrightarrow S^2$ be the equatorial inclusion $x \mapsto (x_1, x_2, 0)$, and let $g = f|_{S^1} = f \circ i \colon S^1 \to S^1$.
<2>2. Since $f(-x) = -f(x)$ for all $x \in S^2$, the restriction $g$ satisfies $g(-x) = -g(x)$ for all $x \in S^1$.
<2>3. Every continuous odd map $g \colon S^1 \to S^1$ has odd degree $\deg(g) \equiv 1 \pmod 2$.
<3>1. Using the standard covering map $p \colon \mathbb{R} \to S^1$ given by $t \mapsto e^{2\pi i t}$, lift $g$ to a continuous map $\widetilde{g} \colon \mathbb{R} \to \mathbb{R}$.
<3>2. The condition $g(t + 1/2) = -g(t) = e^{i\pi} g(t)$ implies $\widetilde{g}(t + 1/2) - \widetilde{g}(t) = k + 1/2$ for some fixed integer $k \in \mathbb{Z}$.
<3>3. The degree of $g$ is $\deg(g) = \widetilde{g}(1) - \widetilde{g}(0) = (\widetilde{g}(1) - \widetilde{g}(1/2)) + (\widetilde{g}(1/2) - \widetilde{g}(0)) = 2(k + 1/2) = 2k + 1$.
<3>4. Thus $\deg(g) \neq 0$.
<3>5. Proof: Standard degree computation of odd maps on the circle.
Q.E.D.

<1>2. Extend $g$ to the upper hemisphere disk $D_+^2 \subset S^2$.
<2>1. The upper hemisphere $D_+^2 = \{(x_1, x_2, x_3) \in S^2 \mid x_3 \ge 0\}$ is homeomorphic to the 2-disk $D^2$, with boundary $\partial D_+^2 = S^1$.
<2>2. The map $F = f|_{D_+^2} \colon D_+^2 \to S^1$ is a continuous map extending $g$ to the entire disk $D_+^2$.
<2>3. If a continuous map $g \colon S^1 \to S^1$ extends to a continuous map $D^2 \to S^1$, then $g$ is nullhomotopic, which implies $\deg(g) = 0$.
<2>4. Proof: The inclusion $S^1 = \partial D^2 \hookrightarrow D^2$ is nullhomotopic since $D^2$ is contractible, so the induced homomorphism $g_* \colon \pi_1(S^1) \to \pi_1(S^1)$ is zero, meaning $\deg(g) = 0$.
Q.E.D.

<1>3. Derive contradiction.
<2>1. <1>1 shows $\deg(g) = 2k + 1 \neq 0$.
<2>2. <1>2 shows $\deg(g) = 0$.
<2>3. This contradiction proves no continuous odd map $f \colon S^2 \to S^1$ can exist.
<2>4. Proof: By <1>1 and <1>2. Q.E.D.

<1>4. Q.E.D. <2>1. Proof: By <1>3.
:::
