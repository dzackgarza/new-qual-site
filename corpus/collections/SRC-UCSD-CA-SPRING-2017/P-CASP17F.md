---
schema: qual/card@1
id: P-CASP17F
kind: problem
title: 'Roots of $z^{87}+36z^{57}+71z^4+z^3-z+1$ in the annulus $1\leq\abs z\leq 2$'
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Rouché
  - Polynomial Roots
relations: []
review: draft
---

::: {.problem}
Find the number of roots of the polynomial
$$
z^{87} + 36z^{57} + 71z^4 + z^3 - z + 1
$$
in the region $1 \leq \abs{z} \leq 2$.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/COMPLEX-EXAM.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. Both applications of Rouché's theorem are made against a named dominant term, and the two numerical bounds are verified rather than asserted, which is what the earlier version of the card left to the reader.

Throughout,
$$
p(z)\coloneqq z^{87}+36z^{57}+71z^{4}+z^{3}-z+1,
$$
zeros are counted with multiplicity, and Rouché's theorem is used in the form: if $\abs{g}<\abs{h}$ on a circle $\abs{z}=r$, then $h$ and $h+g$ have the same number of zeros in $\abs{z}<r$.

::: pf

::: {.pf-step #unit-circle}
$p$ has exactly $4$ zeros in $\abs{z}<1$.

::: pf-proof
Write $p=71z^{4}+g$ with $g\coloneqq z^{87}+36z^{57}+z^{3}-z+1$. On $\abs{z}=1$ one has $\abs{g}\leq1+36+1+1+1=40<71=\abs{71z^{4}}$, so the hypothesis of Rouché's theorem holds with $h=71z^{4}$ and $r=1$. The polynomial $71z^{4}$ has the single zero $z=0$, of multiplicity $4$, so $p$ has exactly $4$ zeros in the open unit disc.
:::

:::

::: {.pf-step #circle-two}
$p$ has exactly $87$ zeros in $\abs{z}<2$.

:::: pf-proof

::: {.pf-step #bound}
On $\abs{z}=2$, $\abs{p-z^{87}}<2^{87}=\abs{z^{87}}$.

::: pf-proof
For $\abs{z}=2$,
$$
\abs{p(z)-z^{87}}=\abs{36z^{57}+71z^{4}+z^{3}-z+1}\leq36\cdot2^{57}+71\cdot2^{4}+2^{3}+2+1=36\cdot2^{57}+1147.
$$
Since $1147<2^{57}$ and $37<2^{30}$, one has $36\cdot2^{57}+1147<37\cdot2^{57}<2^{30}\cdot2^{57}=2^{87}$.
:::

:::

::: {.pf-step #rouche}
The conclusion follows from Rouché's theorem.

::: pf-proof
Step [](#bound){.pf-ref} is the strict inequality $\abs{g}<\abs{h}$ needed, with $h=z^{87}$ and $r=2$; the polynomial $z^{87}$ has the single zero $0$, of multiplicity $87$, so $p$ has exactly $87$ zeros in $\abs{z}<2$.
:::

:::

::::

:::

::: {.pf-step #no-boundary-zeros}
$p$ has no zeros on $\abs{z}=1$ or on $\abs{z}=2$.

::: pf-proof
On $\abs{z}=1$, $\abs{p}\geq\abs{71z^{4}}-\abs{p-71z^{4}}\geq71-40=31>0$. On $\abs{z}=2$, $\abs{p}\geq\abs{z^{87}}-\abs{p-z^{87}}>2^{87}-\big(36\cdot2^{57}+1147\big)>0$ by step [](#bound){.pf-ref}. So the boundary circles of the annulus carry no zeros.
:::

:::

::: pf-step
Therefore the number of roots in $1\leq\abs{z}\leq2$ is
$$
\boxed{83.}
$$

::: pf-proof
A zero of $p$ lies in the closed annulus $1\leq\abs{z}\leq2$ exactly when $\abs{z}<2$ but not $\abs{z}<1$, since step [](#no-boundary-zeros){.pf-ref} excludes the two boundary circles. By steps [](#circle-two){.pf-ref} and [](#unit-circle){.pf-ref} there are $87$ zeros with $\abs{z}<2$ and $4$ of them with $\abs{z}<1$, so the annulus contains $87-4=83$ of them, counted with multiplicity.
:::

:::

:::

:::
