---
schema: qual/card@1
id: P-BERK97S-03
kind: problem
title: A weighted average of an integrable nonnegative function tends to zero
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f:[0,\infty)\to[0,\infty)$ be continuous and suppose
\[
\int_0^\infty f(x)\,dx<\infty.
\]
Prove that
\[
\lim_{n\to\infty}\int_0^n\frac{x f(x)}{n}\,dx=0.
\]
:::

::: {.solution}
Let
$$
I_n\coloneqq\int_0^n\frac{x}{n}f(x)\,dx.
$$

::: pf

::: {.pf-step #s1}

For every $\varepsilon>0$, there exists $A>0$ such that
$$
\int_A^\infty f(x)\,dx<\frac{\varepsilon}{2}.
$$

::: pf-proof

The function $f$ is nonnegative and
$$
\int_0^\infty f(x)\,dx<\infty.
$$
Therefore the tails of this improper integral tend to zero.

:::

:::

::: {.pf-step #s2}

For $n>A$,
$$
0\leq I_n
\leq
\frac{A}{n}\int_0^A f(x)\,dx
+
\int_A^\infty f(x)\,dx.
$$

::: pf-proof

Split the integral at $A$:
$$
I_n
=
\int_0^A\frac{x}{n}f(x)\,dx
+
\int_A^n\frac{x}{n}f(x)\,dx.
$$
On $[0,A]$ one has $0\leq x/n\leq A/n$, while on $[A,n]$ one has
$0\leq x/n\leq1$. Since $f\geq0$,
$$
I_n
\leq
\frac{A}{n}\int_0^Af(x)\,dx
+
\int_A^nf(x)\,dx,
$$
and the last integral is at most the tail integral in the claim.

:::

:::

::: {.pf-step #s3}

For all sufficiently large $n$,
$$
0\leq I_n<\varepsilon.
$$

::: pf-proof

Choose $A$ as in step [](#s1){.pf-ref}. The finite number
$$
C_A\coloneqq A\int_0^A f(x)\,dx
$$
is independent of $n$. Choose $n>A$ sufficiently large that
$$
\frac{C_A}{n}<\frac{\varepsilon}{2}.
$$
Then step [](#s2){.pf-ref} and step [](#s1){.pf-ref} give
$$
0\leq I_n
<
\frac{\varepsilon}{2}
+
\frac{\varepsilon}{2}
=
\varepsilon.
$$

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{
\lim_{n\to\infty}
\int_0^n\frac{x f(x)}{n}\,dx
=0
}.
$$

::: pf-proof

Step [](#s3){.pf-ref} is precisely the $\varepsilon$-definition of $I_n\to0$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required limit.

:::

:::

:::
