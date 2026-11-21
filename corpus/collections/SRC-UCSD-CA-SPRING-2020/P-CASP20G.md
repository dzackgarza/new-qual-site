---
schema: qual/card@1
id: P-CASP20G
kind: problem
title: 'Positive harmonic functions with $h(0)=1$ form a normal family'
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Normal Families
  - Harnack Theorem
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The source is a course examination, so there is no retained solution set behind the card and the problem statement is the source. Each step re-read: Harnack bounds every member of the family on a disc of radius r < 1 between two positive constants because h(0) = 1; the gradient estimate turns that into equicontinuity; Arzela-Ascoli with a diagonal extraction gives the locally uniform limit, which is harmonic because the mean value property passes to such limits; and both h(0) = 1 and positivity pass to the limit. Not claimed: compactness for harmonic functions that are merely bounded below by 0 without the normalisation h(0) = 1.
---

::: {.problem}
Let $\mathcal{H}$ be the family of harmonic functions $h : \DD \to \RR$ with $h(0) = 1$ and $h(z) > 0$ for all $z \in \DD$.
Show that every sequence in $\mathcal{H}$ admits a subsequence that converges uniformly on compact subsets of $\DD$ to a function in $\mathcal{H}$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #harnack}
For $h\in\mathcal H$ and $\abs{z}\le r<1$, $\dfrac{1-r}{1+r}\le h(z)\le\dfrac{1+r}{1-r}$.

::: pf-proof
$h$ is positive and harmonic on the disc with $h(0)=1$, so Harnack's inequality for the disc applies: $\frac{1-\abs{z}}{1+\abs{z}}h(0)\le h(z)\le\frac{1+\abs{z}}{1-\abs{z}}h(0)$. Since $\abs{z}\le r$ and $t\mapsto\frac{1-t}{1+t}$, $t\mapsto\frac{1+t}{1-t}$ are monotone in the appropriate directions on $[0,1)$, replacing $\abs{z}$ by $r$ gives the displayed two-sided bound.
:::

:::

::: {.pf-step #bounded}
$\mathcal H$ is uniformly bounded on every compact subset of $\DD$.

::: pf-proof
A compact $K\subset\DD$ lies in some closed disc $\overline{D(0,r)}$ with $r<1$, and step [](#harnack){.pf-ref} bounds every $h\in\mathcal H$ there between the two positive constants $\frac{1-r}{1+r}$ and $\frac{1+r}{1-r}$.
:::

:::

::: {.pf-step #equicontinuous}
$\mathcal H$ is equicontinuous on every compact subset of $\DD$.

::: pf-proof
For harmonic functions the interior derivative estimate gives, on a compact set $K$, $\sup_{K}\abs{\nabla h}\le C_{K}\sup_{K'}\abs{h}$ for a slightly larger compact $K'\supset K$ and a constant depending only on $K$, and the second factor is bounded uniformly over $\mathcal H$ by step [](#bounded){.pf-ref}. A uniform gradient bound gives equicontinuity by the mean value theorem applied along segments.
:::

:::

::: {.pf-step #subsequence}
Every sequence in $\mathcal H$ has a subsequence converging uniformly on compact subsets of $\DD$ to a harmonic function $h$.

::: pf-proof
Arzelà--Ascoli applies on each $\overline{D(0,r_{j})}$ with $r_{j}\to1$ because the family is uniformly bounded and equicontinuous there by steps [](#bounded){.pf-ref} and [](#equicontinuous){.pf-ref}; a diagonal argument extracts one subsequence converging uniformly on every such disc, hence on every compact set. A locally uniform limit of harmonic functions is harmonic, since each term satisfies the mean value property and the identity passes to the limit.
:::

:::

::: {.pf-step #limitinh}
$h\in\mathcal H$.

::: pf-proof
Uniform convergence on compact subsets includes the point $0$, so $h(0)=\lim h_{n}(0)=1$. For $\abs{z}\le r<1$, step [](#harnack){.pf-ref} gives $h_{n}(z)\ge\frac{1-r}{1+r}$ for every $n$, and passing to the limit preserves a non-strict inequality, so $h(z)\ge\frac{1-r}{1+r}>0$.
:::

:::

::: {.pf-step}
Every sequence in $\mathcal H$ has a subsequence converging to a member of $\mathcal H$.

::: pf-proof
Steps [](#subsequence){.pf-ref} and [](#limitinh){.pf-ref} give
$$
\boxed{\mathcal H\text{ is a normal family: every sequence has a subsequence converging locally uniformly to a function in }\mathcal H.}
$$
The three ingredients are Harnack's inequality for the uniform bound, the gradient estimate for equicontinuity, and Arzelà--Ascoli with a diagonal argument.
:::

:::

:::
:::
