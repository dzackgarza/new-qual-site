---
schema: qual/card@1
id: P-BKF88-2
kind: problem
title: Automorphisms of the complex plane
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/Fall88_extracted.md.
---

::: {.problem}
Determine the group $\operatorname{Aut}(\mathbb C)$ of all one-to-one analytic maps of $\mathbb C$ onto $\mathbb C$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $f:\CC\to\CC$ is a bijective entire function, then $f^{-1}$ is continuous.

::: pf-proof

The function $f$ is nonconstant because it is bijective. By the open mapping theorem, $f$ maps open subsets of $\CC$ to open subsets of $\CC$. Since $f$ is bijective, this is exactly the statement that its inverse $f^{-1}:\CC\to\CC$ is continuous.

:::

:::

::: {.pf-step #s2}

For every bijective entire $f$,
$$
\abs{f(z)}\longrightarrow\infty
\qquad\text{as}\qquad
\abs z\longrightarrow\infty.
$$

::: pf-proof

Suppose otherwise. Then there is a sequence $(z_n)$ with
$$
\abs{z_n}\longrightarrow\infty
$$
while $(f(z_n))$ remains bounded. A bounded sequence in $\CC$ has a convergent subsequence, so after passing to a subsequence,
$$
f(z_n)\longrightarrow w
$$
for some $w\in\CC$. By continuity of $f^{-1}$ from step [](#s1){.pf-ref},
$$
z_n
=
f^{-1}(f(z_n))
\longrightarrow
f^{-1}(w),
$$
contradicting $\abs{z_n}\to\infty$.

:::

:::

::: {.pf-step #s3}

Every bijective entire function is a polynomial.

::: pf-proof

Consider
$$
g(\zeta)=f(1/\zeta)
$$
on a punctured neighborhood of $0$. Step [](#s2){.pf-ref} gives
$$
\abs{g(\zeta)}\longrightarrow\infty
\qquad\text{as}\qquad
\zeta\longrightarrow0.
$$
Thus $g$ has a pole at $0$. Equivalently, the singularity of $f$ at infinity is a pole. An entire function with a pole at infinity is a polynomial.

:::

:::

::: {.pf-step #s4}

Every bijective entire function has degree one.

::: pf-proof

Let $f$ be bijective. By step [](#s3){.pf-ref}, $f$ is a nonconstant polynomial. If $\deg f\geq2$, then $f'$ is a nonconstant polynomial and therefore has a zero $z_0$ by the fundamental theorem of algebra. But an injective holomorphic function has nonzero derivative at every point, so this contradicts injectivity. Hence
$$
\deg f=1.
$$
Therefore
$$
f(z)=az+b
$$
for some $a,b\in\CC$ with $a\neq0$.

:::

:::

::: {.pf-step #s5}

Conversely, every map
$$
z\longmapsto az+b,
\qquad
a\in\CC^\times,
\quad
b\in\CC,
$$
is an automorphism of $\CC$.

::: pf-proof

Such a map is entire and has entire inverse
$$
w\longmapsto\frac{w-b}{a}.
$$
Hence it is one-to-one and onto.

:::

:::

::: {.pf-step #s6}

Therefore
$$
\boxed{
\Aut(\CC)
=
\{z\mapsto az+b:a\in\CC^\times,\ b\in\CC\}.
}
$$
Under the identification $z\mapsto az+b\leftrightarrow(a,b)$, composition is
$$
(a,b)(c,d)=(ac,ad+b).
$$

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give exactly the automorphisms. The composition formula follows from
$$
a(cz+d)+b=(ac)z+(ad+b).
$$

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} determines the automorphism group.

:::

:::

:::
