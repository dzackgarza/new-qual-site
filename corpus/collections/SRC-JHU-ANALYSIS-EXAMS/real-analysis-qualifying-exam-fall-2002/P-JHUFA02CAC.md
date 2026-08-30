---
schema: qual/card@1
id: P-JHUFA02CAC
kind: problem
title: "Equicontinuity and the Arzela-Ascoli theorem on a Sobolev family"
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Arzela-Ascoli Theorem
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

3.i. Define equicontinuity and state the Arzela-Ascoli theorem.

ii.Let $\mathcal { F }$ be the family of real valued functions on [0,1] satisfying $f ( 0 ) = 0$ and $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ^ { \prime } ( x ) ^ { 2 } \ d x \leq 1 } \end{array}$ Show that any sequence in $\mathcal { F }$ has a subsequence that converges uniformly.

::: solution
**Goal:** Define equicontinuity and then prove relative compactness for $\mathcal F$.

<1>1. Equicontinuity:
    *Proof:*  
    A family $\mathcal H\subset C([0,1])$ is equicontinuous at $x_0$ if for every
    $\varepsilon>0$ there is $\delta>0$ such that
    $|x-y|<\delta\Rightarrow |h(x)-h(y)|<\varepsilon$ for every $h\in\mathcal H$.
    It is equicontinuous on $[0,1]$ if this holds at every $x_0$.

<1>2. Arzelà–Ascoli:
    *Proof:*  
    If a family in $C([0,1])$ is pointwise bounded and equicontinuous, then every
    sequence has a uniformly convergent subsequence.

<1>3. Pointwise boundedness for $\mathcal F$:
    *Proof:*  
    Let $f\in\mathcal F$. For $x\in[0,1]$, by Cauchy--Schwarz,
    $$|f(x)-f(0)|\le
    \left(\int_0^x 1^2\,dt\right)^{1/2}\left(\int_0^x |f'(t)|^2\,dt\right)^{1/2}
    \le\sqrt{x}\le1,$$
    and $f(0)=0$, so $|f(x)|\le1$.

<1>4. Equicontinuity for $\mathcal F$:
    *Proof:*  
    Let $x,y\in[0,1]$ with $x>y$ and $f\in\mathcal F$. Again by Cauchy--Schwarz,
    $$|f(x)-f(y)|
    =\left|\int_y^x f'(t)\,dt\right|
    \le \left(\int_y^x 1\,dt\right)^{1/2}
    \left(\int_y^x |f'(t)|^2\,dt\right)^{1/2}
    \le \sqrt{|x-y|}.$$
    For $\varepsilon>0$, pick $\delta=\varepsilon^2$. Then $|x-y|<\delta$
    implies $|f(x)-f(y)|<\varepsilon$ for all $f\in\mathcal F$.

<1>5. Conclusion:
    *Proof:*  
    By <2>, any sequence in $\mathcal F\subset C([0,1])$ has a uniformly convergent
    subsequence.
:::
