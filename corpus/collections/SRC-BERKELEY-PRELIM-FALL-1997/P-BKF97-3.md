---
schema: qual/card@1
id: P-BKF97-3
kind: problem
title: Entire functions with the same modulus as sine
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 in the deterministic MinerU Flash extraction assets/attachments/Fall97_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Extended f/sin across the simple zeros n*pi, observed that the extended
    entire quotient has constant modulus one, and applied Liouville's theorem.
---

::: {.problem}
Let $f$ be entire and suppose
\[
|f(z)|=|\sin z|
\]
for every $z\in\mathbb C$.
Prove that there is a constant $C$ with $|C|=1$ such that
\[
f(z)=C\sin z.
\]
:::

::: {.solution}
<1>1. For every integer $k$,
$$
f(k\pi)=0.
$$

::: {.proof}
The hypothesis gives
$$
\abs{f(k\pi)}
=
\abs{\sin(k\pi)}
=0.
$$
Hence $f(k\pi)=0$.
:::

<1>2. For each integer $k$, the quotient
$$
\frac{f(z)}{\sin z}
$$
has a removable singularity at $z=k\pi$.

::: {.proof}
By step <1>1 and holomorphic factorization at a zero,
$$
f(z)
=
(z-k\pi)F_k(z)
$$
for some function $F_k$ holomorphic near $k\pi$. The zero of $\sin z$ at
$k\pi$ is simple because
$$
\cos(k\pi)=(-1)^k\neq0.
$$
Thus
$$
\sin z
=
(z-k\pi)S_k(z)
$$
near $k\pi$, where $S_k$ is holomorphic and
$$
S_k(k\pi)=(-1)^k\neq0.
$$
Hence on the punctured neighborhood,
$$
\frac{f(z)}{\sin z}
=
\frac{F_k(z)}{S_k(z)},
$$
and the right side is holomorphic at $k\pi$. This supplies the removable
extension.
:::

<1>3. There is an entire function $h$ such that
$$
h(z)=\frac{f(z)}{\sin z}
$$
whenever $\sin z\neq0$.

::: {.proof}
The quotient is holomorphic away from the discrete zero set
$$
\pi\ZZ.
$$
Step <1>2 gives a removable holomorphic extension at every point of that
set. Combining these local extensions gives an entire function $h$.
:::

<1>4. One has
$$
\abs{h(z)}=1
$$
for every $z\in\CC$.

::: {.proof}
If $\sin z\neq0$, the hypothesis gives
$$
\abs{h(z)}
=
\frac{\abs{f(z)}}{\abs{\sin z}}
=1.
$$
The complement of $\pi\ZZ$ is dense in $\CC$, and $h$ is continuous by
step <1>3. Therefore the same equality holds at the removed points by
continuity.
:::

<1>5. The function $h$ is constant.

::: {.proof}
Step <1>4 shows that the entire function $h$ is bounded. Liouville's
theorem therefore gives
$$
h(z)=C
$$
for some constant $C\in\CC$.
:::

<1>6. The constant $C$ satisfies
$$
\abs C=1
$$
and
$$
f(z)=C\sin z
$$
for every $z\in\CC$.

::: {.proof}
Step <1>4 applied to the constant function from step <1>5 gives
$\abs C=1$. On every point with $\sin z\neq0$,
$$
f(z)=h(z)\sin z=C\sin z.
$$
Both sides are entire, so the identity extends to all $z$; equivalently, it
also holds directly at the common zeros.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
