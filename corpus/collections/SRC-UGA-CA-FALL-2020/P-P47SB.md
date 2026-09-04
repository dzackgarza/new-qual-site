---
schema: qual/card@1
id: P-P47SB
kind: problem
title: $|f(0)|\le|a|^2$ for holomorphic $f:\DD\to\DD$ vanishing at $\pm a$, and the
  equality case
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

:::{.problem}
Let $\mathbb{D}:=\{z:|z|<1\}$ denote the open unit disk. Suppose that $f(z): \mathbb{D} \rightarrow \mathbb{D}$ is holomorphic, and that there exists $a \in \mathbb{D} \backslash\{0\}$ such that $f(a)=f(-a)=0$.

- Prove that $|f(0)| \leq|a|^{2}$.

- What can you conclude when $|f(0)|=|a|^{2} ?$

:::

:::{.solution}
For $c\in\DD$, write
\[
\phi_c(z)=\frac{z-c}{1-\overline c z}.
\]

<1>1. If $F:\DD\to\DD$ is holomorphic and $F(c)=0$, then
\[
\left|\frac{F(z)}{\phi_c(z)}\right|\le1
\qquad(z\in\DD),
\]
where the quotient is extended holomorphically at $z=c$.
::: {.proof}
The disk automorphism $\phi_c$ sends $c$ to $0$.
Thus
\[
h(w)=F(\phi_c^{-1}(w))
\]
is a holomorphic self-map of $\DD$ with $h(0)=0$.
Schwarz's lemma gives
\[
|h(w)|\le|w|.
\]
Putting $w=\phi_c(z)$ yields
\[
|F(z)|\le|\phi_c(z)|.
\]
Since $F(c)=\phi_c(c)=0$ and $\phi_c$ has a simple zero at $c$, the quotient extends holomorphically there, and the displayed bound persists by continuity.
:::

<1>2. The function
\[
g(z)=\frac{f(z)}{\phi_a(z)\phi_{-a}(z)}
\]
extends holomorphically to $\DD$ and satisfies $|g(z)|\le1$.
::: {.proof}
Apply <1>1 to $f$ at the zero $a$.
Then
\[
f_1(z)=\frac{f(z)}{\phi_a(z)}
\]
is holomorphic with $|f_1|\le1$.
Because $a\ne0$, $\phi_a(-a)\ne0$, so $f_1(-a)=0$.
Apply <1>1 again, now to $f_1$ at $-a$.
The resulting quotient is exactly $g$.
:::

<1>3. $|f(0)|\le|a|^2$.
::: {.proof}
By <1>2,
\[
1\ge|g(0)|
=\frac{|f(0)|}{|\phi_a(0)|\,|\phi_{-a}(0)|}.
\]
Since
\[
|\phi_a(0)|=|a|=|\phi_{-a}(0)|,
\]
we obtain the claimed inequality.
:::

<1>4. If $|f(0)|=|a|^2$, then there exists $\lambda\in\CC$ with $|\lambda|=1$ such that
\[
\boxed{f(z)=\lambda\phi_a(z)\phi_{-a}(z)}.
\]
::: {.proof}
Equality in <1>3 is equivalent to
\[
|g(0)|=1.
\]
By <1>2, $g$ is holomorphic on $\DD$ and $|g|\le1$.
Thus $g$ attains its maximum modulus at an interior point, so the maximum modulus principle forces
\[
g\equiv\lambda
\]
for some $|\lambda|=1$.
Substituting the definition of $g$ gives the formula.
:::

<1>5. Conversely, every function in <1>4 satisfies the hypotheses and the equality case.
::: {.proof}
Each $\phi_{\pm a}$ is an automorphism of $\DD$, so for $z\in\DD$,
\[
|\lambda\phi_a(z)\phi_{-a}(z)|<1.
\]
The product vanishes at $a$ and $-a$, and at $0$ its modulus is
\[
|\phi_a(0)\phi_{-a}(0)|=|a|^2.
\]
:::

:::
