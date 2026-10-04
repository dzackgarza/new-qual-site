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
\[
f(z)=\frac{z-a}{1-\overline a z},
\qquad |a|<1,
\]
be defined on the unit disk $D=\{z:|z|<1\}$.
Using the Maximum Principle, show that $f$ maps $D$ onto $D$.
:::

::: {.solution}
<1>1. The denominator $1-\overline a z$ is nonzero on the closed unit disk.

::: {.proof}
If $|z|\le1$, then
$$
|\overline a z|\le|a|<1.
$$
Hence $\overline a z\ne1$, so the denominator does not vanish.
:::

<1>2. For every $z$ on the unit circle,
$$
|f(z)|=1.
$$

::: {.proof}
If $|z|=1$, then
$$
|z-a|^2
=(z-a)(\overline z-\overline a)
=1-z\overline a-a\overline z+|a|^2,
$$
while
$$
|1-\overline a z|^2
=(1-\overline a z)(1-a\overline z)
=1-z\overline a-a\overline z+|a|^2.
$$
Thus numerator and denominator have the same modulus.
:::

<1>3. One has
$$
f(D)\subseteq D.
$$

::: {.proof}
By step <1>1, $f$ is holomorphic on a neighborhood of the closed disk and continuous on its closure. Step <1>2 gives
$$
|f|=1
$$
on the boundary. The function $f$ is nonconstant, so the Maximum Principle implies
$$
|f(z)|<1
$$
for every $z\in D$.
:::

<1>4. Define
$$
g(w)\coloneqq\frac{w+a}{1+\overline a w}.
$$
Then
$$
g(D)\subseteq D.
$$

::: {.proof}
The denominator is nonzero on the closed unit disk because $|\overline a w|<1$ there. For $|w|=1$,
$$
|w+a|^2
=1+w\overline a+a\overline w+|a|^2
=|1+\overline a w|^2.
$$
Thus $|g|=1$ on the unit circle. Since $g$ is nonconstant and holomorphic on a neighborhood of the closed disk, the Maximum Principle gives $|g(w)|<1$ for $w\in D$.
:::

<1>5. The maps $f$ and $g$ are inverse to one another on $D$.

::: {.proof}
A direct substitution gives
$$
f(g(w))=w
$$
and
$$
g(f(z))=z
$$
wherever the formulas are defined. Steps <1>1 and <1>4 ensure that all denominators are nonzero on $D$.
:::

<1>6. Therefore
$$
\boxed{f(D)=D}.
$$

::: {.proof}
Step <1>3 gives $f(D)\subseteq D$. Conversely, if $w\in D$, then step <1>4 gives $g(w)\in D$, and step <1>5 gives
$$
f(g(w))=w.
$$
Hence every $w\in D$ lies in $f(D)$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required surjectivity statement.
:::
:::
