---
schema: qual/card@1
id: P-UCLARA12S-11
kind: problem
title: Polynomial reciprocal identity on the unit circle
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $P(z)$ be a polynomial.
Show that there exist an integer $n$ and a polynomial $Q(z)$ such that
$$
P(z)Q(z)=z^n\abs{P(z)}^2
$$
whenever $\abs{z}=1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $P\equiv0$, the conclusion holds with $n=0$ and $Q=0$.


::: pf-proof

Both sides of the required identity are then identically zero.

:::

:::

::: {.pf-step #s1-2}

Suppose
$$
P(z)=a_0+a_1z+\cdots+a_mz^m,
\qquad
a_m\ne0.
$$
Define
$$
Q(z)\coloneqq
\overline{a_m}
+\overline{a_{m-1}}z
+\cdots
+\overline{a_0}z^m.
$$
Then for every $z$ with $\abs z=1$,
$$
Q(z)=z^m\overline{P(z)}.
$$


::: pf-proof

When $\abs z=1$, one has $\overline z=z^{-1}$. Hence
$$
\begin{aligned}
z^m\overline{P(z)}
&=
z^m
\sum_{j=0}^m
\overline{a_j}\,\overline z^j\\
&=
\sum_{j=0}^m
\overline{a_j}z^{m-j}\\
&=
Q(z).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

With $n=m$ and the polynomial $Q$ from step [](#s1-2){.pf-ref},
$$
\boxed{P(z)Q(z)=z^m\abs{P(z)}^2}
$$
for every $\abs z=1$.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
P(z)Q(z)
=
P(z)z^m\overline{P(z)}
=
z^m\abs{P(z)}^2.
$$
Thus the required integer may be taken to be the degree of $P$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} handles the zero polynomial, and step [](#s1-3){.pf-ref} proves the assertion for every nonzero polynomial.

:::

:::

:::
