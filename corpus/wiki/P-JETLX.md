---
schema: qual/card@1
id: P-JETLX
kind: problem
title: "Let $f\\in L^1((0, 2\\pi))$."
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - density
  - l1
relations: []
review: draft
solved: true
---

::: problem
Let $f\in L^1((0, 2\pi))$.

i. Show that for an \( \epsilon>0 \) one can write $f = g+h$ where $g\in L^2((0, 2\pi))$ and $\norm{H}_1 < \epsilon$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Reduce to nonnegative $f$: write $f = f^+ - f^-$ and handle each part; the claim is additive.
Assume $f \ge 0$.
Proof: if $f^+ = g_1 + h_1$ and $f^- = g_2 + h_2$ with $g_i \in L^2$, $\|h_i\|_1 < \eps/2$, then $f = (g_1 - g_2) + (h_1 - h_2)$ with $g_1 - g_2 \in L^2$ and $\|h_1 - h_2\|_1 < \eps$.

<1>2. Truncate: let $g(x) = \min(f(x), M)$ and $h = f - g = \max(f - M, 0)$ for $M > 0$.
Proof: $g, h \ge 0$, measurable, $f = g + h$.

<1>3. $g \in L^2((0, 2\pi))$.
Proof: $g \le M$ pointwise and $g \le f \in L^1$; so $\int g^2 \le M\int g \le M\|f\|_1 < \infty$.

<1>4. $\|h\|_1 \to 0$ as $M \to \infty$.
Proof: $h = (f - M)^+ \downarrow 0$ pointwise as $M \to \infty$ and $h \le f \in L^1$; dominated convergence.

<1>5. Q.E.D.: choose $M$ with $\|h\|_1 < \eps$; then $f = g + h$ with $g \in L^2$ and $\|h\|_1 < \eps$.
Proof: <1>3, <1>4. (Note: the card's second symbol $\norm{H}_1$ is read as $\|h\|_1$ — the truncated part; the argument is the standard $L^2$-density-via-truncation.)
:::
