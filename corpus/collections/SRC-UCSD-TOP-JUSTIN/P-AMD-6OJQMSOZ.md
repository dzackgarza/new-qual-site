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

::: pf

::: pf-step
Reduce to showing there is no odd continuous map $g \colon S^2 \to S^1$.

::: pf-proof

::: pf-step
Suppose for contradiction that there exists a continuous map $f \colon S^2 \to \mathbb{R}^2$ such that $f(x) \neq f(-x)$ for all $x \in S^2$.
:::

::: pf-step
Define $F \colon S^2 \to \mathbb{R}^2 \setminus \{0\}$ by $F(x) = f(x) - f(-x)$.
:::

::: pf-step
$F$ is continuous and antipodal-preserving (odd): $F(-x) = f(-x) - f(x) = -F(x)$.
:::

::: pf-step
Define $g \colon S^2 \to S^1$ by $g(x) = \frac{F(x)}{\|F(x)\|}$.
:::

::: pf-step
The map $g$ is continuous and odd: $g(-x) = \frac{-F(x)}{\|-F(x)\|} = -g(x)$ for all $x \in S^2$.

::: pf-proof
The map $g$ is the composition of the continuous map $F$ with the continuous normalization $y \mapsto y/\|y\|$, so it is continuous; the oddness follows from $F(-x) = -F(x)$.
:::

:::

:::

:::

::: {.pf-step #s2}
Restrict $g$ to the equatorial circle $S^1 \subset S^2$.

::: pf-proof

::: pf-step
Let $h = g|_{S^1} \colon S^1 \to S^1$.
:::

::: pf-step
Since $g$ is odd on $S^2$, $h$ is an odd map on $S^1$: $h(-x) = -h(x)$ for all $x \in S^1$.
:::

::: pf-step
Every continuous odd map $h \colon S^1 \to S^1$ has odd degree $\deg(h) \equiv 1 \pmod 2$.

::: pf-proof

::: pf-step
Parameterize $S^1$ by $[0, 1] / (0 \sim 1)$ via $t \mapsto e^{2\pi i t}$.
Antipodal points correspond to $t$ and $t + 1/2$.
:::

::: pf-step
Lift $h$ to a continuous map $\widetilde{h} \colon \mathbb{R} \to \mathbb{R}$ via the covering map $p(t) = e^{2\pi i t}$.
:::

::: pf-step
The condition $h(t + 1/2) = -h(t) = e^{i\pi} h(t)$ means $p(\widetilde{h}(t + 1/2)) = p(\widetilde{h}(t) + 1/2)$.
:::

::: pf-step
Thus $\widetilde{h}(t + 1/2) - \widetilde{h}(t) = k + 1/2$ for some fixed integer $k \in \mathbb{Z}$ (by connectedness of $\mathbb{R}$).
:::

::: pf-step
The degree of $h$ is given by the total shift over the period 1: $$\deg(h) = \widetilde{h}(1) - \widetilde{h}(0) = (\widetilde{h}(1) - \widetilde{h}(1/2)) + (\widetilde{h}(1/2) - \widetilde{h}(0)) = 2(k + 1/2) = 2k + 1.$$
:::

::: pf-step
Thus $\deg(h) = 2k + 1$ is an odd integer, and in particular $\deg(h) \neq 0$.

::: pf-proof
The lift $\widetilde{h}$ exists by the lifting criterion for the universal cover $\mathbb{R} \to S^1$; the oddness condition forces the half-period shift to be a half-integer, and the degree is the total shift over one period, which is therefore odd.
:::

:::

:::

:::

:::

:::

::: {.pf-step #s3}
Obtain a contradiction via the upper hemisphere disk.

::: pf-proof

::: pf-step
Let $D_+^2 = \{(x_1, x_2, x_3) \in S^2 \mid x_3 \ge 0\}$ be the closed upper hemisphere.
:::

::: pf-step
$D_+^2$ is homeomorphic to the closed 2-disk $D^2$, and its boundary is $\partial D_+^2 = S^1$ (the equator).
:::

::: pf-step
The restriction $g|_{D_+^2} \colon D_+^2 \to S^1$ is a continuous extension of $h = g|_{S^1}$ to the entire disk $D_+^2$.
:::

::: pf-step
If a continuous map $h \colon S^1 \to S^1$ extends to a continuous map $D^2 \to S^1$, then $h$ is nullhomotopic, so $\deg(h) = 0$.

::: pf-proof
The disk $D^2$ is contractible, so the inclusion $\iota \colon S^1 \hookrightarrow D^2$ induces the zero map on $\pi_1(S^1)$; hence $h_* = (g|_{D^2} \circ \iota)_* = 0$, so $\deg(h) = 0$.
:::

:::

:::

:::

::: {.pf-step #s4}
Derive the final contradiction.

::: pf-proof

::: pf-step
By step [](#s2){.pf-ref}, $\deg(h)$ is odd (so $\deg(h) \neq 0$).
:::

::: pf-step
By step [](#s3){.pf-ref}, $\deg(h) = 0$.
:::

::: pf-step
This contradiction shows no such odd map $g \colon S^2 \to S^1$ exists.
:::

::: pf-step
Hence for any continuous $f \colon S^2 \to \mathbb{R}^2$, there exists $x \in S^2$ such that $f(x) = f(-x)$.

::: pf-proof
Step [](#s2){.pf-ref} shows $\deg(h)$ is odd, while step [](#s3){.pf-ref} shows $\deg(h) = 0$; this contradiction rules out the existence of an odd map $g \colon S^2 \to S^1$, and hence of a map $f$ with $f(x) \neq f(-x)$ everywhere.
:::

:::

:::

:::

::: pf-qed
Step [](#s4){.pf-ref} establishes the result.
:::

:::
:::
