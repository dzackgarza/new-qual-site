---
schema: qual/card@1
id: P-WESRA16-A3
kind: problem
title: 'Integration against a nonnegative measurable density and continuity from below'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group A, problem A3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md. Flash severely garbles the opening sentence of part (a), but the displayed definition of $\mu$, the words “is a countably-additive measure,” and part (b) determine the mathematical task.
---

::: {.problem}
Let $f:\RR^d\to[0,\infty)$ be measurable and define
$$
\mu(A)=\int_{\RR^d}f\,\mathbf1_A.
$$

(a) Prove that $\mu$ is a countably additive measure on the Lebesgue measurable sets.

(b) If $M_0\subseteq M_1\subseteq\cdots$ are measurable and $M=\bigcup_nM_n$, prove that
$$
\lim_{n\to\infty}\int_{\RR^d}f\mathbf1_{M_n}
$$
exists, identifying the limit.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has $\mu(\varnothing)=0$.


::: pf-proof

Since $\mathbf1_{\varnothing}=0$,
$$
\mu(\varnothing)=\int_{\RR^d} f\mathbf1_{\varnothing}=0.
$$

:::

:::

::: {.pf-step #s1-2}

If $(A_j)_{j\geq1}$ is pairwise disjoint and $A=\bigcup_{j=1}^\infty A_j$, then
$$
\mu(A)=\sum_{j=1}^\infty\mu(A_j).
$$


::: pf-proof

Set $s_N=\sum_{j=1}^N\mathbf1_{A_j}$. Pairwise disjointness gives
$$
s_N=\mathbf1_{\bigcup_{j=1}^N A_j},
$$
and $s_N$ increases pointwise to $\mathbf1_A$. Since $f\geq0$, the functions $fs_N$ increase pointwise to $f\mathbf1_A$. By the Monotone Convergence Theorem,
$$
\begin{aligned}
\mu(A)
&=\int f\mathbf1_A\\
&=\lim_{N\to\infty}\int fs_N\\
&=\lim_{N\to\infty}\sum_{j=1}^N\int f\mathbf1_{A_j}\\
&=\sum_{j=1}^\infty\mu(A_j).
\end{aligned}
$$
These equalities are in $[0,\infty]$.

:::

:::

::: {.pf-step #s1-3}

The function $\mu$ is a countably additive measure on the Lebesgue measurable subsets of $\RR^d$.


::: pf-proof

For every measurable $A$, the function $f\mathbf1_A$ is nonnegative and measurable, so $\mu(A)\in[0,\infty]$ is defined. Step [](#s1-1){.pf-ref} gives the empty-set axiom and step [](#s1-2){.pf-ref} gives countable additivity. This proves part (a).

:::

:::

::: {.pf-step #s1-4}

If $M_0\subseteq M_1\subseteq\cdots$ and $M=\bigcup_{n=0}^\infty M_n$, then $f\mathbf1_{M_n}$ increases pointwise to $f\mathbf1_M$.


::: pf-proof

The inclusions imply $\mathbf1_{M_n}\leq\mathbf1_{M_{n+1}}$. If $x\notin M$, all these indicators vanish. If $x\in M$, then $x\in M_N$ for some $N$, and therefore $\mathbf1_{M_n}(x)=1$ for every $n\geq N$. Thus $\mathbf1_{M_n}\to\mathbf1_M$ pointwise. Multiplication by the nonnegative function $f$ preserves the monotonicity and the pointwise limit.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\boxed{\lim_{n\to\infty}\int_{\RR^d} f\mathbf1_{M_n}
=\int_{\RR^d} f\mathbf1_M
=\mu(M)}.
$$


::: pf-proof

Apply the Monotone Convergence Theorem to the increasing sequence in step [](#s1-4){.pf-ref}. The limit therefore exists in $[0,\infty]$ and equals the integral of the pointwise limit. This proves part (b).

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} proves part (b).

:::

:::

:::
