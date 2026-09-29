---
schema: qual/card@1
id: P-BKF15-4A
kind: problem
title: The orthogonal-complement involution of the Riemann sphere is antiholomorphic
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Statement checked against F15_Exam.pdf problem 4A; restored the arrows of phi and tau and the broken equation in (a).
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet: the
    orthogonal line to C(w,z) is C(-conj(z),conj(w)), giving
    tau(z)=-1/conj(z) on C^* with tau(0)=infinity and tau(infinity)=0.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked well-definedness under rescaling homogeneous coordinates,
    involutivity, continuity at 0 and infinity, and failure of complex
    differentiability at z=1.
---

::: {.problem}
Let $S = \mathbb{C} \cup \{\infty\}$ be the Riemann sphere.
Let $\phi \colon \mathbb{C}^2 \setminus \{(0,0)\} \to S$ be the map defined by $\phi(w, z) = w/z$ for $z \neq 0$ and $\phi(w, 0) = \infty$.

(a) Prove that there is a unique map $\tau \colon S \to S$ with the following property: $\tau(\phi(w, z)) = \phi(w', z')$ if and only if the one-dimensional subspaces $\mathbb{C} \cdot (w, z)$ and $\mathbb{C} \cdot (w', z')$ are orthogonal under the standard Hermitian inner product on $\mathbb{C}^2$ in which the unit vectors $(1, 0)$ and $(0, 1)$ are orthonormal.

(b) Prove that $\tau$ is continuous and bijective.

(c) Determine, with proof, whether $\tau$ is holomorphic or not.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every nonzero vector $(w,z)\in\CC^2$, its orthogonal
complement is the one-dimensional subspace
$$
\CC\cdot(-\overline z,\overline w).
$$

::: pf-proof

With the standard Hermitian inner product,
$$
\inner{(w,z)}{(-\overline z,\overline w)}
=
w(-z)+z w
=
0.
$$
The vector $(-\overline z,\overline w)$ is nonzero whenever
$(w,z)\ne(0,0)$. Since the orthogonal complement of a nonzero vector in
$\CC^2$ has complex dimension $1$, it is exactly the displayed line.

:::

:::

::: {.pf-step #s2}

Define
$$
\tau(\phi(w,z))
\coloneqq
\phi(-\overline z,\overline w).
$$
This definition is independent of the choice of representative
$(w,z)$.

::: pf-proof

If $(w,z)$ is replaced by
$$
(\lambda w,\lambda z),
\qquad
\lambda\in\CC^\times,
$$
then
$$
(-\overline{\lambda z},\overline{\lambda w})
=
\overline\lambda(-\overline z,\overline w).
$$
The two vectors span the same one-dimensional subspace and therefore
have the same image under $\phi$. Thus $\tau$ is well-defined.

:::

:::

::: {.pf-step #s3}

The map in step [](#s2){.pf-ref} is the unique map satisfying part (a).

::: pf-proof

By step [](#s1){.pf-ref}, for every line
$$
L=\CC\cdot(w,z)
$$
there is exactly one orthogonal one-dimensional subspace, namely
$$
L^\perp
=
\CC\cdot(-\overline z,\overline w).
$$
Hence the value of any map satisfying the condition in part (a) is
forced to be
$$
\phi(-\overline z,\overline w).
$$
Step [](#s2){.pf-ref} shows that these forced values define a map.

:::

:::

::: {.pf-step #s4}

Explicitly,
$$
\boxed{
\tau(\zeta)
=
-\frac1{\overline\zeta}
}
\qquad
(\zeta\in\CC^\times),
$$
with
$$
\tau(0)=\infty,
\qquad
\tau(\infty)=0.
$$

::: pf-proof

If $\zeta=\phi(w,z)=w/z$ with $w,z\ne0$, then
$$
\begin{aligned}
\tau(\zeta)
&=
\phi(-\overline z,\overline w)\\
&=
-\frac{\overline z}{\overline w}\\
&=
-\frac1{\overline{w/z}}\\
&=
-\frac1{\overline\zeta}.
\end{aligned}
$$
If $\zeta=0$, one may take $(w,z)=(0,1)$, whose orthogonal complement
is spanned by $(-1,0)$ and hence maps to $\infty$. If
$\zeta=\infty$, take $(w,z)=(1,0)$; its orthogonal complement is
spanned by $(0,1)$ and maps to $0$.

:::

:::

::: {.pf-step #s5}

The map $\tau$ is an involution:
$$
\tau^2=\operatorname{Id}_S.
$$

::: pf-proof

For $\zeta\in\CC^\times$, step [](#s4){.pf-ref} gives
$$
\tau(\tau(\zeta))
=
-\frac1{
\overline{-1/\overline\zeta}
}
=
\zeta.
$$
Step [](#s4){.pf-ref} also shows that $0$ and $\infty$ are exchanged, so the same
identity holds at those two points.

:::

:::

::: {.pf-step #s6}

The map $\tau$ is continuous on the Riemann sphere.

::: pf-proof

On $\CC^\times$, the formula in step [](#s4){.pf-ref} is a composition of
continuous maps.

If $\zeta\to0$ in $\CC$, then
$$
\abs{\tau(\zeta)}
=
\frac1{\abs{\zeta}}
\longrightarrow\infty,
$$
which is exactly convergence to $\infty$ in the Riemann sphere.

If $\zeta\to\infty$, then
$$
\abs{\tau(\zeta)}
=
\frac1{\abs{\zeta}}
\longrightarrow0.
$$
Thus $\tau$ is continuous at $0$ and at $\infty$ as well.

:::

:::

::: {.pf-step #s7}

The map $\tau$ is bijective.

::: pf-proof

By step [](#s5){.pf-ref}, $\tau$ is its own inverse. Hence it is bijective.

:::

:::

::: {.pf-step #s8}

The map $\tau$ is not holomorphic.

::: pf-proof

If $\tau$ were holomorphic on the Riemann sphere, then its restriction
to a neighborhood of $1\in\CC^\times$ would be complex
differentiable. By step [](#s4){.pf-ref},
$$
\tau(\zeta)=-\frac1{\overline\zeta}.
$$
For real $h\to0$,
$$
\frac{\tau(1+h)-\tau(1)}{h}
=
\frac1{1+h}
\longrightarrow1.
$$
For real $t\to0$ along the imaginary direction,
$$
\frac{\tau(1+it)-\tau(1)}{it}
=
-\frac1{1-it}
\longrightarrow-1.
$$
The two directional difference quotients have different limits, so
$\tau$ is not complex differentiable at $1$.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove part (a), steps [](#s6){.pf-ref} and [](#s7){.pf-ref} prove part (b), and
step [](#s8){.pf-ref} proves part (c).

:::

:::

:::
