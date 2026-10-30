---
schema: qual/card@1
id: P-WESRA10-II5
kind: problem
title: '$L^4$ versus $L^3$ on finite and infinite measure spaces'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
(a) Show that if $\mu(X)<\infty$, then
$$
L^4(X,\mathcal B,\mu)\subseteq L^3(X,\mathcal B,\mu).
$$

(b) Give a measure space and a function $f$ such that $f\in L^4$ but $f\notin L^3$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $\mu(X)<\infty$ and $f\in L^4(X)$, then
$$
\int_X \abs{f}^3\,d\mu
\le
\left(\int_X\abs{f}^4\,d\mu\right)^{3/4}
\mu(X)^{1/4}.
$$


::: pf-proof

Apply Hölder's inequality with conjugate exponents
$$
\frac43
\qquad\text{and}\qquad
4
$$
to the functions $\abs{f}^3$ and $1$:
$$
\int_X \abs{f}^3\,d\mu
\le
\left(\int_X(\abs{f}^3)^{4/3}\,d\mu\right)^{3/4}
\left(\int_X1^4\,d\mu\right)^{1/4}.
$$
This is exactly the displayed inequality.

:::

:::

::: {.pf-step #s1-2}

Therefore, when $\mu(X)<\infty$,
$$
\boxed{L^4(X,\mathcal B,\mu)\subseteq L^3(X,\mathcal B,\mu)}.
$$


::: pf-proof

If $f\in L^4$, the first factor in step [](#s1-1){.pf-ref} is finite, and the second is
finite because $\mu(X)<\infty$. Hence
$$
\int_X\abs{f}^3\,d\mu<\infty,
$$
so $f\in L^3$.

:::

:::

::: {.pf-step #s1-3}

On the infinite-measure space
$$
X=(1,\infty)
$$
with Lebesgue measure, the function
$$
f(x)=x^{-1/3}
$$
satisfies
$$
\boxed{f\in L^4(X)\setminus L^3(X)}.
$$


::: pf-proof

For the fourth power,
$$
\int_1^\infty \abs{f(x)}^4\,dx
=\int_1^\infty x^{-4/3}\,dx
<\infty.
$$
For the third power,
$$
\int_1^\infty \abs{f(x)}^3\,dx
=\int_1^\infty x^{-1}\,dx
=\infty.
$$
Thus $f\in L^4$ but $f\notin L^3$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-3){.pf-ref} gives the counterexample required in
part (b).

:::

:::

:::
