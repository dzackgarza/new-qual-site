---
schema: qual/card@1
id: P-CAEXAMPREP-06
kind: problem
title: Count the zeros of $z^4-5z+1$ in an annulus
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
How many zeros does
$$
z^4-5z+1
$$
have in the annulus $1<|z|<2$?

The source emphasizes that the inner inequality is strict.
:::

::: {.solution}

Let
$$
f(z)=z^4-5z+1.
$$

::: pf

::: {.pf-step #s1-1}

The polynomial $f$ has exactly four zeros in $|z|<2$, counted with multiplicity, and no zero on $|z|=2$.


::: pf-proof

On $|z|=2$,
$$
|-5z+1|\le 5|z|+1=11<16=|z^4|.
$$
By Rouché's theorem, $f=z^4+(-5z+1)$ and $z^4$ have the same number of zeros in $|z|<2$, counted with multiplicity. Thus $f$ has four zeros there. The same strict inequality shows that $f$ cannot vanish on $|z|=2$.

:::

:::

::: {.pf-step #s1-2}

The polynomial $f$ has exactly one zero in $|z|<1$, counted with multiplicity, and no zero on $|z|=1$.


::: pf-proof

On $|z|=1$,
$$
|z^4+1|\le |z|^4+1=2<5=|-5z|.
$$
Rouché's theorem applied to $f=(-5z)+(z^4+1)$ shows that $f$ and $-5z$ have the same number of zeros in the unit disc. Hence $f$ has exactly one zero there, counted with multiplicity. Again, the strict inequality excludes zeros on $|z|=1$.

:::

:::

::: {.pf-step #s1-3}

The number of zeros of $f$ in $1<|z|<2$, counted with multiplicity, is
$$
\boxed{3}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref} there are four zeros with $|z|<2$, and by step [](#s1-2){.pf-ref} exactly one of them has $|z|<1$. Neither boundary circle contains a zero. Therefore precisely $4-1=3$ zeros lie in the strict annulus $1<|z|<2$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required count.

:::

:::

:::
