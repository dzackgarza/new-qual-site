---
schema: qual/card@1
id: P-AZOFF-I08
kind: problem
title: 'Subordination: $g(|z|<r)\subset f(|z|<r)$ for univalent $f$'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Schwarz lemma and reflection principle, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Put the bare f, g, D and Omega into math mode against Schwarz lemma and reflection principle, Problem 8, of Azoff Problems by Topic.pdf; the source itself omits the first part it mentions.
- event: source-corrected
  by: chatgpt
  date: 2026-09-21
  note: >-
    The retained PDF does not assume g(D) is contained in f(D), so the
    printed conclusion is false: with Omega=D, f(z)=z/2 and g(z)=z satisfy
    the printed hypotheses but not the claimed image inclusion. The card
    adds the minimal standard subordination hypothesis g(D)⊆f(D).
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Under the corrected subordination hypothesis, phi=f^{-1}∘g is an
    analytic self-map of the disk fixing zero. Schwarz's lemma gives
    |phi(z)|<=|z|, which immediately sends every radius-r disk into itself
    and yields the desired image inclusion after applying f.
---

::: {.problem}
[Fall 2002 Problem #8] Suppose $f$ and $g$ are holomorphic mappings of the unit disc $D$ into an open domain $\Omega$, $f$ is one-to-one, $g(D)\subseteq f(D)$, and $f(0) = g(0)$. Show that $g(\abs{z} < r) \subset f(\abs{z} < r)$ for each $0 < r < 1$. (The first part of the problem asks for a statement of the Schwarz Lemma.)
:::

::: {.solution}
Write
$$
D_r=\{z\in\CC:\abs{z}<r\}.
$$

::: pf

::: {.pf-step #s1}

Schwarz's lemma states: if $\varphi:\DD\to\DD$ is holomorphic and
$\varphi(0)=0$, then
$$
\abs{\varphi(z)}\leq\abs{z}
$$
for every $z\in\DD$.

::: pf-proof

This is Schwarz's lemma; the source's first part asks for its statement.

:::

:::

::: {.pf-step #s2}

The inverse map
$$
f^{-1}:f(D)\longrightarrow D
$$
is holomorphic.

::: pf-proof

Since $f$ is one-to-one and holomorphic, it is a conformal bijection from
$D$ onto the domain $f(D)$. In particular its derivative does not vanish,
so the holomorphic inverse function theorem gives a holomorphic local
inverse at every point of $f(D)$. These local inverses agree because $f$ is
globally one-to-one, and therefore form the holomorphic inverse $f^{-1}$.

:::

:::

::: {.pf-step #s3}

Define
$$
\varphi=f^{-1}\circ g.
$$
Then $\varphi:\DD\to\DD$ is holomorphic and satisfies $\varphi(0)=0$.

::: pf-proof

The hypothesis $g(D)\subseteq f(D)$ makes the composition
well-defined. Step [](#s2){.pf-ref} shows that it is holomorphic. Moreover,
$$
\varphi(0)
=
f^{-1}(g(0))
=
f^{-1}(f(0))
=
0.
$$

:::

:::

::: {.pf-step #s4}

For every $0<r<1$,
$$
\varphi(D_r)\subseteq D_r.
$$

::: pf-proof

If $z\in D_r$, then $\abs{z}<r$. By step [](#s1){.pf-ref} applied to the function in
step [](#s3){.pf-ref},
$$
\abs{\varphi(z)}
\leq
\abs{z}
<
r.
$$
Thus $\varphi(z)\in D_r$.

:::

:::

::: {.pf-step #s5}

For every $0<r<1$,
$$
\boxed{
g(D_r)\subseteq f(D_r).
}
$$

::: pf-proof

By the definition of $\varphi$,
$$
g=f\circ\varphi.
$$
Therefore step [](#s4){.pf-ref} gives
$$
g(D_r)
=
f(\varphi(D_r))
\subseteq
f(D_r).
$$

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required inclusion.

:::

:::

:::

::: {.remark}
Erratum: the source omits the hypothesis $g(D)\subseteq f(D)$.
Without it the conclusion is false. For example, with
$$
\Omega=D,\qquad f(z)=\frac z2,\qquad g(z)=z,
$$
all printed hypotheses hold, but
$$
g(D_r)=D_r
$$
is not contained in
$$
f(D_r)=D_{r/2}.
$$
The corrected statement adds the subordination hypothesis $g(D)\subseteq f(D)$.
:::
