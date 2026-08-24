---
schema: qual/card@1
id: P-5VQ6H
kind: problem
title: Weak-plus-norm convergence is strong in $L^2$, and the unit ball is not strongly
  compact
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - L²
  - Hilbert Spaces
relations: []
review: draft
---

::: {.problem title="?"}
Let $L^2 = L^2(\mathbb{R}^d)$ be the real Hilbert space endowed with its natural norm $\|\cdot\|$ derived from the real inner product $(f,g) = \int fg\, dm$ (where $dm$ is Lebesgue measure on $\mathbb{R}^d$). We say that $f_n \in L^2$ converges weakly to $f$ if $(f_n, g) \to (f,g)$ for every $g \in L^2$.

- Prove that if $f_n$ converges weakly to $f$ and $\|f_n\| \to \|f\|$ then $f_n$ converges to $f$ in the strong topology.

- Prove that there exists a sequence of bounded functions in $L^2$ which is not converging in $L^2$ but weakly converging up to a subsequence possibly.
  What do you conclude on the unit ball of $L^2$ endowed with the strong topology?
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (First bullet) Weak + norm convergence $\Rightarrow$ strong convergence.
Proof: using the real inner product, \[ \|f_n - f\|^2 = \|f_n\|^2 + \|f\|^2 - 2(f_n, f) . \] Weak convergence gives $(f_n, f) \to (f,f) = \|f\|^2$, and by hypothesis $\|f_n\| \to \|f\|$; hence $\|f_n - f\|^2 \to \|f\|^2 + \|f\|^2 - 2\|f\|^2 = 0$.
<1>2. (Second bullet) A bounded sequence in $L^2$ not converging strongly but weakly converging along a subsequence.
Proof: let $\{e_n\}$ be an orthonormal basis of $L^2(\RR^d)$ (e.g. the Haar basis), all of which are bounded functions.
Since $\|e_n\| = 1$, the sequence is bounded.
It does not converge strongly: $\|e_n - e_m\| = \sqrt2$ for $n\ne m$.
But every bounded sequence in the Hilbert space $L^2$ has a weakly convergent subsequence (the closed unit ball is weakly compact / sequentially weakly compact), and in fact $e_n \rightharpoonup 0$ weakly since $(e_n, g) \to 0$ for every $g$ (Bessel's inequality: $\sum |(e_n,g)|^2 \le \|g\|^2$). So $e_n$ converges weakly (the whole sequence) but not strongly.
<1>3. Conclusion about the unit ball.
Proof: the closed unit ball of $L^2$ is weakly compact (so every bounded sequence has a weakly convergent subsequence) but NOT strongly compact: the sequence $(e_n)$ of <1>2 lies in the unit ball and has no strongly convergent subsequence.
This contrasts finite-dimensionality: in finite dimensions the unit ball is compact.
<1>4. Q.E.D.
:::
