---
schema: qual/card@1
id: P-WESCA07-III1
kind: problem
title: "A disk automorphism maps the disk onto itself"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section III, problem 1 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let
$$
f(z)=\frac{z-a}{1-\overline a z},
\qquad \abs{a}<1,
$$
be defined on the unit disk $D=\{z:\abs{z}<1\}$.
Using the Maximum Principle, show that $f$ maps $D$ onto $D$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The denominator $1-\overline a z$ is nonzero on the closed unit disk.


::: pf-proof

If $\abs{z}\le1$, then
$$
\abs{\overline a z}\le\abs{a}<1.
$$
Hence $\overline a z\ne1$, so the denominator does not vanish.

:::

:::

::: {.pf-step #s1-2}

For every $z$ on the unit circle,
$$
\abs{f(z)}=1.
$$


::: pf-proof

If $\abs{z}=1$, then
$$
\abs{z-a}^2
=(z-a)(\overline z-\overline a)
=1-z\overline a-a\overline z+\abs{a}^2,
$$
while
$$
\abs{1-\overline a z}^2
=(1-\overline a z)(1-a\overline z)
=1-z\overline a-a\overline z+\abs{a}^2.
$$
Thus numerator and denominator have the same modulus.

:::

:::

::: {.pf-step #s1-3}

One has
$$
f(D)\subseteq D.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $f$ is holomorphic on a neighborhood of the closed disk and continuous on its closure. Step [](#s1-2){.pf-ref} gives
$$
\abs{f}=1
$$
on the boundary. The function $f$ is nonconstant, so the Maximum Principle implies
$$
\abs{f(z)}<1
$$
for every $z\in D$.

:::

:::

::: {.pf-step #s1-4}

Define
$$
g(w)\coloneqq\frac{w+a}{1+\overline a w}.
$$
Then
$$
g(D)\subseteq D.
$$


::: pf-proof

The denominator is nonzero on the closed unit disk because $\abs{\overline a w}<1$ there. For $\abs{w}=1$,
$$
\abs{w+a}^2
=1+w\overline a+a\overline w+\abs{a}^2
=\abs{1+\overline a w}^2.
$$
Thus $\abs{g}=1$ on the unit circle. Since $g$ is nonconstant and holomorphic on a neighborhood of the closed disk, the Maximum Principle gives $\abs{g(w)}<1$ for $w\in D$.

:::

:::

::: {.pf-step #s1-5}

The maps $f$ and $g$ are inverse to one another on $D$.


::: pf-proof

A direct substitution gives
$$
f(g(w))=w
$$
and
$$
g(f(z))=z
$$
wherever the formulas are defined. Steps [](#s1-1){.pf-ref} and [](#s1-4){.pf-ref} ensure that all denominators are nonzero on $D$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{f(D)=D}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives $f(D)\subseteq D$. Conversely, if $w\in D$, then step [](#s1-4){.pf-ref} gives $g(w)\in D$, and step [](#s1-5){.pf-ref} gives
$$
f(g(w))=w.
$$
Hence every $w\in D$ lies in $f(D)$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required surjectivity statement.

:::

:::

:::
