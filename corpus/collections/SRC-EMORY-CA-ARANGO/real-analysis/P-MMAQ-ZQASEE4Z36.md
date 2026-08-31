---
schema: qual/card@1
id: P-MMAQ-ZQASEE4Z36
kind: problem
title: State the Dominated Convergence Theorem for Lebesgue integrals.
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
1.  State the Dominated Convergence Theorem for Lebesgue integrals.

2.  Let $\{f_n\}$ be a sequence of measurable functions on a
    Lebesgue measurable set $E$ which converges *in measure* to a
    function $f$ on $E$. Suppose that for every $n$, $|f_n| \leq g$
    with $g$ integrable on $E$. Using the above theorem show that
    `\begin{align*}
        \int_E |f_n-f| \longrightarrow 0 \, .
    \end{align*}`{=tex}
:::

::: {.solution}
**Goal:** (1) State the Dominated Convergence Theorem; (2) use it to prove that if $f_n \to f$ in measure on a measurable set $E$ and $|f_n| \leq g$ with $g$ integrable on $E$, then $\int_E |f_n - f| \to 0$.

<1>1. Statement of the Dominated Convergence Theorem.
    <2>1. Let $\{f_n\}$ be measurable on a Lebesgue measurable set $E$, converging a.e. (or in measure) to $f$, with $|f_n| \leq g$ a.e. for all $n$, where $g \geq 0$ is integrable on $E$. Then $f$ is integrable and $\lim_n \int_E f_n = \int_E f$.
        ::: {.proof}
        this is the statement of the theorem, as requested in part (1). (Equivalently, the conclusion is $\int_E |f_n - f| \to 0$.)
        :::

<1>2. Proof of part (2): convergence in measure plus domination forces $\int_E |f_n - f| \to 0$.
    <2>1. Some subsequence $f_{n_k} \to f$ a.e. on $E$.
        ::: {.proof}
        since $f_n \to f$ in measure, choose indices $n_1 < n_2 < \cdots$ with $m\theset{|f_{n_k} - f| > 2^{-k}} < 2^{-k}$. The sets $B_k = \theset{|f_{n_k} - f| > 2^{-k}}$ satisfy $\sum_k m(B_k) < \infty$, so Borel–Cantelli gives $m(\limsup_k B_k) = 0$; outside $\limsup_k B_k$, $f_{n_k}(x) \to f(x)$.
        :::
    <2>2. $|f| \leq g$ a.e., so $f$ is integrable and $|f_{n_k} - f| \leq 2g$ a.e.
        ::: {.proof}
        pass to the a.e. limit in $|f_{n_k}| \leq g$ using <2>1; then $|f_{n_k} - f| \leq |f_{n_k}| + |f| \leq 2g$ a.e., and $2g$ is integrable.
        :::
    <2>3. $\int_E |f_{n_k} - f| \to 0$.
        ::: {.proof}
        apply the DCT to $h_k := |f_{n_k} - f|$: by <2>1 and <2>2, $h_k \to 0$ a.e. with $|h_k| \leq 2g$ integrable; the theorem's conclusion gives $\int_E h_k \to 0$.
        :::
    <2>4. The full sequence satisfies $\int_E |f_n - f| \to 0$.
        ::: {.proof}
        if not, some $\varepsilon > 0$ and subsequence have $\int_E |f_{n_j} - f| \geq \varepsilon$. Applying <2>1 to that subsequence yields a further subsequence converging a.e., and <2>3 gives $\int |f_{n_{j_l}} - f| \to 0$, contradicting $\geq \varepsilon$. Hence the whole sequence converges to $0$.
        :::
    <2>5. Q.E.D.
        ::: {.proof}
        <2>4 is the desired conclusion of part (2).
        :::
:::
