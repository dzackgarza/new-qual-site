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
solved: true
---

::: {.problem title="?"}
Find the pointwise limit of the sequence of functions $\{f_n\}$ given by $f_n(x)=x^n$ on $[0,1]$.
Is the convergence of $f_n$ to $f$ uniform?
([KRD10, 8.6.A]) Why is $$B=\{f\in C([0,1]):\|f\|_\infty\le1\}$$ not compact?
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** (1) Find the pointwise limit of $f_n(x) = x^n$ on $[0,1]$; (2) decide uniformity; (3) explain why $B = \{f \in C[0,1] : \|f\|_\infty \le 1\}$ is not compact.

<1>1. The pointwise limit is $f(x) = 0$ for $0 \le x < 1$ and $f(1) = 1$.
Proof: for $0 \le x < 1$, $x^n \to 0$; at $x = 1$, $x^n = 1$ for all $n$.

<1>2. The convergence is not uniform on $[0,1]$.
<2>1. Each $f_n$ is continuous.
<2>2. $f$ is discontinuous at $1$: $\lim_{x \to 1^-} f(x) = 0 \neq 1 = f(1)$.
Proof: by <1>1. <2>3. If $f_n \to f$ uniformly, $f$ would be continuous.
Proof: uniform limits of continuous functions are continuous (e.g. Theorem 6.1 / D7-W3). <2>4. Q.E.D. Proof: <2>2 contradicts <2>3. Alternatively: $\|f_n - f\|_\infty = \sup_{x \in [0,1)}x^n = 1 \not\to 0$ — the sup is approached as $x \to 1^-$.

<1>3. $B = \{f \in C[0,1] : \|f\|_\infty \le 1\}$ is not compact.
<2>1. $f_n(x) = x^n$ is a sequence in $B$ with no uniformly convergent subsequence.
Proof: every subsequence $f_{n_k}$ converges pointwise to the same discontinuous $f$ of <1>1; if some subsequence converged uniformly, its uniform limit (necessarily $f$, by uniqueness of pointwise limits) would be continuous, contradiction.
<2>2. In a compact metric space every sequence has a convergent subsequence.
Proof: sequential compactness, equivalent to compactness for metric spaces.
<2>3. Q.E.D. Proof: <2>1 gives a sequence in $B$ without a convergent subsequence, so $B$ is not compact by <2>2. (Intuitively: $B$ is closed and bounded but not equicontinuous, so Arzelà–Ascoli fails.)
:::
