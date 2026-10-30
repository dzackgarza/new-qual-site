---
schema: qual/card@1
id: P-P47SB
kind: problem
title: $\abs{f(0)}\le\abs{a}^2$ for holomorphic $f:\DD\to\DD$ vanishing at $\pm a$, and the equality case
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Zeros
relations: []
review: draft
audit:
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced the invalid Blaschke-factor estimate and unresolved equality scratchpad by two applications of Schwarz's lemma.
---

::: {.problem}
Let $\DD:=\{z:\abs{z}<1\}$ denote the open unit disk. Suppose that $f(z): \DD \rightarrow \DD$ is holomorphic, and that there exists $a \in \DD \backslash\{0\}$ such that $f(a)=f(-a)=0$.

- Prove that $\abs{f(0)} \leq\abs{a}^{2}$.

- What can you conclude when $\abs{f(0)}=\abs{a}^{2} ?$

:::

::: {.solution}
For $c\in\DD$, write
$$
\phi_c(z)=\frac{z-c}{1-\overline c z}.
$$

::: pf

::: {.pf-step #s1}

If $F:\DD\to\DD$ is holomorphic and $F(c)=0$, then
$$
\abs{\frac{F(z)}{\phi_c(z)}}\le1
\qquad(z\in\DD),
$$
where the quotient is extended holomorphically at $z=c$.

::: pf-proof

The disk automorphism $\phi_c$ sends $c$ to $0$.
Thus
$$
h(w)=F(\phi_c^{-1}(w))
$$
is a holomorphic self-map of $\DD$ with $h(0)=0$.
Schwarz's lemma gives
$$
\abs{h(w)}\le\abs{w}.
$$
Putting $w=\phi_c(z)$ yields
$$
\abs{F(z)}\le\abs{\phi_c(z)}.
$$
Since $F(c)=\phi_c(c)=0$ and $\phi_c$ has a simple zero at $c$, the quotient extends holomorphically there, and the displayed bound persists by continuity.

:::

:::

::: {.pf-step #s2}

The function
$$
g(z)=\frac{f(z)}{\phi_a(z)\phi_{-a}(z)}
$$
extends holomorphically to $\DD$ and satisfies $\abs{g(z)}\le1$.

::: pf-proof

Apply step [](#s1){.pf-ref} to $f$ at the zero $a$.
Then
$$
f_1(z)=\frac{f(z)}{\phi_a(z)}
$$
is holomorphic with $\abs{f_1}\le1$.
Because $a\ne0$, $\phi_a(-a)\ne0$, so $f_1(-a)=0$.
Apply step [](#s1){.pf-ref} again, now to $f_1$ at $-a$.
The resulting quotient is exactly $g$.

:::

:::

::: {.pf-step #s3}

$\abs{f(0)}\le\abs{a}^2$.

::: pf-proof

By step [](#s2){.pf-ref},
$$
1\ge\abs{g(0)}
=\frac{\abs{f(0)}}{\abs{\phi_a(0)}\,\abs{\phi_{-a}(0)}}.
$$
Since
$$
\abs{\phi_a(0)}=\abs{a}=\abs{\phi_{-a}(0)},
$$
we obtain the claimed inequality.

:::

:::

::: {.pf-step #s4}

If $\abs{f(0)}=\abs{a}^2$, then there exists $\lambda\in\CC$ with $\abs{\lambda}=1$ such that
$$
\boxed{f(z)=\lambda\phi_a(z)\phi_{-a}(z)}.
$$

::: pf-proof

Equality in step [](#s3){.pf-ref} is equivalent to
$$
\abs{g(0)}=1.
$$
By step [](#s2){.pf-ref}, $g$ is holomorphic on $\DD$ and $\abs{g}\le1$.
Thus $g$ attains its maximum modulus at an interior point, so the maximum modulus principle forces
$$
g\equiv\lambda
$$
for some $\abs{\lambda}=1$.
Substituting the definition of $g$ gives the formula.

:::

:::

::: pf-step

Conversely, every function in step [](#s4){.pf-ref} satisfies the hypotheses and the equality case.

::: pf-proof

Each $\phi_{\pm a}$ is an automorphism of $\DD$, so for $z\in\DD$,
$$
\abs{\lambda\phi_a(z)\phi_{-a}(z)}<1.
$$
The product vanishes at $a$ and $-a$, and at $0$ its modulus is
$$
\abs{\phi_a(0)\phi_{-a}(0)}=\abs{a}^2.
$$

:::

:::

:::

:::
