---
schema: qual/card@1
id: P-JHUFA05ANC
kind: problem
title: "Weak convergence to zero on the circle"
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

3. Let $g _ { n }$ be a sequence of functions in $L ^ { 1 } ( S ^ { 1 } , d \theta )$ where $S ^ { 1 }$ is the unit circle $\{ e ^ { i \theta } : 0 \leq \theta \leq 2 \pi \}$ We say that $g _ { n } \ \to \ 0$ weakly if $\begin{array} { r } { \int _ { S ^ { 1 } } g _ { n } ( e ^ { i \theta } ) f ( e ^ { i \theta } ) d \theta  0 } \end{array}$ a s $n \to \infty$ for all $f \in C ( S ^ { 1 } )$

Question: Suppose that $\left\{ g _ { n } \right\}$ is a sequence in $L ^ { 1 } ( S ^ { 1 } , d \theta )$ and $\begin{array} { r } { \int _ { S ^ { 1 } } e ^ { i k \theta } g _ { n } ( e ^ { i \theta } ) d \theta  0 } \end{array}$ a s $n \to \infty$ for all $k \in \mathbb { Z }$ . Need $g _ { n } \to 0$ weakly?
Give either a proof or a counterexample.

::: {.solution}
<1>1. No, $g_n$ need not converge weakly to $0$.
Proof: exhibit a counterexample.

<1>2. Let $g_n(e^{i\theta}) = n e^{in\theta}$.
Proof: define the sequence.

<1>3. For each fixed $k \in \ZZ$, $\int_{S^1} e^{ik\theta} g_n(e^{i\theta})\, d\theta \to 0$.
Proof: $\int_{S^1} e^{ik\theta} n e^{in\theta}\, d\theta = n\int_{S^1} e^{i(k+n)\theta}\, d\theta$, which is $0$ whenever $k + n \neq 0$; for fixed $k$, this holds for all $n > |k|$, so the integral is $0$ for all sufficiently large $n$.

<1>4. But $g_n$ does not converge weakly to $0$.
<2>1. $\|g_n\|_{L^1} = \int_{S^1} |n e^{in\theta}|\, d\theta = 2\pi n \to \infty$.
Proof: $|e^{in\theta}| = 1$.
<2>2. A weakly convergent sequence in a normed space is bounded (by the uniform boundedness principle).
Proof: the functionals $f \mapsto \int f g_n$ on $C(S^1)$ have norm $\|g_n\|_{L^1}$, and a weakly convergent sequence of functionals is bounded.
<2>3. Hence $g_n$ cannot converge weakly to $0$.
Proof: <2>1 and <2>2.

<1>5. Q.E.D.
Proof: <1>3 and <1>4 give a counterexample.
:::
