---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-METRIC3
kind: problem
title: 'A decreasing sequence of nonnegative continuous functions converges uniformly to zero'
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - compactness
  - convergence-of-functions
relations: []
review: draft
---

:::{.problem title="?"}
(January 2017, 3) Let $(X,d)$ be a compact metric space. Suppose that $\{f_n:X\to[0,\infty)\}$ is a sequence
of continuous functions with $f_n(x)\ge f_{n+1}(x)$ for all $n\in\mathbb N$ and $x\in X$, and such that
$f_n\to0$ pointwise on $X$. Prove that $\{f_n\}_{n=1}^{\infty}$ converges uniformly on $X$.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Prove $f_n \to 0$ uniformly on compact metric $X$, given continuous $f_n: X \to [0, \infty)$, $f_n \ge f_{n+1}$ pointwise, and $f_n \to 0$ pointwise.

<1>1. Fix $\varepsilon > 0$. For each $x \in X$, choose $N(x)$ with $f_{N(x)}(x) < \varepsilon$.
    Proof: pointwise convergence $f_n(x) \to 0$; take $N(x)$ large enough that $f_{N(x)}(x) < \varepsilon$.

<1>2. The sets $U_N := \{x \in X : f_N(x) < \varepsilon\}$ are open and cover $X$.
    Proof: $U_N = f_N^{-1}(-\infty, \varepsilon)$ is open by continuity of $f_N$; and $x \in U_{N(x)}$ for each $x$ by <1>1.

<1>3. Finitely many $U_{N_1}, \ldots, U_{N_m}$ cover $X$; let $N_0 = \max_i N_i$.
    Proof: compactness of $X$ applied to the open cover of <1>2.

<1>4. For all $n \ge N_0$ and all $x \in X$: $f_n(x) < \varepsilon$.
    Proof: $x \in U_{N_i}$ for some $i$, so $f_{N_i}(x) < \varepsilon$; since the sequence is decreasing, $f_n(x) \le f_{N_i}(x) < \varepsilon$ for $n \ge N_i$, and $n \ge N_0 \ge N_i$.

<1>5. $f_n \to 0$ uniformly on $X$.
    Proof: <1>4 shows $\sup_X f_n \le \varepsilon$ for all $n \ge N_0$; since $f_n \ge 0$, $\|f_n\|_\infty \to 0$. (This is Dini's theorem in the special case of a decreasing sequence converging pointwise to $0$.)

:::
