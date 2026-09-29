---
schema: qual/card@1
id: P-BKS16-6A
kind: problem
title: Real 100th roots of $\operatorname{diag}(-1,-1-\epsilon)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Checked the statement and eigenvalue obstruction against Problem 6A in the vendored Berkeley Spring 2016 solution packet.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked spectral mapping, exclusion of real eigenvalues, and the conjugate-pair contradiction for a real 2 by 2 matrix.
---

::: {.problem}
Prove or disprove: there exists an $\epsilon>0$ and a real matrix $A$ such that
$$
A^{100}=\begin{pmatrix}-1&0\\0&-1-\epsilon\end{pmatrix}.
$$
:::

::: {.solution}
The assertion is false.

::: pf

::: {.pf-step #s1}

Suppose, for contradiction, that there are $\epsilon>0$ and a real $2\times2$ matrix $A$ such that
$$
A^{100}
=
\begin{pmatrix}
-1&0\\
0&-1-\epsilon
\end{pmatrix}.
$$
If $\lambda$ and $\mu$ are the two complex eigenvalues of $A$, counted with algebraic multiplicity, then the eigenvalues of $A^{100}$ are
$$
\lambda^{100}
\qquad\text{and}\qquad
\mu^{100}.
$$

::: pf-proof

Over $\CC$, the characteristic polynomial of $A$ splits. Spectral mapping for the polynomial $t^{100}$ says that applying the polynomial to $A$ applies it to each eigenvalue, with multiplicity.

:::

:::

::: pf-step

Neither $\lambda$ nor $\mu$ is real.

::: pf-proof

If, say, $\lambda\in\RR$, then
$$
\lambda^{100}\geq0.
$$
But by step [](#s1){.pf-ref}, $\lambda^{100}$ must be an eigenvalue of
$$
A^{100},
$$
whose two eigenvalues are
$$
-1
\qquad\text{and}\qquad
-1-\epsilon,
$$
both negative. This is impossible. The same argument applies to $\mu$.

:::

:::

::: {.pf-step #s3}

Since $A$ is real and its eigenvalues are nonreal,
$$
\mu=\overline{\lambda}.
$$

::: pf-proof

The characteristic polynomial of a real matrix has real coefficients, so its nonreal roots occur in complex-conjugate pairs.

:::

:::

::: {.pf-step #s4}

The eigenvalues of $A^{100}$ must then be equal.

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s3){.pf-ref}, they are
$$
\lambda^{100}
\qquad\text{and}\qquad
\overline{\lambda}^{100}
=
\overline{\lambda^{100}}.
$$
But each is an eigenvalue of the displayed real diagonal matrix $A^{100}$, so $\lambda^{100}$ is real. Hence
$$
\overline{\lambda^{100}}
=
\lambda^{100}.
$$
Thus the two eigenvalues of $A^{100}$ coincide.

:::

:::

::: {.pf-step #s5}

This contradicts $\epsilon>0$.

::: pf-proof

The two eigenvalues of the proposed value of $A^{100}$ are
$$
-1
\qquad\text{and}\qquad
-1-\epsilon,
$$
which are distinct because $\epsilon>0$. This contradicts step [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Therefore no such $\epsilon>0$ and real matrix $A$ exist.

::: pf-proof

The assumption in step [](#s1){.pf-ref} leads to the contradiction in step [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} disproves the proposed assertion.

:::

:::

:::
