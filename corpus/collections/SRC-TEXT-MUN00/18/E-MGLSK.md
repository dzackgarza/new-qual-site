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

(a) Suppose that $f: \RR \to \RR$ is "continuous from the right," that is,

$$
\lim_{x \to a^+} f(x) = f(a)
$$

for each $a \in \RR$.
Show that $f$ is continuous when considered as a function from $\RR_\ell$ to $\RR$.

(b) Can you conjecture what functions $f: \RR \to \RR$ are continuous when considered as maps from $\RR$ to $\RR_\ell$?
As maps from $\RR_\ell$ to $\RR_\ell$?
We shall return to this question in Chapter 3.
:::

::: {.solution}
(a) Let $V\subseteq\RR$ be open and let $a\in f^{-1}(V)$. Choose $\varepsilon>0$ with
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
Since $[a,a+\delta)$ is a basic neighborhood of $a$ in $\RR_\ell$, the preimage $f^{-1}(V)$ is open in $\RR_\ell$. Hence $f:\RR_\ell\to\RR$ is continuous.

In fact this condition is also necessary, so maps $\RR_\ell\to\RR$ are exactly the ordinary right-continuous functions.

(b) A continuous map $\RR\to\RR_\ell$ must be constant. Indeed each basic set $[c,d)$ in $\RR_\ell$ is both open and closed, so its inverse image is clopen in connected $\RR$; hence every such inverse image is either empty or all of $\RR$, forcing the image to be a singleton.

For maps $f:\RR_\ell\to\RR_\ell$, continuity is equivalent to the following one-sided condition: for every $a\in\RR$ and every $\varepsilon>0$, there exists $\delta>0$ such that
\[
f([a,a+\delta))\subseteq[f(a),f(a)+\varepsilon).
\]
Necessity follows by applying continuity to the basic target neighborhood $[f(a),f(a)+\varepsilon)$. Conversely, suppose the condition holds, and let $a\in f^{-1}([c,d))$. With $\varepsilon=d-f(a)$, the condition gives $\delta>0$ with $f([a,a+\delta))\subseteq[f(a),d)\subseteq[c,d)$, so $f^{-1}([c,d))$ is open in $\RR_\ell$. Equivalently, such functions are right-continuous and locally nondecreasing from the right.
:::
