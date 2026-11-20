---
schema: qual/card@1
id: P-OWBTK
kind: problem
title: A ring of idempotents has characteristic $2$ and is commutative
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Every step of both parts asserted its claim with no proof body; each now carries a
    `pf-proof` that names the distributive law, the cancellation or the instance of the
    hypothesis used, and the closing `pf-qed` that only pointed back at the two parts is
    removed, STYLE-08 forbidding a QED step that does not itself conclude. No claim was
    changed. Checked: both computations recomputed term by term, including that no step uses
    commutativity of multiplication before step 2.6, and that the ring is not assumed to have
    an identity anywhere. Not checked: the examination paper the exercise comes from is not in
    the checkout, so the statement is the card's; the argument is the card's own.
---
::: {.problem}
Let $R$ be a ring (not assumed to have an identity) with the property that $x^2 = x$ for all $x \in R$ (a Boolean ring).

(a) Prove that $2x = 0$ for all $x \in R$ (that is, $R$ has characteristic 2).

(b) Prove that $R$ is commutative.
:::

::: {.solution}

Both parts are computations with the single hypothesis $x^2=x$: part (a) applies it to $x+x$, part (b) to $x+y$.

::: pf

::: pf-step

Every element of $R$ satisfies $2x=0$.

::: pf-proof

Steps 1.1--1.5 compute $(x+x)^2$ in two ways and cancel; step 1.6 records the consequence $x=-x$ that part (b) uses.

::: pf-step

Let $x \in R$. By hypothesis, $x + x \in R$ satisfies the idempotent property $(x + x)^2 = x + x$.

::: pf-proof

$R$ is closed under addition, so $x+x\in R$, and the hypothesis $z^2=z$ is stated for every element $z$ of $R$; apply it to $z=x+x$.

:::

:::

::: pf-step

Expand the left-hand side using the distributive laws of ring arithmetic:
$$(x + x)^2 = (x + x)(x + x) = x^2 + x^2 + x^2 + x^2.$$

::: pf-proof

Multiply out: $(x+x)(x+x)=x(x+x)+x(x+x)$ by left distributivity, and $x(x+x)=x^2+x^2$ by right distributivity, so the product is $(x^2+x^2)+(x^2+x^2)=x^2+x^2+x^2+x^2$, associativity of addition allowing the parentheses to be dropped. (No commutativity of multiplication is used: both factors are $x$.)

:::

:::

::: pf-step

Since $x^2 = x$, the expansion simplifies to:
$$(x + x)^2 = x + x + x + x = 4x.$$

::: pf-proof

Replace each of the four occurrences of $x^2$ by $x$. In the additive group $(R,+)$ the sum $x+x+x+x$ is by definition $4x$, the fourth multiple of $x$.

:::

:::

::: pf-step

Equating the two expressions gives
$$4x = 2x.$$

::: pf-proof

The left side is $(x+x)^2$ computed in step 1.3, the right side is $x+x=2x$ from the hypothesis as read in step 1.1; both name the same element.

:::

:::

::: pf-step

Subtracting $2x$ from both sides in the abelian group $(R, +)$ yields
$$2x = 0 \quad \text{for all } x \in R.$$

::: pf-proof

In the abelian group $(R,+)$ one may add $-2x$ to both sides of $4x=2x$: the left becomes $4x-2x=2x$ (since $4x=2x+2x$) and the right becomes $2x-2x=0$. So $2x=0$, and $x\in R$ was arbitrary.

:::

:::

::: pf-step

In particular, $x = -x$ for all $x \in R$.

::: pf-proof

$2x=0$ says $x+x=0$, that is, $x$ is its own additive inverse: $x=-x$. This holds for every element, and will be applied in step 2.6 to the element $yx$.

:::

:::

:::

:::

::: pf-step

The multiplication on $R$ is commutative: $xy=yx$ for all $x,y\in R$.

::: pf-proof

Steps 2.1--2.6 compute $(x+y)^2$ in two ways, cancel $x$ and $y$, and apply part (a) to $yx$; step 2.7 concludes.

::: pf-step

Let $x, y \in R$. By hypothesis, the element $x + y \in R$ satisfies $(x + y)^2 = x + y$.

::: pf-proof

$R$ is closed under addition, so $x+y\in R$, and the hypothesis $z^2=z$ applies to $z=x+y$.

:::

:::

::: pf-step

Expand the left-hand side using distributivity:
$$(x + y)^2 = x^2 + x y + y x + y^2 = x + x y + y x + y.$$

::: pf-proof

$(x+y)(x+y)=x(x+y)+y(x+y)$ by left distributivity, and $x(x+y)=x^2+xy$, $y(x+y)=yx+y^2$ by right distributivity; the four terms are then replaced by $x+x y+y x+y$ using $x^2=x$ and $y^2=y$. The two middle terms $xy$ and $yx$ are kept apart: commutativity is what is being proved.

:::

:::

::: pf-step

Equating this to $x + y$ gives
$$x + x y + y x + y = x + y.$$

::: pf-proof

Both sides are $(x+y)^2$: the left by step 2.2, the right by the hypothesis as read in step 2.1.

:::

:::

::: pf-step

Subtracting $x + y$ from both sides yields
$$x y + y x = 0.$$

::: pf-proof

In the abelian group $(R,+)$, add $-x$ on the left and $-y$ on the right of $x+xy+yx+y=x+y$: the two sides become $xy+yx$ and $0$.

:::

:::

::: pf-step

Rearranging gives $x y = -y x$.

::: pf-proof

$xy+yx=0$ says that $yx$ is the additive inverse of $xy$, that is $xy=-yx$.

:::

:::

::: pf-step

By Part (a), $-z = z$ for every $z \in R$. Applying this to $z = y x$ gives
$$x y = y x.$$

::: pf-proof

Step 1.6 gives $-z=z$ for every element, in particular for $z=yx$; substituting into $xy=-yx$ of step 2.5 gives $xy=yx$.

:::

:::

::: pf-step

Since $x, y \in R$ were arbitrary, $R$ is commutative.

::: pf-proof

The elements $x$ and $y$ were chosen arbitrarily, so $xy=yx$ holds for every pair of elements of $R$, which is what commutativity of multiplication asserts.

:::

:::

:::

:::

:::
:::