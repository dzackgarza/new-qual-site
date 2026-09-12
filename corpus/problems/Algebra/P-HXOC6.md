---
schema: qual/card@1
id: P-HXOC6
kind: problem
title: Witt's theorem on real quadratic forms
classification:
  areas:
  - algebra
  topics:
  - Quadratic Forms
  - Bilinear Forms
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
State and explain Witt's Cancellation Theorem and Witt's Extension Theorem for quadratic forms (over $\mathbb{R}$ and general fields).
:::

::: solution
Assume throughout that the field $k$ has characteristic different from $2$ and that the quadratic spaces are finite-dimensional and nondegenerate.

**Witt extension theorem (Witt's lemma).** Let $(V,q)$ be a nondegenerate quadratic space. If $U,U'\subseteq V$ and
\[
f:U\xrightarrow{\sim}U'
\]
is an isometry, then there exists an isometry
\[
\widetilde f\in O(V,q)
\]
whose restriction to $U$ is $f$.

A standard proof proceeds by induction on $\dim U$, using reflections in anisotropic vectors and hyperbolic pairs to extend the isometry one vector at a time. The nondegeneracy of $V$ is the hypothesis that makes the extension possible even when the subspace $U$ itself is degenerate.

**Witt cancellation theorem.** If
\[
U\perp W_1\cong U\perp W_2
\]
for nondegenerate quadratic spaces, then
\[
W_1\cong W_2.
\]
More generally, if $U_1\cong U_2$ and
\[
U_1\perp W_1\cong U_2\perp W_2,
\]
then $W_1\cong W_2$.

To see cancellation from extension, identify the two copies of $U$ inside an ambient isometric quadratic space. The isometry between those copies extends by Witt's theorem to an ambient isometry. After composing with that extension, the original ambient isometry fixes $U$; therefore it carries the orthogonal complement $U^\perp=W_1$ onto the orthogonal complement $U^\perp=W_2$.

Over $\mathbb R$, Sylvester's law of inertia gives the concrete classification: every nondegenerate quadratic form is isometric to
\[
x_1^2+\cdots+x_p^2-y_1^2-\cdots-y_q^2,
\]
and the pair $(p,q)$ is a complete isometry invariant. Witt cancellation is then also immediate from additivity of signature under orthogonal direct sum.
:::
