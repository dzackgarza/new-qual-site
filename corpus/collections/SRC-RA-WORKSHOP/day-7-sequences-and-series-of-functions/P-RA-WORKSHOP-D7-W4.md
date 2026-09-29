---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W4
kind: problem
title: Pointwise and uniform convergence of $x^n$ on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Convergence of Functions
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Find the pointwise limit of the sequence of functions $\{f_n\}$ given by $f_n(x)=x^n$ on $[0,1]$.
Is the convergence of $f_n$ to $f$ uniform?
([KRD10, 8.6.A]) Why is $$B=\{f\in C([0,1]):\|f\|_\infty\le1\}$$ not compact?
:::

:::: {.solution}
**Goal:** (1) Find the pointwise limit of $f_n(x) = x^n$ on $[0,1]$; (2) decide uniformity; (3) explain why $B = \{f \in C[0,1] : \|f\|_\infty \le 1\}$ is not compact.

::: pf

::: {.pf-step #s1}
The pointwise limit is $f(x) = 0$ for $0 \le x < 1$ and $f(1) = 1$.
Proof: for $0 \le x < 1$, $x^n \to 0$; at $x = 1$, $x^n = 1$ for all $n$.
:::

::: pf-step
The convergence is not uniform on $[0,1]$.

::: pf-proof

::: pf-step
Each $f_n$ is continuous.
:::

::: {.pf-step #s2-2}
$f$ is discontinuous at $1$: $\lim_{x \to 1^-} f(x) = 0 \neq 1 = f(1)$.
Proof: by step [](#s1){.pf-ref}.
:::

::: {.pf-step #s2-3}
If $f_n \to f$ uniformly, $f$ would be continuous.
Proof: uniform limits of continuous functions are continuous (e.g. Theorem 6.1 / D7-W3).
:::

::: pf-qed
Proof: step [](#s2-2){.pf-ref} contradicts step [](#s2-3){.pf-ref}. Alternatively: $\|f_n - f\|_\infty = \sup_{x \in [0,1)}x^n = 1 \not\to 0$ — the sup is approached as $x \to 1^-$.
:::

:::

:::

::: pf-step
$B = \{f \in C[0,1] : \|f\|_\infty \le 1\}$ is not compact.

::: pf-proof

::: {.pf-step #s3-1}
$f_n(x) = x^n$ is a sequence in $B$ with no uniformly convergent subsequence.
Proof: every subsequence $f_{n_k}$ converges pointwise to the same discontinuous $f$ of step [](#s1){.pf-ref}; if some subsequence converged uniformly, its uniform limit (necessarily $f$, by uniqueness of pointwise limits) would be continuous, contradiction.
:::

::: {.pf-step #s3-2}
In a compact metric space every sequence has a convergent subsequence.
Proof: sequential compactness, equivalent to compactness for metric spaces.
:::

::: pf-qed
Proof: step [](#s3-1){.pf-ref} gives a sequence in $B$ without a convergent subsequence, so $B$ is not compact by step [](#s3-2){.pf-ref}. (Intuitively: $B$ is closed and bounded but not equicontinuous, so Arzelà–Ascoli fails.)
:::

:::

:::

:::
::::
