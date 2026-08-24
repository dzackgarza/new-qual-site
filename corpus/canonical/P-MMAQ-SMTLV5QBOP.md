---
schema: qual/card@1
id: P-MMAQ-SMTLV5QBOP
kind: problem
title: $\lim_{p\to 0^+}\|f\|_p$ exists for $f\in L^1([0,1])$ and is zero if $m\{f=0\}>0$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
---

::: problem
Let $f\in L^1([0,1])$.
Show that

1. The limit $\lim_{p\to 0^+} \| f \|_p$ exists.

2. If $m \{x : f(x) = 0\} > 0$, then the above limit is zero.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For $f \in L^1([0,1])$: (1) show $\lim_{p \to 0^+} \norm{f}_p$ exists; (2) if $m\{x : f(x) = 0\} > 0$, then the limit is $0$.

<1>1. Preparatory bounds.
<2>1. For $0 < p \leq 1$, $\norm{f}_p$ is finite.
Proof: For $t \geq 0$ and $0 < p \leq 1$, $t^p \leq 1 + t$, so $\int |f|^p \leq \int (1 + |f|) = 1 + \norm{f}_1 < \infty$.
<2>2. Interpolation bound: for $0 < p \leq q$, $\norm{f}_p \leq \norm{f}_q \cdot m(\{f \neq 0\})^{1/p - 1/q}$.
Proof: Hölder's inequality with exponents $q/p$ and its conjugate applied to $|f|^p = |f|^p \chi_{\{f \neq 0\}}$: $$\int |f|^p \leq \left(\int |f|^q\right)^{p/q} m(\{f \neq 0\})^{1 - p/q},$$ and taking the $p$-th root gives the claim.
<2>3. Q.E.D. Proof: These bounds are used in <1>2 and <1>4.

<1>2. Proof of (2): if $m\{f = 0\} > 0$, then $\norm{f}_p \to 0$ as $p \to 0^+$.
<2>1. $m(\{f \neq 0\}) = 1 - m(\{f = 0\}) < 1$.
Proof: $[0,1]$ has measure $1$, and the hypothesis gives $m(\{f = 0\}) > 0$.
<2>2. By <1>1<2>2 with $q = 1$: $\norm{f}_p \leq \norm{f}_1 \cdot m(\{f \neq 0\})^{1/p - 1}$ for $0 < p \leq 1$.
Proof: Apply <1>1<2>2 with $q = 1$.
<2>3. $m(\{f \neq 0\})^{1/p - 1} \to 0$ as $p \to 0^+$.
Proof: The base $m(\{f \neq 0\}) \in (0, 1)$ by <2>1 and the exponent $1/p - 1 \to +\infty$.
<2>4. Hence $\norm{f}_p \to 0$.
Proof: $\norm{f}_p \leq \norm{f}_1 \cdot m(\{f \neq 0\})^{1/p - 1} \to 0$ by <2>2 and <2>3, and $\norm{f}_p \geq 0$.
<2>5. Q.E.D. Proof: This proves (2); in particular the limit in (1) exists in this case.

<1>3. The limit formula: for $f$ with $m\{f = 0\} = 0$ and $\log|f| \in L^1$, $\lim_{p \to 0^+} \log \norm{f}_p = \int_0^1 \log|f|$.
<2>1. Lower bound: $\log \norm{f}_p \geq \int \log|f|$ for every $p \in (0, 1]$.
Proof: Jensen's inequality for the concave function $\log$: $\log \int |f|^p \geq \int \log(|f|^p) = p \int \log|f|$, and dividing by $p$ gives $\log \norm{f}_p \geq \int \log|f|$.
<2>2. It suffices to prove the matching upper bound $\limsup_{p \to 0^+} \log \norm{f}_p \leq \int \log|f|$.
Proof: Together with <2>1 this sandwiches $\log \norm{f}_p$.
<2>3. For bounded $f$ with $1/M \leq f \leq M$ (i.e. $\log f$ bounded), $\log \norm{f}_p \to \int \log f$ as $p \to 0^+$.
Proof: Write $f^p = e^{p \log f} = 1 + p \log f + r_p$ with $|r_p| \leq \tfrac{p^2}{2}(\log M)^2 e^{p \log M} \leq C_M p^2$ uniformly (Taylor expansion, $\log f$ bounded by $\pm \log M$). Hence $\int f^p = 1 + p\int \log f + O(p^2)$, so $\log \norm{f}_p = \frac{1}{p}\log\int f^p = \frac{1}{p}\log\left(1 + p\int\log f + O(p^2)\right) \to \int \log f$.
<2>4. Reduce the general case to the bounded case by truncation: for $M > 1$ put $f_M \definedas \min(\max(|f|, 1/M), M)$; then $\log f_M \in [-\log M, \log M]$, $f_M \uparrow |f|$ as $M \to \infty$, and $\int \log f_M \uparrow \int \log|f|$.
Proof: $f_M$ is bounded above and below; monotone convergence applies to $f_M \uparrow |f|$ and $\log f_M \uparrow \log|f|$ (extended reals; here $\log|f| \in L^1$ by the hypothesis of <1>3). <2>5. For each $p$, $\norm{f_M}_p \uparrow \norm{f}_p$ as $M \to \infty$.
Proof: Monotone convergence applied to $f_M^p \uparrow |f|^p$.
<2>6. Hence $\limsup_{p \to 0^+} \log \norm{f}_p \leq \sup_M \lim_{p \to 0^+} \log \norm{f_M}_p = \sup_M \int \log f_M = \int \log|f|$.
Proof: From <2>5, $\log \norm{f}_p = \sup_M \log \norm{f_M}_p$, and $\limsup_{p \to 0} \sup_M g_M(p) \leq \sup_M \limsup_{p \to 0} g_M(p)$; the inner limit is $\int \log f_M$ by <2>3 (bounded case), and the sup is $\int\log|f|$ by <2>4. <2>7. Q.E.D. Proof: By <2>1 and <2>6, $\lim_{p \to 0^+} \log \norm{f}_p = \int \log|f|$, so $\norm{f}_p \to \exp\left(\int \log|f|\right)$.

<1>4. Proof of (1): the limit always exists.
<2>1. Case $m\{f = 0\} > 0$: the limit exists and equals $0$.
Proof: By <1>2. <2>2. Case $m\{f = 0\} = 0$: the limit exists and equals $\exp\left(\int_0^1 \log|f|\right) \in [0, \infty)$.
Proof: Apply <1>3. If $\log|f| \in L^1$, the formula gives a finite limit.
If $\int \log|f| = -\infty$ (i.e. $\log^-|f|$ is not integrable), the same truncation argument applies: <1>3<2>3–<2>6 go through with $\sup_M \int\log f_M = -\infty$, giving $\log\norm{f}_p \to -\infty$ and $\norm{f}_p \to 0$; the lower bound of <1>3<2>1 ($\geq -\infty$) is then vacuous and the upper bound forces the limit.
Hence the limit exists in all cases.
<2>3. Q.E.D. Proof: The two cases of <2>1 and <2>2 exhaust all possibilities; in each the limit exists.
:::
