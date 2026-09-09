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
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $S \coloneqq \{z \in \mathbb{D} \mid \operatorname{Im}(z) \ge 0\}$ be the closed upper half of the unit disk $\mathbb{D}$.
Suppose $f: S \to \mathbb{C}$ is continuous on $S$, real-valued on $S \cap \mathbb{R} = (-1, 1)$, and holomorphic on the interior $S^\circ = \{z \in \mathbb{D} \mid \operatorname{Im}(z) > 0\}$.

Prove that $f$ extends to a holomorphic function on the entire unit disk $\mathbb{D}$ (the Schwarz Reflection Principle).
:::

::: solution
Define
\[
F(z)=
\begin{cases}
f(z),&\Im z\ge0,\\
\overline{f(\overline z)},&\Im z<0.
\end{cases}
\]
Because $f(x)\in\mathbb R$ for $-1<x<1$, the two formulas agree continuously on the real diameter. Thus $F$ is continuous on $\mathbb D$.

On the lower half-disk, $z\mapsto\overline{f(\overline z)}$ is holomorphic. Indeed, if $w=\overline z$, then its derivative is
\[
\overline{f'(w)}.
\]
Hence $F$ is holomorphic off the real diameter.

To cross the diameter, apply Morera's theorem. For any triangle $T\Subset\mathbb D$, split $T$ along the real axis into finitely many polygons lying in the upper and lower half-disks. Approximate any boundary segment on the real axis by parallel segments at heights $\pm\varepsilon$. Cauchy's theorem applies away from the axis, and continuity of $F$ lets $\varepsilon\to0$. Thus
\[
\oint_{\partial T}F(z)\,dz=0.
\]
Morera's theorem implies that $F$ is holomorphic on all of $\mathbb D$. By construction $F=f$ on the upper half-disk.
:::
