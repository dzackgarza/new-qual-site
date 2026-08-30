---
schema: qual/card@1
id: P-JHUFA11ANG
kind: problem
title: ", be the distribution function of a given , where Does tend to a limit as Give a"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Distribution Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

7. Let $\omega ( \alpha ) = | \{ x : | f ( x ) | > \alpha \} | , \alpha > 0$ , be the distribution function of a given $f \in$ $L ^ { p } ( \mathbb { R } ^ { n } )$ , where $p > 0$ Does $\alpha ^ { p } \omega ( \alpha )$ tend to a limit as $\alpha  0 + ?$ Give a proof or counterexample.

::: solution
**Goal:** Determine the limit of $\alpha^p\omega(\alpha)$ as $\alpha\to0^+$.

<1>1. Use layer-cake:
    *Proof:*  
    For nonnegative $|f|^p$,
    \[
    \int_{\mathbb R^n}|f|^p\,dx
    =p\int_0^\infty \alpha^{p-1}\omega(\alpha)\,d\alpha<\infty
    \]
    and $\omega(\alpha)$ is decreasing in $\alpha$.

<1>2. Show the limit is zero:
    *Proof:*  
    Suppose contrary that $\limsup_{\alpha\to0^+}\alpha^p\omega(\alpha)=\ell>0$.
    Choose $\alpha_k\downarrow0$ with $\omega(\alpha_k)\ge \ell\alpha_k^{-p}/2$ and
    $\alpha_{k+1}<\alpha_k/2$.
    Then on $(\alpha_{k+1},\alpha_k)$,
    $\omega(t)\ge \omega(\alpha_k)\ge \ell\alpha_k^{-p}/2$.
    Hence
    \[
    \int_0^\infty t^{p-1}\omega(t)\,dt
    \ge
    \sum_{k\ge1}\int_{\alpha_{k+1}}^{\alpha_k} t^{p-1}\frac{\ell}{2}\alpha_k^{-p}\,dt
    \ge \frac{\ell}{2p}(1-2^{-p})\sum_{k\ge1}1= \infty,
    \]
    contradicting finite $L^p$ norm. So $\lim_{\alpha\to0^+}\alpha^p\omega(\alpha)=0$.
:::
