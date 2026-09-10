---
schema: qual/card@1
id: E-MGLSK
kind: problem
title: Right-continuous functions and the lower limit topology
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Suppose that $f: \mathbb{R} \to \mathbb{R}$ is "continuous from the right," that is,

$$
\lim_{x \to a^+} f(x) = f(a)
$$

for each $a \in \mathbb{R}$.
Show that $f$ is continuous when considered as a function from $\mathbb{R}_\ell$ to $\mathbb{R}$.

(b) Can you conjecture what functions $f: \mathbb{R} \to \mathbb{R}$ are continuous when considered as maps from $\mathbb{R}$ to $\mathbb{R}_\ell$?
As maps from $\mathbb{R}_\ell$ to $\mathbb{R}_\ell$?
We shall return to this question in Chapter 3.
:::

::: {.solution}
(a) Let $V\subseteq\mathbb R$ be open and let $a\in f^{-1}(V)$. Choose $\varepsilon>0$ with
\[
(f(a)-\varepsilon,f(a)+\varepsilon)\subseteq V.
\]
Right-continuity at $a$ gives $\delta>0$ such that
\[
a\le x<a+\delta\implies |f(x)-f(a)|<\varepsilon.
\]
Therefore
\[
[a,a+\delta)\subseteq f^{-1}(V).
\]
Since $[a,a+\delta)$ is a basic neighborhood of $a$ in $\mathbb R_\ell$, the preimage $f^{-1}(V)$ is open in $\mathbb R_\ell$. Hence $f:\mathbb R_\ell\to\mathbb R$ is continuous.

In fact this condition is also necessary, so maps $\mathbb R_\ell\to\mathbb R$ are exactly the ordinary right-continuous functions.

(b) A continuous map $\mathbb R\to\mathbb R_\ell$ must be constant. Indeed each basic set $[c,d)$ in $\mathbb R_\ell$ is both open and closed, so its inverse image is clopen in connected $\mathbb R$; hence every such inverse image is either empty or all of $\mathbb R$, forcing the image to be a singleton.

For maps $f:\mathbb R_\ell\to\mathbb R_\ell$, continuity is equivalent to the following one-sided condition: for every $a\in\mathbb R$ and every $\varepsilon>0$, there exists $\delta>0$ such that
\[
f([a,a+\delta))\subseteq[f(a),f(a)+\varepsilon).
\]
Necessity follows by applying continuity to the basic target neighborhood $[f(a),f(a)+\varepsilon)$. Conversely, if this condition holds, the inverse image of every basic lower-limit interval is open by exactly the same neighborhood argument. Equivalently, such functions are right-continuous and locally nondecreasing from the right.
:::
