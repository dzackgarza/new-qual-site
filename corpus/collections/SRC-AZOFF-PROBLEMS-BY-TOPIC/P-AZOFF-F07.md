---
schema: qual/card@1
id: P-AZOFF-F07
kind: problem
title: Singularity at $\infty$ of an entire function and its zeros
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Laurent expansions and singularities, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    First classified infinity for an arbitrary entire function: removable
    exactly for constants, a pole exactly for nonconstant polynomials, and
    essential exactly for nonpolynomial entire functions. With finitely many
    zeros all three types occur, using 1, z, and exp(z). With infinitely many
    zeros a pole is impossible; the zero function gives the removable case,
    while every nonzero example must be essential, as illustrated by sin(z).
---

::: {.problem}
Let $f$ be entire.
Discuss, with proofs and examples, the types of singularities $f$ might have (removable, pole, or essential) at $\infty$ in each of the following cases.

a) $f$ has at most finitely zeros in $\CC$.

b) $f$ has infinitely many zeros in $\CC$.
:::

::: {.solution}
For the singularity at infinity, use the local coordinate
$$
w=\frac1z
$$
and study
$$
F(w)=f(1/w)
$$
near $w=0$.

::: pf

::: {.pf-step #s1}

The singularity of an entire function $f$ at $\infty$ is removable
if and only if $f$ is constant.

::: pf-proof

Suppose first that the singularity at $\infty$ is removable. Then
$F(w)=f(1/w)$ is bounded for sufficiently small nonzero $w$. Equivalently,
there are $R,M>0$ such that
$$
\abs{f(z)}\leq M
$$
whenever $\abs{z}>R$. Since $f$ is continuous on the compact disk
$\abs{z}\leq R$, it is bounded there as well. Thus $f$ is bounded on all
of $\CC$, and Liouville's theorem implies that $f$ is constant.

Conversely, if $f$ is constant, then $F(w)$ is constant on the punctured
neighborhood of $0$ and extends holomorphically across $0$. Hence the
singularity at $\infty$ is removable.

:::

:::

::: {.pf-step #s2}

The singularity of $f$ at $\infty$ is a pole if and only if $f$ is
a nonconstant polynomial.

::: pf-proof

Write the Taylor expansion
$$
f(z)=\sum_{n=0}^{\infty}a_nz^n.
$$
Then
$$
F(w)
=
f(1/w)
=
\sum_{n=0}^{\infty}a_nw^{-n}.
$$
If $F$ has a pole at $0$, its Laurent series has only finitely many negative
powers and at least one such term. Hence only finitely many $a_n$ are
nonzero and at least one $a_n$ with $n\geq1$ is nonzero. Thus $f$ is a
nonconstant polynomial.

Conversely, if
$$
f(z)=a_0+a_1z+\cdots+a_dz^d,
\qquad
d\geq1,
\qquad
a_d\neq0,
$$
then
$$
F(w)
=
a_0+a_1w^{-1}+\cdots+a_dw^{-d},
$$
so $F$ has a pole of order $d$ at $0$.

:::

:::

::: {.pf-step #s3}

The singularity of $f$ at $\infty$ is essential if and only if $f$
is a nonpolynomial entire function.

::: pf-proof

The function $F(w)=f(1/w)$ is holomorphic on a punctured neighborhood of
$0$, so its isolated singularity there is removable, a pole, or essential.
By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the first two possibilities are exactly constant
functions and nonconstant polynomials. Therefore the remaining entire
functions, precisely the nonpolynomial entire functions, have an essential
singularity at $\infty$.

:::

:::

::: {.pf-step #s4}

In part (a), where $f$ has at most finitely many zeros, all three
types of singularity at $\infty$ can occur.

::: pf-proof

A removable singularity occurs for
$$
f(z)=1,
$$
which has no zeros, by step [](#s1){.pf-ref}.

A pole occurs for
$$
f(z)=z,
$$
which has one zero, by step [](#s2){.pf-ref}.

An essential singularity occurs for
$$
f(z)=e^z,
$$
which has no zeros and is not a polynomial, by step [](#s3){.pf-ref}.
Thus the assumption of finitely many zeros excludes none of the three
singularity types.

:::

:::

::: {.pf-step #s5}

In part (b), a pole at $\infty$ is impossible.

::: pf-proof

If $f$ had a pole at $\infty$, step [](#s2){.pf-ref} would make $f$ a nonconstant
polynomial. A nonzero polynomial has only finitely many zeros, contradicting
the hypothesis that $f$ has infinitely many zeros.

:::

:::

::: {.pf-step #s6}

In part (b), a removable singularity occurs only for the zero
function.

::: pf-proof

If the singularity at $\infty$ is removable, step [](#s1){.pf-ref} says that $f$ is
constant. The only constant function with infinitely many zeros is
$$
f\equiv0.
$$
Conversely, the zero function has every point as a zero and has a removable
singularity at $\infty$.

:::

:::

::: {.pf-step #s7}

Every nonzero entire function with infinitely many zeros has an
essential singularity at $\infty$, and this case occurs.

::: pf-proof

Let $f$ be nonzero entire with infinitely many zeros. By step [](#s6){.pf-ref} its
singularity at $\infty$ is not removable, and by step [](#s5){.pf-ref} it is not a
pole. Therefore it is essential.

For example,
$$
f(z)=\sin z
$$
has the infinitely many zeros $n\pi$, $n\in\ZZ$, and is not a polynomial.
Hence step [](#s3){.pf-ref} shows that its singularity at $\infty$ is essential.

:::

:::

::: {.pf-step #s8}

The classification is therefore:

(a) with at most finitely many zeros, removable, pole, and essential are all
possible;

(b) with infinitely many zeros, a pole is impossible, the removable case is
exactly $f\equiv0$, and every nonzero such function has an essential
singularity at $\infty$.

::: pf-proof

Part (a) is step [](#s4){.pf-ref}. Part (b) follows from steps [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s8){.pf-ref} gives the requested discussion, proofs, and examples.

:::

:::

:::
