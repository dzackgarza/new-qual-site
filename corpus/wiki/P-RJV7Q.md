---
schema: qual/card@1
id: P-RJV7Q
kind: problem
title: Pointwise simple approximation of measurable functions, and Borel representatives
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - density
relations: []
review: draft
solved: true
---

::: problem
Let $f: \RR \to \RR$ be Lebesgue measurable.

1. Show that there is a sequence of simple functions $s_n(x)$ such that $s_n(x) \to f(x)$ for all $x\in \RR$.

2. Show that there is a Borel measurable function $g$ such that $g = f$ almost everywhere.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (Part 1) Reduce to non-negative functions.
Proof: write $f = f^+ - f^-$; if $s_n^+ \to f^+$ and $s_n^- \to f^-$ pointwise with simple $s_n^\pm$, then $s_n = s_n^+ - s_n^-$ is simple and $s_n \to f$ pointwise.
<1>2. Construct simple approximations of a non-negative measurable $g$.
Proof: the standard dyadic truncations \[ s_n(x) = \sum_{k=0}^{n2^n - 1} \frac{k}{2^n}\chi_{\{k/2^n \le g < (k+1)/2^n\}}(x) + n \chi_{\{g \ge n\}}(x) \] are simple, $0 \le s_n \le g$, and $s_n(x) \nearrow g(x)$ for every $x$: indeed $g(x) - s_n(x) \le 2^{-n}$ when $g(x) \le n$, and $s_n(x) = n$ when $g(x) > n$.
Applying this to $g = f^+, f^-$ and using <1>1 proves (1). <1>3. (Part 2) Reduce to indicator functions.
Proof: every measurable function is a pointwise limit of simple functions (<1>2), and a pointwise limit of Borel measurable functions is Borel measurable; so it suffices to show that $\chi_E$ agrees a.e. with a Borel function for every Lebesgue measurable $E \subseteq \RR$.
<1>4. $\chi_E$ agrees a.e. with a Borel function.
Proof: $E$ measurable means $E = B \cup N$ where $B$ is Borel (e.g. a $G_\delta$) and $N$ is null.
Then $\chi_E = \chi_B$ on $\RR \setminus N$, i.e. a.e., and $\chi_B$ is Borel.
<1>5. Conclude (2). Proof: by <1>3 and <1>4, the simple functions from <1>2 can be chosen with Borel level sets (replace each level set by its Borel part), and their pointwise limit is Borel and equals $f$ a.e. <1>6. Q.E.D.
:::
