---
schema: qual/card@1
id: E-XNYTJ
kind: problem
title: Monotone pointwise convergence to a continuous limit is uniform
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §26 Exercise 10, printed p. 171, with Exercise
    21.9; the theorem and both counterexample requests are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 26.10, PDF p. 13. Monotone pointwise convergence
    plus continuity of the terms and the limit gives uniform convergence by a finite
    subcover of the neighbourhoods on which the first N_x terms are within epsilon; the two
    examples show monotonicity and compactness are both needed. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
---

::: {.exercise}

(a) Prove the following partial converse to the uniform limit theorem.

Theorem.
Let $f_n: X \to \RR$ be a sequence of continuous functions, with $f_n(x) \to f(x)$ for each $x \in X$.
If $f$ is continuous, and if the sequence $f_n$ is monotone increasing, and if $X$ is compact, then the convergence is uniform.
[We say that $f_n$ is monotone increasing if $f_n(x) \leq f_{n+1}(x)$ for all $n$ and $x$.]

(b) Give examples to show that this theorem fails if you delete the requirement that $X$ be compact, or if you delete the requirement that the sequence be monotone.
[Hint: See the exercises of §21.]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 26.10, PDF p. 13** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both parts are theirs.

(a) Suppose $f_{n}\to f$ pointwise with $f_{n}\le f$ for all $n$ (monotone increasing), $f$ and each $f_{n}$ continuous, and $X$ compact.

Let $\varepsilon>0$. For $x\in X$ choose $N_{x}$ with $f(x)-f_{n}(x)<\varepsilon$ for $n\ge N_{x}$; by continuity of $f-f_{N_{x}}$ there is a neighbourhood $U_{x}$ of $x$ with $f(z)-f_{N_{x}}(z)<\varepsilon$ for all $z\in U_{x}$. The $U_{x}$ cover the compact $X$, so $U_{x_{1}},\dots,U_{x_{k}}$ do; let $N=\max\{N_{x_{1}},\dots,N_{x_{k}}\}$. Given $z$ and $n\ge N$, choose $i$ with $z\in U_{x_{i}}$; then $f(z)-f_{n}(z)\le f(z)-f_{N}(z)\le f(z)-f_{N_{x_{i}}}(z)<\varepsilon$. So $0\le f-f_{n}<\varepsilon$ everywhere for $n\ge N$: the convergence is uniform.

(b) Neither hypothesis can be dropped. *Monotonicity:* the functions $f_{n}(x)=1/(n^{3}[x-1/n]^{2}+1)$ restricted to the compact interval $[0,1]$ converge pointwise to $0$ without converging uniformly (Exercise 21.9). *Compactness:* $f_{n}(x)=\arctan(x+n)$ on $\RR$ converges pointwise, monotonically, to the constant $\pi/2$, but $f_{n}(-n)=0$ for every $n$, so the convergence is not uniform.
:::
