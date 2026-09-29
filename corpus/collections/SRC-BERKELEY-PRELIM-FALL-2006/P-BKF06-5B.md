---
schema: qual/card@1
id: P-BKF06-5B
kind: problem
title: Entire functions determined by their integrals against $(\sin z)^{-m}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 5B of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained residue argument, including the order
    computation at zero and the absence of other zeros of sin(z) in the
    closed unit disk.
---

::: {.problem}
Let $f$ and $g$ be entire functions such that
\[
\int_{|z|=1}\frac{f(z)}{(\sin z)^m}\,dz
=
\int_{|z|=1}\frac{g(z)}{(\sin z)^m}\,dz
\]
for every positive integer $m$.
Prove that $f=g$.
:::

::: {.solution}

Set
$$
h=f-g.
$$

::: pf

::: {.pf-step #h-integral-zero}
For every positive integer $m$,
$$
\int_{\abs z=1}\frac{h(z)}{(\sin z)^m}\,dz=0.
$$

::: pf-proof
This follows by subtracting the two integrals in the hypothesis and
using linearity of contour integration.
:::

:::

::: {.pf-step #h-local-factorization}
Suppose, for contradiction, that $h$ is not identically zero.
Let
$$
k=\operatorname{ord}_0 h.
$$
Then there is a holomorphic function $u$ near $0$ such that
$$
h(z)=z^ku(z),
\qquad
u(0)\ne0.
$$

::: pf-proof
Since $h$ is entire and not identically zero, its zero at $0$, if
present, has finite order $k\ge0$. The standard local factorization
at a zero gives the displayed expression.
:::

:::

::: {.pf-step #simple-pole-nonzero-residue}
For
$$
m=k+1,
$$
the meromorphic function
$$
\frac{h(z)}{(\sin z)^m}
$$
has a simple pole at $0$ with nonzero residue.

::: pf-proof
Write
$$
\sin z=zv(z),
$$
where $v$ is holomorphic near $0$ and $v(0)=1$. Using step [](#h-local-factorization){.pf-ref} and
$m=k+1$,
$$
\frac{h(z)}{(\sin z)^m}
=
\frac{z^ku(z)}{z^{k+1}v(z)^{k+1}}
=
\frac1z\frac{u(z)}{v(z)^{k+1}}.
$$
Thus the pole is simple and its residue is
$$
\frac{u(0)}{v(0)^{k+1}}
=
u(0)
\ne
0.
$$
:::

:::

::: {.pf-step #no-other-poles}
The function in step [](#simple-pole-nonzero-residue){.pf-ref} has no other poles in
$\abs z\le1$.

::: pf-proof
The zeros of $\sin z$ are the integer multiples of $\pi$. Since
$\pi>1$, the only zero of $\sin z$ in the closed unit disk is
$z=0$. The numerator $h$ is entire, so there are no other possible
poles.
:::

:::

::: {.pf-step #contradiction-m-k1}
The choice $m=k+1$ contradicts step [](#h-integral-zero){.pf-ref}.

::: pf-proof
By steps [](#simple-pole-nonzero-residue){.pf-ref} and [](#no-other-poles){.pf-ref}, the residue theorem gives
$$
\int_{\abs z=1}\frac{h(z)}{(\sin z)^{k+1}}\,dz
=
2\pi i\,u(0)
\ne
0.
$$
But step [](#h-integral-zero){.pf-ref} says that this integral is zero for every positive
integer $m$, including $m=k+1$. This is a contradiction.
:::

:::

::: {.pf-step #f-equals-g}
Therefore
$$
\boxed{f=g}.
$$

::: pf-proof
Step [](#contradiction-m-k1){.pf-ref} shows that the assumption $h\not\equiv0$ is impossible.
Hence $h=f-g\equiv0$.
:::

:::

::: pf-qed
Step [](#f-equals-g){.pf-ref} is the required conclusion.
:::

:::

:::
