---
schema: qual/card@1
id: P-E6JSI
kind: problem
title: Schwarz reflection of a holomorphic function across the diameter of the disk
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $S \coloneqq \{z \in \mathbb{D} \mid \operatorname{Im}(z) \ge 0\}$ be the closed upper half of the unit disk $\mathbb{D}$.
Suppose $f: S \to \mathbb{C}$ is continuous on $S$, real-valued on $S \cap \mathbb{R} = (-1, 1)$, and holomorphic on the interior $S^\circ = \{z \in \mathbb{D} \mid \operatorname{Im}(z) > 0\}$.

Prove that $f$ extends to a holomorphic function on the entire unit disk $\mathbb{D}$ (the Schwarz Reflection Principle).
:::

::: solution
**Goal:** Prove that the reflection extension $F: \mathbb{D} \to \mathbb{C}$ defined by $F(z) = f(z)$ for $\operatorname{Im}(z) \ge 0$ and $F(z) = \overline{f(\bar{z})}$ for $\operatorname{Im}(z) < 0$ is holomorphic on $\mathbb{D}$.

<1>1. Definition of the Extended Function $F(z)$:
    *Proof:*
    <2>1. Define the extension $F: \mathbb{D} \to \mathbb{C}$ by:
        $$F(z) = \begin{cases} f(z) & \text{if } \operatorname{Im}(z) \ge 0, \\ \overline{f(\bar{z})} & \text{if } \operatorname{Im}(z) < 0. \end{cases}$$
    <2>2. Let $S^- = \{z \in \mathbb{D} \mid \operatorname{Im}(z) \le 0\}$ be the lower half-disk, and let $I = (-1, 1) = S \cap S^-$.

<1>2. Continuity of $F$ on $\mathbb{D}$:
    *Proof:*
    <2>1. $F$ is continuous on $S^\circ$ and on $(S^-)^\circ$: on $S^\circ$ it is $f(z)$, and on $(S^-)^\circ$ it is $\overline{f(\bar z)}$, and each of these is a composition of continuous maps ($z \mapsto \bar{z}$, $w \mapsto \bar{w}$, and the holomorphic $f$ are all continuous).
    <2>2. On the real diameter $I = (-1, 1)$, for any $x \in I$:
        - From the upper half-plane: $\lim_{z \to x, \operatorname{Im}(z) \ge 0} F(z) = f(x)$.
        - From the lower half-plane: $\lim_{z \to x, \operatorname{Im}(z) < 0} F(z) = \lim_{\bar{z} \to x} \overline{f(\bar{z})} = \overline{f(x)}$.
    <2>3. Since $f$ is real-valued on $I$, $\overline{f(x)} = f(x)$.
    <2>4. Both one-sided limits agree and equal $F(x) = f(x)$, so $F$ is **continuous on all of $\mathbb{D}$**.

<1>3. Holomorphicity on the Lower Half-Disk:
    *Proof:*
    <2>1. For $z_0 \in (S^-)^\circ$, we compute the complex derivative of $F(z) = \overline{f(\bar{z})}$:
        $$\lim_{h \to 0} \frac{F(z_0 + h) - F(z_0)}{h} = \lim_{h \to 0} \frac{\overline{f(\bar{z}_0 + \bar{h})} - \overline{f(\bar{z}_0)}}{h} = \overline{\lim_{h \to 0} \frac{f(\bar{z}_0 + \bar{h}) - f(\bar{z}_0)}{\bar{h}}} = \overline{f'(\bar{z}_0)}.$$
    <2>2. Since $\bar{z}_0 \in S^\circ$ and $f$ is holomorphic on $S^\circ$, the limit exists.
    <2>3. Thus $F$ is holomorphic on $(S^-)^\circ$.

<1>4. Holomorphicity across the Real Axis via Morera's Theorem:
    *Proof:*
    <2>1. By **Morera's Theorem**, a continuous function on a domain is holomorphic if and only if $\oint_\triangle F(z) \, dz = 0$ for every closed triangle $\triangle \subset \mathbb{D}$.
    <2>2. Let $\triangle \subset \mathbb{D}$ be any closed triangle:
        - **Case 1:** $\triangle$ lies entirely in $S$ or entirely in $S^-$.
            By Cauchy's Theorem on simply connected domains, $\oint_\triangle F(z) \, dz = 0$.
        - **Case 2:** $\triangle$ intersects the real axis $I$.
            Subdivide $\triangle$ into smaller triangles and polygons that lie entirely in $S$ or $S^-$, with one edge along $I$.
            For a polygon $P$ with an edge $[a, b] \subset I$, by shifting the boundary slightly away from $I$ by $\varepsilon > 0$ and using uniform continuity of $F$ as $\varepsilon \to 0$:
            $$\oint_{\partial P} F(z) \, dz = \lim_{\varepsilon \to 0^+} \oint_{\partial P_\varepsilon} F(z) \, dz = 0.$$
    <2>3. Summing over the subdivision, all interior edge integrals cancel, giving:
        $$\oint_\triangle F(z) \, dz = 0.$$
    <2>4. By Morera's Theorem, $F$ is holomorphic on the entire disk $\mathbb{D}$.

<1>5. Conclusion:
    $F(z)$ is holomorphic on $\mathbb{D}$ and restricts to $f(z)$ on $S$. Q.E.D.
:::
