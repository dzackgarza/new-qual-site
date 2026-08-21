---
schema: qual/card@1
id: P-3GWIK
kind: problem
title: The unit ball of $L^2$ is not strongly compact
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Compactness
  - Hilbert Spaces
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Prove that the unit ball of $L^2$ endowed with its natural strong topology is not compact.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. The unit ball $B = \{f \in L^2 : \norm{f}_2 \le 1\}$ is closed and bounded but not compact.
<1>2. Exhibit a sequence in $B$ with no convergent subsequence.
Proof: let $\{e_n\}_{n\ge1}$ be an orthonormal basis of $L^2$ (e.g. the Haar or trigonometric basis on the underlying space).
Then $\norm{e_n}_2 = 1$, so $e_n \in B$ for all $n$, and for $n \ne m$, \[ \norm{e_n - e_m}_2^2 = \norm{e_n}^2 + \norm{e_m}^2 = 2, \] (orthogonality), so $\norm{e_n - e_m}_2 = \sqrt2$ for all $n \ne m$.
<1>3. No subsequence of $(e_n)$ converges.
Proof: any convergent sequence is Cauchy, but by <1>2 every two distinct elements of any subsequence are $\sqrt2$ apart, so no subsequence is Cauchy.
<1>4. $B$ is not compact.
Proof: in a compact metric space every sequence has a convergent subsequence; $(e_n) \subseteq B$ has none (<1>3), so $B$ (with the strong topology) is not compact.
<1>5. Q.E.D.

(Note: $B$ is nevertheless weakly compact — Banach--Alaoglu/Kakutani — and is compact iff $\dim L^2 < \infty$; the failure of strong compactness is precisely why weak topologies are used.
This is the $L^2$ instance of the general fact that the unit ball of an infinite-dimensional normed space is never compact.)
:::
