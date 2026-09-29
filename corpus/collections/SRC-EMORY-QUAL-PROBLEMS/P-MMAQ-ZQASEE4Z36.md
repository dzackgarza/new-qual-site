---
schema: qual/card@1
id: P-MMAQ-ZQASEE4Z36
kind: problem
title: Dominated convergence under convergence in measure
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 3 in both preserved Arango Emory qualifying-problem compilations. The prior solution incorrectly folded convergence in measure into the statement of the Dominated Convergence Theorem; the standard a.e.-convergence statement is restored and the convergence-in-measure result is proved separately by subsequences.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Real Analysis (3) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMRA3, whose solution repeats this subsequence argument."
---

::: {.problem}
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

::: pf

::: pf-step
Statement of the Dominated Convergence Theorem.

::: pf-proof

::: pf-step
Let $\{f_n\}$ be measurable on a Lebesgue measurable set $E$, converging almost everywhere to $f$, with $|f_n| \leq g$ a.e. for all $n$, where $g \geq 0$ is integrable on $E$. Then $f$ is integrable, $|f_n-f|\to0$ in $L^1(E)$, and in particular $\int_E f_n\to\int_E f$.

::: pf-proof
This is Lebesgue's dominated convergence theorem. Part (2) replaces almost-everywhere convergence by convergence in measure through a subsequence argument.
:::

:::

:::

:::

::: pf-step
Proof of part (2): convergence in measure plus domination forces $\int_E |f_n - f| \to 0$.

::: pf-proof

::: {.pf-step #subsequence-converges-ae}
Some subsequence $f_{n_k} \to f$ a.e. on $E$.

::: pf-proof
Since $f_n \to f$ in measure, choose indices $n_1 < n_2 < \cdots$ with $m\theset{|f_{n_k} - f| > 2^{-k}} < 2^{-k}$. The sets $B_k = \theset{|f_{n_k} - f| > 2^{-k}}$ satisfy $\sum_k m(B_k) < \infty$, so Borel–Cantelli gives $m(\limsup_k B_k) = 0$; outside $\limsup_k B_k$, $f_{n_k}(x) \to f(x)$.
:::

:::

::: {.pf-step #f-integrable-and-dominated}
$|f| \leq g$ a.e., so $f$ is integrable and $|f_{n_k} - f| \leq 2g$ a.e.

::: pf-proof
Pass to the a.e. limit in $|f_{n_k}| \leq g$ using step [](#subsequence-converges-ae){.pf-ref}; then $|f_{n_k} - f| \leq |f_{n_k}| + |f| \leq 2g$ a.e., and $2g$ is integrable.
:::

:::

::: {.pf-step #subsequence-integral-to-zero}
$\int_E |f_{n_k} - f| \to 0$.

::: pf-proof
Apply the dominated convergence theorem to $h_k := |f_{n_k} - f|$: by steps [](#subsequence-converges-ae){.pf-ref} and [](#f-integrable-and-dominated){.pf-ref}, $h_k \to 0$ a.e. with $|h_k| \leq 2g$ integrable; the theorem's conclusion gives $\int_E h_k \to 0$.
:::

:::

::: {.pf-step #full-sequence-integral-to-zero}
The full sequence satisfies $\int_E |f_n - f| \to 0$.

::: pf-proof
If not, some $\varepsilon > 0$ and subsequence have $\int_E |f_{n_j} - f| \geq \varepsilon$. Applying step [](#subsequence-converges-ae){.pf-ref} to that subsequence yields a further subsequence converging a.e., and step [](#subsequence-integral-to-zero){.pf-ref} gives $\int |f_{n_{j_l}} - f| \to 0$, contradicting $\geq \varepsilon$. Hence the whole sequence converges to $0$.
:::

:::

::: pf-qed
Step [](#full-sequence-integral-to-zero){.pf-ref} is the desired conclusion of part (2).
:::

:::

:::

:::
:::
