---
schema: qual/card@1
id: P-BKF88-5
kind: problem
title: Young's inequality for inverse increasing functions
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 in the deterministic MinerU Flash extraction assets/attachments/Fall88_extracted.md.
---

::: {.problem}
Let $f:[0,\infty)\to[0,\infty)$ be continuous and strictly increasing onto $[0,\infty)$, and let $g=f^{-1}$.
Prove that for all positive $a,b$,
\[
\int_0^a f(x)\,dx+\int_0^b g(y)\,dy\ge ab,
\]
and determine the condition for equality.
:::

::: {.solution}

::: pf

::: pf-step

One has
$$
f(0)=0,
$$
and $g:[0,\infty)\to[0,\infty)$ is continuous and strictly increasing.

::: pf-proof

Since $f$ is increasing, $f(0)$ is the least value in its range. Because the range is all of $[0,\infty)$, this least value is $0$. The inverse of a continuous strictly increasing bijection between intervals is again continuous and strictly increasing.

:::

:::

::: {.pf-step #s2}

For every $a>0$,
$$
\int_0^a f(x)\,dx
+
\int_0^{f(a)}g(y)\,dy
=
a f(a).
$$

::: pf-proof

Consider the rectangle
$$
[0,a]\times[0,f(a)].
$$
For a fixed height $y\in[0,f(a)]$, strict monotonicity gives
$$
y\leq f(x)
\quad\Longleftrightarrow\quad
g(y)\leq x.
$$
Thus the part of the rectangle lying below the graph $y=f(x)$ has horizontal slice $[g(y),a]$, of length $a-g(y)$. Computing its area by vertical and horizontal slices gives
$$
\int_0^a f(x)\,dx
=
\int_0^{f(a)}\bigl(a-g(y)\bigr)\,dy.
$$
Rearranging yields the asserted identity.

:::

:::

::: {.pf-step #s3}

For fixed $a>0$, define
$$
H(b)
=
\int_0^a f(x)\,dx
+
\int_0^b g(y)\,dy
-ab,
\qquad b>0.
$$
Then $H$ has its unique minimum at $b=f(a)$.

::: pf-proof

By continuity of $g$ and the fundamental theorem of calculus,
$$
H'(b)=g(b)-a.
$$
Since $g$ is strictly increasing and $g(f(a))=a$, one has
$$
H'(b)<0
\quad\text{for }b<f(a),
$$
and
$$
H'(b)>0
\quad\text{for }b>f(a).
$$
Hence $H$ decreases up to $f(a)$ and increases afterward, so $b=f(a)$ is its unique minimum.

:::

:::

::: {.pf-step #s4}

The minimum value of $H$ is $0$.

::: pf-proof

By step [](#s2){.pf-ref},
$$
\begin{aligned}
H(f(a))
&=
\int_0^a f(x)\,dx
+
\int_0^{f(a)}g(y)\,dy
-a f(a)\\
&=0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

Therefore, for all positive $a,b$,
$$
\int_0^a f(x)\,dx
+
\int_0^b g(y)\,dy
\geq
ab,
$$
with equality exactly when
$$
\boxed{b=f(a)},
$$
equivalently when $a=g(b)$.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref},
$$
H(b)\geq H(f(a))=0
$$
for every $b>0$, and equality holds only at the unique minimizer $b=f(a)$. Expanding the definition of $H$ gives the inequality and its equality condition.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is precisely the required inequality and equality criterion.

:::

:::

:::
