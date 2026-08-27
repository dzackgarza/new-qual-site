---
schema: qual/card@1
id: P-AMD-6OJQMSOZ
kind: problem
title: Borsuk–Ulam theorem for maps $S^2\to\mathbb{R}^2$
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove that for any $f: S^2 \to \mathbb{R}^2$, there exists $x\in S^2$ such that $f(x) = f(-x)$.
:::

::: {.solution}
**Goal:** Prove the Borsuk-Ulam theorem in dimension 2: for every continuous map $f \colon S^2 \to \mathbb{R}^2$, there exists a point $x \in S^2$ such that $f(x) = f(-x)$.

<1>1. Reduce to showing there is no odd continuous map $g \colon S^2 \to S^1$.
<2>1. Suppose for contradiction that there exists a continuous map $f \colon S^2 \to \mathbb{R}^2$ such that $f(x) \neq f(-x)$ for all $x \in S^2$.
<2>2. Define $F \colon S^2 \to \mathbb{R}^2 \setminus \{0\}$ by $F(x) = f(x) - f(-x)$.
<2>3. $F$ is continuous and antipodal-preserving (odd): $F(-x) = f(-x) - f(x) = -F(x)$.
<2>4. Define $g \colon S^2 \to S^1$ by $g(x) = \frac{F(x)}{\|F(x)\|}$.
<2>5. The map $g$ is continuous and odd: $g(-x) = \frac{-F(x)}{\|-F(x)\|} = -g(x)$ for all $x \in S^2$.
<2>6. Proof: By construction.
Q.E.D.

<1>2. Restrict $g$ to the equatorial circle $S^1 \subset S^2$.
<2>1. Let $h = g|_{S^1} \colon S^1 \to S^1$.
<2>2. Since $g$ is odd on $S^2$, $h$ is an odd map on $S^1$: $h(-x) = -h(x)$ for all $x \in S^1$.
<2>3. Every continuous odd map $h \colon S^1 \to S^1$ has odd degree $\deg(h) \equiv 1 \pmod 2$.
<3>1. Parameterize $S^1$ by $[0, 1] / (0 \sim 1)$ via $t \mapsto e^{2\pi i t}$.
Antipodal points correspond to $t$ and $t + 1/2$.
<3>2. Lift $h$ to a continuous map $\widetilde{h} \colon \mathbb{R} \to \mathbb{R}$ via the covering map $p(t) = e^{2\pi i t}$.
<3>3. The condition $h(t + 1/2) = -h(t) = e^{i\pi} h(t)$ means $p(\widetilde{h}(t + 1/2)) = p(\widetilde{h}(t) + 1/2)$.
<3>4. Thus $\widetilde{h}(t + 1/2) - \widetilde{h}(t) = k + 1/2$ for some fixed integer $k \in \mathbb{Z}$ (by connectedness of $\mathbb{R}$). <3>5. The degree of $h$ is given by the total shift over the period 1: $$\deg(h) = \widetilde{h}(1) - \widetilde{h}(0) = (\widetilde{h}(1) - \widetilde{h}(1/2)) + (\widetilde{h}(1/2) - \widetilde{h}(0)) = 2(k + 1/2) = 2k + 1.$$ <3>6. Thus $\deg(h) = 2k + 1$ is an odd integer, and in particular $\deg(h) \neq 0$.
<3>7. Proof: By lifting criterion on the universal cover of $S^1$.
Q.E.D.

<1>3. Obtain a contradiction via the upper hemisphere disk.
<2>1. Let $D_+^2 = \{(x_1, x_2, x_3) \in S^2 \mid x_3 \ge 0\}$ be the closed upper hemisphere.
<2>2. $D_+^2$ is homeomorphic to the closed 2-disk $D^2$, and its boundary is $\partial D_+^2 = S^1$ (the equator).
<2>3. The restriction $g|_{D_+^2} \colon D_+^2 \to S^1$ is a continuous extension of $h = g|_{S^1}$ to the entire disk $D_+^2$.
<2>4. If a continuous map $h \colon S^1 \to S^1$ extends to a continuous map $D^2 \to S^1$, then $h$ is nullhomotopic, so $\deg(h) = 0$.
<2>5. Proof: The disk $D^2$ is contractible, so the inclusion $\iota \colon S^1 \hookrightarrow D^2$ induces the zero map on $\pi_1(S^1)$, meaning $h_* = (g|_{D^2} \circ \iota)_* = 0$, so $\deg(h) = 0$.
Q.E.D.

<1>4. Derive the final contradiction.
<2>1. By <1>2, $\deg(h)$ is odd (so $\deg(h) \neq 0$). <2>2. By <1>3, $\deg(h) = 0$.
<2>3. This contradiction shows no such odd map $g \colon S^2 \to S^1$ exists.
<2>4. Hence for any continuous $f \colon S^2 \to \mathbb{R}^2$, there exists $x \in S^2$ such that $f(x) = f(-x)$.
<2>5. Proof: By <1>1–<1>3. Q.E.D.

<1>5. Q.E.D. <2>1. Proof: By <1>4.
:::
