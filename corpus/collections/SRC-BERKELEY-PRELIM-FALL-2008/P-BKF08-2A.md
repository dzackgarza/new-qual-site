---
schema: qual/card@1
id: P-BKF08-2A
kind: problem
title: Entire functions with $f(z)/z$ bounded near infinity are linear
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 2A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the removable singularity and the global boundedness
    needed for Liouville's theorem.
---

::: {.problem}
Suppose $f$ is analytic on the entire complex plane and $f(z)/z$ is bounded in the region $|z|>1$.
Prove that
\[
f(z)=az+b
\]
for some constants $a,b$.
:::

::: {.solution}
Define, for $z\ne0$,
$$
g(z)\coloneqq\frac{f(z)-f(0)}{z}.
$$

<1>1. The function $g$ extends holomorphically to all of $\CC$ by setting
$$
g(0)=f'(0).
$$

::: {.proof}
Since $f$ is entire,
$$
\lim_{z\to0}\frac{f(z)-f(0)}{z}=f'(0).
$$
Thus $g$ has a removable singularity at $0$, and the indicated value gives an entire extension.
:::

<1>2. The entire extension of $g$ is bounded on the region $\abs{z}>1$.

::: {.proof}
By hypothesis, there is $M>0$ such that
$$
\left|\frac{f(z)}{z}\right|\le M
$$
whenever $\abs{z}>1$.
Hence on that region,
$$
\abs{g(z)}
\le
\left|\frac{f(z)}{z}\right|
+\frac{\abs{f(0)}}{\abs{z}}
\le M+\abs{f(0)}.
$$
:::

<1>3. The function $g$ is bounded on all of $\CC$.

::: {.proof}
Step <1>2 gives boundedness outside the closed unit disk.
By step <1>1, $g$ is continuous on the compact disk $\{z:\abs{z}\le1\}$, so it is bounded there as well.
Combining the two bounds gives a global bound.
:::

<1>4. The function $g$ is constant.

::: {.proof}
By steps <1>1 and <1>3, $g$ is an entire bounded function.
Liouville's theorem therefore implies that
$$
g(z)=a
$$
for some constant $a\in\CC$.
:::

<1>5. Consequently
$$
\boxed{f(z)=az+b}
$$
for constants $a,b$.

::: {.proof}
For $z\ne0$, the definition of $g$ and step <1>4 give
$$
f(z)-f(0)=az.
$$
Both sides are continuous at $z=0$, so the identity holds there as well.
Taking $b=f(0)$ gives the stated form.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
