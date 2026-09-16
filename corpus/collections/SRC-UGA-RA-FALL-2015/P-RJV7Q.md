---
schema: qual/card@1
id: P-RJV7Q
kind: problem
title: Pointwise simple approximation of measurable functions, and Borel representatives
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Density
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the UGA Fall 2015 real-analysis qualifying exam recorded by SRC-UGA-RA-FALL-2015.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f: \RR \to \RR$ be Lebesgue measurable.

1. Show that there is a sequence of simple functions $s_n(x)$ such that $s_n(x) \to f(x)$ for all $x\in \RR$.

2. Show that there is a Borel measurable function $g$ such that $g = f$ almost everywhere.
:::
::: {.solution}
<1>1. (Part 1) Reduce to non-negative functions.
::: {.proof}
write $f = f^+ - f^-$; if $s_n^+ \to f^+$ and $s_n^- \to f^-$ pointwise with simple $s_n^\pm$, then $s_n = s_n^+ - s_n^-$ is simple and $s_n \to f$ pointwise.
:::
<1>2. Construct simple approximations of a non-negative measurable $g$.
::: {.proof}
the standard dyadic truncations \[ s_n(x) = \sum_{k=0}^{n2^n - 1} \frac{k}{2^n}\chi_{\{k/2^n \le g < (k+1)/2^n\}}(x) + n \chi_{\{g \ge n\}}(x) \] are simple, $0 \le s_n \le g$, and $s_n(x) \nearrow g(x)$ for every $x$: indeed $g(x) - s_n(x) \le 2^{-n}$ when $g(x) \le n$, and $s_n(x) = n$ when $g(x) > n$.
:::
Applying this to $g=f^+$ and $g=f^-$ and using <1>1 proves part (1).
:::

<1>3. Reduce part (2) to indicator functions.
::: {.proof}
every measurable function is a pointwise limit of simple functions (<1>2), and a pointwise limit of Borel measurable functions is Borel measurable; so it suffices to show that $\chi_E$ agrees a.e. with a Borel function for every Lebesgue measurable $E \subseteq \RR$.
:::
<1>4. $\chi_E$ agrees a.e. with a Borel function.
::: {.proof}
$E$ measurable means $E = B \cup N$ where $B$ is Borel (e.g. a $G_\delta$) and $N$ is null.
:::
Then $\chi_E = \chi_B$ on $\RR \setminus N$, i.e. almost everywhere, and $\chi_B$ is Borel.

<1>5. Conclude part (2).
::: {.proof}
By <1>3 and <1>4, the simple approximants can be replaced almost everywhere by Borel simple functions. Taking the corresponding pointwise limit gives a Borel measurable function $g$ with $g=f$ almost everywhere.
:::
